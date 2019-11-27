import random
import easygui

mynum = random.randint(1,10)
total_count = 7

count = 1
while True:
    if count >= 7:
        exit('you have used all your opportunities!')

    gnum = easygui.enterbox(
        msg='enter a number between 1 and 9:'
    )

    if not gnum:
        easygui.msgbox('you must input a number like string')
        continue

    if not gnum.isdigit():
        easygui.msgbox('you must input a number like string')
        continue

    if int(gnum) == mynum:
        easygui.msgbox(
            msg='congratulations you have find the right number %s,%s tries left.'%(mynum,total_count-count))
        break
    elif int(gnum) > mynum:
        easygui.msgbox(
            msg='%s is bigger than the right number,%s tries left.' % (gnum,total_count-count))
    else:
        easygui.msgbox(
            msg='%s is smaller than the right number,%s tries left.' % (gnum,total_count-count))

    count += 1