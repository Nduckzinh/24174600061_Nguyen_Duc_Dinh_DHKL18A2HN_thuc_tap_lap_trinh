#Bài 6
import math
print("phuong trinh bac 2 co dang la: ax^2 + bx +c = 0")
a = int(input("Nhap he so a (a khac 0): "))
while a == 0:
    print("Yeu cau nhap lai")
    a = int(input("Nhap he so a (a khac 0): "))
b = int(input("Nhap he so b: "))
c = int(input("Nhap he so c: "))
print(f"Phuong trinh bac 2 sau khi nhap he so la: {a}x^2 + {b}x + c = 0")
delta = b**2 - 4*a*c
if delta > 0:
    x1 = ((-b + math.sqrt(delta))/(2*a))
    x2 = ((-b - math.sqrt(delta))/(2*a))
    print(f"phuong trinh co 2 nghiem phan biet la: {x1:.2f} va {x2:.2f}")
elif delta < 0:
    print("phuong trinh vo nghiem.")
else:
    x = -b/2*a
    print(f"nghiem duy nhat cua phuong trinh la: {x:.2f}")
