Communicates with Discord API and returns the invite link for the specific application requested. Needs to be in an *async* function.

## Parameters

|<span style="font-size: 1.8em">**voiceChannel_ID**</span>|
| :---------------------------- |
|ID of the voice channel that the invite link will point at.<br><br>**Type:** `str` or `int`|

|<span style="font-size: 1.8em">**application**</span>|
| :---------------------------- |
|The VC activity/application that you want to create an invite for.<br><br>**Type:** `str` (for pre-defined applications) or `int` (for custom IDs)|
|<span style="font-size: 1.2em">_Pre-defined applications_</span><br>These are the applications/activities that currently come with the discord-together package.<br>These currently include:<table style="width:40%"><tbody><tr><td>Watch Together</td><td>**`youtube`**</td></tr><tr><td>Poker Night</td><td>**`poker`</td>**</tr><tr><td>Chess in the Park</td><td>**`chess`**</td></tr><tr><td>Betrayal.io</td><td>**`betrayal`**</td></tr><tr><td>Fishington.io</td><td>**`fishing`**</td></tr><tr><td>Letter Tile</td><td>**`letter-tile`**</td></tr><tr><td>Word Snack</td><td>**`word-snack`**</td></tr><tr><td>Doodle Crew</td><td>**`doodle-crew`**</td></tr><tr><td>SpellCast</td><td>**`spellcast`**</td></tr><tr><td>Awkword</td><td>**`awkword`**</td></tr><tr><td>Checkers in the Park</td><td>**`checkers`**</td></tr></tbody></table>Use the text in the (brackets) as the application parameter<br><br><br><span style="font-size: 1.2em">_Custom application IDs_</span><br>This is a advanced feature brought by the package which allows you to create links for applications that may not be included default. This option requires you to have the ID for the application. For example, YouTube Together uses the ID `880218394199220334`.<br>So, if you do have the ID, you can use this option in the format that will be coming up under Examples.|

|<span style="font-size: 1.8em">**max_age**</span>&zwnj; &zwnj; <a href="#"><img src="https://img.shields.io/badge/kwarg%20only-%E2%9C%94-success?style=flat-square" alt="kwarg-only yes"></a>|
| :---------------------------- |
|Duration in seconds after which the invite expires. Value has to be between 0 (Unlimited) and 604800 (7 days).<br><br>**Type:** `int`<br>**Default:** `86400 (24 hrs)`|

|<span style="font-size: 1.8em">**max_uses**</span>&zwnj; &zwnj; <a href="#"><img src="https://img.shields.io/badge/kwarg%20only-%E2%9C%94-success?style=flat-square" alt="kwarg-only yes"></a>|
| :---------------------------- |
|ID of the voice channel that the invite link will point at.<br><br>**Type:** `int`<br>**Default:** `0 (unlimited)`|

<hr>

## Returns
A `str` containing the invite link you requested for. (`https://discord.gg/INVITE_CODE_HERE`)

<hr>

## Examples
Creating a link for pre-defined applications
``` python
link = await client.togetherControl.create_link(VC_ID_HERE, 'youtube')
await channel.send(link)
```
Creating a link for custom applications using it's ID
``` python
link = await client.togetherControl.create_link(VC_ID_HERE, '000000000000000000')
await channel.send(link)
```

Creating a link with `max_age` keyword argument (kwarg)
``` python
link = await client.togetherControl.create_link(VC_ID_HERE, 'youtube', max_age = 3600)
await channel.send(link)
```

Creating a link with `max_uses` keyword argument (kwarg)
``` python
link = await client.togetherControl.create_link(VC_ID_HERE, 'youtube', max_uses = 5)
await channel.send(link)
```

Creating a link with both `max_age` and `max_uses` kwargs
``` python
link = await client.togetherControl.create_link(VC_ID_HERE, 'youtube', max_age = 3600, max_uses = 5)
await channel.send(link)
```

<hr>

!!! warning
    Remember, all of these VC activities are made/authorized by Discord and are currently in BETA. You can expect to see bugs and issues with the games sometimes. 
    If you see a bug with Poker Night or Chess in the Park, you can report it on Discord's official "Game Lab" [here](https://discord.gg/JkuGUXWVmV).

If you misspell a pre-defined application name or enter an invalid application ID, don't worry! The package has a built-in exception for such cases. Let's take a look at all the exceptions next.