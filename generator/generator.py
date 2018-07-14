'''
This is some practice using Corey Schafer YT tutorial
'''

def square_numbers(nums):
    ''' Takes a number and returns its square as a list,
        holds the entire result in memory.
    '''
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])
print(my_nums) # [1, 4, 9, 16, 25]

def square_numbers2(nums):
    ''' This is a generator, which takes a number and returns its square
        one at a time, when asked for it. Does not hold the entire result in memory
    '''
    for i in nums:
        yield (i*i)

my_nums = square_numbers2([1,2,3,4,5])
print(my_nums) # <generator object square_numbers2 at 0x1034b9ba0>

print(next(my_nums)) # 1
# can print the rest of the numbers by asking for print each time

'''otherwise can use a forloop to loop over all the results '''
for num in my_nums:
    # here my_nums is the generator
    print(num)

'''Next we can use list comprehension to do this
    Here we will create a list'''
my_nums = [x*x for x in [1,2,3,4,5]]
print(my_nums) # [1, 4, 9, 16, 25]

''' And here we create a generator'''
my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums) #<generator object <genexpr> at 0x10698dba0>

for num in my_nums:
    print(num) # where my_nums is again a generator

'''Can conver everything from the generator into a list, but lose performance advantages'''
print(list(my_nums)) # [1, 4, 9, 16, 25]
