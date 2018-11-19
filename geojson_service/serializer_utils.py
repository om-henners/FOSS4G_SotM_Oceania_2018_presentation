"""
Marshmallow wrappers to produce GeoJSON instead of a flat dictionary.
"""
from flask_marshmallow import Marshmallow
import geoalchemy2
from geoalchemy2.shape import from_shape, to_shape
from marshmallow import fields, pre_load, post_dump, ValidationError
import marshmallow_sqlalchemy as msqla
from shapely import geometry


ma = Marshmallow()


class GeometryField(fields.Field):
    """
    Use shapely and geoalchemy2 to serialize / deserialize a point

    Does make a big assumption about the data being spat back out as
    JSON, but what the hey.
    """

    def _serialize(self, value, attr, obj):
        if value is None:
            return None
        return geometry.mapping(to_shape(value))

    def _deserialize(self, value, attr, data):
        if value is None:
            return None
        return from_shape(geometry.shape(value))


msqla.ModelConverter.SQLA_TYPE_MAPPING[geoalchemy2.Geography] = GeometryField
msqla.ModelConverter.SQLA_TYPE_MAPPING[geoalchemy2.Geometry] = GeometryField
msqla.ModelConverter.SQLA_TYPE_MAPPING[geoalchemy2.Raster] = fields.Raw
msqla.ModelConverter.SQLA_TYPE_MAPPING[geoalchemy2.RasterElement] = fields.Raw


class MarshmallowGeoJSON:
    """
    Base class for wrappping and unwrapping GeoJSON objects.

    Reading from https://marshmallow.readthedocs.io/en/3.0/extending.html it
    should be possible to wrap and unwrap envelopes around the GeoJSON data
    as it comes in and out of the system.
    """
    __geometry_field_name__ = 'geom'  # or geom, or shape, or ....

    def unwrap_feature(self, data):
        """
        Unwrap an individual feature object

        Pull down all the properties field, and then under the geometry
        field name put in the actual geometry data
        """
        if data['type'] != 'Feature':
            raise ValidationError('Expecting a Feature object')
        flat = data['properties']
        flat[self.__geometry_field_name__] = data['geometry']
        return flat

    @pre_load(pass_many=True)
    def unwrap_envelope(self, data, many):
        if 'type' not in data:
            raise ValidationError('GeoJSON type could not be found')
        if many and data['type'] != 'FeatureCollection':
            raise ValidationError('Expecting a FeatureCollection object')

        if not many:
            return self.unwrap_feature(data)

        return [self.unwrap_feature(feature) for feature in data['features']]

    def wrap_feature(self, data):
        """
        Wrap the individual feature as a GeoJSON feature object
        """
        feature = {
            'type': 'Feature',
            'geometry': data.pop(self.__geometry_field_name__)
        }
        feature['properties'] = data
        return feature

    @post_dump(pass_many=True)
    def wrap_with_envelope(self, data, many):
        if not many:
            return self.wrap_feature(data)

        return {
            'type': 'FeatureCollection',
            'features': [self.wrap_feature(feature) for feature in data]
        }
