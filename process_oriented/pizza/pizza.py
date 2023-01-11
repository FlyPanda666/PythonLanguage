import logging

from utils.common import init_logger

init_logger()
logger = logging.getLogger(__name__)

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

print("You ordered a " + pizza["crust"] + "-crust pizza" + "with the following toppings: ")
for topping in pizza["toppings"]:
    print("\t" + topping)

# https://wenku.baidu.com/view/a1beed27bdd5b9f3f90f76c66137ee06eff94e9a.html
# 传递任意数量的实参.
# 如果一个函数可以接受任意数量的参数,那么在函数定义的时候需要对其进行一定的处理.
# 形参名中的星号让Python创建一个名为toppings的空元组,并将接收到的所有值都封装到这个元组中.


def make_pizza(*toppings):
    print(toppings)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings :")
    for topping in toppings:
        print("- " + topping)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# 如果要让函数接收不同类型的实参,必须在函数定义中将接纳任意数量实参的形参放在最后.
# Python先匹配位置实参和关键字实参,再将余下的实参都收集到最后一个形参中.
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings :")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")
