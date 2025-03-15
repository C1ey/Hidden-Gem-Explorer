from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/interactions",
    tags=["interactions"]
)

# Routes will be implemented here 