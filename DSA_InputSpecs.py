import tkinter as tk
import random as ran

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Sets up input frame for notebook tab 2.
# - This can be anything for each TreeView item.
#   Ex: Radio Buttons, Buttons, Entry boxes, Check boxes, etc..
#
# Input_Def - (Widget, Selected TreeView item, LAZY: list_button3 (Apply button))
#           - SETS GLOBAL VARIABLE given_input with integer list!
#           - Display.py USES THIS GLOBAL VARIABLE (because I'm too stupid to pass it correctly)
#           - passed apply button to be able to change it's active color when a widget is updated   :LAZY
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#    TODO: Majority of DSA
#
#     WIP: - List inputs
#    
#    Done: - None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def Input_Def(master, x, list_button3):
    global given_input
    given_input = []
    match x:
        case 0:

            list_label = tk.Label(master, text = "List Input: ")
            list_label.place(anchor = 'nw', x = -10, y = -10)

            list_label2 = tk.Label(master, text = "Please type in a list of numbers seperated by a comma and press enter:", wraplength = 300, justify = 'left')
            list_label2.place(anchor = 'nw', x = -10, y = 10)

            list_Button = tk.Button(master, text = 'add random integer', command = lambda: list_add_rand(list_button3))
            list_Button.place(anchor = 'nw', x = 315, y = 0)

            list_Button = tk.Button(master, text = 'remove end', command = lambda: list_remove_end(list_button3))
            list_Button.place(anchor = 'nw', x = 315, y = 26)

            # Tlc function to pass function correctly for wrapper
            vcmd = master.register(entry_checker)

            # Validate 'key' checks the entered values after each key press
            global list_box
            list_box = tk.Entry(master, bd = 3, width = 40, validate = 'key', validatecommand = (vcmd, "%P"))
            list_box.place(anchor = 'nw', x = 0, y = 50)
            list_box.insert(0, '0,1,2,3,4')

            list_box.bind("<Return>", lambda e: val_ent(e, list_button3))

        case 1:
            pass
    
    return None

# =================================================================================================


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Checks if curr_val entered into entry box is a number or a backspace
#           - returns True if the value is a digit or is a backspace
#           - else returns false and denies key-press
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def entry_checker(curr_val):
    checker_val = curr_val.replace(',', '')
    if curr_val == 'justify':
        return True
    if curr_val == '':
        return True
    if curr_val == ',':
        return True
    if checker_val.isdigit():
        return True
    return False
# =================================================================================================


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Val_ent gets current Notebook tab 2 input values
#           - event triggered
#           - Currently Adds integers to list
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def val_ent(e, list_button3):
    global given_input
    list_button3.config(bg = 'pink', activebackground = 'pink')
    val = ''
    if list_box.get() != '':
        val = list_box.get()

    given_input = val.split(',')
    for x in reversed(given_input):
        if x == '':
            given_input.remove(x)
    

    given_input = [int(x) for x in given_input]

    list_box.delete(0, tk.END)

    return None

# =================================================================================================



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Removes end of given input int list
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def list_remove_end(list_button3):
    list_button3.config(bg = 'pink', activebackground = 'pink')
    if len(given_input) != 0:
        given_input.pop()
# =================================================================================================

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - adds to the end of given input int list a random number 0 - 100
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def list_add_rand(list_button3):
    list_button3.config(bg = 'pink', activebackground = 'pink')
    x = str(ran.randint(0,100))
    given_input.append(x) # type: ignore

# =================================================================================================

# Sample radio buttons for notebook tab 2
'''
radBut0 = tk.Radiobutton(master, text = ' None ', variable = l, value = 0, command = lambda: clicked(l.get()))
radBut0.place(anchor = 'nw', x = -10, y = 10)
radBut1 = tk.Radiobutton(master, text = 'apple', variable = l, value = 1, command = lambda: clicked(l.get()))
radBut1.place(anchor = 'nw', x = -10, y = 30)
radBut2 = tk.Radiobutton(master, text = 'pear', variable = l, value = 2, command = lambda: clicked(l.get()))
radBut2.place(anchor = 'nw', x = -10, y = 50)
'''