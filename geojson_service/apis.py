from flask import Blueprint
from flask_restplus import Api, Resource

from .serialisers import voting_centre_collection
from .models import db, VotingCentre, District


api_pages = Blueprint('api', __name__)
api = Api(
    api_pages,
    title='GeoJSON API',
    version='1.0.0',
    description='API to get GeoJSON for voting districts and centres'
)


@api.route('/centres')
@api.doc('Voting centres')
class CentresAPI(Resource):
    """Voting centres"""

    @api.doc(body='Get a feature collection of Voting Centres')
    def get(self):
        centres = VotingCentre.query.limit(10).all()
        return voting_centre_collection.dump(centres).data
