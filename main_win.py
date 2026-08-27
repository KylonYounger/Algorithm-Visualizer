# ============================================================================================
# Kylon Younger 
# current version 0.0.5 8/14/2026
# Algorithm Visualizer uses tkinter library to create a desktop application that allows a user
# to visualy see animations and graphs of algorithms and their runtimes. 
# This project allows me to get a great understanding of larger projects, 
# data structures, algorithms, git and github, and frontend user interaction.
# ============================================================================================
#
# ============================================================================================
# - GLOBAL PARAMETERS:
#   - global list_num
#   - global main_panel
#   - global notebook_frame_2
#   - global Note_B_label
#   - global tree
#   - global main_P_title
# ============================================================================================
import DSA_descriptions as des
from DSA_InputSpecs import *
import tkinter as tk
from tkinter import ttk


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
        #super.__init__(self, master, label, x_pos, y_pos)

        self.next_ptr = next
        self.prev_ptr = prev

        #if next.label is not None:
        #    self.label += "->" + next.label

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



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - Places Frames into canvas with Label corrasponding to the list integer
#   - GLOBAL PARAM = given_input   (Gets defined in selected())
#   Returns - None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def apply_list(master, apply_button):
    apply_button.config(state = 'disabled')
    box_list = []
    x_pos = 35
    y_pos = 35

    apply_button.config(bg = 'light grey', activebackground = 'light grey')
    clear_frame(master)
    # UPDATE Canvas

    input_obj = get_input_obj()
    if input_obj is not None and type(input_obj) == list:
        for index in range(0, len(input_obj)):
            if index > 0:
                box_temp = box_list[index - 1]
                x_pos += int(box_temp.cget('width'))
                if x_pos >= 680:
                    x_pos = 35
                    y_pos += 50

            box_list.append(box(master, input_obj[index], x_pos, y_pos))

    if input_obj is not None and type(input_obj) == dict:
            temp_list = []
            for x in input_obj:
                temp_list.append(x)
            for index in range(0, len(input_obj)):
                if index > 0:
                    box_temp = box_list[index - 1]
                    x_pos += int(box_temp.cget('width'))
                    if x_pos >= 680:
                        x_pos = 35
                        y_pos += 50
                temp_str = str("{ " + temp_list[index] + " : " + str(input_obj.get(temp_list[index])) + " }")
                box_list.append(box(master, temp_str, x_pos, y_pos))

    if input_obj is not None and type(input_obj) == tuple:
            for index in range(0, len(input_obj)):
                if index > 0:
                    box_temp = box_list[index - 1]
                    x_pos += int(box_temp.cget('width'))
                    if x_pos >= 680:
                        x_pos = 35
                        y_pos += 50

                box_list.append(box(master, input_obj[index], x_pos, y_pos))

    for single_box in box_list:
        single_box.sliding_frame()
    apply_button.config(state = 'active')

# =================================================================================================



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# SELECTED - Gets TreeView selected item, matches the string to given dictionary, and replaces:
#    
#    Done: - Notebook decriptions
#          - Main Canvases label (main_P_title)
#               
#    TODO: - canvas animations / images
#          - user input
#   
#          - Returns None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

def selected(event):
    # Sets main planels lable with tree selected item
    var_label = tree.selection()
    string = tree.item(var_label[0])
    main_P_title.config(text = string["text"])

    Note_B_label.config(state = 'normal')

    # Add much of existing DSAs to diction  : TODO
    matcher_dic = {"List": 0, "Dictionary": 1, "Tuples": 2, "Set": 3}

    Note_B_label.delete(0.0, tk.END)

    # NOTEBOOK TAB 1
    # Set tab 1s' description; Sets Notebook text widget to selected tree item;
    # Uses seperate file dictionary to match "tree.selection()" which is selected user item
    # Turns it into key pair and gets index of key for description to paste
    if matcher_dic.get(string['text']) is not None:
        notebook_text = des.DSA_des_index(matcher_dic[string['text']])
        Note_B_label.insert("1.0", notebook_text)
    Note_B_label.config(state = 'disabled')

    # NOTEBOOK TAB 2
    # Sets buttons and widgets to the corrasponding data structure in the notebook tab.
    # CALL HELPER FUNCTION - contain matcher for each DSA and places into tab 2
    clear_frame(notebook_frame_2)
    
    if matcher_dic.get(string['text']) is not None:
        clear_frame(main_panel)
        apply_button.config(state = 'active')

        # Passes the index of matcher_dic for match statement
        # list_button3 is the apply button
        Input_Def(notebook_frame_2, matcher_dic.get(string['text']), apply_button)

        
    return None

