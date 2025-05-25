def plus(x, y):
    z = input_list[x] + input_list[y]
    print(z)


with open("input.txt", "r") as input_list:
    list_input = []
    for letters in input_list:
        list_input.extend(letters.split(","))
    str_input_1 = str(input_list [1])
    str_input_2 = str(input_list [2])
    if list_input[0] == 1:
        plus(str_input_1, str_input_2)
    print(list_input)