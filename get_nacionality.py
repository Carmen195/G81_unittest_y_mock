import json
import requests
from MyException import MyException

def get_nacionality_by_name(name):

    url = f"https://api.nationalize.io/?name={name}"
    try:
        response = requests.get(url).text
    except ConnectionError:
        raise MyException("Error to connect")
    except TimeoutError:
        raise MyException("Error timeout")
    country_code = json.loads(response)["country"][0]["country_id"]
    return country_code
