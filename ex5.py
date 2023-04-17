def remove_duplicates(input_list):
    return list(set(input_list))

input_list = [1, 2, 3, 4, 4, 5, 5]
output_list = remove_duplicates(input_list)
print(output_list)
