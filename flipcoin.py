import random
import time


repeat = int(input('How many times do you want to flip:'))
head = 0
tail = 0

for i in range(repeat):
    flipped = random.randrange(2)
    if flipped == 0:
        head += 1
    else:
        tail += 1
head_per = round((100/repeat)*head, 2)
tail_per = round((100/repeat)*tail, 2)
print('Tail percent: ', tail_per)
print('Head percent: ', head_per)