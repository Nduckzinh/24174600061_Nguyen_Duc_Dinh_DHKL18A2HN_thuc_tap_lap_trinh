#Bài 10
import math
x = int(input("Nhap vao so x: "))
y = int(input("Nhap vao so y: "))
f = ( math.sin(x) / ( ((2*x + y)/(math.cos(x)) - ((x**y)/(x-y)) )))
print(f"gia tri cua bieu thuc la: {f}")
