from .serializer_utils import MarshmallowGeoJSON, ma
from .models import VotingCentre, District


class VotingCentreGJ(MarshmallowGeoJSON, ma.ModelSchema):

    class Meta:
        model = VotingCentre


class DistrictGJ(MarshmallowGeoJSON, ma.ModelSchema):

    class Meta:
        model = District


voting_centre_collection = VotingCentreGJ(many=True)
voting_centre_feature = VotingCentreGJ()
district_collection = DistrictGJ(many=True)
district_feature = DistrictGJ()
