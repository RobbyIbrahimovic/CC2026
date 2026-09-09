# Trying to make a simple array program

var_array = [i for i in range(101)]

total_sum = 0
for i in var_array:
    total_sum += i

result = total_sum / len(var_array)
print(result)