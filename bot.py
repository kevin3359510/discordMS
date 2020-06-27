import discord
from discord.ext import commands
import token4_MS_機器人

bot = commands.Bot(command_prefix='!')
data = list()
async def boss(message):
  a = message.content[3:]
  b = "=============="+a+"=============="
  await message.channel.send(b)
@bot.event
async def on_ready():
      activity = discord.Game(name="御久好帥 御久好暖")
      await bot.change_presence(status=discord.Status.idle, activity=activity)
async def kevin(message):
  c = message.content[3:]
  s = "<@&" + str(685156600662720591) + ">" + c
  await message.channel.send(s)
def getPlayerInfoEmbed(e):
  embed=discord.Embed(title="報刀資訊", description="1月工會戰報刀資訊")
  embed.add_field(name="編號 boss ID 使用隊伍 傷害 殘秒", value=format(str(e)), inline=False)
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/650696351948210197/664071534146617346/IMG_20200105_023708.jpg?width=461&height=560")
  return embed
async def tree(message):
  A = "高木高木樣樣行 掛掛非洲他都贏\n"+"https://img.ruten.com.tw/s1/d/95/15/21850205362453_605.jpg"
  await message.channel.send(A)
async def tree1(message):
  await message.channel.send("御久好帥 御久好暖")
async def add(message):
    global data
    data.append(message.content[3:])
    i = len(data)
    z = len(data)
    s = "您是本公會第<<" + str(z) + ">>號成員進此王喔。"
    await message.channel.send(s)
async def jk(message):
  b = "來了❤★❤★"
  await message.channel.send(b)
async def l(message):
    global data
    c = 1
    e = ""
    if(len(data) == 0):
        await message.channel.send("暫無資料")
    else:
        for d in data:
              k = str(c)+"."+" "+ d + "\n"
              e += k
              c += 1
        embed = getPlayerInfoEmbed(e)
        await message.channel.send(embed=embed)
async def delete(message):
    global data
    if(message.content[5:].isdigit()):
        data.remove(data[int(message.content[5:])])
    else:
        data.clear()
    a = "出獄囉"
    await message.channel.send(a)
async def edit(message):
    global data
    global data1
    w = message.content[3:].split()
    if(len(w[0])==2):
      data[int(w[0])-1] = message.content[6:]
    if(len(w[0])==1):
      data[int(w[0])-1] = message.content[5:]
async def h(message):
    a = "!卡 <成員>\n"
    b = "進刀喊的 第一個數字是裡面刀的總數 第二個數字是喊的人的編號\n"
    c = "!下樹 all/編號\n"
    d = "清空所有list/清空此編號之資料\n"
    e = "!list\n"
    f = "顯示現有名單\n"
    g = "!e <編號> <資料>\n"
    h = "編輯屬於你編號的資料(編號 boss ID 使用隊伍 傷害 殘秒)\n"
    i = "!c <傷害> <王的血量>\n"
    j = "殘刀秒數\n"
    k = "記住 指令編號資料中間都要加空格 很重要。"
    l = a+b+c+d+e+f+g+h+i+j+k
    await message.channel.send(l)
async def seccc(message):
  #!a 傷害  剩的血量 收王時間 你bot再90去扣 ((傷害-剩餘血量)/傷害)x使用秒數+(110-使用秒數)
  #(剩餘血量/(傷害/90))+20
    w = message.content[3:].split()
    #b = ((int(w[0])-int(w[1]))/int(w[0]))*(90-int(w[2]))+(110-(90-int(w[2])))
    #a = str(b) + "秒"
    #c = "超過了喇你這個小♡笨♡蛋"
    c = ((int(w[0])-int(w[1]))/int(w[0])*90)+20
    x = "超過了喇你這個小♡笨♡蛋"
    if(c <= 20):
        await message.channel.send("王沒死喇 小♡呆♡瓜")
    elif(c > 89):
        await message.channel.send(x)
    else:
        a = str(c)
        await message.channel.send(a)
    #if (b > 90):
      #await message.channel.send(c)
    #else:
      #await message.channel.send(a)
async def secc(message):
  w = message.content[3:].split()
  b = ((int(w[0])-int(w[1]))/int(w[0]))*(90-int(w[2]))+(110-(90-int(w[2])))
  a = str(b) + "秒"
  c = "超過"
  if (b > 90):
    await message.channel.send(c)
  else:
    await message.channel.send(a)
#async def 女裝(message):
  #tag = "@606624041226207233"
  #await message.channel.send(tag)
@bot.event
async def on_message(message):
    print(message)
    msg = message.content.lower()
    user = message.author
    username = user.name
    userid = user.id
    c = "C:\\Users\\kigntilht\\Desktop\\package\\unknown.png"
    a = "C:\\Users\\kigntilht\\Desktop\\package\\i010003_1478157283.jpg"
    b = discord.File(c)
    d = discord.File(a)
    channels = ["額外機器人"]
    if(str(userid)!="651394087009648640"):
        print(username,userid,msg)
        if(msg.startswith("!卡")):
            await add(message)
        if msg=="!list":
            await l(message)
        if (msg.startswith("!下")):
            await delete(message)
        if (msg.startswith("!e")):
            await edit(message)
        if msg=="!help":
            await h(message)
        if (msg.startswith("!c")):
            await seccc(message)
        if (msg.startswith("!a")):
            await secc(message)
        if msg == '!高木' :
            await tree(message)
        if msg == '和我說一遍' :
            await tree1(message)
        if (msg.startswith("!分")):
            await boss(message)
        if(str(message.author.id) == '438616726524002304'):
          if str(message.channel) in channels:
            await message.channel.send(file = d)
        if (msg.startswith ('!出')):
          await kevin(message)
        if(str(message.author.id) == '537926759769702400'):
          if "<@!"+str(438616726524002304)+">" in msg:
            await message.channel.send(file = b)
        if msg == "小智來報刀":
          await jk(message)
bot.run(token4_MS_機器人.getToken())
