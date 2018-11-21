# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.types import Geometry

db = SQLAlchemy()


class District(db.Model):
    __tablename__ = 'district'

    id = db.Column(
        db.Integer,
        primary_key=True,
        server_default=db.text("nextval('district_id_seq'::regclass)")
    )
    name = db.Column(db.String, index=True)
    electors = db.Column(db.Integer)
    projectedp = db.Column(db.Integer)
    members = db.Column(db.Integer)
    electordev = db.Column(db.Float(53))
    projectedd = db.Column(db.Float(53))
    geom = db.Column(Geometry('MULTIPOLYGON', 4326), index=True)

    voting_centres = db.relationship(
        'VotingCentre',
        secondary='district_centre_association',
        back_populates='districts'
    )


class VotingCentre(db.Model):
    __tablename__ = 'voting_centre'

    id = db.Column(
        db.Integer,
        primary_key=True,
        server_default=db.text("nextval('voting_centre_id_seq'::regclass)")
    )
    polling_location_name = db.Column(db.String, index=True)
    venue_name = db.Column(db.String, index=True)
    venue_type = db.Column(db.String)
    property_name = db.Column(db.String)
    flat_number = db.Column(db.String)
    street_number = db.Column(db.String)
    street_name = db.Column(db.String)
    street_type = db.Column(db.String)
    locality = db.Column(db.String)
    postcode = db.Column(db.Integer)
    melway_ref = db.Column(db.String)
    geom = db.Column(Geometry('POINT', 4326), index=True)

    districts = db.relationship(
        'District',
        secondary='district_centre_association',
        back_populates='voting_centres'
    )


t_district_centre_association = db.Table(
    'district_centre_association', db.Model.metadata,
    db.Column('district_id', db.ForeignKey('district.id')),
    db.Column('voting_centre_id', db.ForeignKey('voting_centre.id'))
)
