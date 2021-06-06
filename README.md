<h1><strong>Discord Together</strong></h1>

![PyPI - Downloads](https://img.shields.io/pypi/dm/discord-together?style=flat&logo=acclaim)
![Made for discord.py](https://img.shields.io/badge/Made%20for-discord.py-blue?style=flat&logo=discord)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# 👋 Welcome!
### Discord has released a BETA feature that they call Discord Party Games to only a certain hand-picked servers. This module allows you to temporarily enable such features for your servers! 

<br/>

# 🔩 Installation
## Install [discord-together](https://pypi.org/project/discord-together/)
```
pip install discord-together
```

#### Package dependencies include [discord.py](https://pypi.org/project/discord.py/) and [aiohttp](https://pypi.org/project/aiohttp/)
<br/>

# 🔑 Features
- Easy to use
- Dynamic
- Actively maintained
- [discord.py](https://pypi.org/project/discord.py/) support
- Lightweight

<br/>

# 💻 Code example
This is a simple example of code using this package.

```py
from discord.ext import commands
from discordTogether import DiscordTogether

client = commands.Bot(command_prefix="~")
togetherControl = DiscordTogether(client)

@client.event
async def on_ready():
    print(f"Bot logged into {client.user}.")

@client.command()
async def startYT(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")

client.run("BOT_TOKEN_HERE")
```
<br/>

# 🔧 Options
- **Youtube**
```py
link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
```

- **Poker**
```py
link = await togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
```

- **Chess**
```py
link = await togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
```

- **Betrayal**
```py
link = togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
```

- **Fishing**
```py
link = togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
```

# 📷 Image 

![Invite link](https://cdn.discordapp.com/attachments/450659049659170817/850783760009658389/Screenshot_2021-06-04_231039_3.png)

### *Note: you have to click on the **BLUE LINK**, <u>not the 'Play' button</u>, in order to start the activity !*

<br/>

![YouTube Together](https://cdn.discordapp.com/attachments/450659049659170817/850782952724234290/Screenshot_2021-06-04_231612.png)

<br/>

# 🚀 Others

**This package is under MIT license.**

*Note: This package is not affiliated with Discord or YouTube.*

If you have any problems, you can contact: `Bxllistic#4444`.
(*Discord server will be made if needed.*)

This project was converted to support `discord.py` from the npm package [discord-together](https://www.npmjs.com/package/discord-together) made by [RemyK888](https://github.com/RemyK888)


[**Github repository**](https://github.com/apurv-r/discord-together)

<hr>

## **Made with ❤ by Bxllistic#4444**
#### Credits to RemyK888 for application IDs and foundations

