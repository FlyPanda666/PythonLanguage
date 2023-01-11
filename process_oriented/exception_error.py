import logging

from utils.common import init_logger

init_logger()
logger = logging.getLogger(__name__)

# 使用input函数时,Python将用户输入解读为字符串.
age = input("how old are you ?")
try:
    print(age >= 18)
except TypeError:
    print("###")
    print(int(age) >= 18)

print("*" * 10)


age = 23
try:
    # TypeError: can only concatenate str (not "int") to str
    message = "Happy " + age + "rd Birthday!"
except TypeError:
    print("error")
    message = "Happy " + str(age) + "rd Birthday!"

print(message)


class MyException(Exception):
    """自定义异常类"""
    what: str = "自定义的提示信息!"


def func():
    print("testing exception...")
    raise MyException


try:
    func()
except MyException as e:
    var = e.what
    print(var)
    print("test finish")
