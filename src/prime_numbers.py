from itertools import count


class PrimeNumbers(object):
    ''' PrimeNumbers is a lazy prime number generator
        prim = list(islice(PrimeNumbers(), 10))
        gives a list with 10 prime numbers

        prim = PrimeNumber()
        while True:
            p = next(prime)
    '''
    def __init__(self):
        self._prime_numbers = [2, 3]
        self._counter = count(self._prime_numbers[-1] + 2, 2)

    def __iter__(self):
        return self

    def __next__(self):
        self._generate_prime_number()
        return self._prime_numbers[-3]

    def _generate_prime_number(self):
        def is_prim(x):
            return not any(filter(lambda t: x % t == 0, self._prime_numbers))

        self._prime_numbers.append(next(filter(lambda x: is_prim(x), self._counter)))