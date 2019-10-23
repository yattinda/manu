from tank import Tank

tanks = {"a":Tank("Alpha"), "b":Tank("Blabo"), "c":Tank("Chary")}
alivetanks = len(tanks)

while alivetanks > 1:

    print
    for tankname in sorted( tanks.keys()):
        print (tankname, tanks[tankname])

    first = str(input("who fires??").lower())
    second= str(input("who at??").lower())

    try:
        firsttank = tanks[first]
        secondtank = tanks[second]
    except KeyError:
        print ("NO such Tank")

        continue

    if not firsttank.alive or not secondtank.alive:
        print("already dead")

        continue

    print ("*" *30)

    firsttank.fire_at(secondtank)
    if not secondtank.alive:
        alivetanks -= 1

    print ("*" *30)

for tank in tanks.value:
    if tank.alive:
        print (tank.name, "is the winner")
        break
