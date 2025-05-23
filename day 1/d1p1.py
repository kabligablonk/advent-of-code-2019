def fuel_needed(x):
    total = 0
    for mass in x.readlines():
        mass = (int(mass.strip()) // 3) - 2
        total += mass
        print(mass)
    print(total)

fuel_needed(open("input.txt", "r"))