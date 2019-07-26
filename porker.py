import math
import random

tramp = list(range(1,53))

#print(tramp)

#マークの分類
class trampmake:
	def __init__(self, numnum):
		self.num = numnum
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

#CPUのカードを選ぶ, この繰り返し改善できそう
cpunum1 = random.sample(tramp,2)
tramp_AA = list(set(tramp) - set(cpunum1))
#print(tramp_AA)

cpunum2 = random.sample(tramp_AA,2)
tramp_BB = list(set(tramp_AA) - set(cpunum2))
#print(tramp_BB)

#プレイヤーのカードを選ぶ
playernum1 = random.sample(tramp_BB,2)
tramp_CC = list(set(tramp_BB) - set(playernum1))
#print(tramp_CC)

#二人のとき用
#playernum2 = random.sample(tramp_CC,2)
#tramp_DD = list(set(tramp_CC) - set(playernum2))
#print(tramp_DD)

#print(cpunum1)
#print(cpunum2)
#print(playernum1)
#print(playernum2)

stage1 = random.sample(tramp_CC,3)
#ここまでで最初の場が整う
playernum1[0]

playerhand_1 = trampmake(int(playernum1[0]))
playerhand_2 = trampmake(int(playernum2[1]))

print(playerhand_1.num)
print(playerhand_2.num)

print("your Hand is" + playerhand_1 + "," + playerhand_2)
