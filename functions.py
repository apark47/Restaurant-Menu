# functions.py: function definitions for csw8 final project

def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    It returns None
    """
    print("==========================")
    print("What would you like to do?")
    i = 0
    for key in menu:
        print(key + " - " + menu[key])
        i += 1
    print("==========================")

    return None

def list_helper(list_menu, restaurant_menu_list, spicy_scale_map):
    '''
    param: list_menu (dictionary) - contains the suboptions that will be used in get_selection() for
            whether or not the user wants a complete or vegetarian menu
    param: restaurant_menu_list (list) - a list of dictionaries containing each dish,
            their calories, price, vegetarian status, and spicy level
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
    This function gives the user suboptions for the type of menu that will be displayed (full or vegetarian)
    if the given restaurant_menu_list is not empty. If it is empty, then it asks the user to press Enter to continue.
    It does not return anything

    '''
    if len(restaurant_menu_list) == 0:
        print("WARNING: There is nothing to display!")
        # Pause before going back to the main menu
        input("::: Press Enter to continue")
    else:
        subopt = get_selection("List", list_menu)
        if subopt == 'A':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1)
        elif subopt == 'V':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1, vegetarian_only=True)

######## LIST OPTION ########

def get_selection(action, suboptions, to_upper=True, go_back=False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu
    The function displays a submenu for the user to choose from.
    Asks the user to select an option using the input() function.
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.
    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What field would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper()  # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection


def print_restaurant_menu(restaurant_menu, spicy_scale_map, name_only=False, show_idx=True, start_idx=0, vegetarian_only=False):
    """
    param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
    param: name_only (Boolean)
            If False, then only the name of the dish is printed.
            Otherwise, displays the formatted dish information.
    param: show_idx (Boolean)
            If False, then the index of the menu is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            dish name, where idx is the 0-based index in the list.
    param: start_idx (int)
            an expected starting value for idx that
            gets displayed for the first dish, if show_idx is True.
    param:  vegetarian_only (str)
             If set to False, prints all dishes, regardless of their
             is_vegetarian status ("yes/no" field status).
             If set to True , display only the dishes with
             "is_vegetarian" status set to "yes".
            
    returns: None; only prints the restaurant menu
    purpose: Prints the restaurant menu and formats it.
    """
   # Go through the dishes in the restaurant menu:
    idx = 0
    print("------------------------------------------")
    for dish in restaurant_menu:
        # if vegetarian_only is True and the dish is not vegetarian, skip
        if vegetarian_only and dish['is_vegetarian'] != 'yes':
            continue
       
        # if the index of the task needs to be displayed (show_idx is True), print dish index only
        if show_idx == True:  
            print(f"{idx + start_idx}.", end=" ")
            idx += 1
       
        # print the name of the dish
        print(dish["name"].upper())
       
        # if name_only is False
        if not name_only:
            print(f"* Calories: {dish['calories']}")
            print(f"* Price: {dish['price']:.1f}")
            print(f"* Is it vegetarian: {dish['is_vegetarian']}")
            print(f"* Spicy level: {spicy_scale_map[dish['spicy_level']]}")
            print()

    print("------------------------------------------")


def get_new_menu_dish(dish_list, spicy_scale_map):
    '''
    param: dish_list (list) - a list of information for a given dish, where each element corresponds with its
            name, calorie value, price, vegetarian status, and (optional) spicy level.
            Ex: [ "burrito", "500", "12.90", "yes", "2" ]
            Ex: [ "burrito", "500", "12.90", "yes" ]

    param: spicy_scale_map (dict) - a dictionary that
            contains the mapping between the integer
            priority value of spiciness to its representation
            (e.g., key 1 might map to the spiciness value
            "non spicy")    
    validate each element of the list starting from "name" and until "spicy_level"
    If one of them fails, return the name of parameter
    e.g., "name" if "name" is not 3-25 characters long
    or "is_vegetarian" if that field is not set to boolean,
    as well as the value that fails.

    If the length of the list is wrong, return the length of the list
    If one particular field is invalid, return a tuple of its name and the
    value it had. Ex: ('price', '$xxx') or (spicy_level, idk, maybe)
    If all validations pass, return the list with the dish fields
    correctly set to the parameters.
    '''
    
    if is_valid_name(dish_list[0]) != True:
        return("name", dish_list[0])
    if is_valid_calories(dish_list[1]) != True:
        return("calories", dish_list[1])
    if is_valid_price(dish_list[2]) != True:
        return("price", dish_list[2])
    if is_valid_is_vegetarian(dish_list[3]) != True:
        return("is_vegetarian", dish_list[3])
    if len(dish_list) == 5:
        if is_valid_spicy_level(dish_list[4], spicy_scale_map) != True:
            return ("spicy_level", dish_list[4])
        
    
    new_list = {}
    
    if len(dish_list) != 5:
        return len(dish_list)
    else:
        new_list["name"] = dish_list[0]
        new_list["calories"] = int(dish_list[1])
        new_list["price"] = float(dish_list[2])
        new_list["is_vegetarian"] = dish_list[3]
        new_list["spicy_level"] = int(dish_list[4])
        
    return new_list

def is_num(val):
    """
    The function checks if `val` is a string;
    returns False if `val` is not a string.
    Otherwise, returns True if the string `val`
    contains a valid integer or a float.
    Returns False otherwise.
    """
        
    if type(val) == str:
        val = val.replace(".", "", 1)
            
        if val.isdigit() == True:
            return True
        else:
            return False
    else:
        return False

def is_valid_name(name_str):
    """
    param: name_str (string) - a text that is supposed to
            contain between 3 and 25 characters (inclusive
            of both)
    returns:
        - True if it's a text of the valid length
        - False, otherwise
    purpose: checks if name_str is a valid entry
    """
    if type(name_str) == str:
        if 3 <= len(name_str) <= 25:
            return True
        else:
            return False
    else:
        return False
    

def is_valid_calories(calories_str):
    """
    param: calories_str (str) - a string that is
            expected to represent calories
    returns:
        - True if it's a text containing integer value
        - False, otherwise
    purpose: checks if calories_str is a valid entry
    """
    if type(calories_str) == str:    
        if calories_str.isdigit() == True:
            return True
        else:
            return False
    else:
        return False

def is_valid_price(price_str):
    """
    param: price_str (string) - a string that
            contains a decimal number to represent price
    returns:
        - True if it's a text containing decimal number
        - False, otherwise
    purpose: checks if price_str is a valid entry
    """
    if type(price_str) == str:
        price_str = price_str.replace(".", "", 1)
        if price_str.isdigit() == True:
            return True
        else:
            return False
    else:
        return False


def is_valid_is_vegetarian(vegetarian_str):
    """
    param: vegetarian_str (string) - a string that is
            expected to contain a text "yes" or "no"
    returns:
        - True if it's a text with the valid value
        - False, otherwise
    purpose: checks if vegetarian_str is a valid entry
    """
    if type(vegetarian_str) == str:
        if vegetarian_str == "yes" or vegetarian_str == "no":
            return True
        else:
            return False
    else:
        return False



def is_valid_spicy_level(spicy_level_str, spicy_scale_map):
    """
    param: spicy_level_str (string) - a string that is
            expected to contain the level of spiciness
    param: spicy_scale_map (dict) - a dictionary that
            contains the mapping between the integer
            priority value of spiciness to its representation
            (e.g., key 1 might map to the spiciness value
            "non spicy")
    returns:
        - True if spicy_level_str is a text containing
            an integer value that maps to a key in the
            priority_map
        - False, otherwise
    purpose: checks if spicy_level_str is a valid entry based on what is in spicy_scale_map
    """
    if type(spicy_level_str) == str:
        if int(spicy_level_str) in spicy_scale_map:
            return True
        else:
            return False
    else:
        return False


def print_dish(dish, spicy_scale_map, name_only=False):
    """
    param: dish (dict) - a dictionary object that is expected to contain the following keys:
            - "name": dish's name
            - "calories": calories for this dish
            - "price": price of this dish
            - "is_vegetarian": boolean whether this dish is for vegetarian
            - "spicy_level": integer that represents the level of spiciness
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
            values for each corresponding key are string description of the
            level of spiciness
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the dish is printed.
            Otherwise, displays the formatted restaurant menues.
    returns: None; only prints the restaurant menu item

    This function prints the newly added dish with all of its respective information
    """
    
        # print the name of the dish
    print(dish["name"].upper())
       
        # if name_only is False
    if name_only == False:
        print(f"* Calories: {dish['calories']}")
        print(f"* Price: {dish['price']:.1f}")
        print(f"* Is it vegetarian: {dish['is_vegetarian']}")
        print(f"* Spicy level: {spicy_scale_map[dish['spicy_level']]}")
        print()
    

def add_helper(restaurant_menu_list, spicy_scale_map):
    """
    param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
    param: spicy_scale_map (dict) - a dictionary that
            contains the mapping between the integer
            priority value of spiciness to its representation
            (e.g., key 1 might map to the spiciness value
            "non spicy")
    This function continues to ask the user if they want to add another dish. If they do,
    it appends their new added dish to restaurant_menu_list. The function does not return anything
    """
    
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter each required field, separated by commas.")
        # * `name` : name of the dish
        #     * `calories`: number of calories per serving
        #     * 'is_vegetarian' : if the item is vegetarian
        #     * `price` : price of the item
        #     * 'spicy_level' : 1 - 4
        print("::: name of the dish, calories, price, is it vegetarian ( yes | no ), spicy_level ( 1-4 )")
        dish_data = input("> ")  # get the data 
        dish_values = dish_data.split(",") # process the data into a list
        result_dict = get_new_menu_dish(restaurant_menu_list, spicy_scale_map)  # TODO: attempt to create a new dish for the menu
        if type(result_dict) == dict:
            restaurant_menu_list.append(result_dict)  # TODO: add a new dish to the list of dish menus
            print(f"Successfully added a new dish!")
            print_dish(result_dict, spicy_scale_map)
        elif type(result_dict) == int:
            print(f"WARNING: invalid number of fields!")
            print(f"You provided {result_dict}, instead of the expected 5.\n")
        else:
            print(f"WARNING: invalid dish field: {result_dict}\n")

        print("::: Would you like to add another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()

def is_valid_index(idx, in_list, start_idx=0):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - an expected starting
            value for idx (default is 0); gets
            subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that the provided index
    idx is a valid positive index that can retrieve
    an element from in_list. In other words, it check
    if the input string contains only digits and verifies
    that (idx - start_idx) is >= 0, which allows it to retrieve
    an element from in_list.

    returns:
    - True, if idx is a positive numeric index
    that can retrieve an element from in_list.
    - False if idx is not a string that represents an integer value,
    if int(idx) is < start_idx or exceeds the size of in_list.
    """

    if type(idx) != str:
        return False
    
    if idx.isdigit() == True and int(idx) > 0:
        if len(in_list) > (int(idx) - start_idx) >= 0:
            return True
        else:
            return False
    else:
        return False


