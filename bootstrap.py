from dotenv import dotenv_values
import os

class AppConfig:
    
    def __init__(self, dotenv_path):
        config = dotenv_values(dotenv_path)
        for k in config:
            setattr(self, k, config[k])
