import time
import os
import SendKeys
from pywinauto.application import Application

os.system('title add_spec')
os.system('color B')

app = Application().connect(title_re = "SP-1 by SelbySoft, Inc.", class_name = "#32770")


app2 = Application().Connect(title='add_spec', class_name='ConsoleWindowClass')
consolewindow = app2.add_spec



window = app.Dialog
##window.Wait('ready')
##window.SetFocus()
##window.Click()
##window.TypeKeys('9999')
##window.TypeKeys('{ENTER}')
##window.TypeKeys('m')
##window.TypeKeys('s')

time.sleep(1.4)

def main():

    try:
        window.TypeKeys('a')
        time.sleep(.2)

        consolewindow.SetFocus()

        spec_name = raw_input("spec name: ")
        spec_name = spec_name[:20]
        time.sleep(.3)
        window.TypeKeys(spec_name, with_spaces = True)
        time.sleep(.3)

        window.TypeKeys('{ENTER}')

        menu_group = "PIZZA" #change menu group to what is needed
        window.TypeKeys(menu_group, with_spaces = True)
        for i in range(0,7):
            window.TypeKeys('{ENTER}')
        time.sleep(.4)
        window.TypeKeys('{ENTER}')

        time.sleep(.3)
        
        window.TypeKeys('pizza', with_spaces = True ) ##group size
        window.TypeKeys('{ENTER}')
        base_adder = raw_input("Price: ")
        window.TypeKeys('$')
        window.TypeKeys(base_adder)
        SendKeys.SendKeys("%+{s}")
        window.TypeKeys('{ENTER}')
        time.sleep(.6)
        consolewindow.SetFocus()
    except:
        exit()
    


while True:    
    main()


















