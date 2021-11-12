All the errors that can be raised when you create a invite link.

|<span style="font-size: 1.5em">**discordTogether.errors.InvalidArgument**</span>|
| :---------------------------- |
|Raised when an invalid argument was entered.<br><br>This error can be raised when:<ul style="margin: 5px 0;"><li>Voice Channel ID is incorrect/invalid</li><li>Application name entered was not found within the default applications list</li><li>Custom Application ID was incorrect/invalid</li></ul>|

|<span style="font-size: 1.5em">**discordTogether.errors.RangeExceeded**</span>|
| :---------------------------- |
|Raised when the allowed ranges for max_age and max_uses parameters were exceeded.|

|<span style="font-size: 1.5em">**discordTogether.errors.BotMissingPerms**</span>|
| :---------------------------- |
|Raised when your bot does not have CREATE_INSTANT_INVITE permissions for that specific channel.|

|<span style="font-size: 1.5em">**discordTogether.errors.ConnectionError**</span>|
| :---------------------------- |
|Raised when a general error occured while communicating with Discord API.|