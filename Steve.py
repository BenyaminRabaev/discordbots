import discord 
import os
import time
import random
client = discord.Client()
a = 4
letterlist = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0','m']
types = ['D','C','B','A','S','S+','d','c','b','a','s','s+']

#This bot is one of my favorites (it is also one of the first i've made) , please excuse how immature and stupid it is




from discord.ext import commands

#
bot = commands.Bot(command_prefix="!")
@bot.command()
async def CryptoPrices(ctx,arg):
  await ctx.send("the price of "+arg+" is currently 69 cents")
@bot.command()
async def DungeonSecrets(ctx):
  await ctx.send("discord.gg/dsg")
@bot.command()
async def BigNoob123(ctx):
  await ctx.send("tee hee big noob (XDDDDDD)")
@bot.command()
async def AM(ctx, arg):
  print(ctx.content)
  await ctx.send(arg)
@bot.command()
async def SteveBan (ctx, member:discord.User=None, reason =None):
  if ctx.author.guild_permissions.administrator:
      if member == None or member == ctx.message.author:
          await ctx.channel.send("You cannot ban yourself")
          return
      if reason == None:
          reason = "For being a big meanie!"
      await ctx.guild.ban(member, reason=reason)
      await ctx.channel.send(f"{member} is banned! C R A B R A V E")
  elif ctx.member.guild_permissions.administrator:
    await ctx.send("LMAO YOU CANT BAN ANOTHER ADMIN NOOB")
  else:
    await ctx.send('lol imagine not having admin XD MOMENT')
    

@bot.command()
async def poggers(conte):
  await conte.channel.purge(limit=1)
  await conte.send("<:pog:823591996698001409>")



@bot.command()
async def SteveClear(continuer,numofmessagestoclear):
  if continuer.author.guild_permissions.administrator:
    await continuer.channel.purge(limit=int(numofmessagestoclear))
  else:
    await continuer.channel.send('you dont have admin srry')
@bot.command()
async def queue(mesag, floor, IGN, tepe):
    channelofyes = bot.get_channel(830087808973537301)
    if tepe in types:
        await mesag.send(
            " queueing you for a floor " + floor + " run, you registered as the IGN of " + IGN + " for a  " + tepe + " run! ")
        await channelofyes.send('<@' + str(mesag.author.id) + ">" + "wants a carry react with (instert reaction here)to accept")
        @bot.event
        async def on_reaction(contur,reaction):
          await contur.send("this is a test")


    else:
        await mesag.send("hmmm didn't work maybe you mispelt something?")



@bot.command()
async def bothelp(meg):
  await meg.send('@everyone')
  time.sleep(0.1)
  await meg.channel.purge(limit=2)
@bot.command()
async def insult(cont,arg):
    

  await cont.channel.purge(limit=1)
  r = random.randint(1,3)
  if r == 1:
    await cont.send("go get a life" + arg)
  if r == 2:
    await cont.send("you are dog water" + arg)
  if r == 3:
    await cont.send("you are so garbage" + arg)
@bot.command()
async def custominsult(context,args):
  await context.channel.purge(limit=1)
  await context.send(args)
@bot.command()
async def test(ctx,Wiewie,x):
  x = int(x)
  a = 0
  try:
    await ctx.channel.purge(limit=1)
    time.sleep(1)
    zecorrectword = ''


  #wiewie is going to be a variable within the message

    zecorrectword = ''
    zecorrectword += Wiewie
    zeguessofzeletter = set()




    zeENPESSANT = set()
    for i in zecorrectword:
      zeENPESSANT.add(i)
    if ' ' in zecorrectword:
      zeENPESSANT.remove(" ")


    while x > 0:
      baggate = ''
      france = ''
      zeguess = 'e'
        
        
      
      

      for i in zecorrectword:
        if i in zeENPESSANT:
          baggate += '- '
        else:
          baggate += i + ' '
      await ctx.send(baggate)  
      franchpeople = len(zeENPESSANT)
      if franchpeople == 0:
        await ctx.send("good job nerd")
        break


    
      await ctx.send('enter a letter')

      ''''
      def check(auth):
        return auth.author.id == ctx.author.id
      '''
      message = await bot.wait_for("message")
    
      if message.content in letterlist:
        a += 1
        zeguess = message.content 

        
      else:
        await ctx.send('THATS NOT A LETTER MORON')
      print(zeguess)
      if zeguess in zeENPESSANT:
        await ctx.send("you have " + str(x) + ' guesses left')
        zeENPESSANT.remove(zeguess)
      else:
        x = x - 1
        await ctx.send("you have " + str(x) + 'guesses left')

  
  except:
    await ctx.send("thats not a command boomer boi")

@bot.command()
async def BecomeFrench(ctx):
  await ctx.send("Haughash haughs Wewiei hah F Ranch en poesant AFahaha FRANch Jaqeus")


bot.run(os.getenv('TOKEN')) 
