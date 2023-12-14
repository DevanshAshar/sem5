from bplustree import BPlusTree
import time
bptree = BPlusTree('./b.db',order = 3)
while True:
    choice = int(input("Enter\n1.Insert Value in bptree\n2.Search element in bptree\n3.Print bptree\n4.Delete an element\n0.Exit:\n"))
    if choice ==1:
        value = int(input("Enter the value to be inserted in bptree: \n"))
        element = value.to_bytes(10,'big')
        bptree[value] = element
        print("Value inserted!")
    elif choice ==2:
        value = int(input("Enter the value to be searched in bptree: \n"))
        start_time = time.time()
        if value in bptree:
            print("Element if found in bptree.")
        else:
            print("Element not present in the bptree")
        end_time = time.time()
        print(f"Time of search: {round((end_time-start_time)*1000 , 3)} milliseconds")
    elif choice == 3:
        count = 0
        for key in bptree.keys():
            element = bptree[key]
            element = int.from_bytes(element,'big')
            print(f"value: {element}")
            count +=1
            if count == len(bptree):
                break
    elif choice == 4:
        value = int(input("Enter the value to be deleted from bptree: \n"))
        try:
            bptree.pop(value)
            print("Value deleted from the bptree")
        except:
            print("Value not present in the bptree")
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Invalid input")
