<div align="center">
    <a href="https://pypi.org/project/discord-together"><img src="https://i.ibb.co/nCr7dnf/DT-Logo-New.png" alt="discord-together logo" height="128" style="border-radius: 50%"></a>
    <div>
        <h1><strong>Discord Together</strong></h1>
    </div>
    <div>
        <a href="https://pypi.org/project/discord-together"><img src="https://img.shields.io/pypi/dm/discord-together?color=%23EF0BB9&label= downloads&logo=git lfs&logoColor=fc2a95&?style=flat" alt="discord-together downloads"></a>
        <a href="https://pypi.org/project/discord-together"><img src="https://img.shields.io/pypi/v/discord-together?color=%23EF0BB9&label=version&logo=buffer&?style=flat&logoColor=fc2a95" alt="discord-together version"></a>
        <a href="https://discord.com/invite/2fbyXn2hJV"><img src="https://img.shields.io/discord/860227711402246154.svg?color=%23EF0BB9&label=support server&logo=discord&style=flat&logoColor=fc2a95"></a>
        <a href="https://docs.discord-together.ml"><img src="https://img.shields.io/website?down_color=lightgrey&down_message=offline&label=docs&logo=Read%20the%20Docs&up_color=%23EF0BB9&up_message=online&url=https%3A%2F%2Fdocs.discord-together.ml&logoColor=fc2a95"></a>
    </div>
</div>
<br>
<br>

# 👋 Welcome!
<h3>Discord has released a BETA feature that they call Discord Party Games to only a certain hand-picked servers. This module allows you to temporarily enable such features for your servers!</h3>
<br>

### Use the [docs for discord-together](https://docs.discord-together.ml/) for detailed usage guide.
<br>
<h4>As of  v1.1.2, this BETA feature is only supported on web and updated PC app versions of Discord and is not supported on mobile.</h4>
<br>

# 🔩 Installation
## Install [discord-together](https://pypi.org/project/discord-together/)
```
pip install discord-together
```

#### Package dependencies only include [discord.py](https://pypi.org/project/discord.py/)
<br>

# 🔑 Features
- Easy to use and lightweight
- Actively maintained and updated with latest activites

- Dynamic error handling with custom errors
- Debug mode for invalid invites

<br>

# 💻 Code example
This is a simple example of code using this package.

```py
from discord.ext import commands
from discordTogether import DiscordTogether

client = commands.Bot(command_prefix="~")
togetherControl = DiscordTogether(client)

@client.command()
async def startYT(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")

client.run("BOT_TOKEN_HERE")
```
View the **[docs](https://docs.discord-together.ml/)** for more detailed/advanced examples (like cogs) and explanations!
<br>
<br>

# 📷 Image 

![Invite link](https://cdn.discordapp.com/attachments/678298437854298122/860210951222460446/msedge_Gntg4yflYw.png)

<h3>⚠️ Advisory Note:</h3>
At least one person needs to click on the <strong>BLUE LINK</strong>, not the 'Play' button, in order to start the activity! Once the activity is started, people can join by clicking 'Play'.
<br>
<br>

![YouTube Together](https://cdn.discordapp.com/attachments/678298437854298122/860210751448547328/msedge_HpqALcJCcD.png)

<br>

# 🚀 Others

**This package is under MIT license.** Appropriately tested PR's are more than welcome.

*Note: This package is not affiliated with Discord or YouTube.*

If you have any problems or enquiries, join the [discord-together Support Server](https://discord.gg/2fbyXn2hJV) or you can contact me personally on Discord: `Bxllistic#4444`.

This project was converted to support discord.py from the npm package [discord-together](https://www.npmjs.com/package/discord-together) made by [RemyK888](https://github.com/RemyK888)

<br>
<hr>

## **Made with ❤ by Bxllistic#4444**
Credits to [@RemyK888](https://github.com/RemyK888) for application IDs and foundations
