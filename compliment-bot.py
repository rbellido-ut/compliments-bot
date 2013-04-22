import random
import time
import sys
import signal

from twitter import Twitter, OAuth, read_token_file

# Let's handle keyboard interrupts gracefully
def keyb_interrupt_handler(signal, frame):
	print '\nBye!'
	sys.exit(0)
signal.signal(signal.SIGINT, keyb_interrupt_handler)

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


# grab the first screen name in the first/latest mention
#print mentioners[0]['entities']['user_mentions'][0]['screen_name']

# start loop
# check if the id of the first mention is different from the previous id
# if different:
#	tweet a random compliment
#	update previd
# sleep for 1 min

mentioners = twitter.statuses.mentions_timeline()
previd = mentioners[0]['id']

while True:
	mentioners = twitter.statuses.mentions_timeline()
	newid = mentioners[0]['id']

	if (previd != newid):
		replyto = mentioners[0]['entities']['user_mentions'][0]['screen_name']
		message = '@%s %s' % replyto, random.choice(compliments)
		#twitter.statuses.update(status=message)
		print message
		previd = mentioners[0]['id']

	# sleep for 1 minute before continuing again
	time.sleep(60)