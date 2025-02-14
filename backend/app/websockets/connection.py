from typing import List, Dict
from fastapi import WebSocket
from fastapi.websockets import WebSocketState
import logging

logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, pool_id: int):
        await websocket.accept()
        if pool_id not in self.active_connections:
            self.active_connections[pool_id] = []
        self.active_connections[pool_id].append(websocket)

    def disconnect(self, websocket: WebSocket, pool_id: int):
        if pool_id in self.active_connections:
            self.active_connections[pool_id].remove(websocket)

    async def broadcast_to_pool(self, pool_id: int, message: dict):
        print(message)
        if pool_id in self.active_connections:
            for connection in self.active_connections[pool_id]:
                await connection.send_json(message)
