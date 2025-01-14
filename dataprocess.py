import pandas as pd
import numpy as np
import scipy.stats as st

df = pd.read_excel('阻断.xlsx',header=None)
origin_data = df.iloc[:,2].values
mask = np.isnan(origin_data)
origin_data = origin_data[~mask]
mean = np.mean(origin_data)
std = np.std(origin_data)

threshold = 3*std

outliers = np.where(np.abs(origin_data-mean)>threshold)

clean_data = np.delete(origin_data,outliers)
np.savetxt('第三列.txt',clean_data)