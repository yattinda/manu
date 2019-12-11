#! /usr/bin/env python3
# mapIT.py コマンドラインやクリップボードに指定した住所の地図を習得する

import webbrowser, sys , pyperclip
if len(sys.argv) > 1:
    #コマンドラインから住所を習得
    address = "".join(sys.argv[1:])
else:
    #クリップボードから住所を習得
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)

#./mapIT.py （住所）　　をコマンドラインで実行
