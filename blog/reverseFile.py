# 打开一个文件
f = open("cihuai.txt", "r",encoding='utf8')

# 打开一个文件
fw = open("cihuaiRever.txt", "a+")




n=0;
list= ['']
for line in f:
    if line.__contains__("http"):
         n=n+1
         print(line, end='')
         list.insert(0,line)

         # print(line)

for line in list:
    fw.write(line)
# 关闭打开的文件
f.close()
fw.close()

