# The Humble Developer

Humble Bundle is hosted on [Google App Engine][gae], which I have
limited experience with.  When I applied for an engineering position
with them, I created this project running on Google App Engine as my
cover letter.  Unfortunately the position had already been filled. =(

[gae]: https://developers.google.com/appengine/


## Prerequisites

* Install Python 2.7:

  ```bash
  sudo apt-get install python2.7
  ```

* Install [Google App Engine SDK for Python][sdk] (tested with v1.9.6):

  ```bash
  wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.6.zip
  unzip google_appengine_1.9.6.zip
  ```

[sdk]: https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python


## Usage

```bash
cd /path/to/project

google_appengine/dev_appserver.py .
```

Then visit http://localhost:8080/ to see it in action.
