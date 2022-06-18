#A bot that you can ask for memes for, it is CURRENTLY non functional (there's a bug I need to fix but I haven't used it for 2 years so why bother) this was written in the present

import discord 
from keep_alive import keep_alive
import os
import json
import requests 
import random
import time
client = discord.Client()

@client.event


async def on_ready():
  print("ya boi memer is back")
  


a = 0
@client.event
async def on_message(message):
  print(message.author)
  print(message.content)
  YourMessage = input('send your message')
  await message.send(YourMessage)
  if message.author == client.user:
    return
while True:
  if a == 0:
    SendMessage = input("send your message")
    a = input("a")
    message.channel.send(SendMessage)

 #idiotic swear filter (kinda) ↓ ↓ ↓ 
  ''''
  if message.content.startswith('/d start'):
    await message.channel.send("BISH I SWARE IF U SAY FREAKING UWU I WILL BAN YO DUM AS")
 

  if message.content.startswith ("fuck"):
    await message.channel.send("STAP I WILL BAN YOU")

  if message.content.startswith ("bitch"):
    await message.channel.send("STAP I WILL BAN YOU")

  if message.content.startswith ("shit"):
    await message.channel.send("STAP I WILL BAN YOU")


  if message.content.startswith ("cock"):
    await message.channel.send("STAP I WILL BAN YOU")
  if message.content.startswith ("cock"):
    await message.channel.send("STAP I WILL BAN YOU")
    
  



    if message.content.startswith ("!lememeboicommands"):
      await message.channel.send('meme')
      await message.channel.send('insult Thedansquad')
      await message.channel.send('DONT SAY UWU GODDAM IT')
  

  if message.content.startswith('!insult yair'):
    b = random.randint(1,3)

    if b == 1:
      await message.channel.send('yairttheking ur not gae')
    if b == 2:
      await message.channel.send('yairttheking ur so dog water')
    if b == 3:
      await message.channel.send('@yairttheking ur a filthy rage simper')

  if message.content.startswith('!insult thedansquad'):
    time.sleep(3)
    a = random.randint(1,3)

    if a == 1:
      await message.channel.send('@Thedansquad#9600 your a nice person at times')
    if a == 2:
      await message.channel.send('your pretty damn smart')
    if a == 3:
      await message.channel.send('@Thedansquad#9600 your not annoying')
  
  if message.content.startswith('!meme'):
    Sovietglory = random.randint(1,420)
    r = random.randint(1,30)
    
    if r == 1:
      await message.channel.send('https://www.youtube.com/watch?v=SNTGRhVgNrU')
    
    if r == 2:
      await message.channel.send('https://www.youtube.com/watch?v=2RLXWlCIYDo')
    if r == 3:
      await message.channel.send('https://www.youtube.com/watch?v=X4UdnWoK754')
    if r == 4:
      await message.channel.send('https://www.youtube.com/watch?v=eEa3vDXatXg')
    if r == 5:
      await message.channel.send('https://www.youtube.com/watch?v=TsHrJM1AExc')
    if r == 6:
      await message.channel.send('https://www.youtube.com/watch?v=YUK30QROXtc')
    if r == 7:
      await message.channel.send('https://www.youtube.com/watch?v=YUK30QROXtc')
    if r == 8:
      await message.channel.send('https://www.youtube.com/watch?v=T23s3O6iSiU')
    if r == 9:
      await message.channel.send('https://www.youtube.com/watch?v=mHB5yzcz7xY')
    if r == 10:
      await message.channel.send('https://www.youtube.com/watch?v=F2r1dS93Wdw')
    if r == 11:
      await message.channel.send('https://www.youtube.com/watch?v=F2XzU1esuFY')
    if r == 12:
      await message.channel.send('https://www.youtube.com/watch?v=j8qp3ITVqY0')
    ('https://www.youtube.com/watch?v=TiC8pig6PGE')
    if r == 13:
      await message.channel.send('https://www.youtube.com/watch?v=fMCN-b0ic_k')
 
    if r == 15:
      await message.channel.send('https://www.youtube.com/watch?v=T3qrj4B08sc')
    if r == 16:
      await message.channel.send('https://www.youtube.com/watch?v=7zpxgyG7eGk')
    if r == 17:
      await message.channel.send('https://www.youtube.com/watch?v=FO3tpxxdzko')
    if r == 18:
      await message.channel.send('https://www.youtube.com/watch?v=E94f_b92wl4')
    if r == 19:
      await message.channel.send('https://www.youtube.com/watch?v=Kt6mv_gnKxY')
    if r == 20:
      await message.channel.send('https://www.youtube.com/watch?v=0MW0mDZysxc')
    if r == 21:
      await message.channel.send('https://www.youtube.com/watch?v=c7BVtGnlxT8')
    if r == 22:
      await message.channel.send('https://www.youtube.com/watch?v=IdoD2147Fik')
    if r == 23:
      await message.channel.send('https://www.youtube.com/watch?v=wZdfyQJ40nQ')
    if r == 24:
      await message.channel.send('https://www.youtube.com/watch?v=6-7NDP8V-6A')
    if r == 25:
      await message.channel.send('https://www.youtube.com/watch?v=iIgEWRb61IQ')
    
    if Sovietglory == 69:
      await message.channel.send('https://www.youtube.com/watch?v=U06jlgpMtQs')
      await message.channel.send('SOVIET GLORY')
    if Sovietglory == 420:
      await message.channel.send('https://www.youtube.com/watch?v=kPu-yI3baLs')
      
      

client.run(os.getenv('TOKEN'))  
keep_alive()
'''
