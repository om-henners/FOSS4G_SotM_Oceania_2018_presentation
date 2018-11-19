from flask import abort
from flask.views import MethodView
from flask_rest_api import Api, Blueprint

from .serialisers import VotingCentreGJ
from .models import db, VotingCentre, District


api_pages = Blueprint(
    'api',
    __name__,
    description='Operations of voting centres',
    url_prefix='/api'
)
api = Api()

def register_definitions():

    api.spec.definition('VotingCentre', schema=VotingCentreGJ)
    api.register_blueprint(api_pages)


@api_pages.route('/centres')
class CentresList(MethodView):
    """Voting centres"""

    @api_pages.response(VotingCentreGJ(many=True))
    def get(self):
        """Get 10 voting centres"""
        centres = VotingCentre.query.limit(10).all()
        return centres


@api_pages.route('/centres/<int:centre_id>')
class Centre(MethodView):

    @api_pages.response(VotingCentreGJ)
    def get(self, centre_id):
        """Get a voting centre by ID"""
        item = VotingCentre.query.filter(VotingCentre.id==centre_id).first()
        if not item:
            abort(404, f"No voting centre found with ID {centre_id}")
        return item