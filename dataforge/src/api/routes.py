from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from pydantic import BaseModel
from dataforge.src.common_modules import get_db
from dataforge.src.api.models import PowerData

router = APIRouter()

# Pydantic Models
class PowerDataCreate(BaseModel):
    gid: int
    sid: int
    stat: int
    rcnt: int
    r_current: int
    y_current: int
    b_current: int
    t_current: int
    ry_volt: int
    yb_volt: int
    br_volt: int
    vll_avg: int
    r_volt: int
    y_volt: int
    b_volt: int
    vln_avg: int
    r_watts: int
    y_watts: int
    b_watts: int
    t_watts: int
    r_var: int
    y_var: int
    b_var: int
    t_var: int
    r_voltampere: int
    y_voltampere: int
    b_voltampere: int
    kva: int
    r_powerfactor: float
    y_powerfactor: float
    b_powerfactor: float
    avg_pf: float
    frequency: float

class PowerDataUpdate(BaseModel):
    stat: int
    rcnt: int
    t_current: int

class PowerDataDelete(BaseModel):
    gid: int
    sid: int


# Endpoints
@router.get("/power_data")
async def get_power_data(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PowerData))
    data = result.scalars().all()
    return data


@router.post("/power_data")
async def create_power_data(data: PowerDataCreate, db: AsyncSession = Depends(get_db)):
    power_data = PowerData(**data.dict())
    db.add(power_data)
    await db.commit()
    return power_data


@router.put("/power_data/{gid}/{sid}")
async def update_power_data(gid: int, sid: int, data: PowerDataUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PowerData).filter(PowerData.gid == gid, PowerData.sid == sid))
    power_data = result.scalars().first()
    if not power_data:
        raise HTTPException(status_code=404, detail="PowerData entry not found")

    for key, value in data.dict().items():
        setattr(power_data, key, value)

    await db.commit()
    return power_data


@router.delete("/power_data")
async def delete_power_data(data: PowerDataDelete, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PowerData).filter(PowerData.gid == data.gid, PowerData.sid == data.sid))
    power_data = result.scalars().first()
    if not power_data:
        raise HTTPException(status_code=404, detail="PowerData entry not found")

    await db.delete(power_data)
    await db.commit()
    return {"message": f"PowerData entry with gid={data.gid} and sid={data.sid} deleted successfully."}



