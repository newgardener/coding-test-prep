n = 5
data = [8, 5, 4, 7, 2]

""" Insertion Sort """
for i in range(1, n):
    for j in range(i, 0, -1):
        if data[j - 1] > data[j]:
            data[j], data[j - 1] = data[j - 1], data[j]
        else:
            break

for x in data:
    print(x)
