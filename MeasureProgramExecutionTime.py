import time
import random
from BinarySearchAlgorithm import binary_search as bs

random_list = list(range(10000000))
init_num = 6000000

# 1st Approach
start = time.time()
random_choice = random.choice(random_list)
while random_choice != init_num:
    random_choice = random.choice(random_list)
end = time.time()
print(end - start)

# 2nd Approach
start2 = time.time()
for el in random_list:
    if el == init_num:
        break
end2 = time.time()
print(end2 - start2)

# 3rd Approach
start3 = time.time()
result = bs(random_list, init_num)
end3 = time.time()
print(end3 - start3)
