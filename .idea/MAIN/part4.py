# binary search

# def find_book_title(books, target_word):
#     book_dict = {}

#     # Create a hash table/dictionary with book titles as keys
#     for title in books:
#         words = title.split()
#         for word in words:
#             if word.lower() not in book_dict:
#                 book_dict[word.lower()] = [title]
#             else:
#                 book_dict[word.lower()].append(title)

#     # Look up the target word in the hash table
#     if target_word.lower() in book_dict:
#         return book_dict[target_word.lower()]
#     else:
#         return []

# def binary_search(books, target):
#     left = 0
#     right = len(books) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         mid_book = books[mid]
        
#         if mid_book == target:
#             return mid
        
#         if mid_book < target:
#             left = mid + 1
#         elif mid_book > target:
#             right = mid - 1
    
#     return -1

# # Example usage
# books = [
#     "Alice in Wonderland",
#     "Brave New World",
#     "Harry Potter and the Chamber of Secrets",
#     "Pride and Prejudice",
#     "Summer night",
#     "To Kill a Mockingbird",
#     "To Kill a Man",
#     "War and Peace",
    
# ]

# target_word = "summer"
# result = find_book_title(books, target_word)


# if len(result) > 0:
#     print(f"The word '{target_word}' is found in the following book(s):")
#     for title in result:
#         print(title)
#         search = binary_search(books,title)
#         if search != -1:
#             print(f"{title} is found at index {search}.")
#         else:
#             print(f"{title} is not found in the list.")
# else:
#     print(f"No book title found with the word '{target_word}'.")


#B+ tree

class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []
        self.values = []
        self.child_pointers = []

class BPlusTree:
    def __init__(self):
        self.root = BPlusTreeNode(is_leaf=True)

    def insert(self, key, value):
        node = self.root
        if len(node.keys) == 0:
            node.keys.append(key)
            node.values.append(value)
        else:
            if len(node.keys) >= 1:
                i = 0
                while i < len(node.keys) and key > node.keys[i]:
                    i += 1
                node.keys.insert(i, key)
                node.values.insert(i, value)

    def search(self, key):
        node = self.root
        while not node.is_leaf:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.child_pointers[i]
        return node.values if key in node.keys else []

def find_book_title(books, target_word):
    bptree = BPlusTree()

    # Construct the B+ tree
    for index, title in enumerate(books):
        words = title.split()
        for word in words:
            word = word.lower()
            bptree.insert(word, (index, title))

    # Look up the target word in the B+ tree
    target_word = target_word.lower()
    result = bptree.search(target_word)

    return result

# Example usage
books = [
    "Alice in Wonderland",
    "Brave New World",
    "Harry Potter and the Chamber of Secrets",
    "Pride and Prejudice",
    "To Kill a Mockingbird",
    "War and Peace",
    "1984"
]

target_word = "peace"
result = find_book_title(books, target_word)

if len(result) > 0:
    print(f"The word '{target_word}' is found in the following book(s):")
    for index, title in result:
        print(f"Index: {index}, Title: {title}")
else:
    print(f"No book title found with the word '{target_word}'.")
