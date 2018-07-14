import memory_profiler
import random
import time

names = ['Vlad', 'Victor', 'Alex', 'Karina', 'Valeria']
majors = ['Math', 'Engineering', 'CompSci', 'Business', 'Chem']

print ('Memory (Before): {}Mb'.format(memory_profiler.memory_usage_psutil()) )

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

# t1 = time.clock()
# people = people_generator(1000000)
# t2 = time.clock()

print ( 'Memory (After) : {}Mb'.format(memory_profiler.memory_usage_psutil()) )
print ( 'Took {} Seconds'.format(t2-t1) )
