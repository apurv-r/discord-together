Represents **DiscordTogether** client instance. Needs to be defined in an *async* function.

## Parameters

|<span style="font-size: 1.8em">**token**</span>|
| :---------------------------- |
|The bot's token to use for Discord API authorization.<br><br>**Type:** `str`|

|<span style="font-size: 1.8em">**debug**</span>&zwnj; &zwnj; <a href="#"><img src="https://img.shields.io/badge/kwarg%20only-%E2%9C%94-success?style=flat-square" alt="kwarg-only yes"></a>|
| :---------------------------- |
|Debug toggle keyword argument. To be used in case of invalid invites being outputted from `DiscordTogether`.<br><br>**Type:** bool<br>**Default:** False|    

## Methods

|<span style="font-size: 1.8em">**create_link(`VC_ID`, `APPLICATION`, `MAX_AGE=0`, `MAX_USES=0`)**</span>|
| :---------------------------- |
|Communicates with Discord API and returns the invite link for the specific application requested.<br><br>Refer [here]() for in-dept information.<br><br>Parameters:<br>- VC_ID<br>The ID of the voice channel that you want to create an invite link to.<br>- APPLICATION<br>The choice of application that you want to create an invite for.<br>- MAX_AGE (kwarg)<br>Optional duration in seconds after which the invite expires.<br>- MAX_USES (kwarg)<br>Optional maximum number of times this invite can be used.<br><br>Returns: `str`|

## Attributes

|<span style="font-size: 1.8em">**default_choices**</span>|
| :---------------------------- |
|Returns a list of all the default activity choices that the package offers.<br><br>**Type:** `list`|
