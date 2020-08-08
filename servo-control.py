"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
# from adafruit_servokit import ServoKit
import asyncio
import logging
import websockets

logging.basicConfig(level=logging.INFO)

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
# kit = ServoKit(channels=16)

count = 0
angle = 0
while count < 9:
    if angle > 149:
        angle = 0
    else:
        # print(angle)
        # kit.servo[0].angle = angle
        angle = angle + 1
        time.sleep(.05)

print("running")


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
