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


To facilitate that, one can define that route explitictly/manually or by using [flask-discoverer](https://github.com/adsabs/flask-discoverer)

## development

A Vagrantfile and puppet manifest are available for development within a virtual machine. To use the vagrant VM defined here you will need to install *Vagrant* and *VirtualBox*. 

  * [Vagrant](https://docs.vagrantup.com)
  * [VirtualBox](https://www.virtualbox.org)

To load and enter the VM: `vagrant up && vagrant ssh`