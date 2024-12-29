import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    DB_NAME = os.getenv('DB_NAME', 'twitter_trends')

    TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
    TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')

    PROXYMESH_USERNAME = os.getenv('PROXYMESH_USERNAME')
    PROXYMESH_PASSWORD = os.getenv('PROXYMESH_PASSWORD')
    PROXYMESH_HOST = os.getenv('PROXYMESH_HOST')