import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('part7.txt', 'r') as file:
    for line in file:
        title, ownership, revenue, costs = line.split()
        profit[title] = int(revenue) - int(costs)
        if profit.setdefault(title) >= 0:
            prof = prof + profit.setdefault(title)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f"Average profit {prof_aver:.2f}")
    else:
        print(f"Average profit is absent. Everyone works at a loss")
    pr = {"Average profit ": round(prof_aver)}
    print(f"The profit of each company: {profit}, {pr}")
    profit.update(pr)

with open('part7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f"A json file was created with the following content: \n "
          f" {js_str}")
