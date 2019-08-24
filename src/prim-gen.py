import time
from itertools import takewhile, islice, repeat
from prime_numbers import PrimeNumbers

c = 20000
p = 0
i=0
for p in PrimeNumbers():
    start = time.time()
    i += 1
    end = time.time() - start
    print('Prim: {}. Count:{} {:1.3f}s Dichte {:1.3f}'.format(p, i,  end, float(i) / float(p)))

# prim = PrimeNumbers()
#
# start = time.time()
# prim = list(takewhile(lambda x: x < 224738, prim))
# end = time.time() - start
# print(prim)
# print(
#     '1. Prim: {}. It took for {}: {:1.3f}s Dichte {:1.3f}'.format(prim[-1], len(prim), end, float(len(prim)) / float(prim[-1])))

# start = time.time()
# prim = list(map(lambda x: next(x), repeat(PrimeNumbers(), c)))
# for p in prim:
#     pass
# end = time.time() - start
# print(prim)
# print('2. Prim: {}. It took for {}: {:1.3f}s Dichte {:1.3f}'.format(prim[-1], c, end, float(c) / float(p)))

# start = time.time()
# prim = list(islice(PrimeNumbers(), c))
# time.sleep(1)
# print(prim)
# end = time.time() - start
# print('3. Prim: {}. It took for {}: {:1.3f}s Dichte {:1.3f}'.format(prim[-1], c, end, float(c) / float(prim[-1])))
#
# start = time.time()
# prim = PrimeNumbers()
# for i in range(c):
#     p = next(prim)
# end = time.time() - start
# print('4. Prim: {}. It took for {}: {:1.3f}s Dichte {:1.3f}'.format(p, c, end, float(c) / float(p)))
# # print(list(prim))