# =================================================================================================



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - helper_window creates new window that gets the passed widget children and lists them to be
#   to be selected and passed to other functions.
#   Returns - None
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def helper_window(e, widget):
    # only if ~ is pressed creates new window
    if e.char == "~":
        
        # New window
        helper = tk.Tk()
        
        # LABELS
        label = tk.Label(helper, text = 'Dev tool for notebook Tab 2')
        label.pack()
        
        label_x = tk.Label(helper, text = 'x position of wiget')
        label_x.pack()
        
        label_y = tk.Label(helper, text = 'y position of wiget')
        label_y.pack()
        
        box_label = tk.Label(helper, text = 'List of Child widgets')
        box_label.pack()

        # ENTRY
        ent_y = tk.Entry(helper, bd = 1)
        ent_y.pack()
        
        ent_x = tk.Entry(helper, bd = 1)
        ent_x.pack()

        # sets list box with a list of all child widgets of current selected DSA in treeview
        child_list_box = tk.Listbox(helper)
        for item in widget.winfo_children():
            child_list_box.insert(tk.END, item)

        child_list_box.pack()
        child_list = widget.winfo_children()

        # Passes the box list and tuple of widget children that can be accessed
        helper.bind('<Return>', lambda e: apply_new_pos(e, ent_x.get(), ent_y.get(), child_list_box, child_list))

        # Sets dict for printing after the helper window closes
        global temp_dic
        temp_dic = {}
        helper.protocol("WM_DELETE_WINDOW", lambda: on_close(helper, temp_dic))

# =================================================================================================


# on_close prints the last dictionary values added or changed
def on_close(helper, temp_dic):
    if temp_dic is not None:
        print(temp_dic)
    helper.destroy()
# =================================================================================================


# Applies the new x and y pos of the selected child widget in the widget box
# updates the dictionary to print last x y values
def apply_new_pos(e, pos_x, pos_y, child_box, child_list):
    # Sets the selected list box children with the entry box numbers
    selection = child_box.curselection()
    if selection:
        index = selection[0]
        # Changes selected widget x and y pos
        child = child_list[index]
        child.place(x = pos_x, y = pos_y)
        temp_str = str(pos_x) + " " + str(pos_y)
        temp_dic.update({str(child) + " :": temp_str})
# =================================================================================================




# =================================================================================================

# Main

