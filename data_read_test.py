import struct
import os
import numpy
import matplotlib.pyplot as plt
import pandas as pd

#############################################################
# TDX Day Line Data Format                                  #
#    0      1      2      3      4      5        6      7   #
# integer float  float  float  float  float   integer float #
#  Date    Open  High   Low     Close  Amount  Volume resv  #
#############################################################
def unpack_tdx(filename):
    f = open(filename,"rb")
    size = os.path.getsize(filename)
    l = list()
    for i in range(size/32):
        d = struct.unpack("IfffffIf",f.read(32))
        l.append(d)
    return l

al = unpack_tdx("data.day/f/29#AL8.day")
ml = unpack_tdx("data.day/f/29#ML8.day")

diff = list()
date = list()
for i in range(len(al)):
    diff.append(al[i][4]-ml[i][4])
    date.append(al[i][0])

ts = pd.Series(diff,index=date)
ts.cumsum()
ts.plot()
