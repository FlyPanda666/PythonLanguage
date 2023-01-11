import logging

from utils.common import init_logger

init_logger()
logger = logging.getLogger(__name__)

# 列表生成式,列表生成式的性能高于列表的操作.
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)
print(type(odd_list))


def handle_item(item):
    return item * item


odd_list = [handle_item(i) for i in range(21) if i % 2 == 1]
print(odd_list)

# 生成器表达式
odd_gen = (i for i in range(21) if i % 2 == 1)
print(type(odd_gen))
print(next(odd_gen))
print(next(odd_gen))

odd_list = list(odd_gen)
print(type(odd_list))
print(odd_list)

# 字典推导式
my_dict = {"bobby1": 22, "bobby2": 23}
ans = {key: value for value, key in my_dict.items()}
print(ans)

# 集合推导式
my_set = {key for key in my_dict.keys()}
print(my_set)
print(type(my_set))
