import requests
from discord import Client, InvalidArgument
from discord.ext.commands import Bot
from typing import Union

defaultApplications = {                  # Credits to RemyK888
    'youtube':'755600276941176913', 
    'poker':'755827207812677713',
    'betrayal':'773336526917861400',
    'fishing':'814288819477020702',
    'chess':'832012586023256104'
}

class DiscordTogether():
    """
    Controls invite generations.

    ...

    Attributes
    ----------
    client/bot : discord.Client/discord.Bot
        The client/bot variable used for your bot project.

    Methods
    -------
    create_link(voiceChannelID, option):
        Generates a invite link to a VC with the Discord Party VC Feature.
    """

    def __init__(self, client : Union[Client, Bot]):
        """
        Constructs necessary discord.Client/discord.bot attribute.

        Parameters
        ----------
            client/bot : discord.Client/discord.Bot
                The client/bot variable used for your bot project.

        """

        if client:
            try:
                self.token = client.http.token
            except:
                raise AttributeError("The client variable inputted has no \"token\" attribute.")
        else:
            raise ValueError("Valid bot token parameter is needed.")
    
    def create_link(self, voiceChannelID, option):
        '''
        Generates a invite link to a VC with the Discord Party VC Feature.

        Parameters:
                voiceChannelID (int): ID of the voice channel to create the activity for
                option (str): A option amongst the predefined choices ("youtube","poker","betrayal","fishing","chess")

        Returns:
                invite_link (str): A discord invite link which, upon clicked, starts the custom activity in the VC.
        '''
        
        if option and (option.lower().replace(" ","") in defaultApplications.keys()):
            r = requests.post(f"https://discord.com/api/v8/channels/{voiceChannelID}/invites",
                                json={
                                    'max_age': 86400,
                                    'max_uses': 0,
                                    'target_application_id': defaultApplications[option],
                                    'target_type': 2,
                                    'temporary': False,
                                    'validate': None
                                }, 
                                headers = {
                                    'Authorization': f'Bot {self.token}',
                                    'Content-Type': 'application/json'
                                }
                            )
            result = r.json()
            if result["errors"] or ("code" not in result.keys()):
                raise ConnectionError("An error occured while retrieving data from Discord API.")
            else:
                return f"https://discord.com/invite/{result['code']}"
        else:
            raise InvalidArgument("Invalid activity option chosen. You may only choose between (\"youtube\",\"poker\",\"chess\",\"fishing\",\"betrayal\")")
