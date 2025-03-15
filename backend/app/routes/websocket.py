from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List

router = APIRouter(
    prefix="/ws",
    tags=["websocket"]
)

# WebSocket connections will be implemented here 