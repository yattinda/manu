from collections import deque

document = input("please documents:")

dq = deque(document)

while len(dq) > 1:
	if dq.popleft() != dq.pop():
		print("Too Bad")
		break
	else:
		print("OK")
	
