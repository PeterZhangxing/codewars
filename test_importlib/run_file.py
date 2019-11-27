#!/usr/bin/python3.5


config_file = "for_import.For_test"

import importlib

file_path,class_name = config_file.split('.')
m = importlib.import_module(file_path)

if hasattr(m,class_name):
    cls = getattr(m,class_name)
    print(cls.print_copy_right())
    obj = cls("zhangxing",120,"Male")
    print(obj.print_info())