#TEST

import itertools

#iterateur - count
Test1 = itertools.count(10)
print (Test1)

#cycle
Test2 = itertools.cycle('ABCD')
print (Test2)

#repeat
Test3 = itertools.repeat(10,5)
print (Test3)

#accumulate
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print (list(itertools.accumulate(data)))
#print (list(itertools.accumulate(data, operator.mul)))     # running product
print (list(itertools.accumulate(data, max)))              # running maximum

#permutation
print (list(itertools.permutations(['g', 'e', 'k'])))
antoine = (list(itertools.permutations(['a', 'n', 't', 'o', 'i', 'n', 'e'])))
cathia =  (list(itertools.permutations(['c', 'a', 't', 'h', 'i', 'a'])))

for element in cathia:
    print (element)
print (len(cathia))

for element in antoine:
    print (element)
print (len(antoine))
