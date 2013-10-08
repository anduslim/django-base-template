
# Django 1.5 Base Template (Adapted from [Xenith][xenith_base]) #

## About ##

This version of the project template is designed for Django 1.5.

This project is originally forked from [Xenith][xenith_base].
The settings file has refactored to be clearer  and the project has been adapted
to suit the architecture that I have been using.
See Features for a clearer idea on the modules that are being used.

[xenith_base]: https://github.com/xenith/django-base-template


## Features ##

By default, this project template includes:

A set of basic templates built from HTML5Boilerplate 4.1.0 and Twitter Bootstrap 2.3.1 (located in the
base app)

Templating:

- Markdown
- django_compressor for compressing javascript/css/less/sass

Security:

- bleach
- python-bcrypt2 - uses bcrypt for password hashing by default

Background Tasks:

- Celery

Migrations:

- South

Caching:

- python-memcached

Admin:

- Includes django-admin-toolbar for development and production (enabled for superusers)
- Includes django-debug-toolbar-user-panel, which is quite useful, but is disabled until it fully supports Django 1.5

Testing:

- nose and django-nose
- pylint, pep8, and coverage

Database:

- PostgreSQL

Email:

- AWS SES

File Storage:

- AWS S3

Shell:

-iPython

Logging (Sentry):

- Raven

Admin Profile Thumbnail:

- Gravatar

Any of these options can added, modified, or removed as you like after creating your project.


## Prerequisites ##

- Python 2.6 or 2.7
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)

## How to use this project template to create your project ##

- Create your working environment and virtualenv
- Install Django 1.5 ($ pip install Django>=1.5)
- $ django-admin.py startproject --template https://github.com/anduslim/django-base-template/zipball/master --extension py,md,rst projectname
- $ cd projectname
- $ pip install -r requirements/local.txt
- $ cp projectname/settings/local-dist.py projectname/settings/local.py
- $ python manage.py syncdb
- $ python manage.py migrate
- $ python manage.py runserver

That's all you need to do to get the project ready for development. When you deploy your project into production, you should look into getting certain settings from environment variables or other external sources. (See SECRET_KEY for an example.)

There isn't a need to add settings/local.py to your source control, but there are multiple schools of thought on this. The method I use here is an example where each developer has their own settings/local.py with machine-specific settings. You will also need to create a version of settings/local.py for use in deployment that you will put into place with your deployment system (Fabric, chef, puppet, etc).

The second school of thought is that all settings should be versioned, so that as much of the code/settings as possible is the same across all developers and test/production servers. If you prefer this method, then make sure *all* necessary settings are properly set in settings/base.py, and then edit settings/__init__.py so it no longer reraises the exception. (ie, by replacing 'raise' with 'pass'). As it is, settings/local.py should only be overriding settings from settings/base.py anyway. (You could also just set the DJANGO_SETTINGS_MODULE environment variable to "{{ project_name }}.settings.base" directly.)


License
-------
This software is licensed under the [New BSD License][BSD]. For more
information, read the file ``LICENSE``.

[BSD]: http://opensource.org/licenses/BSD-3-Clause
