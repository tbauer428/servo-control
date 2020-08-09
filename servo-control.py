import time
from adafruit_servokit import ServoKit
import asyncio
import logging
import websockets

logging.basicConfig(level=logging.INFO)

kit = ServoKit(channels=16)


async def send_message(websocket, message):
    await websocket.send(message)
    print("Sent: " + message)


angle = 0
maximum_servo_angle = 150
minimum_servo_angle = 0


async def handler(websocket, path):
    global angle
    global kit
    async for message in websocket:
        print("Received: " + message)
        if message == "ROTATE_RIGHT":
            if angle == maximum_servo_angle:
                print(angle)
                pass
            else:
                angle += 1
                kit.servo[0].angle = angle
                print(angle)
        elif message == "ROTATE_LEFT":
            if angle == minimum_servo_angle:
                print(angle)
                pass
            else:
                angle -= 1
                kit.servo[0].angle = angle
                print(angle)

start_server = websockets.serve(handler, "192.168.1.54", 8080)

print("servo-control.py is running")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
