# import array
x = [1, 2, 3, 4, 5]
# print(x)


# x = array.array("i",[1, 2, 3, 4, 5])
# print(x)
# print(type(x))

# nilaiSiswa = [80, 90, 85, 75, 95]
# print(nilaiSiswa[0])

# for nilaiSiswa in nilaiSiswa:
#     print(nilaiSiswa)

# jumlahAbsen = [3 for i in range(5)]
# print(jumlahAbsen)

# for i in range(5):
#     jumlahAbsen[i] = i
# print(jumlahAbsen)

var_arr = [1, 2, 3, 4, 5]
for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i + 1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, next elements: {next_element}")
