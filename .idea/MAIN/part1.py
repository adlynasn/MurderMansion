from collections import deque


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def bfs(root):
    visited = set()
    queue = deque()
    queue.append(root)

    print("*** Start searching for clues *** ")
    print("")
    while queue:
        node = queue.popleft()
        print(node.name)  # You can modify this to perform any operation on the node

        visited.add(node)

        for child in node.children:
            if child not in visited:
                queue.append(child)
    print("")
    print("*** Complete Searching all rooms ***")


# Build the tree based on the given diagram
entrance = Node("Entrance")
main_hall = Node("Main Hall")
dining = Node("Dining")
utility = Node("Utility")
kitchen = Node("Kitchen")
balcony = Node("balcony")
courtyard = Node("Courtyard")
library = Node("Library")
stairs = Node("stairs")
room1 = Node("Room 1")
void = Node("Void")
room3 = Node("Room 3")
room2 = Node("Room 2")
upper_Balcony1 = Node("Upper Balcony 1")
upper_Balcony2 = Node("Upper Balcony 2")
master_Bedroom = Node("Master Bedroom")
Upper_Utility = Node("Upper Utility")

entrance.add_child(main_hall)
main_hall.add_child(utility)
main_hall.add_child(dining)
main_hall.add_child(courtyard)
dining.add_child(kitchen)
dining.add_child(balcony)
courtyard.add_child(library)
library.add_child(stairs)
stairs.add_child(room1)
room1.add_child(void)
void.add_child(room3)
room3.add_child(room2)
room3.add_child(upper_Balcony1)
room2.add_child(upper_Balcony2)
room2.add_child(master_Bedroom)
master_Bedroom.add_child(Upper_Utility)

bfs(entrance)
