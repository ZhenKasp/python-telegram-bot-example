import json 
import requests
import time
import urllib 
import logging
import signal
import sys

def getText(update):
    return update["message"]["text"]

def getLocation(update):
    return update["message"]["location"]

def getChatId(update):
    return update["message"]["chat"]["id"]

def getUpId(update):
    return int(update["update_id"])

def getResult(updates):
    return updates["result"]

def getDesc(w):
    return w["weather"][0]["description"]

def getTemp(w):
    return w["main"]["temp"]

def getCity(w):
    return w["name"]


logger = logging.getLogger("weather-telegram")
logger.setLevel(logging.DEBUG)

cities = ["London", "Brasov"]
def sigHandler(signal, frame):
    logger.info("SIGINT received. Exiting... Bye bye")
    sys.exit(0)


def configLogging():
    handler = logging.FileHandler("run.log", mode="w")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)