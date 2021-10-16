# How to upgrade

Upgrade to the latest version with:

```
pip install --upgrade discord-together
```

Show the currently installed version with:

```
pip show discord-together
```

<hr>

## Upgrading from 1.1.x to 1.2.x

### What's new?

- Rewrite of entire backend to support any fork of discord.py
- Removed ActivityLink class
- Optimized error handling

### Changes to import names

The import name for the package was changed due to confusions arising with the capitalizations of the import names:
=== "1.2.x"

    ``` python
    from discord_together import DiscordTogether
    ```

=== "1.1.x"

    ``` python
    from discordTogether import DiscordTogether
    ```

### Changes to `DiscordTogether` class constructor

The DiscordTogether constructor now is async, therefore, it would need to be placed in any async function. This is because the package now created it's own aiohttp session that it uses to communicate with Discord API. It is recommended to define this class within the `on_ready()` function of your bot.py file or in any cog.

Due to removing all discord.py dependencies, the package now requires you to input your bot's token into the constructor instead of your client instance. This is so that the API calls that the package makes are authorized under your bot's credentials.

The togetherControl class instance is now also stored as a bot variable (aka `client.togetherControl`) so that the instance can be used anywhere throughout your bot.

=== "1.2.x"

    ``` python
    client = commands.Bot(command_prefix="~")

    @client.event
    async def on_ready():
        client.togetherControl = await DiscordTogether("TOKEN_HERE")
    ```

=== "1.1.x"

    ``` python
    client = commands.Bot(command_prefix="~")
    togetherControl = DiscordTogether(client)
    ```

### Changes to `create_link()` function

A minor change of using the bot variable instead of just `togetherControl`.

=== "1.2.x"

    ``` python
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    ```

=== "1.1.x"

    ``` python
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    ```