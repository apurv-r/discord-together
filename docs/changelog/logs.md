# Logs

## v1.2.2 <small>- 2021/11/06</small>
* Added 2 new activities
    * > Awkword (awkword)
    * > Checkers in the Park (checkers)

## v1.2.1 <small>- 2021/10/20</small>
* Added SpellCast to default activities
* Fixed a bug with ConnectionError

## v1.2.0 <small>- 2021/10/15</small>
* Rewrite of entire backend to support any fork of discord.py, now supports any fork
* Removed ActivityLink class, replaced with string output
* Optimized error handling by removing redundant custom errors
* Updated Watch Together's application ID

## v1.1.2 <small>- 2021/09/25</small>
* Added 3 new activities (Credits to @awesomehet2124)
    * > Letter Tile (letter-tile)
    * > Word Snack (word-snack)
    * > Doodle Crew (doodle-crew)
* Added DiscordTogether.default_choices attribute to list all default application choices as a listGeneral optimizations

## v1.1.1 <small>- 2021/07/29</small>
* Added Python 3.6 and above support!
* Added docs and discord server badges to README.md
* Added max_age and max_uses kwargs to create_link()
* Added InvalidCustomID and RangeExceeded custom errors.
* Updated the application ID for 'CG 2 Dev' which is now 'Chess in the Park'
* Created ActivityLink object that is returned after using create_link.
* Fixed debug mode outputs not appearing for custom ID attempts.
* Optimized code and fixed redundancies.

## v1.1.0 <small>- 2021/07/03</small>
* Switched to using Semantic Versioning for this package. (Reason for the version jump)
* Fixed a TypeError caused by inputting options with uppercase letters / strings with spaces in them.
* Fixed typos within files.
* Added a Type check for both parameters of create_link()

## v1.0.8 <small>- 2021/07/02</small>
Pretty big update after taking suggestions and feedback from the package end-users.

* Switched from a new aiohttp session to using the bot's aiohttp session (Thanks to @Hunter2807)
* Added support for AutoShardedClient and AutoShardedBot (Thanks @NotFlameDev)
* Added custom errors to make error handling easier
* Updated README.md with better advisory notes and documentation
* Optimized a few parts of the code
* Added a debug mode kwarg that sends the JSON result attained from the API. This should be used in the case of invalid invite links being sent out.
``` python
togetherControl = DiscordTogether(client, debug=True)
```