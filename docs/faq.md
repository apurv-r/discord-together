# Frequently Asked Questions

!!! question "Can I create my own activity?"
    As of right now, only activities sanctioned by Discord are allowed to be used through the package. If any more activity ID's are available, the package will be updated to include them.

!!! question "I am receiving an error saying 'Activity Ended' when I click the invite link."
    This can be caused due to too many people clicking the invite link at once. Remember, only one person needs to click the invite link and others can join by clicking the 'Play' button.

!!! question "The package is giving out invalid invite links."
    If this ever happens, you can turn on debug mode by heading over to the `DiscordTogether()` constructor and adding a kwarg named `debug=True`. Once debug mode is active, the package will send you the json result that it receives from Discord API. The result will contain information for us to isolate the issue and try to fix it. `v1.0.8` and above has error handlers for most of the commonly found false invite link causes.

!!! question "The party games / voice activities do not work on my device."
    As mentioned in the package description, this is still a BETA feature. As of writing this, it is only supported for updated PC versions of Discord and web versions of Discord.

!!! question "The party games / voice activities aren't loading."
    It is possible that Discord Together applications may not load sometimes. To fix this go into settings and Authorized Apps. Then remove whichever app that isn't loading, eg: Watch Together, Poker Night etc. After that fully close and reopen Discord. This should fix the issue.

!!! question "My invites show 'The user has been banned from this guild' whenever I make a new invite."
    This can happen if you have any alt accounts/bots banned from that server since Discord bans users via IP. So you would have to unban these accounts/bots to get your invites working again.