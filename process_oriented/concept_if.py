import logging

from utils.common import init_logger

init_logger()
logger = logging.getLogger(__name__)

requested_toppings = "mushroom"

if requested_toppings != "anchovies":
    print("Hold the anchovies")


requested_toppings = ["mushroom", "onions", "pineapple"]
print("mushroom" in requested_toppings)
print("pepperoni" in requested_toppings)


# if-elif-else结构功能强大,但仅适合用于只有一个条件满足的情况。
# 有时候必须检查你关心的所有条件,在这种情况下,应使用一系列不包含elif和else代码块的简单if语句.
# 如果你只想执行一个代码块,就使用if-elif-else结构,
# 如果你要运行多个代码块,就使用一系列独立的if语句.

requested_toppings = ["mushroom", "green peppers", "extra cheese"]

if "mushroom" in requested_toppings:
    print("adding mushroom")
if "pepperoni" in requested_toppings:
    print("adding pepperoni")
if "extra cheese" in requested_toppings:
    print("adding extra cheese")

print("\nFinished making your pizza!")


for requested_topping in requested_toppings:
    print("adding " + requested_topping + ".")

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print("adding " + requested_topping + ".")


requested_toppings = []
# 将列表名用在条件表达式中,Python将在列表至少包含一个元素时返回True,并在列表为空时返回False.
if requested_toppings:
    for requested_topping in requested_toppings:
        print("adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")


available_toppings = [
    "mushroom", "olives", "green peppers",
    "pepperoni", "pineapple", "extra cheese"
]

requested_toppings = ["mushroom", "french fires", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding " + requested_topping + " .")
    else:
        print("Sorry, we don't have " + requested_topping + " .")
print("\nFinished making your pizza!")
