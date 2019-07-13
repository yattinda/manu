import math
import random

tramp = [range(1,53)]

class trampnum():
	def thirteen(self):
		return (int(self) % 13) + 1

class Card:
	def __init__(self, name, number):
		if trumpnum == 1:
			return "A"
		if trumpnum == 11:
			return "J"
		if trumpnum == 12:
			return "Q"
		if trumpnum == 13:
			return "K"

#にんずうせっていしたい
#human = int(input("How many people?"))

#if 0 <= human and 3 >= human:
#	print("OK")
	
#random.sampleはリストを返す

#CPUのカードを選ぶ
cpunum1 = random.sample(tramp,1)
tramp1 = tramp.pop(cpunum1)

cpunum2 = random.sample(trump1,1)
tramp2 = tramp1.pop(cpunum2)

#プレイヤーのカードを選ぶ
playernum1 = random.sample(trump2,1)
tramp3 = tramp2.pop(playernum1)

playernum2 = random.sample(trump3,1)
tramp4 = tramp3.pop(playernum2)

print(cpunum1)
print(cpunum2)
print(playernum1)
print(playernum2)
