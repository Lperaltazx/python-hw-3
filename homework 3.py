def its_a_function():
    
    shop_list = {}

    while True:
        what_do = input("Would you like to add an item, remove an item, show your list, or quit? ")
        if (what_do == 'quit'):
            print("Thanks! See you soon!")
            for key, value in shop_list.items():
                print(value," ",key)
            break
        
        elif (what_do == 'show'):
            for key, value in shop_list.items():
                print(value," ",key)
            
        elif (what_do == 'add'):
            item_tobe_added = input("What would you like to add? " )
            if item_tobe_added in shop_list:
                shop_list[item_tobe_added] += 1
            else:
                shop_list[item_tobe_added] = 1
        
        elif (what_do == 'delete'):
            item_tobe_deleted = input("What would you like to delete? ")
            if item_tobe_deleted in shop_list:
                del shop_list[item_tobe_deleted]
            else:
                print("You don't have that in your list.")
        
        else:
            print("Please enter add, delete, show, or quit.")
            
its_a_function()







