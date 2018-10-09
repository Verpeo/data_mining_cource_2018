def calc_factorial(N):
    if N<= 1:
        return 1
    return N*calc_factorial(N-1)

test_list = []
for i in range(10):
    test_list.append(calc_factorial(i))

print(test_list)
print('-----------------------------------------------------------------')
def max_of_three(a,b,c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num

print(max_of_three(3,2,1))
print('-----------------------------------------------------------------')
def get_factorial_generator():
    fact = 1
    max_deep = 100
    counter = 0
    while counter <= max_deep: #while true
        if counter > 0:
            fact = fact*counter
        counter += 1
        yield fact


factorial_generator = get_factorial_generator()
print(next(factorial_generator))  # печатает 1
print(next(factorial_generator))  # печатает 1
print(next(factorial_generator))  # печатает 2
print(next(factorial_generator))  # печатает 6
print(next(factorial_generator))  # печатает 24

print('-----------------------------------------------------------------')
source_list = [1, 5, 20,31, 3, 7]
fact_list = [calc_factorial(i) for i in  source_list if i <= 30  ]
print(fact_list)
print('-----------------------------------------------------------------')
with  open('Onegin_utf8.txt','r', encoding='utf-8') as utf_8_onegin,  open('Onegin_windows1251.txt','r', encoding='windows-1251') as win_1251_onegin:
    print('Is it the same files? Answer is {}'.format(win_1251_onegin.read()==utf_8_onegin.read()))
