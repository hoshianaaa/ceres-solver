# https://www.jstage.jst.go.jp/article/jjspe/76/10/76_10_1130/_pdf
# 2リンクアームの観測モデル
# y(i) = x3 * sin(q1,i + x1) + x4 * sin(q1,i + x1 + q2,i + x2) + x5

import math

def deg2rad(d):
  return d * math.pi / 180

def rad2deg(r):
  return r * 180 / math.pi

x1 = 10 # (/deg)
x2 = 10 # (/deg)
x3 = 4.5 # (/m)
x4 =  2.5 # (/m)
x5 = 1.5 # (/m)

count = 0
for i in range(10):
  for j in range(10):
    q1 = 5 * i
    q2 = 5 * j
    y = x3 * math.sin(deg2rad(q1 + x1)) + x4 * math.sin(deg2rad(q1 + x1 + q2 + x2)) + x5
    # print(str(q1) + "," + str(q2) + "," + str(y))
    print(str(deg2rad(q1)) + "," + str(deg2rad(q2)) + "," + str(y) + ",")
    count = count + 1

print("count:", count)
