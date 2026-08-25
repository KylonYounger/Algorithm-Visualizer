import tkinter as tk
import random as ran

global input_obj
input_obj = None

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
    global input_obj

    match x:
        case 0:
            # LIST FACTS: 
            # Can have multiple data types
            # can have duplicates
            # can change, add, remove after created
            # is ordered
            input_obj = []

            list_label = tk.Label(master, text = "List Input: ")
            list_label.place(anchor = 'nw', x = 0, y = -10)

            list_label2 = tk.Label(master, text = "Please type in a list of data seperated by a comma and press enter:", wraplength = 300, justify = 'left', relief = 'solid', bd = 1)
            list_label2.place(anchor = 'nw', x = 0, y = 9)

            list_Button = tk.Button(master, text = 'add random integer', command = lambda: list_add_rand(input_obj, list_button3))
            list_Button.place(anchor = 'nw', x = 315, y = 0)

            list_Button = tk.Button(master, text = 'remove end', command = lambda: list_remove_end(input_obj, list_button3))
            list_Button.place(anchor = 'nw', x = 315, y = 26)

            list_change = tk.Label(master, bd = 1, text = "Change the list value at the specific index: \n(0 is the starting number)", relief = 'solid')
            list_change.place(anchor = 'nw', x = 0, y = 73)

            list_bullet = tk.Label(master, bd = 1, text = "Lists Can have:\n - Any data types \n - Is ordered \n - Changeable data \n - Allowed Duplicates", relief = 'solid')
            list_bullet.place(anchor = 'nw', x = 315, y = 75)



            # Tlc function to pass function correctly for wrapper
            vcmd = master.register(entry_checker)

            # Validate 'key' checks the entered values after each key press
            global list_box
            list_box = tk.Entry(master, bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            list_box.place(anchor = 'nw', x = 0, y = 45)
            list_box.insert(0, '0,1,2,3,4')

            global list_box_index
            global list_box_val

            list_box2_Label = tk.Label(master, bd = 3, text = ":Enter a list index")
            list_box2_Label.place(anchor = 'nw', x = 38, y = 108)

            list_box3_Label = tk.Label(master, bd = 3, text = " :Enter a value to change that index")
            list_box3_Label.place(anchor = 'nw', x = 65, y = 128)

            list_box_index = tk.Entry(master, bd = 3, width = 5, validate = 'key', validatecommand = (vcmd, "%P"))
            list_box_index.place(anchor = 'nw', x = 0, y = 110)

            list_box_val = tk.Entry(master, bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            list_box_val.place(anchor = 'nw', x = 0, y = 130)

            list_box.bind("<Return>", lambda e: val_ent(e, input_obj, list_button3))
            list_box_index.bind("<Return>", lambda e: list_change_index(int(list_box_index.get()),list_box_val.get(), list_button3, input_obj))
            list_box_val.bind("<Return>", lambda e: list_change_index(int(list_box_val.get()), list_box_val.get(), list_button3, input_obj))

        case 1:
            # store data values in key:value pairs
            # Ordered
            # Changeable
            # NO duplicates

            dic_label_1 = tk.Label(master, text = 'Dictionary Input: ')
            dic_label_1.place(anchor= 'nw', x = -10, y = -10)

            dic_bullet = tk.Label(master, bd = 1, text = "Dictionaries have:\n - Key:Value Pairs \n - Is ordered \n - Changeable data \n - No Duplicates", relief = 'solid')
            dic_bullet.place(anchor = 'nw', x = 320, y = 85)



    
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
    if checker_val.isalnum():
        return True
    return False
# =================================================================================================


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Val_ent gets current Notebook tab 2 input values
#           - event triggered
#           - Currently Adds integers to list
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def val_ent(e, input_obj, list_button3):
    list_button3.config(bg = 'pink', activebackground = 'pink')
    val = ''
    if list_box.get() != '':
        val = list_box.get()

    input_obj = val.split(',')
    for x in reversed(input_obj):
        if x == '':
            input_obj.remove(x)

    list_box.delete(0, tk.END)

# =================================================================================================



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Removes end of given input int list
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def list_remove_end(input_obj, list_button3):
    list_button3.config(bg = 'pink', activebackground = 'pink')
    if len(input_obj) != 0:
        input_obj.pop()
# =================================================================================================

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - adds to the end of given input int list a random number 0 - 100
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def list_add_rand(input_obj, list_button3):
    list_button3.config(bg = 'pink', activebackground = 'pink')
    x = str(ran.randint(0,100))
    input_obj.append(x) # type: ignore

# =================================================================================================

def list_change_index(x, new_num, list_button3, input_obj):
    if x <= len(input_obj):
        list_button3.config(bg = 'pink', activebackground = 'pink')
        input_obj[x] = new_num
        list_box_index.delete(0, tk.END)
        list_box_val.delete(0, tk.END)
    else:
        # place label for bad index of change location!
        pass


def get_input_obj():
    if input_obj is not None:
        return input_obj
    return None