else:
    new_list = new_stuff.split(",")
    index = input("Add this to a cerain spot? Press enter for the end of the list, "
                  "or give me a number. Currently {} items in list.".format(len(shopping_list)))
    try:
      if index:
        spot = int(index) - 1 
        for item in new_list:
          shopping_list.insert(spot, item.strip())
          spot += 1
      else:             
        for item in new_list:
          shopping_list.append(item.strip())
    except:
      if index == str(index):
# Here I made a loop if user put in string it give a prompt with an input:
        while True:
          index = input("Please, put in a number: ")
          if index == int(index):
            break
          elif index == str(index):
            continue
      if index:
        spot = int(index) - 1 
        for item in new_list:
          shopping_list.insert(spot, item.strip())
          spot += 1
      else:             
        for item in new_list:
          shopping_list.append(item.strip())
