# StravaPyServer

This is a simple web-server built on Django that can be run from localhost to handle authentication with the oauth interface from Strava.com (http://strava.github.io/api/#access).

To use:

1) Clone the repository
2) Visit http://labs.strava.com/developers/ to register your application and to get the appropriate tokens
3) Modify the settings files at StravaR/settings.py (at the very end) to point to some files with the appropriate keys
4) Ensure that django is installed
5) From command line, in the directory of the repository, run ```python manage.py runserver'''
6) Open a browser to http://localhost:8000
7) Follow the directions in the interface
8) Copy your generated key into a file and make sure IT NEVER ENTERS INTO VERSION CONTOL (or someone could post data to your account and break things!)
