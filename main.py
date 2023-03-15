
file = open("nt.txt")
reader = file.read()
reader = reader.replace("\n", "")
list = reader.split(" ")

result = []
for el in list:
    if len(el) >= 7:
        result.append(el)

final = "\n".join(result)
file.close()
file2 = open("333.txt", "w", encoding="utf-8")
file.write