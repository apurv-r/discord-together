from discord import Client, AutoShardedClient, InvalidArgument
from discord.ext.commands import Bot, AutoShardedBot, BotMissingPermissions
from discord.http import Route
from typing import Union
from .errors import InvalidChannelID, InvalidActivityChoice


defaultApplications = {  # Credits to RemyK888
    'youtube': '755600276941176913',
    'poker': '755827207812677713',
    'betrayal': '773336526917861400',
    'fishing': '814288819477020702',
    'chess': '832012586023256104'
}

class DiscordTogether:
    """
    Controls invite generations.
    ----------
    Attributes
    - client/bot : discord.Client | discord.AutoShardedClient | commands.Bot | commands.AutoShardedBot
    - debug (bool) (default = False) : Debug mode toggle
    -------
    Methods
    - create_link(voiceChannelID : int, option : str) :
    """

    def __init__(self, client: Union[Client, Bot, AutoShardedClient, AutoShardedBot], **kwargs):
        """
        Controls invite generations.
        ----------
        Attributes
        - client/bot : The client/bot variable used for your project
        - debug (bool) (default = False) : Debug mode toggle => used to identify error code in case of invalid invite links
        -------
        Methods
        - create_link(voiceChannelID : int, option : str) : Creates a invite link
        """

        if isinstance(client, (Client, AutoShardedClient, Bot, AutoShardedBot)):
            self.client = client
        else:
            raise ValueError("The client/bot object parameter is not valid.")
        
        debug = kwargs.get("debug", False)
        if isinstance(debug, bool):
            self.debug = debug
        else:
            self.debug = False
            print('\033[93m'+"[WARN] (discord-together) Debug parameter did not receive a bool object. Reverting to Debug = False."+'\033[0m') 


    async def create_link(self, voiceChannelID: int, option: str) -> str:
        """
        Generates an invite link to a VC with the Discord Party VC Feature.
        ----------
        Parameters:
            - voiceChannelID (int): ID of the voice channel to create the activity for
            - option (str): A option amongst the predefined choices ("youtube","poker","betrayal","fishing","chess") or a custom ID (as str)
        ----------
        Returns:
            - invite_link (str): A discord invite link which, upon clicked, starts the custom activity in the VC.
        """
        
        # Type checks
        if not isinstance(voiceChannelID, (str,int)):
            raise TypeError(f"'voiceChannelID' parameter MUST be of type string or integer, not a \"{type(voiceChannelID).__name__}\" type.")
        if not isinstance(option, (str,int)):
            raise TypeError(f"'option' parameter MUST be of type string or integer, not a \"{type(option).__name__}\" type.")

        # Pre Defined Application ID
        if option and (str(option).lower().replace(" ", "") in defaultApplications.keys()):   

            data = {
                'max_age': 86400,
                'max_uses': 0,
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
                if "10003" in str(e):
                    raise InvalidChannelID("Voice Channel ID is invalid.")
                elif "50013" in str(e):
                    raise BotMissingPermissions(["CREATE_LINK"])  
                elif "130000" in str(e):
                    raise ConnectionError("API resource is currently overloaded. Try again a little later.")      
                else:
                    raise ConnectionError("An error occurred while retrieving data from Discord API.")

            if self.debug:
                print('\033[95m'+'\033[1m'+'[DEBUG] (discord-together) Response Output:\n'+'\033[0m'+str(result))
            
            return f"https://discord.com/invite/{result['code']}"



        # User Defined Application ID
        elif option and (str(option).replace(" ", "") not in defaultApplications.keys()) and str(option).replace(" ","").isnumeric():
            
            data = {
                'max_age': 86400,
                'max_uses': 0,
                'target_application_id': str(option).replace(" ", ""),
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
                if "10003" in str(e):
                    raise InvalidChannelID("Voice Channel ID is invalid.")
                elif "target_application_id" in str(e):
                    option = str(option).replace(" ", "")
                    raise InvalidArgument(f"\"{option}\" is an invalid custom application ID.")
                elif "50013" in str(e):
                    raise BotMissingPermissions(["CREATE_LINK"])  
                elif "130000" in str(e):
                    raise ConnectionError("API resource is currently overloaded. Try again a little later.")      
                else:
                    raise ConnectionError("An error occurred while retrieving data from Discord API.")

            if self.debug:
                print('\033[95m'+'\033[1m'+'[DEBUG] (discord-together) Response Output:\n'+'\033[0m'+str(result))

            return f"https://discord.com/invite/{result['code']}"
        
        else:
            raise InvalidActivityChoice("Invalid activity option chosen. You may only choose between (\"youtube\",\"poker\",\"chess\",\"fishing\",\"betrayal\") or input a custom application ID as a string.")
