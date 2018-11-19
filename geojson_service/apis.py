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
class CentresAPI(MethodView):
    """Voting centres"""

    @api_pages.response(VotingCentreGJ(many=True))
    def get(self):
        centres = VotingCentre.query.limit(10).all()
        return centres
