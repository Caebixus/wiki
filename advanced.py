# class Animal:
#     property = "something"
#     property_list = ['Ruby', 'Safi', 'Beamy']
#     property_dict = {
#         'key_1': 'Value'
#     }
#
#     def this_is_a_method(self):
#         print(self.property_dict)
#
#     @property
#     def get_ruby(self):
#         return self.property_list[0]
#
# the_animal = Animal()
# print(the_animal.property_dict.get('key_1'))


# to instantiate class -> animal = Animal()
# print(the_animal.property)

# private property of class -> its when property should be used only in class itself and not outside
# it starts with _ -> _private_property = "private string"

# Method
# Method is just a function inside class
# first parameter is usually (self)
# to activate method of a class -> the_animal.this_is_a_method()

# decorator -> @property
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.
# pokud je tam decorator @property tak nemusíme používat () jelikož je to property té class
# decorator is a function wrapper so that we can execute  action before or after original function
# how to construct decorator:
# def my_decorator(func):
#   def wrapper():
#       print("do something") # before original func
#       func()
#       print("original function end here") # after original func
#   return wrapper
#
# @my_decorator
# def myfunc():
#     print("My name is Kalob")
#
# myfunc()


# generator (for data science)
# generator is memory efficiant and do math only when demanded
# function which work one number at the time from a list (huge list usually)
# yield word is making generator generator
# how to construct generator:
def my_generator():
  for num in range(50):
      yield num ** num

for big_num in my_generator():
    print(big_num)