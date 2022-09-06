import random
import time

new_list = []
old_list = []

def generateRandomNumber():
    num = random.randint(0,100)
    return num

for i in range(0,15):
    new_list.append(generateRandomNumber)

while True:
    number = generateRandomNumber()
    if number not in old_list:
        if len(old_list) < 10:
            old_list.append(number)
        else:
            old_list.pop(0)
            old_list.append(number)
    print(old_list)
    time.sleep(2)