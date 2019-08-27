import math
import random

tramp = list(range(1,53))

#print(tramp)

#マークの分類
#class trampmake:
#	def __init__(self, numnum):
#		self.num = numnum
#		return (int(self) % 13) + 1

def divisionnum(apple):
	banana = (int(apple) % 13) + 1

	return banana

def divisionmark(melon):
	orange = int(melon) // 13
	if orange = 0:
		return "♡"
	elif orange = 1:
		return "◇"
	elif orange = 2:
		return "♧"
	else:
		return "♧"


#how to use
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

playerhand_1 = divisionnum(playernum1[0])
playerhand_2 = divisionnum(playernum1[1])
stage1_1 = divisionnum(stage1[0])
stage1_2 = divisionnum(stage1[1])
stage1_3 = divisionnum(stage1[2])
cpunum1_1 = divisionnum(cpunum1[0])
cpunum1_2 = divisionnum(cpunum1[1])
cpunum2_1 = divisionnum(cpunum2[0])
cpunum2_2 = divisionnum(cpunum2[1])

#print(playerhand_1)
#print(playerhand_2)

print("your Hand is " + str(playerhand_1) + "," + str(playerhand_2))

print("table hand is " + str(stage1_1) + "," + str(stage1_2) + "," + str(stage1_3))


def win:
	if
