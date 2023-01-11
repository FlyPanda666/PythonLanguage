import logging
import pizza
from pizza import make_pizza
from pizza import make_pizza as mp
import pizza as p
from utils.common import init_logger

init_logger()
logger = logging.getLogger(__name__)

# Python读取这个文件时,代码行import pizza 让Python打开文件pizza.py,并将其中的所有函数都复制到这个程序中.
# 只需要编写一条import语句并在其中指定模块名,就可在程序中使用该模块中的所有函数.
# import 模块名 这种方式导入整个模块.
# from 模块名 import 函数名 这种方式导入模块中的特定函数.
# 使用as给函数指定别名
# 如果要导入的函数的名称可能与程序中现有的名称冲突,或者函数的名称太长,可指定简短而独一无二的别名 — 函数的另一个名称.
# 还可以给模块指定别名.给模块指定别名,但是该模块中的所有函数的名称都不会改变.
# from 模块名 import * 导入模块中的所有函数,这种情况最好不采用.
# Python可能遇到多个名称相同的函数或变量,进而覆盖函数,而不是分别导入所有的函数.
# 最佳的做法是,要么只导入你需要使用的函数,要么导入整个模块并使用句点表示法.

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

make_pizza(12, "mushrooms", "green peppers", "extra cheese")
mp(12, "mushrooms", "green peppers", "extra cheese")

p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")
