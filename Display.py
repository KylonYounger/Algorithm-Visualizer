import tkinter as tk
import DSA_InputSpecs as Inp

'''
    - Thoughts and ideas
        "apply list" will soon have to be able to take a class object and apply
        that to any type of selected tree item. Then either a play button or the
        apply button will start / reset the animations.

'''


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Places Frames into canvas with Label corrasponding to the list integer
#   - GLOBAL PARAM = given_input   (Gets defined in selected())
#   Returns - None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def apply_list(master, list_button3):
    x_pos = 50
    list_button3.config(bg = 'light grey', activebackground = 'light grey')
    clear_frame(master)
    # UPDATE Canvas
    for x in Inp.given_input:
        global box_temp
        box_temp = tk.Frame(master, bd = 10, width = 50, height = 50, relief = 'raised')
        box_temp.place(x = x_pos, y = 120)
        x_pos += 50

        box_label = tk.Label(box_temp, text = x)
        box_label.place(anchor = 's', x = 14, y = 25)

    return None

# =================================================================================================



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Clears any given widget of its children
#   Returns - None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def clear_frame(frame):
    # Destroy all widgets inside the frame
    for widget in frame.winfo_children():
        widget.destroy()

# =================================================================================================