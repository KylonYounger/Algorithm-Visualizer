import tkinter as tk
import random as ran
import DSA as dsa
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
global return_str
return_str = ""
def Input_Def(master, x, apply_button):
    global input_obj
    BUILT_IN_DSA_POS = [[20, 20]]

    # Tlc function to pass function correctly for wrapper
    vcmd = master.register(entry_checker)

    top_label = tk.Label(master)
    top_label.place(anchor = 'nw', x = -10, y = -10)

    main_entry_label = tk.Label(master, wraplength = 300, justify = 'left', relief = 'solid', bd = 1)
    main_entry_label.place(anchor = 'nw', x = 0, y = 9)

    general_label2 = tk.Label(master)
    general_label2.place(anchor = 'nw', x = -10, y = 30)

    general_label3 = tk.Label(master)
    general_label3.place(anchor = 'nw', x = -10, y = 60)

    general_label4 = tk.Label(master)
    general_label4.place(anchor = 'nw', x = -10, y = 80)

    general_bullet = tk.Label(master, bd = 1, relief = 'solid')

    main_entry_box = tk.Entry(master, bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
    main_entry_box.place(anchor = 'nw', x = 0, y = 45)

    general_entry1 = tk.Entry(master, bd = 3, width = 5, validate = 'key', validatecommand = (vcmd, "%P"))
    general_entry2 = tk.Entry(master, bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
    general_entry3 = tk.Entry(master, bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))

    general_button1 = tk.Button(master)
    general_button2 = tk.Button(master)

    match x:
        case 0: # List
            input_obj = []
            set_pos_seq(BUILT_IN_DSA_POS)

            # LABELS
            top_label.config(text = "List Input: ")

            main_entry_label.config(text = "Please type in a list of data seperated by a comma and press enter:")

            general_label2.config(bd = 3, text = ":Enter a list index")
            general_label2.place(anchor = 'nw', x = 38, y = 108)

            general_label3.config(bd = 3, text = " :Enter a value to change that index")
            general_label3.place(anchor = 'nw', x = 65, y = 128)

            general_label4.config(bd = 1, text = "Change the list value at the specific index: \n(0 is the starting number)", relief = 'solid')
            general_label4.place(anchor = 'nw', x = 0, y = 73)

            general_bullet.config(text = "Lists Can have:\n - Any data types \n - Is ordered \n - Changeable data \n - Allowed Duplicates")
            general_bullet.place(anchor = 'nw', x = 315, y = 87)

            # ENTRY
            # Validate 'key' checks the entered values after each key press  
            main_entry_box.insert(0, '0,1,2,3,4')
    
            general_entry1.place(anchor = 'nw', x = 0, y = 110)
            general_entry2.place(anchor = 'nw', x = 0, y = 130)
            
            main_entry_box.bind("<Return>", lambda e: val_ent(e, apply_button, widget = main_entry_box))
            general_entry1.bind("<Return>", lambda e: change_index(index_entry = general_entry1, val_entry = general_entry2, apply_button = apply_button, input_obj = input_obj))
            general_entry2.bind("<Return>", lambda e: change_index(index_entry = general_entry1, val_entry = general_entry2, apply_button = apply_button, input_obj = input_obj))
            
            # BOXES
            general_button1.config(text = 'add random integer', command = lambda: add_rand(input_obj, apply_button))
            general_button1.place(anchor = 'nw', x = 315, y = 0)

            general_button2.config(text = 'remove end', command = lambda: remove_end(input_obj, apply_button))
            general_button2.place(anchor = 'nw', x = 315, y = 26)

        case 1: # dictionary
            input_obj = {}
            set_pos_seq(BUILT_IN_DSA_POS)

            # LABELS
            top_label.config(text = 'Dictionary Input: ')

            main_entry_label.config(justify = 'left', text = ' Please type in a dictionary of data seperated by a ":" and press enter: ')
            main_entry_label.place(anchor= 'nw', x = -3, y = 12)

            general_label2.config(justify = 'left', text = '\nAdd/Change key: ')
            general_label2.place(anchor= 'nw', x = -7, y = 67)

            general_label3.config(text = 'Add/Change value: ')
            general_label3.place(anchor= 'nw', x = -7, y = 124)

            general_bullet.config(text = "Dictionaries have:\n - Key:Value Pairs \n - Is ordered \n - Changeable data \n - No Duplicates")
            general_bullet.place(anchor = 'nw', x = 320, y = 85)

            # ENTRY BOXES
            main_entry_box.config(bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            main_entry_box.place(anchor = 'nw', x = -3, y = 49)
            main_entry_box.insert(0, "1:2,Apple:4")

            general_entry2.config(bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            general_entry2.place(anchor = 'nw', x = -3, y = 102)

            general_entry3.config(bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            general_entry3.place(anchor = 'nw', x = -3, y = 144)

            main_entry_box.bind("<Return>", lambda e: val_ent(e, apply_button, widget = main_entry_box))
            general_entry2.bind("<Return>", lambda e: change_index(general_entry2, general_entry3, input_obj, apply_button))
            general_entry3.bind("<Return>", lambda e: change_index(general_entry2, general_entry3, input_obj, apply_button))

            # BUTTONS
            general_button1.config(text = "Add random key", command = lambda: add_rand(input_obj, apply_button))
            general_button1.place(anchor= 'nw', x = 210, y = 100)

            general_button2.config(text = "Remove last key", command = lambda: remove_end(input_obj, apply_button))
            general_button2.place(anchor = 'nw', x = 210, y = 127)

        case 2: # Tuple
            # Tuple Facts:
            #   Ordered, unchangeable, allowed duplicates
            input_obj = ()
            set_pos_seq(BUILT_IN_DSA_POS)

            # LABELS
            top_label.config(text = 'Tuple Input: ')
            
            general_bullet.config(text = "Tuples:\n - Are ordered \n - Unchangeable data \n - Allow duplicates")
            general_bullet.place(anchor = 'nw', x = 310, y = 100)

            main_entry_label.config(wraplength = 400, justify = 'left', text = ' Please type in a tuple of data seperated by a "," to create a new tuple and press enter: ', bd = 1, relief = 'solid')
            main_entry_label.place(anchor = 'nw', x = -3, y = 10)

            general_label2.config(text = 'Join a new tuple to the existing one: ')
            general_label2.place(anchor = 'nw', x = -5, y = 69)

            general_label3.config(justify = 'left', text = 'Enter a size of random values to be created\n into a new tuple: ')
            general_label3.place(anchor = 'nw', x = -7, y = 110)
    
            # ENTRY
            main_entry_box.config(bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            main_entry_box.place(anchor = 'nw', x = -3, y = 48)
            main_entry_box.insert(0, "1,2,True,4,apple,apple")

            main_entry_box.bind("<Return>", lambda e: val_ent(e, apply_button, widget = main_entry_box))

            general_entry2 = tk.Entry(master, bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            general_entry2.place(anchor = 'nw', x = -3, y = 88)

            general_entry2.bind("<Return>", lambda e: join_tuple(e, apply_button, widget = general_entry2))

            general_entry3.config(bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            general_entry3.place(anchor = 'nw', x = -3, y = 145)

            general_entry3.bind("<Return>", lambda e: rand_tuple_size(e, apply_button, widget = general_entry3))

        case 3: # Set

            input_obj = set()
            set_pos_seq(BUILT_IN_DSA_POS)
            
            # LABELS
            top_label.config(text = 'Set Input: ')
            
            general_bullet.config(text = "Sets:\n - Are unordered \n - Unchangeable \n - No duplicates")
            general_bullet.place(anchor = 'nw', x = 337, y = 100)

            main_entry_label.config(wraplength = 400, justify = 'left', text = ' Please type in a set of data seperated by a "," and press enter: ', bd = 1, relief = 'solid')
            main_entry_label.place(anchor = 'nw', x = -3, y = 20)

            # ENTRY
            main_entry_box.config(bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            main_entry_box.place(anchor = 'nw', x = -3, y = 48)
            main_entry_box.insert(0, "1,2,True,4")
            main_entry_box.bind("<Return>", lambda e: val_ent(e, apply_button, widget = main_entry_box))

            # BOXES
            general_button1.config(text = "Add random item", command = lambda: add_rand(input_obj, apply_button))
            general_button1.place(anchor= 'nw', x = 10, y = 100)

            general_button2.config(text = "Remove random item", command = lambda: remove_end(input_obj, apply_button))
            general_button2.place(anchor = 'nw', x = 10, y = 127)

        case 4: # Frozenset
            input_obj = frozenset()
            set_pos_seq(BUILT_IN_DSA_POS)

            # LABELS
            top_label.config(text = 'frozen sets Input: ')
            
            general_bullet.config(text = "Frozen sets:\n - Are unordered \n - Unchangeable \n - No duplicates \n - Immutable")
            general_bullet.place(anchor = 'nw', x = 338, y = 87)

            main_entry_label.config(wraplength = 400, justify = 'left', text = ' Please type in a set of data seperated by a "," and press enter to create a new frozen set: ', bd = 1, relief = 'solid')
            main_entry_label.place(anchor = 'nw', x = -3, y = 15)

            # ENTRY
            main_entry_box.config(bd = 3, width = 47, validate = 'key', validatecommand = (vcmd, "%P"))
            main_entry_box.place(anchor = 'nw', x = -3, y = 55)
            main_entry_box.insert(0, "1,2,True,4")
            main_entry_box.bind("<Return>", lambda e: val_ent(e, apply_button, widget = main_entry_box))
            
        case 10: # Stacks
            stack_obj = dsa.stack()
            input_obj = []
            set_pos_seq([[354, 20]])

            # Labels
            top_label.config(text = 'Stack Input: ')

            main_entry_label.config(text = "Please enter in a stack item: ")
                        
            general_bullet.config(text = "Stacks:\n - [LIFO] \n Built top down \n - Uses List type")
            general_bullet.place(anchor = 'nw', x = 342, y = 100)

            # Entrys
            main_entry_box.config(bd = 3, width = 10, validate = 'key', validatecommand = (vcmd, "%P"))
            main_entry_box.place(anchor = 'nw', x = -3, y = 55)
            main_entry_box.bind("<Return>", lambda e: stack_prop(apply_button, obj = stack_obj, widget = main_entry_box, opp = "push"))

            # Buttons
            general_button1.config(text = "Pop off Stack", command = lambda: stack_prop(apply_button, obj = stack_obj, opp = "pop"))
            general_button1.place(anchor = 'nw', x = 210, y = 100)

        case _:
            input_obj = []
            
            
    return None

# =================================================================================================

def stack_prop(apply_button, obj, widget, opp = None):
    global input_obj
    val = widget.get()
    apply_button.config(bg = 'pink', activebackground = 'pink')
    match opp:
        case "push":
            obj.push(val)
        case 'pop':
            return_str = obj.pop()
        case "peek":
            return_str = obj.peek()
        case "size":
            return_str = obj.size()
    
    input_obj = obj.stack
    widget.delete(0, tk.END)
        

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Checks if curr_val entered into entry box is a number or a backspace
#           - returns True if the value is a digit or is a backspace
#           - else returns false and denies key-press
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# FIXME: Just ignore all null spaces encountered
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
def val_ent(e, apply_button, widget):
    global input_obj
    
    apply_button.config(bg = 'pink', activebackground = 'pink')
    val = widget.get()
    temp_list = val.split(',')

    for x in reversed(temp_list):
        if x == ',' or x == '':
            temp_list.remove(x)

    if type(input_obj) == list:
        input_obj = temp_list
    elif type(input_obj) == tuple:
        input_obj = tuple(temp_list)
    elif type(input_obj) == set:
        input_obj = set(temp_list)  
    elif type(input_obj) == frozenset:
        input_obj = frozenset(temp_list)
    elif type(input_obj) == dict:
        # Adds list objects after removing ',' and ':'
        for x in range(0, len(temp_list)):
            temp_val = temp_list[x]
            temp_other = temp_val.split(':')
            input_obj.update({temp_other[0] : temp_other[1]})
        
        
    widget.delete(0, tk.END)

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

def join_tuple(e, apply_button, widget):
    # Changes apply button to pink
    global input_obj
    apply_button.config(bg = 'pink', activebackground = 'pink')
    val = widget.get()
    temp_list = val.split(',')
        
    # Check for any additional list unwanteds
    for x in reversed(temp_list):
        if x == ',':
            temp_list.remove(x)
        if x == '':
            temp_list.remove(x)
            
    input_obj = tuple(input_obj) + tuple(temp_list)
        
    widget.delete(0, tk.END)
    
# =================================================================================================

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Create new tuple of random integers based on size of val
#       - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def rand_tuple_size(e, apply_button, widget):
    global input_obj
    apply_button.config(bg = 'pink', activebackground = 'pink')
    val = widget.get()
    if val.isalpha():
        return

    temp_list = []
    for x in range(0, int(val)):
        temp_list.append(ran.randint(0, 1000))

    input_obj = tuple(temp_list)
    widget.delete(0, tk.END)

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


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - sets starting x and y pos for the DSA
# - Returns list of x and y
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def set_pos_seq(list):
    global pos_list
    pos_list = [] + list
# =================================================================================================

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Gets starting x and y pos for the DSA
# - Returns list of x and y
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def get_pos_seq():
    return pos_list
# =================================================================================================

def get_ret_string():
    return return_str