"""defines a function that gets a random qutoe"""
import requests
import json


def get_quote() -> str:
    """makes a request to the zen quotes API to
    get a random qoute

    Returns:
        str: quote text and quote auther
    """
    try:
        # making a request to the ZenQoute API
        quote_url = "https://zenquotes.io/api/random"
        response = requests.get(quote_url)

        # decode the response from the API
        decoded_response = response.content.decode('utf-8')
        data = json.loads(decoded_response)

        # getting quote in the right format
        quote = f"{data[0]['q']}\n - {data[0]['a']}"
        return quote

    except requests.RequestException as e:
        return f"An error occured: {e}"