def delete_dish(in_list, idx, start_idx=0):
    """
    param: in_list - a list from which to remove a dish
    param: idx (str) - a string that is expected to
            contain a representation of an integer index
            of a dish in the provided list
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing
    The function first checks if the input list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from in_list.
    On success, the function saves the dish from in_list
    and returns it after it is deleted from in_list.
    returns:
    If the input list is empty, return 0.
    If idx is not of type string, return None.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from the input list.
    Helper functions:
    - is_valid_index()
    """
    if in_list == []:
        return 0
    if type(idx) != str:
        return None
    if is_valid_index(idx, in_list, start_idx) == False:
        return -1
    else:
        removed_var = in_list[int(idx) - start_idx]
        in_list.pop(int(idx) - start_idx)
        return removed_var

def delete_helper(restaurant_menu_list, spicy_scale_map):
    """
    param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
    param: spicy_scale_map (dict) - a dictionary that
            contains the mapping between the integer
            priority value of spiciness to its representation
            (e.g., key 1 might map to the spiciness value
            "non spicy")
    returns: restaurant_menu_list (list) - the updated restaurant_menu_list after
             respective deletions
    This function continues to ask the user if they want to delete another dish. If they do,
    it deletes their dish from restaurant_menu_list.
    """

    continue_action = 'y'
    while continue_action == 'y':
        if not restaurant_menu_list:
            print("WARNING: There is nothing to delete!")
            break
        print("Which dish would you like to delete?")
        print("Press A to delete the entire menu for this restaurant, M to cancel this operation")
        print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1)
        user_option = input("> ")
        if user_option == "A" or user_option == "a":
            print(f"::: WARNING! Are you sure you want to delete the entire menu ?")
            print("::: Type Yes to continue the deletion.")
            user_option = input("> ")
            if user_option == "Yes":
                restaurant_menu_list = []
                print(f"Deleted the entire menu.")
            else:
                print(f"You entered '{user_option}' instead of Yes.")
                print("Canceling the deletion of the entire menu.")
            break
        elif user_option == 'M' or user_option == 'm':
            break
        result = delete_dish(restaurant_menu_list, user_option, 1)
        if type(result) == dict:
            print("Success!")
            print(f"Deleted the dish |{result['name']}|")
        elif result == 0:  # delete_item() returned an error
            print("WARNING: There is nothing to delete.")
        elif result == -1:  # is_valid_index() returned False
            print(f"WARNING: |{user_option}| is an invalid dish number!")

        print("::: Would you like to delete another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()
    return restaurant_menu_list

def save_menu_to_csv(restaurant_menu_list, filename):
    """
    param: restaurant_menu_list(list of dict) - The list shore dictionary of dishes 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the menu items. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every dishes dictionary in the dictionaries list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:
    * name
    * calories
    * price
    * is_vegetarian
    * spicy_level
    
    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    import os

    if filename[-4:] != ".csv":
        return -1

    with open(filename, 'w', newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        string_list = []
        
        for index, dish in enumerate(restaurant_menu_list):
            string_list = [dish["name"], dish["calories"], dish["price"], dish["is_vegetarian"], dish["spicy_level"]]
            #string_list.append(index)
            csv_writer.writerow(string_list)
        


def save_helper(restaurant_menu_list):
    """
    param: restaurant_menu_list(list of dict) - The list shore dictionary of dishes

    The function ensures that the filename ends with ".csv" and allows them to enter a valid
    file name if they choose to. If the filename has the proper ending, the function prints that
    the user has successfully saved the restaurant menu to the (printed) filename. The function
    does not return anything.
    """
    
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = save_menu_to_csv(restaurant_menu_list, filename)  # TODO: Call the function with appropriate inputs and capture the output
        if result == -1:  # TODO
            print(f"WARNING: |{filename}| is an invalid file name!")  # TODO
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully saved restaurant menu to |{filename}|")
            break

def load_menu_from_csv(filename, restaurant_menu_list, spicy_scale_map):
    """
    param: filename (str) - the name of the file from which to read the contents.
    param: restaurant_menu_list (list) - A list of dish dictionary objects to which
            the dishes read from the provided filename are appended.
            If restaurant_menu_list is not empty, the existing menu items are not deleted.
    param: spicy_scale_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the spicy value "Not Spicy" or "Low")
            Needed by the helper function (see below).

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` (for csv.reader()) and `import os`
    (for `os.path.exists()).

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode.
    For each row in the csv file, the function will count each row (1-based counting) and
    proceed to create a new restaurant menu item using the `get_new_menu_dish()` function.
    - If the function `get_new_menu_dish()` returns a valid dish object (dictionary),
    it gets appended to the end of the `in_list`.
    - If the `get_new_menu_dish()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid dish data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_list` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_list and their indices are appended to the new list that's returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read into the `in_list`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_menu_dish().

    Helper functions:
    - get_new_menu_dish()
    """

    import csv
    import os
    
    if filename[-4:] != ".csv":
        return -1
    if not os.path.exists(filename):
        return None
        
    unprocessed_vals = []
    
    with open(filename, 'r') as myfile:
        file_reader = csv.reader(myfile)

        row_num = 1
        for row in file_reader:
            dish = get_new_menu_dish(row, spicy_scale_map)
            if type(dish) == dict:
                restaurant_menu_list.append(dish)
            else:
                unprocessed_vals.append(row_num)
            row_num += 1
            
        else:
            return unprocessed_vals
    
def load_helper(restaurant_menu_list, spicy_scale_map):
    """
    param: restaurant_menu_list (list) - A list of dish dictionary objects to which
            the dishes read from the provided filename are appended.
            If restaurant_menu_list is not empty, the existing menu items are not deleted.
    param: spicy_scale_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the spicy value "Not Spicy" or "Low")
            Needed by the helper function (see below).

    The function ensures that the filename ends with ".csv" and allows them to enter a valid
    file name if they choose to. If the filename has the proper ending, the function prints that
    the user has successfully saved the restaurant menu to the (printed) filename. The function
    does not return anything.
    """
    
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = load_menu_from_csv(restaurant_menu_list, filename, spicy_scale_map)  # TODO: Call the function with appropriate inputs and capture the output
        if result == -1:  # TODO
            print(f"WARNING: |{filename}| was not found file name!")  # TODO
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully saved restaurant menu to |{filename}|")
            break


        

def update_menu_dish(restaurant_menu_list, idx, spicy_scale_map, field_key, field_info, start_idx=0):
    """
    param: restaurant_menu_list (list) - a menu that contains
            a list of dishes
    param: idx (str) - a string that is expected to contain an integer
            index of a dish in the input list
    param: spicy_scale_map (dict) - a dictionary that contains the mapping
            between the integer spiciness value (key) to its representation
            (e.g., key 1 might map to the priority value "non spicy")
            Needed if "field_key" is "priority" to validate its value.
    param: field_key (string) - a text expected to contain the name
            of a key in the info_list[idx] dictionary whose value needs to
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            info_list[idx][field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing
    The function first calls one of its helper functions
    to validate the idx and the provided field.
    If validation succeeds, the function proceeds with the update.
    return:
    If info_list is empty, return 0.
    If the idx is invalid, return -1.
    If the field_key is invalid, return -2.
    If validation passes, return the dictionary info_list[idx].
    Otherwise, return the field_key.
    Helper functions:
    The function calls the following helper functions:
    - is_valid_index()
     Depending on the field_key, it also calls:
-    - is_valid_name()
-    - is_valid_calories()
-    - is_valid_price()
-    - is_valid_is_vegetarian()
-    - is_valid_spicy_level()
    """

    
    if restaurant_menu_list == []:
        return 0

    if field_key == "name":
        if is_valid_name(field_info) == True:
            restaurant_menu_list[idx][field_key] = field_info
            return restaurant_menu_list[int(idx)]
        else:
            return -2

    if field_key == "calories":
        if is_valid_calories(field_info) == True:
            restaurant_menu_list[idx][field_key] = int(field_info)
            return restaurant_menu_list[int(idx)]
        else:
            return -2
    
    if field_key == "price":
        if is_valid_price(field_info) == True:    
            restaurant_menu_list[idx][field_key] = float(field_info)
            return restaurant_menu_list[int(idx)]
        else:
            return -2

    if field_key == "is_vegetarian":
        if is_valid_is_vegetarian(field_info) == True:    
            restaurant_menu_list[idx][field_key] = field_info
            return restaurant_menu_list[int(idx)]
        else:
            return -2

    if field_key == "spicy_level":
        if is_valid_spicy_level(field_info, spicy_scale_map) == True:
            restaurant_menu_list[idx]["spicy_level"] = int(field_info)
            new_list = restaurant_menu_list
            return new_list[int(idx)]
        else:
            return -2
    if is_valid_index(idx, restaurant_menu_list, start_idx) != True:
        return -1

    else:
        return field_key


def update_helper(restaurant_menu_list, spicy_scale_map):
    """
    param: restaurant_menu_list (list) - A list of dish dictionary objects to which
            the dishes read from the provided filename are appended.
            If restaurant_menu_list is not empty, the existing menu items are not deleted.
    param: spicy_scale_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the spicy value "Not Spicy" or "Low")
            Needed by the helper function (see below).
    helper function: update_menu_dish() and is_valid_index()
    
    This function checks if the number the user enters corresponds to a dish. It
    tells the user if they have succesfully updated the dish or not and/or tells them
    if the menu was not updated if the dish number they entered was invalid. If restaurant_menu_list
    is empty, it tells that to the user.
    It does not return anything.
    
    """
    continue_action = 'y'
    while continue_action == 'y':
        if restaurant_menu_list == []: #TODO
            print("WARNING: There is nothing to update!")
            break
        print("::: Which dish would you like to update?")
        print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1)
        print("::: Enter the number corresponding to the dish.")
        user_option = input("> ")
        if is_valid_index(user_option, restaurant_menu_list) == True: #TODO - check to see if the number is valid
            dish_idx = int(user_option) - 1
            subopt = get_selection("update", restaurant_menu_list[dish_idx], to_upper=False, go_back=True)
            if subopt == 'M' or subopt == 'm':  # if the user changed their mind
                break
            print(f"::: Enter a new value for the field |{subopt}|") # TODO
            field_info = input("> ")
            result = update_menu_dish(restaurant_menu_list, dish_idx, spicy_scale_map, subopt, field_info, start_idx=0) #TODO
            if type(result) == dict:
                print(f"Successfully updated the field |{subopt}|:") # TODO
                print_dish(result, spicy_scale_map)  # TODO
            else:  # update_menu_dish() returned an error
                print(f"WARNING: invalid information for the field |{subopt}|!") # TODO
                print(f"The menu was not updated.")
        else:  # is_valid_index() returned False
            print(f"WARNING: |{user_option}| is an invalid dish number!") # TODO

        print("::: Would you like to update another menu dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()
        # ---------------------------------------------------------------


def get_restaurant_expense_rating(restaurant_menu_list):
    """
    param: restaurant_menu_list - a list of restaurants and their dishes (list of dicts)
    
    Computes the average price of all the items on the menu and display the expense rating of the restaurant.
    average_price < 10 -> Expense rating is : $
    10 <= average_price < 20 -> Expense rating is : $$
    average_price >= 20: Expense rating is : $$$
    
    returns: the average price of the items as a float
    """
    price_list = []
    for dish in restaurant_menu_list:
        price_list.append(dish["price"])

    average_price = sum(price_list) / len(price_list)

    if average_price < 10:
        print("Expense rating is : $")
        print()
    if 10 <= average_price < 20:
        print("Expense rating is : $$")
        print()
    if average_price >= 20:
        print("Expense rating is : $$$")
        print()
    return average_price
        

