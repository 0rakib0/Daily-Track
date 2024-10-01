from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


class TestConsumer(AsyncConsumer):
    
    async def websocket_connect(self, evnt):
        print("Websocket succeefully connected...")
        
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print("Receive message from frontend", event)
        
    
    async def websocket_disconnect(self, event):
        print("Socket Connection lost...", event)
        raise StopConsumer()