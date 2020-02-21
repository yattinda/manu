import time
while True:
    try:
    time = int(input("秒数を指定してください") )
    signal = input("スタートを入力してください")
    except:
        print("ERROR!もう一度やりなおしてね！")

print("3秒後に開始します")
sleep(3)
print("start!!")
start = time.time()
    #timetime()でスタンプを押した人の名前と時間を記録
    #もし全員がスタンプを押したら終了
    #時間を超えた人は終了
winnername =
winnertime =
print("勝者は"+winnername+"で、時間は"+winnertime+"です")
onemore = input("もう一度繰り返しますか（Y/N）")
if onemore == N or onemore == n:
    break
