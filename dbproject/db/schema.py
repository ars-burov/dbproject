# coding: utf-8
from sqlalchemy import CHAR, Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Numeric, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Airport(Base):
    __tablename__ = 'airport'

    airp_id = Column(Numeric(6, 0), primary_key=True)
    airp_name = Column(String(50), nullable=False)
    code = Column(String(30), nullable=False)
    airp_city = Column(String(30), nullable=False)
    airp_cntry = Column(String(20), nullable=False)
    airp_type = Column(CHAR(1), nullable=False)


class CabCl(Base):
    __tablename__ = 'cab_cls'

    cab_id = Column(Numeric(5, 0), primary_key=True)
    cab_name = Column(String(30), nullable=False)


class Insurance(Base):
    __tablename__ = 'insurance'

    ins_id = Column(Numeric(6, 0), primary_key=True)
    plan_name = Column(String(30), nullable=False)
    desc = Column(String(100), nullable=False)
    ins_cost = Column(Numeric(6, 2), nullable=False)


class MealPl(Base):
    __tablename__ = 'meal_pl'

    mp_id = Column(Numeric(5, 0), primary_key=True)
    mp_name = Column(String(30), nullable=False)


class Model(Base):
    __tablename__ = 'model'

    mid = Column(Numeric(6, 0), primary_key=True)
    pl_name = Column(String(30), nullable=False)
    manufc = Column(String(30), nullable=False)
    eng_cnt = Column(Numeric(2, 0), nullable=False)
    fleet_cnt = Column(Numeric(4, 0), nullable=False)


class Passenger(Base):
    __tablename__ = 'passenger'

    pid = Column(Numeric(6, 0), primary_key=True, nullable=False)
    p_fname = Column(String(30), nullable=False)
    p_lname = Column(String(30), nullable=False)
    p_nationality = Column(String(30), nullable=False)
    p_gender = Column(CHAR(1), nullable=False)
    p_passportno = Column(String(10), nullable=False)
    p_passexdate = Column(Date, nullable=False)
    p_dob = Column(Date, nullable=False)
    p_type = Column(CHAR(1), primary_key=True, nullable=False)


class Customer(Passenger):
    __tablename__ = 'customer'
    __table_args__ = (
        ForeignKeyConstraint(['pid', 'p_type'], ['passenger.pid', 'passenger.p_type']),
    )

    pid = Column(Numeric(6, 0), primary_key=True, nullable=False)
    p_type = Column(CHAR(1), primary_key=True, nullable=False)
    c_id = Column(Numeric(6, 0), nullable=False, unique=True)
    c_street = Column(String(50), nullable=False)
    c_city = Column(String(50), nullable=False)
    c_cntry = Column(String(50), nullable=False)
    c_email = Column(String(50), nullable=False)
    c_contctno = Column(Numeric(10, 0), nullable=False)
    c_cntrycode = Column(String(4), nullable=False)
    c_pass_cnt = Column(Numeric(4, 0), nullable=False)
    c_er_fname = Column(String(30), nullable=False)
    c_er_lname = Column(String(30), nullable=False)
    c_econtctno = Column(Numeric(10, 0), nullable=False)
    c_ecntcode = Column(String(4), nullable=False)
    c_type = Column(CHAR(1), nullable=False)


class BookAgent(Customer):
    __tablename__ = 'book_agent'
    __table_args__ = (
        ForeignKeyConstraint(['pid', 'p_type'], ['customer.pid', 'customer.p_type']),
    )

    pid = Column(Numeric(6, 0), primary_key=True, nullable=False)
    ag_name = Column(String(30), nullable=False)
    web_addr = Column(String(30), nullable=False)
    ag_cntctno = Column(Numeric(10, 0), nullable=False)
    p_type = Column(CHAR(1), primary_key=True, nullable=False)


class Mbrshp(Customer):
    __tablename__ = 'mbrshp'
    __table_args__ = (
        ForeignKeyConstraint(['pid', 'p_type'], ['customer.pid', 'customer.p_type']),
    )

    pid = Column(Numeric(6, 0), primary_key=True, nullable=False)
    m_name = Column(String(30), nullable=False)
    assc_airl = Column(String(30), nullable=False)
    m_stdate = Column(Date, nullable=False)
    m_end_date = Column(Date, nullable=False)
    p_type = Column(CHAR(1), primary_key=True, nullable=False)


