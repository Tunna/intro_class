"""
Lists Lecture Exercise.
This project is a shopping list app.
We have a global list that will be our shopping list.
Make sure your code deals with upper and lower case.
"""
shopping_list = []


def add_shopping_list(item):
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "%s has been added." % (item)
    else:
        print "This item %s already exists!" % (item)
    return sorted_shopping_list()


def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list


def remove_item(item):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed." % (item)
    else:
        print "%s was not on the list." % (item)
    return sorted_shopping_list()


def write_to_file(file_name):
    with open(file_name, mode = "w") as my_file:
        for item in shopping_list:
            # Writing to the file
            my_file.write(item + "\n")


def write_to_file_append(file_name, food_text):
    with open(file_name, mode = "a") as my_file:
        my_file.write(food_text + "\n")            


def read_file_by_iteration(file_name):
    output_list = []
    with open(file_name) as my_file:
        for line in my_file: 
            clean_line = line.strip()
            shopping_list = output_list.append(clean_line)
    return shopping_list


def main():
    
    # TEST FUNCTIONS
    # 1 - add 4 times to your shopping list
    print add_shopping_list("apple")
    print add_shopping_list("steak")
    print add_shopping_list("beef")
    print add_shopping_list("mustard")

    # 2 - Add an item that is already in the list. what happens?
    print add_shopping_list("apple")
    print add_shopping_list("pear")
    print add_shopping_list("orange")

    # 3 - Remove an item on your list
    print remove_item("apple")

    # 4 - Remove an item that is not in the list. what happens?
    print remove_item("chicken")

    file_name = "shopping_list_file.txt"
    
    write_to_file(file_name)

    write_to_file_append(file_name, "mango")

    read_file_by_iteration(file_name)

  

if __name__ == "__main__":
    main()