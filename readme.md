### About
This is a simple example of a twitter bot using tweepy. It posts latitude, longitude, velocity, and altitude of the International Space center to twitter.

### Install and Run
```sh
$ pip install requests
$ pip install tweepy
$ python ISS_twitter.py
```

### Setup Cron
You can use a simple cron job to run the bot at specified times. Here is an example crontab file to run the script every hour.

```sh
0 * * * * python /path/to/ISS_twitter.py
```

### Credits:
* [Tweepy Docs](http://www.tweepy.org/)
* [Where is the ISS at?](http://wheretheiss.at/w/developer)

### License
* See imported libraries, api's for their own licenses.
* [ISS_twitter.py is released under MIT License](http://opensource.org/licenses/MIT)
