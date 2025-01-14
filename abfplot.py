import pyabf
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft

abf = pyabf.ABF(r"J:\JL\加药-Erastin\加药-Erastin-3h-2\药-1-10-19\2024_12_22_8001.abf")
x = abf.sweepX
y = abf.sweepY
k = 100000
t1 = 28.4
t2 =t1+0.4
xp = x[int(t1*k):int(t2*k)]
yp = y[int(t1*k):int(t2*k)]
fy = np.abs(fft(yp))/20000

np.savetxt(r"J:\JL数据处理\E\2024_12_22_8001.abf28.4.txt",yp)
np.savetxt(r"J:\JL数据处理\E\2024_12_22_8001.abf28.4f.txt",fy)
print("处理成功")