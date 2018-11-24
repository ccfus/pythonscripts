from my_module import find_index
#import my_module
#import my_module as nm

import random

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)

random_course = random.choice(courses)
print(random_course)