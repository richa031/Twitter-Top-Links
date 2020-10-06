# Twitter Top Links Web App

Twitter Top Links is a Django App for displaying top domains shared by authenticated users.

* The app will let the user login with Twitter.
* Once authenticated, the app pulls just the tweet's that contain URLs from a users stream
(friends + users post) for the past 7 days.
* Persist the tweets in the database
* Once stored, the application then computes and display
    * a. Actual Tweets containing links
    * b. Which user has shared the most links
    * c. List of Top Domains that have been shared so far
 
## Installation
* Follow these to install and set-up development server locally.

### Prerequisites
* Make sure Python 3.x, pip, git are installed on your system. 
    * Clone this repository:
    
```git clone https://github.com/kill-gear/twitter-top-links.git```

Once cloned, create a virtual environment in the root directory of this repository:

```python3 -m venv ttlenv```

Then activate this virtual environment using:

```source ./ttlenv/bin/activate ``` 

For Windows, check venv documentation for exact usage
Now install the dependencies using the following command:

```python3 -m pip install -r requirements.txt```

### Server Configuration

* There's a file named ```exampleconfig.py``` and the relevant keys and save as ```config.py```
    
    * Get ```CONSUMER_KEY``` and ```CONSUMER_SECRET``` from your project on [Twitter's Developer Portal](https://developer.twitter.com/en/docs/labs/getting-started)
        * Default: ```''```
    
    * ```TWEETS_SINCE_DAYS``` Specify number of days for which tweets will be fetched.
        * Default: ```100```
    
    * ```TWEETS_COUNT``` Speciy max number of tweets to fetch (supersedes TWEETS_SINCE_DAYS).
        * Default: ```50```
    
    * ```TOP_COUNT``` Specify max number of URLs and Users to display on home page.
        * Default: ```10```
    
    * ```CALLBACK_URL``` Specify the url at which twitter callbacks when user authenticates.
        * This URL should be in CALLBACK URLS in your Twitter Developer Application, [check official documentation.](https://developer.twitter.com/en/docs/apps/callback-urls)
        * For local development add ```http://127.0.0.0.1/callback/```
        * For Deploying on cloud use appropriate Domain Name.
            * Exampple for 'pythonanywhere' with username - example : ```http://example.pythonanywhere.com/callback/```
            * ```"callback/"``` is the endpoint which handles redirect from twitter authentication

### Set-up DB (SQLite3)
* Make Migrations - It is responsible for creating new migrations based on the changes you have made to your models.

```python3 manage.py makemigrations```
* Migrate - It is responsible for applying migrations, as well as unapplying and listing their status.

```python3 manage.py migrate```
* Initially it is required to make & set-up DB but whenever you edit your model fields then also run migrations.

### Create superuser for Django Admin
* It's needed to create a user account that has control over everything on the site.
```
python3 manage.py createsuperuser
```
    Set username, email and password and go to below mentioned URL:
  
```127.0.0.1:8000/admin``` (Default) to log-in and view the models and DB.

### Start the Development Server
And we're done! Time to start the web server and see if our website is working!

```python3 manage.py runserver```
![Screenshot (38)](https://user-images.githubusercontent.com/32764563/95241904-13e09280-082c-11eb-9beb-9559a9afc116.png)

![Screenshot (40)](https://user-images.githubusercontent.com/32764563/95241999-3a9ec900-082c-11eb-80b2-86346a4c34e8.png)

![Screenshot (41)](https://user-images.githubusercontent.com/32764563/95242152-6752e080-082c-11eb-9276-dcba3efe9215.png)


***
