#!/usr/bin/python3.5

def validate_pin(pin):
    if pin.isdecimal():
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    print(validate_pin('1234'))
    print(validate_pin('123445'))
    print(validate_pin('12344e'))