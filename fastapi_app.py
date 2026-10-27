import json
import os
from fastapi import FastAPI
import requests

def create_app():
    print("Hello world!")
    app = FastAPI()

    @app.post('/greetings')
    async def say_hello(input_data: dict):
        return {'hello_string': f'{input_data["name"]}, your env is {os.getenv("MY_ENV")}'}

    @app.get('/actuator/health')
    async def health():
        return "I'm working!"

    return app
