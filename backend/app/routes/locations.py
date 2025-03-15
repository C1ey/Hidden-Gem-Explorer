from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Location

router = APIRouter()

@router.post("/locations/")
async def add_location(location: Location, db: AsyncSession = Depends(get_db)):
    db.add(location)
    await db.commit()
    return {"message": "Location added!"}
