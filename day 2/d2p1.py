def plus(x, y):
    z = int(separated_list_elements[x]) + int(separated_list_elements[y])
    print(z)

with open("input.txt", "r") as input_list:
    separated_list_elements = []
    for elements in input_list:
        separated_list_elements.extend(elements.split(","))
    string_input_1 = int(separated_list_elements [1])
    string_input_2 = int(separated_list_elements [2])
    if int(separated_list_elements[0]) == 1:
        plus(string_input_1, string_input_2)