class SpclReq(Base):
    __tablename__ = 'spcl_req'

    srid = Column(Numeric(6, 0), primary_key=True)
    sr_name = Column(String(50), nullable=False)


class Airline(Base):
    __tablename__ = 'airline'

    airl_id = Column(Numeric(6, 0), primary_key=True)
    airl_name = Column(String(30), nullable=False)
    hub = Column(String(3), nullable=False)
    hq_city = Column(String(30), nullable=False)
    hq_cntry = Column(String(30), nullable=False)
    airp_id = Column(ForeignKey('airport.airp_id'), nullable=False)

    airp = relationship('Airport')
    model = relationship('Model', secondary='airl_mod')


class Invoice(Base):
    __tablename__ = 'invoice'

    inv_id = Column(Numeric(6, 0), primary_key=True)
    inv_date = Column(Date, nullable=False)
    inv_amt = Column(Numeric(7, 2), nullable=False)
    ins_id = Column(ForeignKey('insurance.ins_id'), nullable=False)

    ins = relationship('Insurance')


t_airl_mod = Table(
    'airl_mod', metadata,
    Column('airl_id', ForeignKey('airline.airl_id'), primary_key=True, nullable=False),
    Column('mid', ForeignKey('model.mid'), primary_key=True, nullable=False)
)


class Flight(Base):
    __tablename__ = 'flight'

    f_id = Column(Numeric(6, 0), primary_key=True)
    f_number = Column(String(20), nullable=False)
    airl_id = Column(ForeignKey('airline.airl_id'), nullable=False)

    airl = relationship('Airline')


class PassIn(Base):
    __tablename__ = 'pass_ins'
    __table_args__ = (
        ForeignKeyConstraint(['pid', 'p_type'], ['customer.pid', 'customer.p_type']),
    )

    buy_date = Column(Date, nullable=False)
    pid = Column(Numeric(6, 0), primary_key=True, nullable=False)
    ins_id = Column(ForeignKey('insurance.ins_id'), primary_key=True, nullable=False)
    p_type = Column(CHAR(1), primary_key=True, nullable=False)

    ins = relationship('Insurance')
    customer = relationship('Customer')


class Payment(Base):
    __tablename__ = 'payment'

    pay_id = Column(Numeric(6, 0), primary_key=True)
    p_date = Column(Date, nullable=False)
    p_amt = Column(Numeric(7, 2), nullable=False)
    p_method = Column(CHAR(1), nullable=False)
    p_cardno = Column(Numeric(20, 0), nullable=False)
    pay_fname = Column(String(30), nullable=False)
    pay_lname = Column(String(30), nullable=False)
    invoice_inv_id = Column(ForeignKey('invoice.inv_id'), nullable=False)

    invoice_inv = relationship('Invoice')


class AirpFl(Base):
    __tablename__ = 'airp_fl'

    port_type = Column(CHAR(1), nullable=False)
    airp_dept_date = Column(DateTime(True), nullable=False)
    airp_id = Column(ForeignKey('airport.airp_id'), primary_key=True, nullable=False)
    f_id = Column(ForeignKey('flight.f_id'), primary_key=True, nullable=False)

    airp = relationship('Airport')
    f = relationship('Flight')


class FlightPsngr(Base):
    __tablename__ = 'flight_psngr'
    __table_args__ = (
        ForeignKeyConstraint(['pid', 'p_type'], ['customer.pid', 'customer.p_type']),
    )

    fpid = Column(Numeric(7, 0), primary_key=True, nullable=False)
    f_id = Column(ForeignKey('flight.f_id'), nullable=False)
    pid = Column(Numeric(6, 0), nullable=False)
    cab_id = Column(ForeignKey('cab_cls.cab_id'), nullable=False)
    mp_id = Column(ForeignKey('meal_pl.mp_id'), nullable=False)
    srid = Column(ForeignKey('spcl_req.srid'), nullable=False)
    fp_id = Column(Numeric(6, 0), primary_key=True, nullable=False)
    p_type = Column(CHAR(1), nullable=False)

    cab = relationship('CabCl')
    f = relationship('Flight')
    mp = relationship('MealPl')
    customer = relationship('Customer')
    spcl_req = relationship('SpclReq')
