SAMPLE_APPLICATION_PARAM = {
  'message':'config params should be prefixed with the application name',
  'reason': 'this will allow easier integration if this app is incorporated as a python module',
}
SAMPLE_APPLICATION_ADSWS_API_URL = 'https://api.adsabs.harvard.edu'


# This parameter isn't required to be prefixed with the application name
# This parameter is required only if this application makes requests to the adsws-api
# We will provide this application with a token if that is the case
ADSWS_API_TOKEN = 'secret'
