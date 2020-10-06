# Add / update relevant fields
# rename this file to config.py

CONSUMER_KEY=''  # Twitter Application consumer key

CONSUMER_SECRET=''  # Twitter Application consumer secret

TWEETS_SINCE_DAYS=100  # Retrieve tweets from last X days

TWEETS_COUNT=50 # Retrieve only 'X' tweets from user's timeline

TOP_COUNT=10  # Display only top 'X' urls and domains

# Twiiter will callback with tokens here
# URL must be whitelisted in twitter dev application
CALLBACK_URL='http://127.0.0.1:8000/callback/'
