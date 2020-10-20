with open("part1.txt", "w") as my_part1_w:
    x = False
    while not x:
        input_line = input("Input your text: ")
        if input_line == "":
            x = True
        else:
            newline = input_line + '\n'
            my_part1_w.writelines(newline)

with open("part1.txt", "r") as my_part1_r:
    print(my_part1_r.readlines())
