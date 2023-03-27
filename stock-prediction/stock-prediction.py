import time
import math
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import LSTM
import numpy as np
import pandas as pd
import sklearn.preprocessing as prep
import os

# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

df = pd.read_csv('000002-from-1995-01-01.csv')
df.head()
