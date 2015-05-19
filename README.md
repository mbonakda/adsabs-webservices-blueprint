[![Build Status](https://travis-ci.org/adsabs/adsabs-webservices-blueprint.svg?branch=master)](https://travis-ci.org/adsabs/adsabs-webservices-blueprint)

# adsabs-webservices-blueprint

A sample Flask application for backend adsabs (micro) web services. To integrate into the ADS-API, an application must expose a `/resources` route that advertises that application's resources, scopes, and rate limits. 

`GET` on `/resources` should return `JSON` that looks like:

    {
        "/route": {
            "scopes": ["red","green"],
            "rate_limit": [1000,86400],
            "description": "docstring for this route",
            "methods": ["HEAD","OPTIONS","GET"],
        }
    }


To facilitate that, one can define that route explitictly/manually or by using [flask-discoverer](https://github.com/adsabs/flask-discoverer). This blueprint is pre-configured to do just this.

## development

For convenience, a Vagrantfile and puppet manifest are available to facilitate development within a virtual machine. To use the vagrant VM defined here you will need to install *Vagrant* and *VirtualBox*.

  * [Vagrant](https://docs.vagrantup.com)
  * [VirtualBox](https://www.virtualbox.org)

To load and enter the VM: `vagrant up && vagrant ssh`

## database migrations (only relevant when a database is managed by the application)

To make changes to the database schema associated with the application:

  * Update the database model in `models.py`
  * execute: `python manage.py db migrate`
  * if necessary, make manual changes in the migration scripts generated in `migrations/versions` (see notes below)
  * execute: `python manage.py db upgrade`

Notes:

1. Installation of `Flask-Migrate` created the directory `migrations`. If the application uses `SQLALCHEMY_DATABASE_URI` as database URI, you can ignore the following remark. If the application uses `SQLALCHEMY_BINDS` to define the database URI, the script `migrations/env.py` needs a manual update: replace `current_app.config.get('SQLALCHEMY_DATABASE_URI')` by `current_app.config.get('SQLALCHEMY_BINDS')['sample']`
2. After running the `migrate` step, some manual editing of the migration script will be necessary because of the definition of one of the table columns: the column `Column(postgresql.ARRAY(String))` gets translated into `sa.Column('bar', postgresql.ARRAY(String()), nullable=True)` in the migration, which will throw an exception if left unedited. The entry `String()` has to be changed into `sa.String()`. This is true in general for all types used in `ARRAY`.
