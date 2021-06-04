<center>
<h1><strong>Discord Together</strong></h1>

![PyPI - Downloads](https://img.shields.io/pypi/dm/discordTogether?style=for-the-badge)
![Made for discord.py](https://img.shields.io/badge/Made%20for-discord.py-blue?style=for-the-badge&logo=appveyor)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
</center>



# 🔩 Installation
## Install [discordTogether](https://pypi.org/project/discordTogether/)
```
pip install discordTogether
```

#### Package dependencies include [discord.py](https://pypi.org/project/discord.py/) and [requests](https://pypi.org/project/requests/)
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
import discord
from discordTogether import DiscordTogether

client = discord.Client(prefix="~")
togetherControls = DiscordTogether(client)

@client.event
async def on_ready():
    print(f"Bot logged into {client.user}.")

@client.command()
async def startYT(ctx):
    link = togetherControls.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")
```
<br/>

# 🔧 Options
- **Youtube**
```py
link = togetherControls.create_link(ctx.author.voice.channel.id, 'youtube')
```

- **Poker**
```py
link = togetherControls.create_link(ctx.author.voice.channel.id, 'poker')
```

- **Chess**
```py
link = togetherControls.create_link(ctx.author.voice.channel.id, 'chess')
```

- **Betrayal**
```py
link = togetherControls.create_link(ctx.author.voice.channel.id, 'betrayal')
```

- **Fishing**
```py
link = togetherControls.create_link(ctx.author.voice.channel.id, 'fishing')
```

# 📷 Image 

![Invite link](https://media.discordapp.net/attachments/835896457454026802/837968506846183474/2021-05-01_10h26_17.png)

### *Note: you have to click on the BLUE LINK, not the 'Play' button, in order to start the activity !*

<br/>

![YouTube Together](https://media.discordapp.net/attachments/835896457454026802/837968510843093033/2021-05-01_10h27_31.png?width=1229&height=676)

<br/>

# 🚀 Others

**This package is under MIT license.**

*Note: This package is not affiliated with Discord or YouTube.*

If you have any problems, you can contact: `Bxllistic#4444`.
(*Discord server will be made if needed.*)

This project was converted to support `discord.py` from the npm package [discord-together](https://www.npmjs.com/package/discord-together) made by [RemyK888](https://github.com/RemyK888)


[**Github repository**](https://github.com/apurv-r/discordTogether)

<hr>

## **Made with ❤ by Bxllistic#4444**
#### Credits to RemyK888 for application IDs

