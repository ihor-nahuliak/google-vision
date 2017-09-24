# Parcelbox (Backend)

This is the backend server for the Parcelbox project. The backend receives an image upload from the native Android app, forwards the image to the Google Cloud SDK for facial recognition and then sends an update to the Parcelbox using Pubnub.

Made with lots of love at [propTech{hacks} 2017](http://proptechhacks.de/)

## Installation
1. Clone this repository on your local device
1. Make sure you have Python 3.3 (or newer) and pip installed
1. Install the [Google Cloud SDK](https://cloud.google.com/sdk/downloads) for image recognition and set it up with your Google Account
1. Install Google Cloud Python SDK: `sudo pip install --upgrade google-cloud`
1. Install Flask: `sudo pip install Flask`
1. Install Pubnub: `sudo pip install 'pubnub>=4.0.13'`
1. Run with: `export FLASK_APP=flask_api.py && flask run --host=0.0.0.0`

## Used software
* Google Cloud SDK for facial recognition
* Flask for an easy REST server
* Pubnub for real-time communication with the Parcelbox
