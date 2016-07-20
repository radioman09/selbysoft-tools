import time
import os
import SendKeys
from pywinauto.application import Application

os.system('title add_spec')
os.system('color B')

app = Application().connect(title_re = "SP-1 by SelbySoft, Inc.", class_name = "#32770")


##app2 = Application().Connect(title='add_spec',
##                             class_name='ConsoleWindowClass')
##consolewindow = app2.add_spec


window = App.Dialog


time.sleep(1.4)

def main():

    try:
        time.sleep(.2)

        #consolewindow.SetFocus()
        window.TypeKeys(spec_name, with_spaces = True)
        time.sleep(.3)

        window.TypeKeys('{ENTER}')

        window.TypeKeys(menu_group, with_spaces = True)
        for i in range(0,7):
            window.TypeKeys('{ENTER}')
        time.sleep(.4)
        window.TypeKeys('{ENTER}')

        time.sleep(.3)
        
        window.TypeKeys('{ENTER}')
        window.TypeKeys(base_adder)
        SendKeys.SendKeys("%+{s}")
        window.TypeKeys('{ENTER}')
        time.sleep(.6)
        #consolewindow.SetFocus()
    except:
        exit()
    


while True:    
    main()


















