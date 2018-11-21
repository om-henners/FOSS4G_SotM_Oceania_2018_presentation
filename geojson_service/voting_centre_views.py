from flask import Blueprint, Response, render_template

from .models import db, VotingCentre, District


vc_pages = Blueprint('voting_centres', __name__)


@vc_pages.route('/district/<district>')
def get_centres_in_district(district):
    query = db.session.query(
        VotingCentre.venue_name,
        VotingCentre.street_number,
        VotingCentre.street_name,
        VotingCentre.street_type,
        VotingCentre.locality,
        VotingCentre.postcode
    ).join(
        VotingCentre.districts
    ).filter(
        db.and_(
            VotingCentre.venue_type == 'Voting Centre',
            District.name.contains(district)
        )
    ).order_by(
        VotingCentre.venue_name
    )

    return Response(render_template(
        'output.csv',
        rows=query.all(),
        fieldnames=[
            'venue_name',
            'street_number',
            'street_name',
            'street_type',
            'locality',
            'postcode']
        ),
        mimetype='text/plain'
    )