# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table, text
from geoalchemy2.types import Geometry
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class District(Base):
    __tablename__ = 'district'

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('district_id_seq'::regclass)")
    )
    name = Column(String, index=True)
    electors = Column(Integer)
    projectedp = Column(Integer)
    members = Column(Integer)
    electordev = Column(Float(53))
    projectedd = Column(Float(53))
    geom = Column(Geometry('MULTIPOLYGON', 4326), index=True)

    voting_centres = relationship(
        'VotingCentre',
        secondary='district_centre_association',
        back_populates='districts'
    )


class VotingCentre(Base):
    __tablename__ = 'voting_centre'

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('voting_centre_id_seq'::regclass)")
    )
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

    districts = relationship(
        'District',
        secondary='district_centre_association',
        back_populates='voting_centres'
    )


t_district_centre_association = Table(
    'district_centre_association', metadata,
    Column('district_id', ForeignKey('district.id')),
    Column('voting_centre_id', ForeignKey('voting_centre.id'))
)
