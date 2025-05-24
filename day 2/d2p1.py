with open("input.txt", "r") as input_list:
    data = list(input_list)
    list_input = []
    for letters in data:
        list_input.extend(letters.split(","))
    print(list_input)