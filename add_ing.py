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

        ing_name = raw_input("spec name: ")
        ing_name = ing_name[:20]
       
        window.TypeKeys(ing_name, with_spaces = True)
      

        window.TypeKeys('{ENTER}')

        menu_group = "BAR" #change menu group to what is needed
        window.TypeKeys(menu_group, with_spaces = True)
        for i in range(0,11):
            window.TypeKeys('{ENTER}')

     
        
        window.TypeKeys('sparkling wine', with_spaces = True ) ##group size
        window.TypeKeys('{ENTER}')
        window.TypeKeys('{ENTER}')
        window.TypeKeys('$')
        consolewindow.SetFocus()
        window.TypeKeys(raw_input("enter $ amount: "))
        SendKeys.SendKeys("%+{s}")
        window.TypeKeys('{ENTER}')
        time.sleep(.6)
        consolewindow.SetFocus()
    except:
        exit()
    


while True:    
    main()


















