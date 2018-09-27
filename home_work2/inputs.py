MaxTry = 1000
TryCount = 0
max_value = None
min_value = None
counter = 0
summ = 0
while True:
    TryCount += 1
    input_str = input()
    if input_str.upper() == 'DONE':
        break
    try:
        new_num = int(input_str)
        summ += new_num
        counter += 1
        if counter ==1:
            max_value = new_num
            min_value = new_num
        else:
            max_value = max(max_value,new_num)
            min_value = min(new_num,min_value)
    except :
        print("Wrong Input!")
    if TryCount >= MaxTry:
        print('Enough now!!')
        break

if counter > 0:
    print('average = {}, max value: {}, min value: {}  '.format(round(float(summ)/float(counter),2),max_value,min_value))

print('----------------------------------------')

d1={'Item1': {'Name': 'Cake', 'Price': 20},
 'Item2': {'Name': 'Pie', 'Price': 10},
 'Item3': {'Name': 'Chocobar', 'Price': 5}}
d2={'Item4': {'Name': 'Brownie', 'Price': 15},
 'Item5': {'Name': 'Cake', 'Price': 20}}

# for key in sorted( d2.keys()):
#     if not ( d2[key] in d1.values()):
#         d1[key] = d2[key]

l = list(d1.values())
#version 1
d1 = {**d1 ,   **{key:value for key, value   in d2.items() if not value in l}}

#version 2

# for key, value in d2.items():
#     if not value in l:
#         d1[key] = value


print (d1)
print('Sum of d products is: {}'.format(sum(item['Price'] for item in d1.values())))


print('----------------------------------------')

d1 = {'Item1': 120, 'Item2': 100, 'Item3': 500}
d2 = {'Item1': 5, 'Item2': 12, 'Item3': 7}

d = dict()
for key in d1.keys() & d2.keys():
    d[key] = d1[key]*d2[key]

print(d)
print('----------------------------------------')
