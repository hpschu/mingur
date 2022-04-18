from dotenv import dotenv_values
import os

class AppConfig:
    settings = {}
    
    def __init__(self, dotenv_path):
        config = dotenv_values(dotenv_path)
        for k in config:
            print(k)
            print(config[k])
            print(os.getcwd())
            setattr(self, k, config[k])
