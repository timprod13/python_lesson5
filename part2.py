with open("part2.txt", "r") as my_part2:
    line_count = 0
    letter_count = 0
    for line in my_part2:
        line_count += 1
        letter_count = line.count(" ") + 1
        print(f"{letter_count} words in line {line_count}")
    print(f"{line_count} lines in file")
