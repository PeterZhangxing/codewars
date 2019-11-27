#!/usr/bin/python3.5

class For_test(object):

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        info_dic = {"name":self.name,"age":self.age,"gender":self.gender}
        my_info = "my name is {name},and i am {age} years old,i am a {gender}".format(**info_dic)
        return my_info

    @staticmethod
    def print_copy_right():
        import datetime
        return datetime.date.today()