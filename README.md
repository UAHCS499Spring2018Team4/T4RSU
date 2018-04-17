# T4RSU
Team 4 Real Estate Utility

## Dependencies
* Python 3.mumble
  * Developed on 3.4 and 3.6
* Django 2.0
  * Might work with earlier versions
* Pillow
  * Developed with 5.0.0
* Some kind of `cron`
  * For daily hit count emails

## Setup
It's a Django app. [It's easy.](https://docs.djangoproject.com/en/2.0/topics/install/#install-apache-and-mod-wsgi)

1. Unpack it somewhere.
2. Turn off `DEBUG`.
3. Point the app at your email system.
4. Point your web server at it.
5. (Optional) Set up daily hit count emails.

### Daily Hit Count
Add this to a crontab somewhere:

`/path/to/manage.py shell < /path/to/daily.py`
