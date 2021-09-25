from aiohttp import ClientSession
from discord import Client, AutoShardedClient
from discord.ext.commands import Bot, AutoShardedBot, BotMissingPermissions
from discord.http import Route
from typing import Union, Optional
from .errors import InvalidChannelID, InvalidActivityChoice, InvalidCustomID, RangeExceeded


defaultApplications = { 
    # Credits to RemyK888
    'youtube': '755600276941176913',
    'poker': '755827207812677713',
    'betrayal': '773336526917861400',
    'fishing': '814288819477020702',
    'chess': '832012774040141894',
    # Credits to awesomehet2124
    'letter-tile': '879863686565621790',
    'word-snack': '879863976006127627',
    'doodle-crew': '878067389634314250'
}

class ActivityLink:
    """
    Holds three variations of the invite link. Without any attributes, returns complete http link (https://discord.gg/invite_code)
    ----------
    Attributes
    - short_link
        Returns (discord.gg/invite_code)
    - raw_code
        Returns (raw_code)
    """
    def __init__(self, inviteCode : str):
        self.raw_code = inviteCode
        self.short_link = f"discord.gg/{inviteCode}"
    def __str__(self):
        return f"https://discord.gg/{self.raw_code}"

class DiscordTogether:
    """
    Controls invite generations.
    
    Parameters
    ----------
    client/bot: Union[:class:`discord.Client`, :class:`discord.AutoShardedClient`, :class:`commands.Bot`, :class:`commands.AutoShardedBot`]
        The client/bot variable used for your project
    debug: :class:`bool` 
        (default = False) Debug mode toggle
    
    Methods
    -------
    create_link(voiceChannelID : int, option : str)

    Attributes
    -------
    default_choices
        Gives all the default application choices that you have
    """

    default_choices = list(defaultApplications.keys())

    def __init__(self, client: Union[Client, Bot, AutoShardedClient, AutoShardedBot], *, debug: Optional[bool] = False):
        """
        Controls invite generations.

        Parameters
        ----------
        client: Union[:class:`discord.Client`, :class:`discord.ext.Bot`]
            The client/bot variable used for your project
        debug: Optional[:class:`bool`]
            Debug mode toggle, used to identify error code in case of invalid invite links.
            Default value is false.
        
        Methods
        -------
        create_link(voiceChannelID : int, option : str, *, max_age : Optional[int], max_uses : Optional[int])
            Creates a invite link
        """

        if isinstance(client, (Client, AutoShardedClient, Bot, AutoShardedBot)):
            self.client = client
        else:
            raise ValueError("The client/bot object parameter is not valid.")
        
        if isinstance(debug, bool):
            self.debug = debug
        else:
            self.debug = False
            print('\033[93m'+"[WARN] (discord-together) Debug parameter did not receive a bool object. Reverting to Debug = False."+'\033[0m') 
        
    
    async def create_link(self, voiceChannelID: Union[int,str], option: Union[int,str], *, max_age: Optional[int] = 0, max_uses: Optional[int] = 0) -> ActivityLink:
        """
        Generates an invite link to a VC with the Discord Party VC Feature.

        Parameters
        ----------
        voiceChannelID: Union[:class:`str`, :class:`int`]
            ID of the voice channel to create the activity for
        option: Union[:class:`str`, :class:`int`]
            A option amongst the predefined choices (DiscordTogether.default_choices) or a custom ID
        max_age: Optional[:class:`int`]
            Optional duration in seconds after which the invite expires. 
            Value has to be between 0 (Unlimited) and 604800 (7 days), default is 86400 (24 hrs).
        max_uses: Optional[:class:`int`]
            Optional maximum number of times this invite can be used.
            Value has to be between 0 to 100, default is 0 (Unlimited).
        
        Returns
        ----------
        :class:`ActivityLink`
            A class that contains the discord invite link which, upon clicked, starts the custom activity in the VC. 
        """
        
        # Type checks
        if not isinstance(voiceChannelID, (str,int)):
            raise TypeError(f"'voiceChannelID' argument MUST be of type string or integer, not a {type(voiceChannelID).__name__!r} type.")
        if not isinstance(option, (str,int)):
            raise TypeError(f"'option' argument MUST be of type string or integer, not a {type(option).__name__!r} type.")
        
        # Max Range checks
        if not 0 <= max_age <= 604800:
            raise RangeExceeded(f'max_age parameter value should be an integer between 0 and 604800')
        if not 0 <= max_uses <= 100:
            raise RangeExceeded(f'max_uses parameter value should be an integer between 0 and 100')

        # Pre Defined Application ID
        if option and (str(option).lower().replace(" ", "") in defaultApplications.keys()):   

            data = {
                'max_age': max_age,
                'max_uses': max_uses,
                'target_application_id': defaultApplications[str(option).lower().replace(" ","")],
                'target_type': 2,
                'temporary': False,
                'validate': None
            }
            
            try:
                result = await self.client.http.request(
                    Route("POST", f"/channels/{voiceChannelID}/invites"), json = data
                )
            #Error Handling
            except Exception as e:
                if self.debug:
                    async with ClientSession() as session:  
                        async with session.post(f"https://discord.com/api/v8/channels/{voiceChannelID}/invites",
                                        json=data, 
                                        headers = {
                                            'Authorization': f'Bot {self.client.http.token}',
                                            'Content-Type': 'application/json'
                                        }
                                    ) as resp:
                            result = await resp.json()
                    print('\033[95m'+'\033[1m'+'[DEBUG] (discord-together) Response Output:\n'+'\033[0m'+str(result))

                if e.code == 10003 or "channel_id: snowflake value" in e.text:
                    raise InvalidChannelID("Voice Channel ID is invalid.")
                elif e.code == 50013:
                    raise BotMissingPermissions(["CREATE_INSTANT_INVITE"])  
                elif e.code == 130000:
                    raise ConnectionError("API resource is currently overloaded. Try again a little later.")      
                else:
                    raise ConnectionError(f"[status: {e.status}] (code: {e.code}) : An unknown error occurred while retrieving data from Discord API.")

            if self.debug:
                print('\033[95m'+'\033[1m'+'[DEBUG] (discord-together) Response Output:\n'+'\033[0m'+str(result))
            
            return ActivityLink(result['code'])



        # User Defined Application ID
        elif option and (str(option).replace(" ", "") not in defaultApplications.keys()) and str(option).replace(" ","").isnumeric():
            
            data = {
                'max_age': max_age,
                'max_uses': max_uses,
                'target_application_id': str(option).replace(" ", ""),
                'target_type': 2,
                'temporary': False,
                'validate': None
            }

            try:
                result = await self.client.http.request(
                    Route("POST", f"/channels/{voiceChannelID}/invites"), json = data
                )
            # Error Handling
            except Exception as e:
                if self.debug:
                    async with ClientSession() as session:  
                        async with session.post(f"https://discord.com/api/v8/channels/{voiceChannelID}/invites",
                                        json=data, 
                                        headers = {
                                            'Authorization': f'Bot {self.client.http.token}',
                                            'Content-Type': 'application/json'
                                        }
                                    ) as resp:
                            result = await resp.json()
                    print('\033[95m'+'\033[1m'+'[DEBUG] (discord-together) Response Output:\n'+'\033[0m'+str(result))

                if e.code == 10003 or "channel_id: snowflake value" in e.text:
                    raise InvalidChannelID("Voice Channel ID is invalid.")
                elif "target_application_id" in e.text:
                    raise InvalidCustomID(str(option).replace(" ", "")+" is an invalid custom application ID.")
                elif e.code == 50013:
                    raise BotMissingPermissions(["CREATE_INSTANT_INVITE"])  
                elif e.code == 130000:
                    raise ConnectionError("API resource is currently overloaded. Try again a little later.")      
                else:
                    raise ConnectionError(f"[status: {e.status}] (code: {e.code}) : An unknown error occurred while retrieving data from Discord API.")

            if self.debug:
                print('\033[95m'+'\033[1m'+'[DEBUG] (discord-together) Response Output:\n'+'\033[0m'+str(result))

            return ActivityLink(result['code'])
        
        else:
            raise InvalidActivityChoice("Invalid activity option chosen. You may only choose between (\"{}\") or input a custom application ID.".format('", "'.join(defaultApplications.keys())))
