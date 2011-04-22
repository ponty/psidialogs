#"""
#"""
#
#from psidialogs.easygui_api import *
#import psidialogs
#
#def main(backend = ''):
#    if not backend:
#        backend = psidialogs.choice(psidialogs.all_backends(), 'Select backend!')
#    psidialogs.set_backend( force_backend=backend ) 
#    _test()
#    
#TkVersion=''
#EasyGuiRevisionInfo = ''
# 
#def _test():
#    """
#    copy from easygui.py
#    """    
#    # simple way to clear the console
#    print "\n" * 100
#    # START DEMONSTRATION DATA ===================================================
#    choices_abc = ["This is choice 1", "And this is choice 2"]
#    message = "Pick one! This is a huge choice, and you've got to make the right one " \
#        "or you will surely mess up the rest of your life, and the lives of your " \
#        "friends and neighbors!"
#    title = ""
#
#    # ============================= define a code snippet =========================
#    code_snippet = ("dafsdfa dasflkj pp[oadsij asdfp;ij asdfpjkop asdfpok asdfpok asdfpok"*3) +"\n"+\
#"""# here is some dummy Python code
#for someItem in myListOfStuff:
#    do something(someItem)
#    do something()
#    do something()
#    if somethingElse(someItem):
#        doSomethingEvenMoreInteresting()
#
#"""*16
#    #======================== end of code snippet ==============================
#
#    #================================= some text ===========================
#    text_snippet = ((\
#"""It was the best of times, and it was the worst of times.  The rich ate cake, and the poor had cake recommended to them, but wished only for enough cash to buy bread.  The time was ripe for revolution! """ \
#*5)+"\n\n")*10
#
#    #===========================end of text ================================
#
#    intro_message = ("Pick the kind of box that you wish to demo.\n\n"
#     + "In EasyGui, all GUI interactions are invoked by simple function calls.\n\n" +
#    "EasyGui is different from other GUIs in that it is NOT event-driven.  It allows" +
#    " you to program in a traditional linear fashion, and to put up dialogs for simple" +
#    " input and output when you need to. If you are new to the event-driven paradigm" +
#    " for GUIs, EasyGui will allow you to be productive with very basic tasks" +
#    " immediately. Later, if you wish to make the transition to an event-driven GUI" +
#    " paradigm, you can move to an event-driven style with a more powerful GUI package" +
#    "such as anygui, PythonCard, Tkinter, wxPython, etc."
#    + "\n\nEasyGui is running Tk version: " + str(TkVersion)
#    )
#
#    #========================================== END DEMONSTRATION DATA
#
#
#    while 1: # do forever
#        choices = [
#            "msgbox",
#            "buttonbox",
#            "choicebox",
#            "multchoicebox",
#            "textbox",
#            "ynbox",
#            "ccbox",
#            "enterbox",
#            "codebox",
#            "integerbox",
#            "boolbox",
#            "indexbox",
#            "filesavebox",
#            "fileopenbox",
#            "passwordbox",
#            "multenterbox",
#            "multpasswordbox",
#            "diropenbox"
#
#            ]
#        choice = choicebox(intro_message, "EasyGui " + EasyGuiRevisionInfo, choices)
#
#        if choice == None: return
#
#        reply = choice.split()
#
#        if   reply[0] == "msgbox":
#            reply = msgbox("short message", "This is a long title")
#            print "Reply was:", reply
#
#        elif reply[0] == "buttonbox":
#            reply = buttonbox()
#            print "Reply was:", reply
#
#            reply = buttonbox(message, "Demo of Buttonbox with many, many buttons!", choices)
#            print "Reply was:", reply
#
#        elif reply[0] == "boolbox":
#            reply = boolbox()
#            print "Reply was:", reply
#
#        elif reply[0] == "integerbox":
#            reply = integerbox(
#                "Enter a number between 3 and 333",
#                "Demo: integerbox WITH a default value",
#                222, 3, 333)
#            print "Reply was:", reply
#
#            reply = integerbox(
#                "Enter a number between 0 and 99",
#                "Demo: integerbox WITHOUT a default value"
#                )
#            print "Reply was:", reply
#
#        elif reply[0] == "diropenbox":
#            title = "Demo of diropenbox"
#            msg = "This is a test of the diropenbox.\n\nPick the directory that you wish to open."
#            d = diropenbox(msg, title)
#            print "You chose directory...:", d
#
#        elif reply[0] == "fileopenbox":
#            f = fileopenbox()
#            print "You chose to open file:", f
#
#        elif reply[0] == "filesavebox":
#            f = filesavebox()
#            print "You chose to save file:", f
#
#        elif reply[0] == "indexbox":
#            title = reply[0]
#            msg   =  "Demo of " + reply[0]
#            choices = ["Choice1", "Choice2", "Choice3", "Choice4"]
#            reply = indexbox(msg, title, choices)
#            print "Reply was:", reply
#
#        elif reply[0] == "passwordbox":
#            reply = passwordbox("Demo of password box WITHOUT default"
#                + "\n\nEnter your secret password", "Member Logon")
#            print "Reply was:", str(reply)
#
#            reply = passwordbox("Demo of password box WITH default"
#                + "\n\nEnter your secret password", "Member Logon", "alfie")
#            print "Reply was:", str(reply)
#
#        elif reply[0] == "enterbox":
#            reply = enterbox("Enter the name of your best friend:", "Love!", "Suzy Smith")
#            print "Reply was:", str(reply)
#
#            reply = enterbox("Enter the name of your worst enemy:", "Hate!")
#            print "Reply was:", str(reply)
#
#        elif reply[0] == "multenterbox":
#            msg = "Enter your personal information"
#            title = "Credit Card Application"
#            fieldNames = ["Name","Street Address","City","State","ZipCode"]
#            fieldValues = []  # we start with blanks for the values
#            fieldValues = multenterbox(msg,title, fieldNames)
#
#            # make sure that none of the fields was left blank
#            while 1:
#                if fieldValues == None: break
#                errmsg = ""
#                for i in range(len(fieldNames)):
#                    if fieldValues[i].strip() == "":
#                        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
#                if errmsg == "": break # no problems found
#                fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
#
#            print "Reply was:", fieldValues
#
#        elif reply[0] == "multpasswordbox":
#            msg = "Enter logon information"
#            title = "Demo of multpasswordbox"
#            fieldNames = ["Server ID", "User ID", "Password"]
#            fieldValues = []  # we start with blanks for the values
#            fieldValues = multpasswordbox(msg,title, fieldNames)
#
#            # make sure that none of the fields was left blank
#            while 1:
#                if fieldValues == None: break
#                errmsg = ""
#                for i in range(len(fieldNames)):
#                    if fieldValues[i].strip() == "":
#                        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
#                if errmsg == "": break # no problems found
#                fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
#
#            print "Reply was:", fieldValues
#
#
#        elif reply[0] == "ynbox":
#            reply = ynbox(message, title)
#            print "Reply was:", reply
#
#        elif reply[0] == "ccbox":
#            reply = ccbox(message)
#            print "Reply was:", reply
#
#        elif reply[0] == "choicebox":
#            longchoice = "This is an example of a very long option which you may or may not wish to choose."*2
#            listChoices = ["nnn", "ddd", "eee", "fff", "aaa", longchoice
#                    , "aaa", "bbb", "ccc", "ggg", "hhh", "iii", "jjj", "kkk", "LLL", "mmm" , "nnn", "ooo", "ppp", "qqq", "rrr", "sss", "ttt", "uuu", "vvv"]
#
#            message = "Pick something. " + ("A wrapable sentence of text ?! "*30) + "\nA separate line of text."*6
#            reply = choicebox(message, None, listChoices)
#            print "Reply was:", reply
#
#            message = "Pick something. "
#            reply = choicebox(message, None, listChoices)
#            print "Reply was:", reply
#
#            message = "Pick something. "
#            reply = choicebox("The list of choices is empty!", None, [])
#            print "Reply was:", reply
#
#        elif reply[0] == "multchoicebox":
#            listChoices = ["aaa", "bbb", "ccc", "ggg", "hhh", "iii", "jjj", "kkk"
#                , "LLL", "mmm" , "nnn", "ooo", "ppp", "qqq"
#                , "rrr", "sss", "ttt", "uuu", "vvv"]
#
#            message = "Pick as many choices as you wish."
#            reply = multchoicebox(message,"DEMO OF multchoicebox", listChoices)
#            print "Reply was:", reply
#
#        elif reply[0] == "textbox":
#            message = "Here is some sample text. " * 16
#            reply = textbox(message, "Text Sample", text_snippet)
#            print "Reply was:", reply
#
#        elif reply[0] == "codebox":
#            message = "Here is some sample code. " * 16
#            reply = codebox(message, "Code Sample", code_snippet)
#            print "Reply was:", reply
#
#        else:
#            msgbox("Choice\n\n" + choice + "\n\nis not recognized", "Program Logic Error")
#            return
#
#
###if __name__ == '__main__':
###    _test()
