guess_me = 7
start = 1
while True:
	if guess_me > start:
		print("too low")
	elif guess_me < start:
		print("too high")
		break
	else:
		print("found it!")
		break
	start += 1


