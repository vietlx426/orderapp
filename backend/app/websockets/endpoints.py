from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from .connection import ConnectionManager
from app.schemas.pool import PoolOrderCreate
import json
import logging

logger = logging.getLogger(__name__)
router = APIRouter()
manager = ConnectionManager()

@router.websocket("/ws/{pool_id}")
async def websocket_endpoint(websocket: WebSocket, pool_id: int):
    await manager.connect(websocket, pool_id)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket, pool_id)
