try:
    with open("part5.txt", "w+") as my_part5_w:
        num_sum = 0
        input_line = input("Enter numbers separated by space: ")
        my_part5_w.writelines(input_line)
        numbers = input_line.split()
        for i in numbers:
            num_sum += int(i)
        print(num_sum)
except ValueError:
    print("Wrong values. Input error!")
