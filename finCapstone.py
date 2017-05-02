from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime

key = 'AIzaSyBh9lo7ruqvMWabcJWufswS8E8PpkKvxVs'

BAC = data.DataReader("BAC", 'google', start='2006-01-01', end='2016-01-01')

print(BAC)
