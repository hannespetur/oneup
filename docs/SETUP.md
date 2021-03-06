This setup recipe is thought for 'semi' production setup using Ubuntu 14.04 LTS. For development setup or people wanting to try this out on their PC note, big chunks of ingredients here are unneccesary so check out the (to be written) **QUICKSETUP.md** doc.

# Update our system

Let's get started by making sure our system is up to date.

	$ sudo apt-get update && sudo apt-get upgrade

We're using `git` so make sure you have that installed:

	$ sudo apt-get install git

We're going to use the web package manager `bower`:

	$ sudo apt-get install nodejs
	$ sudo npm install -g bower

For more information about `bower` check out [bower.io](http://bower.io/).

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

	$ nano environment.py

Paste the following into `environment.py`:

	environment = 'development'

Then create a settings file for `development`:

	$ cp oneup/settings/default.py oneup/settings/development.py
	$ nano oneup/settings/development.py

Remember to change the `SECRET_KEY` and the `DATABASES` settings in `development.py`:

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

# Using the test app
You can use the test app for anything... it's your area for testing out django! This section will have information about things to try out in the test app.

## Test simple html
At the top-level there is a very simple example of how we can use django to host two simple html files using templates. You can view the two pages with a server running at [http://localhost:8000/](http://localhost:8000/) and [http://localhost:8000/about](http://localhost:8000/about). Both of the files use the template at oneup/apps/test/templates/base.html.

## Test simple poll server
Following the tutorial at: [https://docs.djangoproject.com/en/1.8/intro/tutorial01/](https://docs.djangoproject.com/en/1.8/intro/tutorial01/) we can play around with a simple poll server. The server uses postgreSQL to store questions and answers and keeps track of how many users have voted each question.

First you'll have to create a migration of the model and then apply it to the database. You do this using:

	$ python manage.py makemigrations polls
	$ python manage.py migrate

If your database is properly set up you shouldn't get any errors. By visiting the [admin page](http://localhost:8000/admin/) you can add questions and answers (as well as change their results^^).

The index page at [http://localhost:8000/polls/](http://localhost:8000/polls/) will have up to 5 newest polls, the user can then view the polls in more detail at e.g. [http://localhost:8000/polls/1](http://localhost:8000/polls/1) to view poll 1. [http://localhost:8000/polls/1/results/](http://localhost:8000/polls/1/results/) will show the results for poll 1 and [http://localhost:8000/polls/1/vote/](http://localhost:8000/polls/1/vote/) is the vote page of poll 1.