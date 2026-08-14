import tkinter as tk


def entry_checker(curr_val):
    if curr_val == '':
        return True
    if curr_val.isdigit():
        return True
    
    return False

def val_ent(e):
    global val
    global given_input
    if list_box.get() != '':
        val = list_box.get()
    given_input.append(int(val))

    list_label3.config(text = str(given_input))
    list_label3.place(anchor = 'nw', x = -10, y = 60)

    list_box.delete(0, tk.END)

    return None


    

def Input_Def(master, x):
    l = tk.IntVar()
    global given_input
    given_input = []
    match x:
        case 0:

            list_label = tk.Label(master, text = "List Input: ")
            list_label.place(anchor = 'nw', x = -10, y = -10)

            list_label2 = tk.Label(master, text = "Please enter a number to enter into the list:")
            list_label2.place(anchor = 'nw', x = -10, y = 10)

            # Tlc function to pass function correctly for wrapper
            vcmd = master.register(entry_checker)

            global list_box
            # Validate 'key' checks the entered values after each key press
            list_box = tk.Entry(master, bd = 3, width = 40, validate = 'key', validatecommand = (vcmd, "%P"))
            list_box.place(anchor = 'nw', x = 0, y = 30)

            list_box.bind("<Return>", val_ent)

            global list_label3
            list_label3 = tk.Label(master)

        case 1:
            pass
    
    return given_input





# Sample radio buttons for notebook tab 2
'''
radBut0 = tk.Radiobutton(master, text = ' None ', variable = l, value = 0, command = lambda: clicked(l.get()))
radBut0.place(anchor = 'nw', x = -10, y = 10)
radBut1 = tk.Radiobutton(master, text = 'apple', variable = l, value = 1, command = lambda: clicked(l.get()))
radBut1.place(anchor = 'nw', x = -10, y = 30)
radBut2 = tk.Radiobutton(master, text = 'pear', variable = l, value = 2, command = lambda: clicked(l.get()))
radBut2.place(anchor = 'nw', x = -10, y = 50)
'''