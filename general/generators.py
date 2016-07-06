import itertools


#generators - one result at a time using next
#until exhausted then StopIteration
def reverse(data):
    for idx in range(len(data)-1, -1, -1):
        yield data[idx]

g = reverse('abcd')
print g.next()
for char in g:
    print char



#generator expression
data = 'abcd'
g = (data[i] for i in range(len(data)-1, -1, -1))
for char in g:
    print char



#generator with infinite iterator
def divisible_by_nine(nums):
    for n in nums:
        if n % 9 == 0:
            yield n

#first 50 ints starting at 42 that are divisible by 9
print list(itertools.islice(divisible_by_nine(itertools.count(42)), 50))



#https://www.youtube.com/watch?v=EnSu9hHGq5o
#abstracting the iteration
#from Ned Batchelder
def interesting_lines(f):
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        if not line:
            continue
        yield line

with open('example.txt') as f:
    for line in interesting_lines(f):
        print 'doing something with:', line