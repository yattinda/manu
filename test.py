import random
testtest = input("PPAP")

#1:グー 2:チョキ 3:パー
if testtest == "グー":
        userhand = 1

elif testtest =="チョキ":
        userhand = 2

elif testtest == "パー":
        userhand = 3

else:
    userhand = 4

cpuhand = random.randint(1,3)


if cpuhand == 1:
        returnhand = "グー"
elif cpuhand == 2:
        returnhand = "チョキ"
elif cpuhand == 3:
    returnhand = "パー"



status = (userhand - cpuhand + 2) % 3
#0:負け　1:勝ち　2:あいこ 基準は出した人

if status == 0:
    message = "あなたは負け犬です。惨めですね。"
elif status == 1:
    message = "機械相手に勝って何が楽しいんですか"
elif status == 2:
    message = "おっぱいもませろ童貞野郎"

if userhand == 4:
    finalreturn = "グー、チョキ、パーをカタカナで入力してね♡"
else:
    finalreturn = "私は"+returnhand+"をだしました",message




print(finalreturn)
