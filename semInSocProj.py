import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from sklearn.linear_model import LinearRegression


df = read_csv("AI_index_db.csv")

df = df.fillna(0)
print(df.head(10))








