my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
translated = []
with open("part4_r.txt", "r") as my_part4_r:
    for line in my_part4_r:
        piece = line.split(" - ")
        if piece[0] in my_dict:
            translated.append(my_dict[piece[0]] + " - " + piece[1])

with open("part4_w.txt", "w") as my_part4_w:
    my_part4_w.writelines(translated)
