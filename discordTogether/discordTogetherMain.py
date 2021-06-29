import aiohttp
from discord import Client, InvalidArgument, utils, AutoShardedClient
from discord.ext.commands import Bot, AutoShardedBot
from typing import Union

defaultApplications = {                  # Credits to RemyK888
    'youtube':'755600276941176913', 
    'poker':'755827207812677713',
    'betrayal':'773336526917861400',
    'fishing':'814288819477020702',
    'chess':'832012586023256104'
}

class DiscordTogether:
    """
    Controls invite generations.
    ...
    Attributes
    ----------
    client/bot : discord.Client/commands.Bot/discord.AutoShardedClient/commands.AutoShardedBot
          The client/bot variable used for your bot project.
    Methods
    -------
    create_link(option, voiceChannelID, voiceChannelName, guildID):
        Generates a invite link to a VC with the Discord Party VC Feature.
    """

    def __init__(self, client : Union[Client, Bot, AutoShardedClient, AutoShardedBot]):
        """
        Constructs necessary discord.Client/discord.bot attribute.
        Parameters
        ----------
            client/bot : discord.Client/commands.Bot/discord.AutoShardedClient/commands.AutoShardedBot
          The client/bot variable used for your bot project.
        """

        if client:
            try:
                self.client = client
            except:
                raise AttributeError("The client variable inputted has no \"token\" attribute.")
        else:
            raise ValueError("Valid bot token parameter is needed.")
    
    async def create_link(self, option, voiceChannelID: int = None, voiceChannelName: str = None, guildID: int = None):
        '''
        Generates a invite link to a VC with the Discord Party VC Feature.
        Parameters:
                option (str): A option amongst the predefined choices ("youtube","poker","betrayal","fishing","chess")
                voiceChannelID (int) (Defaults to None): ID of the voice channel to create the activity for
                voiceChannelName (str) (Defaults to None): The name of the Voice Channel. If this is provided, the Guild ID should also be provided
                guildID (int) (Defaults to None): The ID of the guild in which the command is being executed. Required if voiceChannelName is provided
        Returns:
                invite_link (str): A discord invite link which, upon clicked, starts the custom activity in the VC.
        '''
        if guildID is None and voiceChannelName is not None:
            raise ValueError("Please provide a valid Guild ID because the Voice Channel Name is provided")
        if guildID is not None and voiceChannelName is None:
            continue
        if guildID is not None and voiceChannelName is not None and voiceChannelID is None:
            guild = self.client.get_guild(guildID)
            vcObject = utils.get(guild.voice_channels, name=voiceChannelName)
            if vcObject is None:
                raise ValueError("Please make sure the Voice Channel name and Guild ID is/are correct")
            if vcObject is not None:
                voiceChannelID = vcObject.id
        if voiceChannelID is not None and voiceChannelName is None and guildID is None:
            continue
        # Pre Defined Application ID
        if option and (str(option).lower().replace(" ","") in defaultApplications.keys()):
            async with aiohttp.ClientSession() as session:         # Credits to VineyS for updating code with aiohttp
                async with session.post(f"https://discord.com/api/v8/channels/{voiceChannelID}/invites",
                                json={
                                    'max_age': 86400,
                                    'max_uses': 0,
                                    'target_application_id': defaultApplications[option],
                                    'target_type': 2,
                                    'temporary': False,
                                    'validate': None
                                }, 
                                headers = {
                                    'Authorization': f'Bot {self.client.http.token}',
                                    'Content-Type': 'application/json'
                                }
                            ) as resp:
                    result = await resp.json()
            if ("errors" in result.keys()) or ("code" not in result.keys()):
                raise ConnectionError("An error occured while retrieving data from Discord API.")
            else:
                return f"https://discord.com/invite/{result['code']}"

        # User Defined Application ID
        elif option and (str(option).lower().replace(""," ") not in defaultApplications.keys()):
            async with aiohttp.ClientSession() as session:         # Credits to VineyS for updating code with aiohttp
                async with session.post(f"https://discord.com/api/v8/channels/{voiceChannelID}/invites",
                                json={
                                    'max_age': 86400,
                                    'max_uses': 0,
                                    'target_application_id': str(option),
                                    'target_type': 2,
                                    'temporary': False,
                                    'validate': None
                                }, 
                                headers = {
                                    'Authorization': f'Bot {self.client.http.token}',
                                    'Content-Type': 'application/json'
                                }
                            ) as resp:
                    result = await resp.json()
            if ("errors" in result.keys()) or ("code" not in result.keys()):
                if "target_application_id" in result['errors'].keys():
                    raise InvalidArgument(f"\"{str(option)}\" is an invalid custom application ID.")
                else:
                    raise ConnectionError("An error occured while retrieving data from Discord API.")
            else:
                return f"https://discord.com/invite/{result['code']}"
        else:
            raise InvalidArgument("Invalid activity option chosen. You may only choose between (\"youtube\",\"poker\",\"chess\",\"fishing\",\"betrayal\") or input a custom application ID as a string.")
