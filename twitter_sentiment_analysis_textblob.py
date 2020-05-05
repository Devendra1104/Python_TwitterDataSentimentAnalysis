import tweepy as tw
from textblob import  TextBlob

consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

def fetch_tweets(search_words): #username

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    # print(auth)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth)
    # print(api)
    # number_of_tweets=10
    date_since = "2020-01-14"
    # tweets = api.user_timeline(screen_name=username,since = date_since)
    tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since)

    positive = 0
    negative = 0
    neutral = 0

    for tweet in tweets:
        # print(tweet.text)
        analysis = TextBlob(tweet.text)
        # print("Sentiment of the tweet is:",analysis.sentiment.polarity)
        if analysis.sentiment.polarity == 0:
            neutral += 1
        elif analysis.sentiment.polarity < 0 :
            negative += 1
        elif analysis.sentiment.polarity > 0:
            positive += 1

    print("Positive tweets: ",positive)
    print("Negative tweets: ", negative)
    print("Neutral tweets: ", neutral)



print("Sentiment analysis for #CAA")
fetch_tweets('CAA')

'''
print("Sentiment analysis for @MotilalOswalLtd")
fetch_tweets('@MotilalOswalLtd')
print("Sentiment analysis for @YESBANK")
fetch_tweets('@YESBANK')
'''
