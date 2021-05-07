from pytwitterscraper  import TwitterScraper
import pandas as pd

# Instatiate TwitterScraper object
tw = TwitterScraper()

# Get user profile info
###### EDIT username variable to get your data ######
# Had to make my profile public to scrape tweets
# username is you twitter handle minus the @ symbol
username = '<your twitter handle>'
profile = tw.get_profile(name=username)
profile_id = profile.__dict__['id']    # profile id

# Planned to get all of my tweets (see count parameter in tw.get_tweets) but only got tweets up to 2017
num_tweets = profile.__dict__['tweet'] # number of total tweets

# Scrape tweets
print('Scraping tweets...')
tweets = tw.get_tweets(id=profile_id, count=num_tweets)
print('Scraping tweets done! Saving to csv...')

tweet_id, datetime, lang, text, hashtags, media, urls, likes, relay, retweet = ([] for i in range(10))

for tweet in tweets.contents:
    tweet_id.append(tweet['id'])
    datetime.append(tweet['created_at'])
    lang.append(tweet['lang'])
    text.append(tweet['text'])
    hashtags.append(tweet['hashtags'])
    media.append(tweet['hashtags'])
    urls.append(tweet['urls'])
    likes.append(tweet['likes'])
    relay.append(tweet['relay'])
    retweet.append(tweet['retweet'])

tweets_tuple = list(zip(tweet_id, datetime, lang, text, hashtags, media, urls, likes, relay, retweet))
tweets_df = pd.DataFrame(tweets_tuple, columns = ['ID', 'Created at', 'Lang', 'Text', 'Hashtags', 'Media', \
                                                  'URLS', 'Likes', 'Relay', 'Retweet'])

tweets_df.to_csv(f'tweets_{username}.csv', index=False)
print('Tweets saved to csv!')
