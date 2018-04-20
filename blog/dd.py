
from lxml import etree
import requests
from urllib.request import urlretrieve

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}

url = 'http://mp.weixin.qq.com/s/17a5gHHRzNaFEP2iqMAUmA'
# url = 'http://mp.weixin.qq.com/s/myYnHrZt4_ABo3s5FBOr7Q'

html = requests.get(url=url, headers=header).content.decode('utf-8')  ##获取网页代码
# print(html)

dom_tree = etree.HTML(html)  # XPath匹配

try:
    # 标题
    media_name = dom_tree.xpath('//*[@id="js_content"]/p[4]/span/strong[1]/span/text()')
    media_name = media_name[0][1:]
    print(media_name)

    # 要下载的文件
    string = dom_tree.xpath('//*[@id="js_content"]/p[6]/mpvoice/@voice_encode_fileid')
    print(string)
    file = 'http://res.wx.qq.com/voice/getvoice?mediaid=' + str(string[0])
    print(file)

except:
    # 标题
    media_name1 = dom_tree.xpath('//*[@id="js_content"]/p[4]/span/strong[1]/span/text()')
    media_name1 = media_name1[0][1:]
    print(media_name1)

    media_name2 = dom_tree.xpath('//*[@id="js_content"]/p[5]/span/strong[1]/span/text()')
    media_name2 = media_name2[0]
    print(media_name2)

    media_name = media_name1 + media_name2
    print(media_name)

    # 要下载的文件
    string = dom_tree.xpath('//*[@id="js_content"]/p[7]/mpvoice/@voice_encode_fileid')
    print(string)
    file = 'http://res.wx.qq.com/voice/getvoice?mediaid=' + str(string[0])
    print(file)

# 下载到本地
urlretrieve(file, './' + media_name + '.mp3')