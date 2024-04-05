import dice
from fastapi import FastAPI, HTTPException
from typing import List


app = FastAPI(title="Roll API", version="1.0.0")


@app.get("/dice", response_model=list[int], tags=["Roll"])
async def roll_dice(amount, sides)->List[int]:
    """Roll dice."""
    books = roll(amount, sides)
    return books


def roll(amount:int, sides:int)->list[int]:
    return dice.roll(f'{amount}d{sides}')