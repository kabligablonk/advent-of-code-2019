with open("input.txt", "r") as f:
    total = 0
    # keep total out of the loop to keep it constant
    for x in f.readlines():
        mass = int(x)
        fuel = ((mass//3) -2)
        # declaring variables for each input in the file
        while fuel > 0:
            total += fuel
            # add the fuel that was just computed for to the total
            fuel = ((fuel//3) -2)
    print(total)