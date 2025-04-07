import requests
import keys
from twilio.rest import Client

ACCOUNT_SID = keys.account_sid
TWILIO_AUTH_TOKEN = keys.twilio_auth_token

NUMBER = keys.number
MY_NUMBER = keys.my_number

ALPHA_KEY = keys.alpha_key
NEWS_KEY = keys.news_key

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stocks_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT,params=stocks_parameters)
stock_response.raise_for_status()
stock_response_data = stock_response.json()

yesterday_data = list(stock_response_data['Time Series (Daily)'].values())[1]
other_day_data = list(stock_response_data['Time Series (Daily)'].values())[2]

yesterday_closing = float(list(yesterday_data.values())[3])
other_day_closing = float(list(other_day_data.values())[3])
difference = yesterday_closing - other_day_closing
percentage =(abs(difference)/yesterday_closing) * 100

if percentage >= 5 or percentage <= -5:
    print('trigger')
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_KEY,
        "sortBy": "publishedAt",
        "language": "en"
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_response_data = news_response.json()

    news_data = news_response_data['articles'][:3] # Get first 3

    for news in news_data:
        headline = news['title']
        brief = news['description']
        text_message = (f"{STOCK_NAME}: {round(percentage, 2)}%\n"
                        f"Headline: {headline}\n"
                        f"Brief: {brief}")
        client = Client(ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body=text_message,
            from_=NUMBER,
            to=MY_NUMBER,
        )
        print(message.body)
