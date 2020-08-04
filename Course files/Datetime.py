# datetime
# 计算输入的日期是一年中的第几天
import datetime as t

dtstr = input('Enter the datetime:(20170228):')
d = dtstr[0:4]+"年"+dtstr[4:6]+"月"+dtstr[6:]+"日"
dt = t.datetime.strptime(dtstr, "%Y%m%d")

print("你输入的日期是:{}".format(d))
andtstr = dtstr[:4] + '0101'
andt = t.datetime.strptime(andtstr, "%Y%m%d")

print("你输入的日期是这一年中的第:" + str((int((dt - andt).days)) + 1)+"天")
