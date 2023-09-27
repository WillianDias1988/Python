array = [5, 2, 4, 6, 1, 3, 2, 8, 9, 10, 15, 3, 0, 25]
j = 1
i = 0
chave = 0

for j in range(len(array)):
    chave = array[j]
    i = j-1
    while i >= 0 and array[i] > chave:
        array[i+1] = array[i]
        i = i-1
    array[i+1] = chave
print(array)
