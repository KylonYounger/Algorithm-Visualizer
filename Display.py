import tkinter as tk
import DSA_InputSpecs as Inp

'''
    - Thoughts and ideas
        "apply list" will soon have to be able to take a class object and apply
        that to any type of selected tree item. Then either a play button or the
        apply button will start / reset the animations.

        - Create class that allows the object instance of a Frame with a label. This should be the base
        class that allows for sub-classes and inheritance to take place.

'''
BOX_WIDTH = 50
BOX_HEIGHT = 50
BOX_RELIEF = 'raised'


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Class for Display box
#   - Uses 
#   - Inherites from Frame 
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
class box(tk.Frame):
    def __init__(self, master, label, x_pos, y_pos):
        super().__init__(master, width = BOX_WIDTH, height = BOX_HEIGHT, relief = BOX_RELIEF, bd = 10)

        self.y_mov_s = 0
        self.fin_pos = y_pos
        self.place(x = x_pos)
        
        self.box_label = tk.Label(self, text = label)
        self.box_label.place(anchor = 's', x = 14, rely = 0.9) # CENTER OF BOX_TEMP

    def sliding_frame(self):
        if self.y_mov_s <= self.fin_pos:
            self.y_mov_s += 1
            self.update_idletasks()
            self.place(y = self.y_mov_s)
            self.after(3, self.sliding_frame)


# =================================================================================================



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Places Frames into canvas with Label corrasponding to the list integer
#   - GLOBAL PARAM = given_input   (Gets defined in selected())
#   Returns - None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def apply_list(master, list_button3):
    x_pos = 35
    name_index = 0

    list_button3.config(bg = 'light grey', activebackground = 'light grey')
    clear_frame(master)
    # UPDATE Canvas
    for x in Inp.given_input:
        x_pos += 50
        box(master, x, x_pos, 125).sliding_frame()

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