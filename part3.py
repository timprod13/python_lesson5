with open("part3.txt", "r") as my_part3:
    line_count = 0
    amount = 0
    low_earning = []
    for line in my_part3:
        line_count += 1
        piece = line.split(" ")
        if int(piece[1]) < 20000:
            low_earning.append(piece[0])
        amount += int(piece[1])

print(f"Persons with salary less than 20 thousands: {low_earning}")
print(f"Average income of employees: {int(amount / line_count)}")
