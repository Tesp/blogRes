from wxpy import *
bot = Bot()

# 机器人账号自身
my_friend = ensure_one(bot.search('小闫'))
xiaoi = XiaoI('WOATyFqc8Bb0', 'Lr12jocPwyuGNhD6zQUE')

# 使用小 i 机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    print(msg)
    xiaoi.do_reply(msg)

embed()