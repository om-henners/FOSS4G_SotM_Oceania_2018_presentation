from flask import Flask, jsonify

from complete_models import db, VotingCentre
from serializer_utils import ma, MarshmallowGeoJSON

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://username:password@host:port/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma.init_app(app)


class VotingCentreGJ(MarshmallowGeoJSON, ma.ModelSchema):
    class Meta:
        model = VotingCentre

@app.route('/')
def hello_world():
    row = db.session.query(VotingCentre).limit(100).all()
    serializer = VotingCentreGJ(many=True)
    geojson = serializer.dump(row).data
    return jsonify(geojson)
