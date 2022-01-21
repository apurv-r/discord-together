### Steps to setup

Using discord-together is quite simple.

* First, import the DiscordTogether constructor
``` python
from discord_together import DiscordTogether
```
* Next, create a variable to store the class instance. This variable must be defined in a async function, like on_ready()
``` python
@client.event
async def on_ready():
    client.togetherControl = await DiscordTogether("BOT_TOKEN_HERE")
    # This creates a bot variable. You can also use the global keyword here instead.
```
* Finally, you can use the `create_link` function
``` python
@client.command()
async def start(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")
```

<hr>
Here are some examples to add further clarity:

### within your bot.py file <small>(using dpy 1.7.2)</small>
``` python linenums="1"
from discord.ext import commands
from discord_together import DiscordTogether

client = commands.Bot(command_prefix="~")

@client.event
async def on_ready():
    print(f"Bot logged into {client.user}.")
    client.togetherControl = await DiscordTogether("BOT_TOKEN_HERE")
    # This makes a bot variable that can be used anywhere within your bot's code, even within cogs.

@client.command()
async def start(ctx):
    # Here we consider that the user is already in a VC accessible to the bot.
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")

client.run("BOT_TOKEN_HERE")
```

### within any cogs
``` python linenums="1"
from discord.ext import commands
from discord_together import DiscordTogether

class YoutubeTogetherCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.togetherControl = await DiscordTogether("BOT_TOKEN_HERE") 
        # Remember to only use this if you haven't already made a bot variable for `togetherControl` in your bot.py file.
        # If you have already declared a bot variable for it, you can use `self.client.togetherControl` to access it's functions
    
    @commands.command()
    async def start(self, ctx):
        # Here we consider that the user is already in a VC accessible to the bot.
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.send(f"Click the blue link!\n{link}")

def setup(client):
    client.add_cog(YoutubeTogetherCog(client))
```

!!! info
    If your discord.py fork supports it, you can even use `client.http.token` instead of inputting your actual token string into the DiscordTogether class constructor.
    ``` python
    client.togetherControl = await DiscordTogether(client.http.token)
    ```


<figure markdown> 
  ![Invite Example](https://media.discordapp.net/attachments/678298437854298122/897822880396623882/assets2F-MfXMFAe3HfRR02VFC_W2F-MfYXzH1YYW63qW0Hl992F-MfYlVJWaEHV2sTBTi2u2F68747470733a2f2f63646e2e64.png?width=492&height=268){ width="500" }
  <figcaption>Voila! An invite into the future of Discord</figcaption>
</figure>

That's an invite created!

Before we continue, let's clarify what we just did:

* `DiscordTogether(token)` is used to initialize the DiscordTogether instance. This allows the module to authorize the request with your bot's credentials when sent to Discord's API. It does not interfere any of the bot's properties. The package uses a token rather than just a bot variable to allow support for any fork of discord.py
* `create_link()`  is the only function within this library. It's purpose is to create an invite link into the application that you entered as an argument. Find more insight into using this method here

That would conclude the quick setup guide for DiscordTogether.

!!! warning "Advisory Note"
    At least one person needs to click on the BLUE LINK, not the 'Play' button, in order to start the activity. Once the activity is started, people can join by clicking 'Play'. 

    Multiple people clicking the blue link at once can cause a "Activity Ended" error screen, however it's not a common occurrence.