import os

from environs import Env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = Env()
env.read_env()

DEBUG = env.bool("DEBUG", default=True)
