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
    all_boxes = []

    def __init__(self, master, label, x_pos, y_pos):
        super().__init__(master, width = BOX_WIDTH, height = BOX_HEIGHT, relief = BOX_RELIEF, bd = 10)

        self.label = label
        self.y_mov_s = 0
        self.fin_pos = y_pos
        self.x_fin = x_pos

        if len(str(label)) >= 5:
            self.config(width = BOX_WIDTH + ((len(str(label))) * 5))
            
        self.box_label = tk.Label(self, text = label)
        self.box_label.place(anchor = 's', relx = .5, rely = 0.9) # CENTER OF BOX_TEMP

    # Animation for the insert of a new block
    def sliding_frame(self):
        self.place(x = self.x_fin)
        fac = (self.fin_pos - 35) / 100
        print(fac)
        while(True):
            if self.y_mov_s <= self.fin_pos:
                self.y_mov_s += (0.01 + fac)
                self.place(y = self.y_mov_s)
                self.update()
            else:
                break
        

# =================================================================================================

# BOX INHERITANCE CLASS, will use the box class to create a NODE object.
# This will just be a standard box with a value and "pointer" to the next object
# Pointer can be an arrow or it might be the next values number?
class node_box(box):
    def __init__(self, master, label, x_pos, y_pos, next = None, prev = None):
        super.__init__(self, master, label, x_pos, y_pos)

        self.next_ptr = next
        self.prev_ptr = prev

        if next.label is not None:
            self.label += "->" + next.label




# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Places Frames into canvas with Label corrasponding to the list integer
#   - GLOBAL PARAM = given_input   (Gets defined in selected())
#   Returns - None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def apply_list(master, list_button3):
    
    box_list = []
    x_pos = 35
    y_pos = 35

    list_button3.config(bg = 'light grey', activebackground = 'light grey')
    clear_frame_object(master)
    # UPDATE Canvas

    for index in range(0, len(Inp.given_input)):
        if index > 0:
            box_temp = box_list[index - 1]
            x_pos += int(box_temp.cget('width'))
            if x_pos >= 680:
                x_pos = 35
                y_pos += 50

        box_list.append(box(master, Inp.given_input[index], x_pos, y_pos))

    for single_box in box_list:
        single_box.sliding_frame()


    return None

# =================================================================================================




# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Clears any given widget of its children
#   Returns - None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def clear_frame_object(frame):
    # Destroy all widgets inside the frame
    # box contains 
    for widget in frame.winfo_children():
        widget.destroy()

# =================================================================================================