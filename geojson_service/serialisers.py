from marshmallow import fields

from .serializer_utils import MarshmallowGeoJSON, ma
from .models import VotingCentre, District


class VotingCentreTable(ma.ModelSchema):
    class Meta:
        model = VotingCentre


class DistrictTable(ma.ModelSchema):
    class Meta:
        model = District


class VotingCentreGJ(MarshmallowGeoJSON, ma.ModelSchema):

    class Meta:
        model = VotingCentre

    districts = fields.Nested(DistrictTable, only='name', many=True, dump_only=True)


class DistrictGJ(MarshmallowGeoJSON, ma.ModelSchema):
    class Meta:
        model = District

    voting_centres = fields.Nested(VotingCentreTable, only=('venue_name'), many=True, dump_only=True)


voting_centre_collection = VotingCentreGJ(many=True)
voting_centre_feature = VotingCentreGJ()
district_collection = DistrictGJ(many=True)
district_feature = DistrictGJ()
