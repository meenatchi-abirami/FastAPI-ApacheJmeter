from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PowerData(Base):
    __tablename__ = "power_data"
    
    gid = Column(Integer, primary_key=True, autoincrement=False)  # Assuming 'gid' is unique
    sid = Column(Integer, nullable=False)
    stat = Column(Integer, nullable=False)
    rcnt = Column(Integer, nullable=False)
    r_current = Column(Integer, nullable=False)
    y_current = Column(Integer, nullable=False)
    b_current = Column(Integer, nullable=False)
    t_current = Column(Integer, nullable=False)
    ry_volt = Column(Integer, nullable=False)
    yb_volt = Column(Integer, nullable=False)
    br_volt = Column(Integer, nullable=False)
    vll_avg = Column(Integer, nullable=False)
    r_volt = Column(Integer, nullable=False)
    y_volt = Column(Integer, nullable=False)
    b_volt = Column(Integer, nullable=False)
    vln_avg = Column(Integer, nullable=False)
    r_watts = Column(Integer, nullable=False)
    y_watts = Column(Integer, nullable=False)
    b_watts = Column(Integer, nullable=False)
    t_watts = Column(Integer, nullable=False)
    r_var = Column(Integer, nullable=False)
    y_var = Column(Integer, nullable=False)
    b_var = Column(Integer, nullable=False)
    t_var = Column(Integer, nullable=False)
    r_voltampere = Column(Integer, nullable=False)
    y_voltampere = Column(Integer, nullable=False)
    b_voltampere = Column(Integer, nullable=False)
    kva = Column(Integer, nullable=False)
    r_powerfactor = Column(Float, nullable=False)
    y_powerfactor = Column(Float, nullable=False)
    b_powerfactor = Column(Float, nullable=False)
    avg_pf = Column(Float, nullable=False)
    frequency = Column(Float, nullable=False)
