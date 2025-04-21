num = int(input('Enter a digit '))
count = 0

if num == 0:
    count = 1
else:
    num = abs(num)
    while num > 0:
        num //= 10
        count += 1

print('Total number of digits are', count)
