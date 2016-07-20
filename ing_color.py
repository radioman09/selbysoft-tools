import time
import os
import SendKeys
from pywinauto.application import Application

os.system('title add_spec')
os.system('color B')

app = Application().connect(title_re = "SP-1 by SelbySoft, Inc.", class_name = "#32770")





window = app.Dialog


time.sleep(1.4)


for i in range(0,6):

    window.TypeKeys('e')
    time.sleep(.2)

    for i in range(0,5):
        window.TypeKeys('{ENTER}')

    window.TypeKeys('9')
    SendKeys.SendKeys("%+{s}")
    window.TypeKeys('y')
    window.TypeKeys('n')


















