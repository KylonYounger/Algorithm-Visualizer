
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# DSA_des_index - takes in a index for given description
#       Returns - String
# =================================================================================================

def DSA_des_index(x):
    my_des_dic = {0:
    """List -
    A List is a built in python data structure that allow for multiple items to be stored in one variable.
    A list in python is not able to be changed in the way the items are ordered. This means that when an
    item is assigned an index any copies of the list we keep those items in the same order always. This also
    means that any similar items like 3 and 3 in a list is also kept in the same order which is very useful
    for later data structures. A python list will also allow duplicates in its' list.

    Ex: my_list = [0, 1, 2, 3, 4]
    """,
    1: 
    """Dictionary -
    A dictionary in python is a way to store some value with a key assigned to it. Dictionaries are ordered,
    meaning they keep thier same key-value order to other pairs. They are changable, meaning that you can change
    their assigned values and keys. Dictionairies do not allow duplicates; This is because the way to find a
    value of a item is through its' key and with duplicated keys, you will have duplicated values.

    Ex: my_diction = {key: value, 13: "apple"}
    """,
    2:
    """Tuples -
    - A tuple allows to store multiple items in a single variable.\n\
    - Tuple items are ordered, unchangable meaning after creation the data cannot be changed and tuples are allow duplicate values.
    \n- Tuples can have multiple data types.
    
    Ex: my_tuple = (1, 2, True, 4, "apple", "apple")
    """,
    3:
    """Sets -
    - Sets are used to store multiple items in a single variable.\n\
    - Sets are unorderd meaning everytime a set is used the items in the set\n\
        are placed randomly and cannot be refered to be index or key.\n\
    - Sets cannot have duplicate values.\n\
    - Sets are unchangeable, meaning after adding or removing you cannot change the values\
        inside the set.\n\
    - Sets can have different data types.

    Ex: my_set = {0, 1, 2, "apple", True}
    """,
    4:
    """Frozen Sets - 
    - Frozen sets are exactly the same as normal sets except you cannot add or remove items.

    - Although frozen sets are the same as sets, frozen sets have it's own methods that allow to return \
a version of the frozen set that is compaired to another set.
    """
    }
    
    return my_des_dic[x]
