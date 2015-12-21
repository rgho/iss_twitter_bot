
import tweepy
import json
import requests

def tweet(tweet_text):
	# == OAuth Authentication ==
	#
	# This mode of authentication is the new preferred way
	# of authenticating with Twitter.

	# The consumer keys can be found on your application's Details
	# page located at https://dev.twitter.com/apps (under "OAuth settings")
	consumer_key=""
	consumer_secret=""

	# The access tokens can be found on your applications's Details
	# page located at https://dev.twitter.com/apps (located
	# under "Your access token")
	access_token=""
	access_token_secret=""

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.secure = True
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	# If the authentication was successful, you should
	# see the name of the account print out
	# print api.me().name

	# If the application settings are set for "Read and Write" then
	# this line should tweet out the message to your account's
	# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
	api.update_status(status=tweet_text)


def get_iss_data():
	# Get current ISS data from WTISS. Convert JSON to python dict.
	url = 'https://api.wheretheiss.at/v1/satellites/25544'
	r = requests.get(url)
	result =  (r.text).encode('ascii', 'ignore')
	result = json.loads(result)
	return result

def iss_tweet():
	# Get ISS data as dictionary.
	data = get_iss_data()

	# Extract relevant data. Cast as strings. Force limit length.
	lat = str(data['latitude'])[:8] + '' 
	lon = str(data['longitude'])[:8] + '' 
	velocity = str(data['velocity'])[:8] + ' km/hr' 
	altitude = str(data['altitude'])[:6] + ' km' 

	# Construct tweet.
	tweet = "Intl. Space station (Zarya) current position: %s latitude, %s longitude. Speed: %s. Altitude: %s" % (lat,lon,velocity,altitude)

	# Print tweet and number of chars in tweet. 
	# print tweet
	# print len(tweet)
	return tweet

def main():
	# Get the text of the tweet and then tweet it!
	tweet_text = iss_tweet()
	tweet(tweet_text)


if __name__ == '__main__':
	main()



