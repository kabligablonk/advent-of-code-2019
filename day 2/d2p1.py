def plus(x, y, a):
    z = int(separated_list_elements[x]) + int(separated_list_elements[y])
    separated_list_elements[a] = z
    final_list_elements.extend(separated_list_elements[0:4])
    del separated_list_elements[0:4]

def multiply(x, y, a):
    z = int(separated_list_elements[x]) * int(separated_list_elements[y])
    separated_list_elements[a] = z
    final_list_elements.extend(separated_list_elements[0:4])
    del separated_list_elements[0:4]

with open("input.txt", "r") as input_list:
    separated_list_elements = []
    final_list_elements = []
    for elements in input_list:
        separated_list_elements.extend(elements.split(","))
    while True:
        opcode = int(separated_list_elements[0])
        string_input_1 = int(separated_list_elements [1])
        string_input_2 = int(separated_list_elements [2])
        string_input_3 = int(separated_list_elements [3])
        if opcode == 1:
            plus(string_input_1, string_input_2, string_input_3)
        if opcode == 2:
            multiply(string_input_1, string_input_2, string_input_3)
