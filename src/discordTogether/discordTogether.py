import requests

defaultApplications = {
    'youtube':'755600276941176913', 
    'poker':'755827207812677713',
    'betrayal':'773336526917861400',
    'fishing':'814288819477020702',
    'chess':'832012586023256104'
}

class DiscordTogether():
    def __init__(self, client):
        if client:
            try:
                self.token = client.http.token
            except:
                raise AttributeError("The client variable inputted has no \"token\" attribute.")
        else:
            raise ValueError("Valid bot token parameter is needed.")
    
    def create_link(self, voiceChannelID, option):
        if option and option.lower() in defaultApplications.keys():
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
                                    'Authorization': f'Bot {self.client}',
                                    'Content-Type': 'application/json'
                                }
                            )
            result = r.json()
            if result["errors"] or ("code" not in result.keys()):
                raise ConnectionError("An error occured while retrieving data from Discord API.")
            else:
                return f"https://discord.com/invite/{result['code']}"
        else:
            raise ValueError("Invalid activity option chosen.")
        

