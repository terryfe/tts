import struct
import os

/**
 通达信历史日线格式
    0      1      2      3      4      5        6      7
 integer float  float  float  float  float   integer float
 日期     开盘价  最高价  最低价  收盘价   成交额   成交量   保留
*/
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
