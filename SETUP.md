# Update our system

This setup is thought for Ubuntu 14.04 LTS.

Let's get started by making sure our system is up to date.

	$ sudo apt-get update && sudo apt-get upgrade

We're using `git` so make sure you have that installed:

	$ sudo apt-get install git

# PostgreSQL

To install PostgreSQL run the following command:

	$ sudo apt-get install postgresql postgresql-contrib

Create a database user and a new database for the app. Grab a [perfect password from GRC](https://www.grc.com/passwords.htm).

	$ sudo su - postgres
	postgres@django:~$ createuser --interactive -P
	Enter name of role to add: <username here>
	Enter password for new role: 
	Enter it again: 
	Shall the new role be a superuser? (y/n) n
	Shall the new role be allowed to create databases? (y/n) n
	Shall the new role be allowed to create more new roles? (y/n) n
	postgres@django:~$
	
	postgres@django:~$ createdb --owner <username again> <db name here>
	postgres@django:~$ logout
	$

In order to use Django with PostgreSQL we'll use the python module `psycopg2` (database adapter), it requires the following dependencies:

	$ sudo aptitude install libpq-dev python-dev

# Application user

Even though Django has a pretty good [security track record](http://django.readthedocs.org/en/latest/releases/security.html), web applications can become compromised. If the application has limited access to resources on your server, potential damage can also be limited. Your web applications should run as system users with limited privileges.

Let's start by creating a folder for our webpage. I've decided to keep my webpage project in `/var/webpages/<project name>` but you can choose any path you want really, as long as you're sure nothing else you're going to setup on your machine is going to use that path. For this particular project we'll be using the project name `oneup`:

	$ sudo mkdir -p /var/webpages/oneup

Create a user for your app, named `webber` and assigned to a system group called `webspinner`.

	$ sudo groupadd --system webspinner
	$ sudo useradd --system --gid webspinner --shell /bin/bash --home /var/webpages/oneup webber

And now let's change ownership of the folder to our trusty but privileges stripped `webber`:

	$ sudo chown webber /var/webpages/oneup

If you want to allow other users than our trusty `webber` to have write access to the project folder then add the user to the `webspinner` group. You can check what groups you're a member of by issuing the `groups` command or `id`, you add yourself to the group with this command:

	$ sudo usermod -a -G webspinner `whoami`

**Note:** Group memberships are assigned during login, so you may need to log out and back in again for the system to recognize your new group.

# Install python virtualenv

[Virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool which allows you to create separate Python environments on your system. It allows you to run applications with different sets of requirements concurrently and is easy to install:

	$ sudo apt-get install python-virtualenv

# Create a new virtualenv and run django server

Now let's create a virtual python environment in our project directory as our trusty `webber` user:

	$ sudo su - webber
	$ umask g+w
	$ cd /var/webpages/oneup
	$ virtualenv .
	$ source bin/activate
	$ nano .profile

Paste the following into `.profile`:

	source ~/bin/activate

	umask g+w

	function ll() {
		ls -al $1
	}

Our environment is now ready, let's install a few things on it:

	$ pip install django
	$ pip install psycopg2

Now let's clone the current version of our project from github:

	$ git clone git@github.com:hannespetur/oneup.git

Now let's set our `environment` to `development`:

	$ touch environment.py
	$ nano environment.py

Paste the following into `environment.py`:

	environment = 'development'

Then create a settings file for `development`:

	$ mkdir oneup/settings
	$ cp oneup/settings.py oneup/settings/development.py
	$ nano oneup/settings/development.py

Remember to edit the `SECRET_KEY` and change the `DATABASES` settings in `development.py`:

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': '<database name>',
	        'USER': '<database user>',
	        'PASSWORD': '<database user password>',
	        'HOST': 'localhost',
	        'PORT': '', # Set to empty string for default.
	    }
	}

afterwards run:

	$ python manage.py migrate
	$ python manage.py runserver localhost:8000

[It works! Squee!](http://localhost:8000/) Of course, you haven't actually done any work yet.
