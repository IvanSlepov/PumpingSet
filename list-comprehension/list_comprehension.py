import timeit
import time
import test_data
import functools


def number_sum(x: int, y: int) -> int:
    return x + y


print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))


mapped_list: list = list(map(number_sum, test_data.test_list, test_data.test_list_2))
mapped_list_2: list = list(map(lambda x, y: x * y, test_data.test_list, test_data.test_list_2))

filtered_list: list = list(filter(lambda some_number: 3 < some_number < 15, test_data.test_list))

reduced_to_sum: int = functools.reduce(lambda a, b: a + b, test_data.test_list)

print(reduced_to_sum)
print(filtered_list)
print(mapped_list)
print(mapped_list_2)

