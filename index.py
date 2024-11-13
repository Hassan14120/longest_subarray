def longest_subarray(array):
    max_length = 0 
    for i in range(len(array)):
        counter_1 =0
        counter_2 = 0
        for j in range(i, len(array)):
            if array[j] == 0:
                counter_1 += 1
            else:
                count_1 += 1
            if counter_1 == counter_2:
                max_length = max(max_length, j - i + 1)

    return max_length  


binary_array = [0,1,0,1,0,1,0,1]
print(longest_subarray(binary_array))