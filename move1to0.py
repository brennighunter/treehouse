#Move the 1 to position 0. You can do this in one step with .pop() and .insert().

the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

>>> the_list.insert(0, the_list.pop(3))
