import os
import time
import asyncio
from datetime import datetime

COEFF = 1


async def task1(plant, water, grow, live):
    COEFF = 0.001
    print(f"0 Beginning of sowing the {plant} plant")
    print(f"1 Soaking of the {plant} started")
    await asyncio.sleep(COEFF * water)
    print(f'2 Soaking of the {plant} is finished')
    print(f'3 Shelter of the {plant} is supplied')
    await asyncio.sleep(COEFF * grow)
    print(f'4 Shelter of the {plant} is removed')
    print(f'5 The {plant} has been transplanted')
    await asyncio.sleep(COEFF * live)
    print(f'6 The {plant} has taken root')
    print(f'9 The seedlings of the {plant} are ready')


async def food(plant):
    COEFF = 0.001
    print(f'7 Application of fertilizers for {plant}')
    await asyncio.sleep(COEFF * 3)
    print(f'7 Fertilizers for the {plant} have been introduced')
    print(f'8 Treatment of {plant} from pests')
    await asyncio.sleep(COEFF * 5)
    print(f'8 The {plant} is treated from pests')

async def sowing(*data):
    tasks = []
    for plant in data:
        tasks.append(asyncio.create_task(task1(*plant)))
        tasks.append(asyncio.create_task(food(plant[0])))
    await asyncio.gather(*tasks)



data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]
asyncio.run(sowing(*data))