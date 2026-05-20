a = [10, 20, 30, 40, 50, 60]
b = a[1:5:2]

sum_val = 0
for i in b:
    if i > 25:
        sum_val += i

print(sum_val)
