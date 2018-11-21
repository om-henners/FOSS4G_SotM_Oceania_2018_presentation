# Spatial data APIs - making your spatial data public without giving away database access

In this repository are three things:

1. The PDF of my presentation, which contains the technical details, and explanation of how to put the more complex example togther.
2. The code I wrote in the workshop, in the "workshop_simplified" folder (minus the database connections and passwords). If you need those again please reach out. Otherwise you should be able to run / deploy this as we were doing in the afternoon with `flask run` from that folder.
3. The more complex example I put togther as part of building the workshop. It can still be run from your machine with `flask run`. However there are a few steps you need to take first (more details in the slides):
   1. Create a file `settings.cfg` which contains:

          SECRET_KEY=b'secret key'
          SQLALCHEMY_DATABASE_URI='postgresql://username:password@host:port/database'
          SQLALCHEMY_TRACK_MODIFICATIONS=False
          OPENAPI_URL_PREFIX='/api/doc'
          OPENAPI_SWAGGER_UI_PATH='/swagger'
          OPENAPI_SWAGGER_UI_VERSION='3.18.3'
   2. Set an environment variable `GEOJSON_SERVER_SETTINGS` with the path to this file
   3. `pip install -r requirements.txt` to install the required libraries for this server

Please feel free to use and abuse, especially the [GeoJSON Marshmallow Serializer](http://bit.ly/foss4g_marshmallow), and feel free to get in contact. Twitter at [@om_henners](https://twitter.com/om_henners) to go with the theme of the conference.
