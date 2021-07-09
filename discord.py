import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix="!")
@client.command()
async def mcst(ctx):
    r = requests.get('https://api.minetools.eu/ping/[SERVER-IP-ADDRESS]/[PORT]')
    json_data = r.json()

    max = str(json_data["players"]["max"])
    online = str(json_data["players"]["online"])
    Version = str(json_data["version"]["name"])

    embed = discord.Embed(
        title= "Server Info",

        #description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン:' + Version,
        description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン: [任意のバージョン]', 

        color=discord.Color.dark_green()
    )
    print('コマンドが実行されました。')

    await client.change_presence(activity=discord.Game(name="!mcst"))
    
    embed.set_thumbnail(url="http://minecraft-jp.info/img/logo.png")

    await ctx.send(embed=embed)
    
client.run('DISCORD-BOT-TOKEN')
