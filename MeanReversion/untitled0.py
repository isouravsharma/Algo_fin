import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf 

data = yf.download(tickers='RELIANCE.NS', interval='1d', period='5y')

data['Adj Close']


