from AlphaAdvantageDaily import AlphaAdvantageDaily
from NewsApi import NewsApi

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock = AlphaAdvantageDaily(STOCK_NAME)

increase = stock.percent_increase()
print(increase)
if increase is None:
    increase=2.3

print(f"Stock {STOCK_NAME} change was {increase:.2f}%")

articles = NewsApi.search_in_title(COMPANY_NAME)[:3]

print(articles)
print(len(articles))

simple_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

for a in simple_articles:
    txt = {'body': a,
           'from': "123456789"
           }
    print(f"{txt['from']} \n {txt['body']}")

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
