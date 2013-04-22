import random

from twitter import Twitter, OAuth, read_token_file

# get the list of compliments
f = open('compliments.txt', 'r')
compliments = f.read().strip('\n').split('\n')
f.close()

# Note: make these files yourself!
# read the oauth
oauth_filename = 'oauth'
oauth_token, oauth_token_secret = read_token_file(oauth_filename)

# read the consumer keys
consumer_filename = 'consumer'
consumer_key, consumer_secret = read_token_file(consumer_filename)

twitter = Twitter(auth=OAuth(oauth_token,
                            oauth_token_secret,
                            consumer_key,
                            consumer_secret
                            )
                )

mentioners = twitter.statuses.mentions_timeline()

print mentioners[0]['entities']['user_mentions'][0]['screen_name']