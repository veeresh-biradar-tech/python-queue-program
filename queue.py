# Python Program To Perform Queue And Its Operation

queue= []
reverse= []

def push(queue):
    try:
        element= int(input("Enter The Value You Want To Push In Queue : "))
        queue.append(element)
        print(f"Item {element} Is Pushed In Queue")
    except ValueError:
        print("Enter Only Integer Value To Push")

def pop(queue):
    if not len(queue)== 0:
        return queue.pop(0)
    print("Queue Is Empty So can't Pop")

def display(queue):
    if not len(queue)== 0:
        return queue
    print("Queue Is Empty No Values To Display")


while True:
    print("----- Perform Queue Operation -----")
    print("1 -- Push")
    print("2 -- Pop")
    print("3 -- Display")
    print("4 -- Exit")

    try:
        choice= int(input("Enter Your Choice : "))
        if choice== 1:
            push(queue)
        elif choice== 2:
            print(f"Item {pop(queue)} Is Poped")
        elif choice== 3:
            print(f"Queue items Are {display(queue)}")
        elif choice== 4:
            break
        else:
            print("Enter Only 1, 2, 3, or 4")
    except ValueError:
        print("Enter Integers Only")
