import math

horsenum = int(input("出馬順\n"))
distance = int(input("レースの距離\n"))
to_curve = int(input("コーナーまでの距離\n"))
corner = int(input("コーナー数\n"))

#以下参考データ
print("以下参考データ")
letternum = int(input("参考レースの出馬順\n")) 
letterdis = int(input("参考レースの距離\n"))
lettercurve = int(input("参考レースのコーナーまでの距離\n"))
lettercorner = int(input("参考レースのコーナー数\n"))
time = int(input("参考レースのタイム（秒)\n"))
column = int(input("その時内から何列目？\n"))
#情報入力

differ = math.pow(letternum -1,2) + math.pow(lettercurve,2)
letterinout = ((column - 1)  * (math.pi)) * 0.5
referdis = letterdis + math.sqrt(differ)  - lettercurve + (letterinout * lettercorner)
#参考レースの実距離

referspead = referdis / time
#参考レースの速さ

truediffer = math.pow(horsenum -1,2) + math.pow(to_curve,2)
print("予想タイム")	
for pig in range(1,4):
	inout = ((pig -1) * (math.pi)) * 0.5
	truedistance = distance + math.sqrt(truediffer) - to_curve + (inout * corner)
#レースの距離

	answertime = truedistance / referspead
#予想時間

	print(answertime)
