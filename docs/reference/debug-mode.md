DiscordTogether provides a way for you to assess problems that may arise when creating invite links.

Debug mode is best used when the package is returning invalid invite codes without raising any errors.

## Usage of Debug Mode
``` python linenums="1"
from discord.ext import commands
from discord_together import DiscordTogether

client = commands.Bot(command_prefix="~")

@client.event
async def on_ready():
    print(f"Bot logged into {client.user}.")
    client.togetherControl = await DiscordTogether("BOT_TOKEN_HERE", debug=True)
    # Debug kwarg set to True


@client.command()
async def start(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")

client.run("BOT_TOKEN_HERE")
```

Now, whenever you run the `create_link` method, the package will print the JSON output that is returned by Discord's API.

It will look something like this:
<figure markdown> 
  ![Debug Mode Success](https://media.discordapp.net/attachments/678298437854298122/898239076048732170/assets2F-MfXMFAe3HfRR02VFC_W2F-MfbnPjhNzgknKnSkssi2F-Mfbt4uX7pJKC7sJ9mPY2FIMlF.png?width=990&height=182)
  <figcaption>a debug output for a successful invite creation</figcaption>
</figure>
<figure markdown> 
  ![Debug Mode Error](https://media.discordapp.net/attachments/678298437854298122/898827804051906590/assets2F-MfXMFAe3HfRR02VFC_W2F-MfbzKdCNsMgvB8Tur5A2F-Mfc0AL6Sbm8zrIpneBP2Fg342.png?width=994&height=94)
  <figcaption>a debug output for an unsuccessful invite creation</figcaption>
</figure>

These JSON response outputs may be difficult to read or understand but they provide vital information to help point out the cause of the error.

It isn't advisable to keep debug mode set to `True` during deployment, only use it during development. You may turn it off once you know your problem is solved.