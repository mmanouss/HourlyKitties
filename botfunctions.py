import requests
import os

def envGet(env_name: str, heroku_hosting: bool) -> str:
    if heroku_hosting == True:
        return os.environ[env_name]
    else:
        from dotenv import load_dotenv
        load_dotenv(env_name+'.env')
        return os.getenv(env_name)
    
def getKitty(CAT_KEY: str) -> str:
    headers = {'x-api-key': CAT_KEY} if CAT_KEY else {}
    response = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
    data = response.json()
    return data[0]['url']