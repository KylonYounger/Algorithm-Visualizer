# ============================================================================================
# Kylon Younger 
# current version 0.0.1 7/21/2026
# Algorithm Visualizer uses tkinter library to create a desktop application that allows a user
# to visualy see animations and graphs of algorithms and their runtimes. 
# This project allows me to get a great understanding of larger projects, 
# data structures, algorithms, git and github, and frontend user interaction.
# ============================================================================================

import tkinter as tk
from tkinter import ttk


def selected_list_item(event):
    global main_P_title
    new_label = tree.focus()
    main_P_title = tk.Label(text = str(new_label))
#apple

# Main allows for imports of .py files that contain event structures or REPLACEING window widgets for certain data structure and algorithms.
def main():
    root = tk.Tk()
    root.title("Algorithm Visualizer")
    #root.iconbitmap()
    root.geometry("750x550")
    root.minsize(500, 550)
    root.maxsize(750, 550)

    # Main Panel to allow images and animations.
    main_panel = tk.PanedWindow(root, bd = 10, bg = 'dark grey', relief = 'sunken')
    main_panel.place(anchor = 'nw', relx = 0.45, rely = 0.5, x = 10, y = 100)
    main_panel.pack(fill = "both", ipady = 137, side = "top")
    
    global main_P_title
    # Sample Title label in panel
    main_P_title = tk.Label(main_panel, text = "MAIN PANEL", activebackground = 'dark grey')
    main_P_title.pack(side = "top")

    # FRAME widget - around the tree selector for DSA
    frame = tk.LabelFrame(root, padx = 10, text = 'Data Structures and Algorithms', pady = 100, border = 5, relief = 'ridge')
    frame.place(relx = 0.5, rely = 1.0, anchor = 's', relwidth = .99)

    # Weird frame grid placer for tree viewer. If did not exist, frame will not display.
    # probaly need future fix
    display_frame_lable = tk.Label(frame, pady = 0)
    display_frame_lable.grid(row = 0, column = 0)

    global tree
    # Tree widget - contains all DSA options to display.
    tree = ttk.Treeview(frame, selectmode = "browse", show = 'tree', yscrollcommand = 'tree_scroll_bar')
    tree.place(relx = 0.01, rely = 0.999, anchor = 'nw', width = 275, y = -110, x = -10)
    # tree.tag_configure(tagname = 'font_change', font = 'Broadway')
    tree.bind("<<TreeviewSelect>>", selected_list_item)

    # Tree Scroll Bar - Needs improvment..
    tree_scroll_bar = tk.Scrollbar(tree)
    tree_scroll_bar.config(command = tree.yview)
    tree_scroll_bar.place(in_ = tree, x = 271, relx = 0.01, relheight = 0.99, anchor = 'e', y = 101)

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


    #Sorting Algorithms (parent and children)
    tree.insert(parent = '', index = 3, iid = 3, text = "Sorting Algorithms")
    tree.insert(parent = '3', index = 0, text = "Item 1")


    root.mainloop()
if __name__ == "__main__":
    main()


# Font viewer to copy and change font
"""
    # Source - https://stackoverflow.com/a/53717785
    # Posted by jimmiesrustled, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-07-21, License - CC BY-SA 4.0

    root.title('Font Families')
    fonts=list(font.families())
    fonts.sort()

    def populate(frame):
        '''Put in the fonts'''
        listnumber = 1
        for i, item in enumerate(fonts):
            label = "listlabel" + str(listnumber)
            label = tk.Label(frame,text=item,font=(item, 16))
            label.grid(row=i)
            label.bind("<Button-1>",lambda e,item=item:copy_to_clipboard(item))
            listnumber += 1

    def copy_to_clipboard(item):
        root.clipboard_clear()
        root.clipboard_append("font=('" + item.lstrip('@') + "', 12)")

    def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
    frame = tk.Frame(canvas, background="#ffffff")
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    populate(frame)
"""