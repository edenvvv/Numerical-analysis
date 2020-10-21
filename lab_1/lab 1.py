import math
import sys
# 1
num1 = float(input("enter the a (in a*(b/c-d)-e): "))
num2 = float(input("enter the b (in a*(b/c-d)-e): "))
num3 = float(input("enter the c (in a*(b/c-d)-e): "))
num4 = int(input("enter the d (in a*(b/c-d)-e): "))
num5 = int(input("enter the e (in a*(b/c-d)-e): "))
print(math.fabs(num1*(num2/num3-num4)-num5)-sys.float_info.epsilon)

# 2.1
print(f"Machine precision is: {sys.float_info.epsilon}")
