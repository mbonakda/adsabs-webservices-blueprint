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


To facilitate that, one can define that route explitictly (see i.e. `sample_application/views.py`), or by  using [flask-discoverer](https://github.com/adsabs/flask-discoverer) (see i.e. `sample_application2/app.py`)
