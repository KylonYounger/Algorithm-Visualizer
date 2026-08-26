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
    global input_obj

    # Tlc function to pass function correctly for wrapper
    vcmd = master.register(entry_checker)

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

            list_Button = tk.Button(master, text = 'add random integer', command = lambda: add_rand(input_obj, list_button3))
            list_Button.place(anchor = 'nw', x = 315, y = 0)

            list_Button = tk.Button(master, text = 'remove end', command = lambda: remove_end(input_obj, list_button3))
            list_Button.place(anchor = 'nw', x = 315, y = 26)

            list_change = tk.Label(master, bd = 1, text = "Change the list value at the specific index: \n(0 is the starting number)", relief = 'solid')
            list_change.place(anchor = 'nw', x = 0, y = 73)

            list_bullet = tk.Label(master, bd = 1, text = "Lists Can have:\n - Any data types \n - Is ordered \n - Changeable data \n - Allowed Duplicates", relief = 'solid')
            list_bullet.place(anchor = 'nw', x = 315, y = 75)


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

            list_box.bind("<Return>", lambda e: val_ent(e, input_obj, list_button3, list_box.get()))
            list_box_index.bind("<Return>", lambda e: change_index(index_entry = list_box_index, val_entry = list_box_val, list_button3 = list_button3, input_obj = input_obj))
            list_box_val.bind("<Return>", lambda e: change_index(index_entry = list_box_index, val_entry = list_box_val, list_button3 = list_button3, input_obj = input_obj))

        case 1:
            # store data values in key:value pairs
            # Ordered
            # Changeable
            # NO duplicates
            input_obj = {}

            # LABELS
            dic_label_1 = tk.Label(master, text = 'Dictionary Input: ')
            dic_label_1.place(anchor= 'nw', x = -10, y = -10)

            global dic_entry1_label
            dic_entry1_label = tk.Label(master, justify = 'left', text = ' Please type in a dictionary of data seperated by a ":" and press enter: ', bd = 1, relief = 'solid')
            dic_entry1_label.place(anchor= 'nw', x = -4, y = 15)

            dic_entry2_label = tk.Label(master,justify = 'left', text = 'To change dictionary {Key:Value} pairs \nEnter key here: ')
            dic_entry2_label.place(anchor= 'nw', x = -7, y = 67)

            dic_entry2_label = tk.Label(master, text = 'Enter value here: ')
            dic_entry2_label.place(anchor= 'nw', x = -7, y = 124)

            dic_bullet = tk.Label(master, bd = 1, text = "Dictionaries have:\n - Key:Value Pairs \n - Is ordered \n - Changeable data \n - No Duplicates", relief = 'solid')
            dic_bullet.place(anchor = 'nw', x = 320, y = 85)
            
            #ENTRY BOXES
            global dic_entry_box
            dic_entry_box = tk.Entry(master, bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            dic_entry_box.place(anchor= 'nw', x = -3, y = 42)
            dic_entry_box.insert(0, "1:2,Apple:4")

            global dic_index_box
            dic_index_box = tk.Entry(master, bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            dic_index_box.place(anchor= 'nw', x = -3, y = 102)

            global dic_val_box
            dic_val_box = tk.Entry(master, bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            dic_val_box.place(anchor= 'nw', x = -3, y = 144)

            dic_entry_box.bind("<Return>", lambda e: val_ent(e, input_obj, list_button3, dic_entry_box.get()))
            dic_index_box.bind("<Return>", lambda e: change_index(dic_index_box, dic_val_box, input_obj, list_button3))
            dic_val_box.bind("<Return>", lambda e: change_index(dic_index_box, dic_val_box, input_obj, list_button3))

            # BUTTONS

            dic_button_1 = tk.Button(master, text = "Add random key", command = lambda: add_rand(input_obj, list_button3))
            dic_button_1.place(anchor= 'nw', x = 210, y = 100)

            dic_button_2 = tk.Button(master, text = "Remove last key", command = lambda: remove_end(input_obj, list_button3))
            dic_button_2.place(anchor= 'nw', x = 210, y = 127)

        

    
    return None

# =================================================================================================



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Checks if curr_val entered into entry box is a number or a backspace
#           - returns True if the value is a digit or is a backspace
#           - else returns false and denies key-press
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def entry_checker(curr_val):
    checker_val = curr_val.replace(',', '')
    checker_val = checker_val.replace(':', '')
    if curr_val == 'justify':
        return True
    if curr_val == '':
        return True
    if curr_val == ',':
        return True
    if curr_val == ':':
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
def val_ent(e, input_obj, list_button3, val):
    list_button3.config(bg = 'pink', activebackground = 'pink')
    temp_list = val.split(',')

    if type(input_obj) == list:
        # Remove existing items
        input_obj.clear()

        # Append new items
        for x in range(0, len(temp_list)):
            input_obj.append(temp_list[x])

        # Check for any additional list spaces
        for x in reversed(input_obj):
            if x == ',':
                input_obj.remove(x)
            if x == '':
                input_obj.remove(x)
        list_box.delete(0, tk.END)

    if type(input_obj) == dict:
        if val.find(':') == -1:
            dic_entry1_label.config(font = ("bold", 10), text = "BAD INPUT, PLEASE ENTER Key:Value \n EX: 1:2", foreground = 'red')
            dic_entry1_label.place(x = -3, y = 6)
            return
        else:
            dic_entry1_label.config(foreground = 'black', font = "TkDefaultFont", text = ' Please type in a dictionary of data seperated by a ":" and press enter: ')
            dic_entry1_label.place(anchor= 'nw', x = -4, y = 15)

        temp_list = val.split(',')
        # given input 1:2, 2:4, 8:2

        input_obj.clear()


        for x in range(0, len(temp_list)):
            temp_val = temp_list[x]
            temp_other = temp_val.split(':')
            input_obj.update({temp_other[0] : temp_other[1]})

        for x in reversed(input_obj):
            if x == ',':
                input_obj.pop(x)
            if x == '':
                input_obj.pop(x)
        dic_entry_box.delete(0, tk.END)

# =================================================================================================



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Removes end of given input int list
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def remove_end(input_obj, list_button3):
    list_button3.config(bg = 'pink', activebackground = 'pink')
    if len(input_obj) != 0 and type(input_obj) == list:
        input_obj.pop()
    if len(input_obj) != 0 and type(input_obj) == dict:
        input_obj.popitem()
# =================================================================================================

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - adds to the end of given input int list a random number 0 - 100
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def add_rand(input_obj, list_button3):
    list_button3.config(bg = 'pink', activebackground = 'pink')
    x = str(ran.randint(0,1000))
    if type(input_obj) == list:
        input_obj.append(x)
    if type(input_obj) == dict:
        input_obj.update({x: ran.randint(0,1000)})

# =================================================================================================

def change_index(index_entry, val_entry, input_obj, list_button3):
    list_button3.config(bg = 'pink', activebackground = 'pink')
    
    if type(input_obj) == list and int(index_entry.get()) <= len(input_obj):
        input_obj[int(index_entry.get())] = val_entry.get()

    else:
        # place label for bad index of change location!
        pass

    if type(input_obj) == dict:
        for x in input_obj.keys():
            if x == index_entry.get():
                input_obj[index_entry.get()] = val_entry.get()

    index_entry.delete(0, tk.END)
    val_entry.delete(0, tk.END)

def get_input_obj():
    if input_obj is not None:
        return input_obj
    return None
