def is_phone_number(text):

    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-" :
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-" :
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

#print(is_phone_number("090-208-9426"))

message = input("message")

for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print("電話番号は" + chunk)
print("完了")
