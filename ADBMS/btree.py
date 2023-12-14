from BTrees.IIBTree import IIBTree
import time
def print_menu():
    print("1. Insert")
    print("2. Search")
    print("3. Show Tree")
    print("4. Exit")
    return input("Enter your choice: ")
b_tree = IIBTree(order=5)
while True:
    choice = print_menu()
    if choice == '1':
        value = int(input("Enter Element to Insert : "))
        insertion_start_time = time.time()
        b_tree.insert(value, value)
        insertion_end_time = time.time()
        print("Element inserted into the B tree.")
        print(f"Insertion time: {round((insertion_end_time-insertion_start_time)*1000,3)} milliseconds")
    elif choice == '2':
        value = int(input("Enter Element to Search : "))
        search_start_time = time.time()
        if value in b_tree:
            search_end_time = time.time()
            print("Value found in the tree")
            print(f"Search time: {round((search_end_time-search_start_time)*1000,3)} milliseconds")
        else:
            print("Value not found in the tree")
    elif choice == '3':
        print("B Tree:")
        print(list(b_tree.items()))
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