# =================================================================================================
# Main allows for imports of .py files that contain event structures or REPLACEING window widgets for certain data structure and algorithms.
def main():


    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # MAIN WINDOW
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    root = tk.Tk()
    root.title("Algorithm Visualizer")
    #root.iconbitmap()
    root.geometry("780x550")
    #root.minsize(750, 550)
    #root.maxsize(750, 550)

    # =================================================================================================



    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # CANVAS for main display of Animations/DSAs
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Main Panel to allow images and animations.
    global main_panel
    main_panel = tk.Canvas(root, bd = 10, bg = 'dark grey', relief = 'sunken', width = 760, height = 800, scrollregion = (0, 0, 2000, 2000))
    main_panel.pack()
    main_panel.bbox("all")

    main_canvas_scroll = tk.Scrollbar(root, orient = 'vertical', command = main_panel.yview)
    main_panel.config(yscrollcommand = main_canvas_scroll.set)
    main_canvas_scroll.place(relx = 0.9, rely = 0.2, relheight = 1)
    
    # =================================================================================================
    
   

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # Label Display
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    
    # Title label in panel
    global main_P_title
    main_P_title = tk.Label(root, text = "Select your DSA", relief = 'raised')
    main_P_title.place(relx = 0.5, anchor = 'n')

    # =================================================================================================

    

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # FRAME for Notebook and TreeView
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # FRAME widget - around the tree selector for DSA and the notebook widget
    frame = tk.LabelFrame(root, padx = 10, text = 'Data Structures and Algorithms', pady = 100, border = 5, relief = 'ridge')
    frame.place(relx = 0.5, rely = 1.0, anchor = 's', relwidth = .99)

    # =================================================================================================



    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # NOTEBOOK Display
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Notebook it's self
    main_notebook = ttk.Notebook(root)
    main_notebook.place(relx = 0.8, rely = 1.0, anchor = 's' + 'e', relwidth = 0.59, x = 140, y = -12)
    
    # Frame for 1st tab (Description tab)
    notebook_frame = tk.Frame(root, padx = 10, pady = 10, border = 5, relief = 'ridge', height = 190)
    notebook_frame.place(relx = 0.75, rely = 1.0, anchor = 'n', relwidth = 0.62)

    # frame for 2nd tab (Function Input)
    global notebook_frame_2
    notebook_frame_2 = tk.Frame(root, padx = 10, pady = 10, border = 5, relief = 'ridge', height = 190)
    notebook_frame_2.place(relx = 0.75, rely = 1.0, anchor = 'n', relwidth = 0.62)
    # Dev tool for tab 2 input setup
    root.bind("<asciitilde>", lambda event: helper_window(event, notebook_frame_2))

    global apply_button
    apply_button = tk.Button(root, command = lambda: apply_list(main_panel, apply_button), text = 'apply', state = 'disabled')
    apply_button.place(anchor = 'nw', x = 728, y = 277)

    # Label for notebook frame
    global Note_B_label
    Note_B_label = tk.Text(notebook_frame, height = 11, state = 'disabled', wrap = 'word', width = 53, yscrollcommand = 'NB_scroll')
    Note_B_label.place(anchor = 'nw', x = -10, y = -10)

    # adding tabs and labels
    main_notebook.add(notebook_frame, text = "Description")
    main_notebook.add(notebook_frame_2, text = "Function Input")

    # Notebook Scroll bar - Needs improvement..
    NB_scroll = tk.Scrollbar(root, orient = 'vertical')
    NB_scroll.config(command = Note_B_label.yview)
    NB_scroll.place(in_ = Note_B_label, x = 402, relx = 0.1, relheight = 0.99, anchor = 'e', y = 87)

    # =================================================================================================



    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # TREE Display
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    # Tree widget - contains all DSA options to display.
    global tree
    tree = ttk.Treeview(frame, selectmode = "browse", show = 'tree', yscrollcommand = 'tree_scroll_bar')
    tree.place(relx = 0.01, rely = 0.999, anchor = 'nw', width = 275, y = -110, x = -10)

    # Mouse double left click for tree widget and enter too select the tree
    tree.bind("<Double-1>", lambda event : selected(event))
    tree.bind("<Return>", lambda event : selected(event))


    # Tree Scroll Bar - Needs improvement..
    tree_scroll_bar = tk.Scrollbar(tree, orient = 'vertical')
    tree_scroll_bar.config(command = tree.yview)
    tree_scroll_bar.place(in_ = tree, x = 271, relx = 0.01, relheight = 0.99, anchor = 'e', y = 101)

    # Weird frame grid placer for tree viewer. If did not exist, frame will not display.
    # probaly need future fix
    display_frame_lable = tk.Label(frame, pady = 0)
    display_frame_lable.pack()

    # =================================================================================================



    # =================================================================================================
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    
    # Hard-Coded Info Section

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # =================================================================================================

    # Built-In Data Structures (parent and children)
    tree.insert(parent = '', index = 0, iid = 0, text = "Built-In Data Structures (Python)")
    tree.insert(parent = '0', index = 0, text = "List")
    tree.insert(parent = '0', index = 1, text = "Dictionary")
    tree.insert(parent = '0', index = 2, text = "Tuples")
    tree.insert(parent = '0', index = 3, iid = 'set', text = "Set")
    tree.insert(parent = 'set', index = 0, text = 'frozen set')

    # User-Defined Data Structures (parent and children)
    tree.insert(parent = '', index = 1, iid = 1, text = "User-Defined Data Structures")
    tree.insert(parent = '1', index = 0, text = "Stacks")
    tree.insert(parent = '1', index = 1, text = "Queue")
    tree.insert(parent = '1', index = 2, text = "Deque")
    tree.insert(parent = '1', index = 3, text = "Linked List")
    tree.insert(parent = '1', index = 4, text = "Trees")
    tree.insert(parent = '1', index = 5, text = "Graphs")
    tree.insert(parent = '1', index = 6, text = "Hash Table")

    # Searching Algortims (parent and children)
    tree.insert(parent = '', index = 2, iid = 2, text = "Searching Algortims") # root
    tree.insert(parent = '2', index = 0, iid = 4, text = "Linear based") # internal
    tree.insert(parent = '4', index = 0, text = "Linear Search")
    tree.insert(parent = '4', index = 1, text = "Binary Search")
    tree.insert(parent = '4', index = 2, text = "Jump Search")
    tree.insert(parent = '4', index = 3, text = "Interpolation Search")
    tree.insert(parent = '4', index = 4, text = "Ternary Search")
    tree.insert(parent = '2', index = 1, iid = 5, text = "Non-Linear Based") # internal
    tree.insert(parent = '5', iid = 6, index = 0, text = "Binary Search Tree") # internal
    tree.insert(parent = '6', index = 0, text = "Binary Tree Traversal")
    tree.insert(parent = '5', index = 2, text = "B-Tree (might remove)")
    tree.insert(parent = '5', index = 3, text = "Trie Search / Prefix Tree (might remove)")
    tree.insert(parent = '5', index = 4, text = "Breadth First Search")
    tree.insert(parent = '5', index = 5, text = "Depth First Search")
    tree.insert(parent = '5', index = 6, text = "Weight Based Graph Search")

    # Sorting Algorithms (parent and children)
    tree.insert(parent = '', index = 3, iid = 3, text = "Sorting Algorithms")
    tree.insert(parent = '3', index = 0, text = "Item 1")

    # =================================================================================================

    root.mainloop()
if __name__ == "__main__":#
    main()

# END