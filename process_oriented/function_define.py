import logging
from typing import *
from utils.common import init_logger

init_logger()
logger = logging.getLogger(__name__)


def greet_user():
    """显示简单的问候语.
    :return:
    """
    print("Hello !")


greet_user()


# 在函数定义时,变量user_name是一个形参,函数完成其工作所需的一项信息.
def greet_user(user_name: str):
    """显示简单的问候语.
    :param user_name:
    :return:
    """
    print("Hello ," + user_name.title() + " !")


# 在函数调用时,传入的值是一个实参.实参是调用函数时传递给函数的信息.
greet_user("jesse")


def greet_users(names: List[str]):
    """列表作为函数的参数.
    :param names:
    :return:
    """
    for n in names:
        msg = "Hello, " + n.title() + " !"
        print(msg)


user_names = ["hannah", "ty", "margot"]
greet_users(user_names)


def get_formatted_name(first_name: str, last_name: str):
    """返回整洁的姓名.
    :param first_name:
    :param last_name:
    :return:
    """
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)


def get_formatted_name(first_name: str, middle_name: str, last_name: str):
    """格式化姓名.
    :param first_name:
    :param middle_name:
    :param last_name:
    :return:
    """
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("john", "lee", "hooker")
print(musician)


# 函数的形参中,如果有缺省参数,那么缺省参数应该放在最后.
def get_formatted_name(first_name: str, last_name: str, middle_name: str = ""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
musician = get_formatted_name("john", "hooker", "lee")
print(musician)


# 传递实参,向函数传递实参的方式很多,可使用位置实参,关键字实参,列表和字典.
# 位置实参,Python必须将函数调用中的每个实参都关联到函数定义中的一个形参.
# 位置实参的顺序很重要.
def describe_pet(animal_type: str, pet_name: str):
    """显示宠物的信息.
    :param animal_type:
    :param pet_name:
    :return:
    """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("hamster", "harry")
describe_pet("dog", "willie")

# 关键字实参
# 关键词实参是传递给函数的键-值对.
# 关键词实参让你无需考虑函数调用中的实参顺序,还清楚地指出了函数调用中各个值的用途.
# 关键字实参的顺序无关紧要.
describe_pet(animal_type="hamster", pet_name="harry")


# 默认值,默认值指的是函数定义的时候使用的技巧,而位置参数和关键字参数是函数调用时使用的技巧.
# 编写函数时,可以给每个形参指定默认值.
# 在调用函数中给形参提供了实参时,Python将使用指定的实参值,否则,将使用形参的默认值.
# 使用默认值,在形参列表中必须先列出没有默认值的形参,再列出有默认值的实参.
def describe_pet(pet_name, animal_type="dog"):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name="while")


# 可变参数
# 需要接受任意数量的实参,但事先不知道传递给函数的会是什么样的信息时,这种情况下,可以将函数编写成能够接受任意数量的键值对.
# 形参中的两个星号让Python创建一个名为user_info的空字典.并将收到的所有名称-值对都封装到这个字典中.
def build_profile(first: str, last: str, **user_info: Any):
    """传入可变参数,并且传入的是字典的格式.
    :param first:
    :param last:
    :param user_info:
    :return:
    """
    logger.info(type(user_info))
    profile = {"first_name": first, "last_name": last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)
logger.info(get_type_hints(build_profile))


def build_profile(first: str, last: str, *user_info: Any):
    """传入可变参数,并且出入的是元祖的格式.
    :param first:
    :param last:
    :param user_info:
    :return:
    """
    logger.info(type(user_info))
    profile = {"first_name": first, "last_name": last, "other_info": []}
    for key in user_info:
        profile["other_info"].append(key)
    return profile


user_profile = build_profile("albert", "einstein", "princeton", "physics")
print(user_profile)

# 各种参数之间的组合
# 顺序: 位置参数, 默认参数, 可变参数, 命名关键字参数, 关键字参数.
