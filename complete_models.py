# coding: utf-8
from sqlalchemy import ARRAY, Boolean, CheckConstraint, Column, Float, ForeignKey, Integer, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.orm import relationship

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class District(db.Model):
    __tablename__ = 'district'

    id = Column(Integer, primary_key=True, server_default=text("nextval('district_id_seq'::regclass)"))
    name = Column(String, index=True)
    electors = Column(Integer)
    projectedp = Column(Integer)
    members = Column(Integer)
    electordev = Column(Float(53))
    projectedd = Column(Float(53))
    geom = Column(Geometry('MULTIPOLYGON', 4326), index=True)

    voting_centres = relationship('VotingCentre', secondary='district_centre_association')



class VotingCentre(db.Model):
    __tablename__ = 'voting_centre'

    id = Column(Integer, primary_key=True, server_default=text("nextval('voting_centre_id_seq'::regclass)"))
    polling_location_name = Column(String, index=True)
    venue_name = Column(String, index=True)
    venue_type = Column(String)
    property_name = Column(String)
    flat_number = Column(String)
    street_number = Column(String)
    street_name = Column(String)
    street_type = Column(String)
    locality = Column(String)
    postcode = Column(Integer)
    melway_ref = Column(String)
    geom = Column(Geometry('POINT', 4326), index=True)


t_district_centre_association = Table(
    'district_centre_association', db.Model.metadata,
    Column('district_id', ForeignKey('district.id')),
    Column('voting_centre_id', ForeignKey('voting_centre.id'))
)
