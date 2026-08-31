import tkinter as tk
import random as ran

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Sets up input frame for notebook tab 2.
# - This can be anything for each TreeView item.
#   Ex: Radio Buttons, Buttons, Entry boxes, Check boxes, etc..
#
# Input_Def - (Widget, Selected TreeView item, LAZY: apply_button (Apply button))
#           - SETS GLOBAL VARIABLE given_input with integer list!
#           - passed apply button to be able to change it's active color when a widget is updated   :LAZY
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#    TODO: Majority of DSA
#
#     WIP: - List inputs
#    
#    Done: - None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def Input_Def(master, x, apply_button):
    global input_obj

    general_label = tk.Label(master)
    general_label.place(anchor= 'nw', x = -10, y = -10)

    general_bullet = tk.Label(master, bd = 1, relief = 'solid')
    

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

            # LABELS
            general_label.config(text = "List Input: ")

            list_label2 = tk.Label(master, text = "Please type in a list of data seperated by a comma and press enter:", wraplength = 300, justify = 'left', relief = 'solid', bd = 1)
            list_label2.place(anchor = 'nw', x = 0, y = 9)
            
            list_box2_Label = tk.Label(master, bd = 3, text = ":Enter a list index")
            list_box2_Label.place(anchor = 'nw', x = 38, y = 108)

            list_box3_Label = tk.Label(master, bd = 3, text = " :Enter a value to change that index")
            list_box3_Label.place(anchor = 'nw', x = 65, y = 128)

            list_change = tk.Label(master, bd = 1, text = "Change the list value at the specific index: \n(0 is the starting number)", relief = 'solid')
            list_change.place(anchor = 'nw', x = 0, y = 73)

            general_bullet.config(text = "Lists Can have:\n - Any data types \n - Is ordered \n - Changeable data \n - Allowed Duplicates")
            general_bullet.place(anchor = 'nw', x = 315, y = 87)
            # ENTRY
            
            # Validate 'key' checks the entered values after each key press
            global list_box
            list_box = tk.Entry(master, bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            list_box.place(anchor = 'nw', x = 0, y = 45)
            list_box.insert(0, '0,1,2,3,4')
            
            global list_box_index
            list_box_index = tk.Entry(master, bd = 3, width = 5, validate = 'key', validatecommand = (vcmd, "%P"))
            list_box_index.place(anchor = 'nw', x = 0, y = 110)
            
            global list_box_val
            list_box_val = tk.Entry(master, bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            list_box_val.place(anchor = 'nw', x = 0, y = 130)

            list_box.bind("<Return>", lambda e: val_ent(e, apply_button, list_box.get()))
            list_box_index.bind("<Return>", lambda e: change_index(index_entry = list_box_index, val_entry = list_box_val, apply_button = apply_button, input_obj = input_obj))
            list_box_val.bind("<Return>", lambda e: change_index(index_entry = list_box_index, val_entry = list_box_val, apply_button = apply_button, input_obj = input_obj))

            # BOXES
            list_Button = tk.Button(master, text = 'add random integer', command = lambda: add_rand(input_obj, apply_button))
            list_Button.place(anchor = 'nw', x = 315, y = 0)

            list_Button = tk.Button(master, text = 'remove end', command = lambda: remove_end(input_obj, apply_button))
            list_Button.place(anchor = 'nw', x = 315, y = 26)

        case 1:
            # store data values in key:value pairs
            # Ordered
            # Changeable
            # NO duplicates
            input_obj = {}

            # LABELS
            general_label.config(text = 'Dictionary Input: ')

            global dic_entry1_label
            dic_entry1_label = tk.Label(master, justify = 'left', text = ' Please type in a dictionary of data seperated by a ":" and press enter: ', bd = 1, relief = 'solid')
            dic_entry1_label.place(anchor= 'nw', x = -4, y = 15)

            dic_entry2_label = tk.Label(master,justify = 'left', text = '\nAdd/Change key: ')
            dic_entry2_label.place(anchor= 'nw', x = -7, y = 67)

            dic_entry2_label = tk.Label(master, text = 'Add/Change value: ')
            dic_entry2_label.place(anchor= 'nw', x = -7, y = 124)

            general_bullet.config(text = "Dictionaries have:\n - Key:Value Pairs \n - Is ordered \n - Changeable data \n - No Duplicates")
            general_bullet.place(anchor = 'nw', x = 320, y = 85)

            # ENTRY BOXES
            global dic_entry_box
            dic_entry_box = tk.Entry(master, bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            dic_entry_box.place(anchor = 'nw', x = -3, y = 42)
            dic_entry_box.insert(0, "1:2,Apple:4")

            global dic_index_box
            dic_index_box = tk.Entry(master, bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            dic_index_box.place(anchor = 'nw', x = -3, y = 102)

            global dic_val_box
            dic_val_box = tk.Entry(master, bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            dic_val_box.place(anchor = 'nw', x = -3, y = 144)

            dic_entry_box.bind("<Return>", lambda e: val_ent(e, apply_button, dic_entry_box.get()))
            dic_index_box.bind("<Return>", lambda e: change_index(dic_index_box, dic_val_box, input_obj, apply_button))
            dic_val_box.bind("<Return>", lambda e: change_index(dic_index_box, dic_val_box, input_obj, apply_button))

            # BUTTONS
            dic_button_1 = tk.Button(master, text = "Add random key", command = lambda: add_rand(input_obj, apply_button))
            dic_button_1.place(anchor= 'nw', x = 210, y = 100)

            dic_button_2 = tk.Button(master, text = "Remove last key", command = lambda: remove_end(input_obj, apply_button))
            dic_button_2.place(anchor = 'nw', x = 210, y = 127)

        case 2:
            # Tuple Facts:
            #   Ordered, unchangeable, allowed duplicates
            input_obj = ()

            # LABELS
            general_label.config(text = 'Tuple Input: ')
            
            general_bullet.config(text = "Tuples:\n - Are ordered \n - Unchangeable data \n - Allow duplicates")
            general_bullet.place(anchor = 'nw', x = 310, y = 100)

            tuple_label_2 = tk.Label(master, wraplength = 400, justify = 'left', text = ' Please type in a tuple of data seperated by a "," to create a new tuple and press enter: ', bd = 1, relief = 'solid')
            tuple_label_2.place(anchor = 'nw', x = -3, y = 10)

            tuple_label_3 = tk.Label(master, text = 'Join a new tuple to the existing one: ')
            tuple_label_3.place(anchor = 'nw', x = -5, y = 69)

            tuple_label_3 = tk.Label(master, justify = 'left', text = 'Enter a size of random values to be created\n into a new tuple: ')
            tuple_label_3.place(anchor = 'nw', x = -7, y = 110)

            

            # ENTRY
            global tuple_entry_box
            tuple_entry_box = tk.Entry(master, bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            tuple_entry_box.place(anchor = 'nw', x = -3, y = 48)
            tuple_entry_box.insert(0, "1,2,True,4,apple,apple")

            tuple_entry_box.bind("<Return>", lambda e: val_ent(e, apply_button, tuple_entry_box.get()))

            global tuple_entry_box2
            tuple_entry_box2 = tk.Entry(master, bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            tuple_entry_box2.place(anchor = 'nw', x = -3, y = 88)

            tuple_entry_box2.bind("<Return>", lambda e: join_tuple(e, apply_button, tuple_entry_box2.get()))

            global tuple_entry_box3
            tuple_entry_box3 = tk.Entry(master, bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            tuple_entry_box3.place(anchor = 'nw', x = -3, y = 145)

            tuple_entry_box3.bind("<Return>", lambda e: rand_tuple_size(e, apply_button, tuple_entry_box3.get()))

        case 3:

            input_obj = set()
            # LABELS
            general_label.config(text = 'Set Input: ')
            
            general_bullet.config(text = "Sets:\n - Are unordered \n - Unchangeable \n - No duplicates")
            general_bullet.place(anchor = 'nw', x = 337, y = 100)

            set_input_label = tk.Label(master, wraplength = 400, justify = 'left', text = ' Please type in a set of data seperated by a "," and press enter: ', bd = 1, relief = 'solid')
            set_input_label.place(anchor = 'nw', x = -3, y = 20)
            # ENTRY
            global set_entry_box
            set_entry_box = tk.Entry(master, bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            set_entry_box.place(anchor = 'nw', x = -3, y = 48)
            set_entry_box.insert(0, "1,2,True,4")
            
            set_entry_box.bind("<Return>", lambda e: val_ent(e, apply_button, set_entry_box.get()))

            # BOXES
            set_add_button = tk.Button(master, text = "Add random item", command = lambda: add_rand(input_obj, apply_button))
            set_add_button.place(anchor= 'nw', x = 210, y = 100)

            set_remove_end = tk.Button(master, text = "Remove random item", command = lambda: remove_end(input_obj, apply_button))
            set_remove_end.place(anchor = 'nw', x = 210, y = 127)

        case 4:
            input_obj = frozenset()
            # LABELS
            general_label.config(text = 'frozen set Input: ')
            
            general_bullet.config(text = "Frozen sets:\n - Are unordered \n - Unchangeable \n - No duplicates \n - Immutable")
            general_bullet.place(anchor = 'nw', x = 338, y = 87)

            fset_input_label = tk.Label(master, wraplength = 400, justify = 'left', text = ' Please type in a set of data seperated by a "," and press enter to create a new frozen set: ', bd = 1, relief = 'solid')
            fset_input_label.place(anchor = 'nw', x = -3, y = 15)
            # ENTRY
            global fset_entry_box
            fset_entry_box = tk.Entry(master, bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            fset_entry_box.place(anchor = 'nw', x = -3, y = 55)
            fset_entry_box.insert(0, "1,2,True,4")
            
            fset_entry_box.bind("<Return>", lambda e: val_ent(e, apply_button, fset_entry_box.get()))
            
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
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def val_ent(e, apply_button, val):
    global input_obj
    # Changes apply button to pink
    apply_button.config(bg = 'pink', activebackground = 'pink')
    temp_list = val.split(',')

    if type(input_obj) == list:
        # Remove existing items
        input_obj.clear()

        # Append new items
        for x in range(0, len(temp_list)):
            input_obj.append(temp_list[x])

        # Check for any additional list unwanteds
        for x in reversed(input_obj):
            if x == ',':
                input_obj.remove(x)
            if x == '':
                input_obj.remove(x)
        list_box.delete(0, tk.END)
        
    # Error checking for bad input, currently works for none ":" in the entry box
    # configs the label text and position to GUI the user
    if type(input_obj) == dict:
        if val.find(':') == -1:
            dic_entry1_label.config(font = ("bold", 10), text = "BAD INPUT, PLEASE ENTER Key:Value \n EX: 1:2", foreground = 'red')
            dic_entry1_label.place(x = -3, y = 6)
            return
        else:
            dic_entry1_label.config(foreground = 'black', font = "TkDefaultFont", text = ' Please type in a dictionary of data seperated by a ":" and press enter: ')
            dic_entry1_label.place(anchor= 'nw', x = -4, y = 15)

        # removes previous data
        input_obj.clear()
        temp_list = val.split(',')
        # Adds list objects after removing ',' and ':'
        for x in range(0, len(temp_list)):
            temp_val = temp_list[x]
            temp_other = temp_val.split(':')
            input_obj.update({temp_other[0] : temp_other[1]})

        # Checks that the data is not a space or commma
        for x in reversed(input_obj):
            if x == ',':
                input_obj.pop(x)
            if x == '':
                input_obj.pop(x)
        dic_entry_box.delete(0, tk.END)


    if type(input_obj) == tuple:
        # Remove existing items
        input_obj = () # sets global input_obj with nothing
        temp_list = val.split(',')

        # Check for any additional list unwanteds
        for x in reversed(temp_list):
            if x == ',':
                temp_list.remove(x)
            if x == '':
                temp_list.remove(x)

        input_obj = tuple(temp_list)
        
        tuple_entry_box.delete(0, tk.END)


    if type(input_obj) == set:
        # Unordered, unchangeable, unidexed, multiple data types
        input_obj.clear()

        for x in reversed(temp_list):
            if x == ',':
                temp_list.remove(x)
            if x == '':
                temp_list.remove(x)
                
        for x in temp_list:
            input_obj.add(x)
        
        set_entry_box.delete(0, tk.END)

    if type(input_obj) == frozenset:
        input_obj = frozenset()
        temp_list = val.split(',')
        
        # Check for any additional list unwanteds
        for x in reversed(temp_list):
            if x == ',':
                temp_list.remove(x)
            if x == '':
                temp_list.remove(x)

        input_obj = frozenset(temp_list)
        
        fset_entry_box.delete(0, tk.END)
# =================================================================================================



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Removes end of given input object
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def remove_end(input_obj, apply_button):
    # Changes apply button to pink
    apply_button.config(bg = 'pink', activebackground = 'pink')
    # Checks if non-empty and is correct type, then removes item
    if len(input_obj) == 0:
        return
    match input_obj:
        case list():
            input_obj.pop()
        case dict():
            # Removes last added key
            input_obj.popitem()
        case set():
            input_obj.pop()
# =================================================================================================


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - adds to the end of given input int list a random number 0 - 100
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def add_rand(input_obj, apply_button):
    # Changes apply button to pink
    apply_button.config(bg = 'pink', activebackground = 'pink')
    
    # Gets random string value and adds to input_obj
    x = str(ran.randint(0,1000))
    match input_obj:
        case list():
            input_obj.append(x)
        case dict():
            # currently just updates the key value of the random key
            # if the key does not exist will add the key with the random value
            input_obj.update({x: ran.randint(0,1000)})
        case set():
            input_obj.add(x)
        
        # FIXME: Need a way to check all existing keys and if the random key does not exist then
        #        adds it, other wise if it does, it needs to call another random key to check against
# =================================================================================================




# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - change_index takes the global input_obj and modifies it, this is done through the passed widgets of
#   index_entry and val_entry which are entry box widgets passed.
# - apply_button is the apply button just being changed to pink after entering in data
#           - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def change_index(index_entry, val_entry, input_obj, apply_button):
    # Changes apply button to pink
    apply_button.config(bg = 'pink', activebackground = 'pink')

    # Checks if input_obj is a list type and the index values is in range of the length
    if type(input_obj) == list and int(index_entry.get()) <= len(input_obj):
        
        # sets the index of list to the entered value
        input_obj[int(index_entry.get())] = val_entry.get()

    else:
        # place label for bad index of change location!
        pass

    # Checks if input_obj is a dict type
    # Adds/changes key:value depending on if the key exist
    if type(input_obj) == dict:
        input_obj.update({index_entry.get(): val_entry.get()})

    index_entry.delete(0, tk.END)
    val_entry.delete(0, tk.END)

# =================================================================================================



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Joins new tuple to existing one
#       - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

def join_tuple(e, apply_button, val):
    # Changes apply button to pink
    global input_obj
    apply_button.config(bg = 'pink', activebackground = 'pink')
    
    temp_list = val.split(',')
        
    # Check for any additional list unwanteds
    for x in reversed(temp_list):
        if x == ',':
            temp_list.remove(x)
        if x == '':
            temp_list.remove(x)
            
    input_obj = tuple(input_obj) + tuple(temp_list)
        
    tuple_entry_box2.delete(0, tk.END)
    
# =================================================================================================

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Create new tuple of random integers based on size of val
#       - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def rand_tuple_size(e, apply_button, val):
    global input_obj
    apply_button.config(bg = 'pink', activebackground = 'pink')
    if val.isalpha():
        return

    temp_list = []
    for x in range(0, int(val)):
        temp_list.append(ran.randint(0, 1000))

    input_obj = tuple(temp_list)
    tuple_entry_box3.delete(0, tk.END)

# =================================================================================================


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Gets global input_obj
# - Returns input_obj
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def get_input_obj():
    if input_obj is not None:
        return input_obj
    return None
# =================================================================================================