from functions import *


the_menu = {
    "L" : "List",
    "A" : "Add",
    "U" : "Update",
    "D" : "Delete",
    "M" : "Show average price",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"
    }

spicy_scale_map = {
        1: "Not spicy",
        2: "Low-key spicy",
        3: "Hot",
        4: "Diabolical",
    }

restaurant_menu_list = [
    {
        "name": "burrito",
        "calories": 500,
        "price": 12.90,
        "is_vegetarian": "yes",
        "spicy_level": 2
    },
    {
        "name": "rice bowl",
        "calories": 400,
        "price": 14.90,
        "is_vegetarian": "no",
        "spicy_level": 3
     },
     {
        "name": "margherita",
        "calories": 800,
        "price": 18.90,
        "is_vegetarian": "no",
        "spicy_level": 2
     }
    ]


assert print_main_menu(the_menu) == None


assert get_selection("L", the_menu) == "List"
assert get_selection("A", the_menu) == "Add"
assert get_selection("m", the_menu, go_back=True) == None


assert is_num("6.7") == True
assert is_num("12r9") == False
assert is_num("781") == True

assert is_valid_name("a") == False
assert is_valid_name("bo") == False
assert is_valid_name(42) == False
assert is_valid_name(["soup"]) == False
assert is_valid_name("soup") == True

assert is_valid_spicy_level("1", spicy_scale_map) == True
assert is_valid_spicy_level("90", spicy_scale_map) == False
assert is_valid_spicy_level(1, spicy_scale_map) == False


assert is_valid_is_vegetarian("yes") == True
assert is_valid_is_vegetarian("no") == True
assert is_valid_is_vegetarian(4) == False
assert is_valid_is_vegetarian("abc") == False

assert is_valid_price("1.2") == True
assert is_valid_price("1.2.3") == False
assert is_valid_price(1.2) == False
assert is_valid_price("12") == True


assert is_valid_calories("123") == True
assert is_valid_calories("12.3") == False
assert is_valid_calories(123) == False
assert is_valid_calories("abc") == True


assert get_new_menu_dish([ "a", "500", "12.90", "yes"], spicy_scale_map) == ("name", "a")
assert get_new_menu_dish([ "burrito", "50.0", "12.90", "yes"], spicy_scale_map) == ("calories", "50.0")
assert get_new_menu_dish([ "burrito", "500", "abc", "yes"], spicy_scale_map) == ("price", "abc")
assert get_new_menu_dish([ "burrito", "500", "12.90", "not an answer"], spicy_scale_map) == ("is_vegetarian", "not an answer")
assert get_new_menu_dish([ "burrito", "500", "12.90", "yes"], spicy_scale_map) == {"name":"burrito", "calories":"500", "price":"12.90", "is_vegetarian":"yes"}

assert get_new_menu_dish([ "a", "500", "12.90", "yes", "2"], spicy_scale_map) == ("name", "a")
assert get_new_menu_dish([ "burrito", "50.0", "12.90", "yes", "2"], spicy_scale_map) == ("calories", "50.0")
assert get_new_menu_dish([ "burrito", "500", "abc", "yes", "2"], spicy_scale_map) == ("price", "abc")
assert get_new_menu_dish([ "burrito", "500", "12.90", "not an answer", "2"], spicy_scale_map) == ("is_vegetarian", "not an answer")
assert get_new_menu_dish([ "burrito", "500", "12.90", "not an answer", "9"], spicy_scale_map) == ("spicy_level", "9")
assert get_new_menu_dish([ "burrito", "500", "12.90", "yes", "2"], spicy_scale_map) == {"name":"burrito", "calories":"500", "price":"12.90", "is_vegetarian":"yes", "spicy_level":"2"}


assert is_valid_index("3", [1, 2, 3, 4]) == True
assert is_valid_index(1, [1, 2, 4]) == False
assert is_valid_index("10", [3, 5, 6]) == False
assert is_valid_index("-9", [1, 2, 3, 5]) == False
assert is_valid_index("8", [4, 5, 6, 7], 6) == True

assert delete_dish([], "2") == 0
assert delete_dish([1, 2, 3], 2) == None
assert delete_dish([1, 2, 3], "9") == -1
assert delete_dish([1, 2, 3], "2") == 3
assert delete_dish([1, 2, 3], "5", 4) == 2


assert save_menu_to_csv("test", restaurant_menu_list, spicy_scale_map) == -1
assert save_menu_to_csv("", restaurant_menu_list, spicy_scale_map) == None
assert save_menu_to_csv("saved_menu.csv", restaurant_menu_list, spicy_scale_map) == []


assert load_menu_from_csv("yay", restaurant_menu_list, spicy_scale_map) == -1
assert load_menu_from_csv("", [1, 2, 3], spicy_scale_map) == None
assert load_menu_from_csv("testing.csv", [{1:"one"}, {2:"two"}, {3:"three"}], spicy_scale_map) == []

assert get_restaurant_expense_rating(["burrito", "500", "5.0", "yes"]) == 5.0
assert get_restaurant_expense_rating(["burrito", "500", "15.0", "yes"]) == 15.0
assert get_restaurant_expense_rating(["burrito", "500", "25.0", "yes"]) == 25.0


assert update_menu_dish([], "1", spicy_scale_map, "price", "20.0") == 0
assert update_menu_dish(retaurant_menu_list, "abc", spicy_scale_map, "price", "20.0") == -1
assert update_menu_dish(retaurant_menu_list, "1", spicy_scale_map, "spicy_level", "40") == -2 

