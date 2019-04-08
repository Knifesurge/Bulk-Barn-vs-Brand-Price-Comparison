# main.py
import matplotlib as mpl
import pandas as pd
import numpy as np
import json

data = {}

def load_file():
    global data
    fh = open('prices.json','r')
    data = json.load(fh)
    return

