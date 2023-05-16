# https://www.jstage.jst.go.jp/article/jjspe/76/10/76_10_1130/_pdf
# 2リンクアームの観測モデル
# y(i) = x3 * sin(q1,i + x1) + x4 * sin(q1,i + x1 + q2,i + x2) + x5

x1 = 10
x2 = 20
x3 = 10
x4 =  15
x5 = 5

q1 = 10
q2 = 20

y = x3 * math.sin( 
