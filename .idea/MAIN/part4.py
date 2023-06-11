# binary search

def find_book_title(books, target_word):
    book_dict = {}

    # Create a hash table/dictionary with book titles as keys
    for title in books:
        words = title.split()
        for word in words:
            if word.lower() not in book_dict:
                book_dict[word.lower()] = [title]
            else:
                book_dict[word.lower()].append(title)

    # Look up the target word in the hash table
    if target_word.lower() in book_dict:
        return book_dict[target_word.lower()]
    else:
        return []

def binary_search(books, target):
    left = 0
    right = len(books) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_book = books[mid]
        
        if mid_book == target:
            return mid
        
        if mid_book < target:
            left = mid + 1
        elif mid_book > target:
            right = mid - 1
    
    return -1

# Example usage
books = [
    "Alice in Wonderland",
    "Brave New World",
    "Harry Potter and the Chamber of Secrets",
    "Pride and Prejudice",
    "Summer night",
    "To Kill a Mockingbird",
    "To Kill a Man",
    "War and Peace",
    
]

target_word = "summer"
result = find_book_title(books, target_word)


if len(result) > 0:
    print(f"The word '{target_word}' is found in the following book(s):")
    for title in result:
        print(title)
        search = binary_search(books,title)
        if search != -1:
            print(f"{title} is found at index {search}.")
        else:
            print(f"{title} is not found in the list.")
else:
    print(f"No book title found with the word '{target_word}'.")


# #B+ tree
# class Book:
#     def __init__(self, title, location):
#         self.title = title
#         self.location = location


# class BPlusTree:
#     def __init__(self, order):
#         self.order = order
#         self.root = None
    
#     def search(self, keyword):
#         if self.root is None:
#             return "Library is empty."
#         else:
#             results = []
#             self._search_node(self.root, keyword, results)
#             if not results:
#                 return "Book not found."
#             return results
    
#     def _search_node(self, node, keyword, results):
#         if node.is_leaf:
#             for i in range(len(node.keys)):
#                 if keyword in node.keys[i].title:
#                     results.append(node.keys[i])
#         else:
#             for i in range(len(node.keys)):
#                 if keyword < node.keys[i].title:
#                     return self._search_node(node.children[i], keyword, results)
#             return self._search_node(node.children[-1], keyword, results)
    
#     def insert(self, book):
#         if self.root is None:
#             self.root = BPlusTreeNode(self.order, is_leaf=True)
#             self.root.keys.append(book)
#         else:
#             if len(self.root.keys) >= self.order - 1:
#                 old_root = self.root
#                 self.root = BPlusTreeNode(self.order)
#                 self.root.children.append(old_root)
#                 self._split_child(self.root, 0)
#             self._insert_non_full(self.root, book)
    
#     def _split_child(self, parent, index):
#         child = parent.children[index]
#         new_child = BPlusTreeNode(self.order, is_leaf=child.is_leaf)
#         parent.keys.insert(index, child.keys[self.order//2])
#         parent.children.insert(index+1, new_child)
#         new_child.keys = child.keys[self.order//2+1:]
#         child.keys = child.keys[:self.order//2]
        
#         if not child.is_leaf:
#             new_child.children = child.children[self.order//2+1:]
#             child.children = child.children[:self.order//2+1]
    
#     def _insert_non_full(self, node, book):
#         i = len(node.keys) - 1
#         if node.is_leaf:
#             node.keys.append(None)
#             while i >= 0 and book.title < node.keys[i].title:
#                 node.keys[i+1] = node.keys[i]
#                 i -= 1
#             node.keys[i+1] = book
#         else:
#             while i >= 0 and book.title < node.keys[i].title:
#                 i -= 1
#             i += 1
#             if len(node.children[i].keys) >= self.order - 1:
#                 self._split_child(node, i)
#                 if book.title > node.keys[i].title:
#                     i += 1
#             self._insert_non_full(node.children[i], book)


# class BPlusTreeNode:
#     def __init__(self, order, is_leaf=False):
#         self.keys = []
#         self.children = []
#         self.is_leaf = is_leaf
#         self.order = order


# def main():
#     bplus_tree = BPlusTree(4)  # Specify the order of the B+ tree
    
#     # Insert books into the library (sorted alphabetically)
#     bplus_tree.insert(Book("Harry Potter and the Sorcerer's Stone", 3001))
#     bplus_tree.insert(Book("Harry Potter and the Chamber of Secrets", 3002))
#     bplus_tree.insert(Book("Summer Night", 2250))
#     bplus_tree.insert(Book("The Great Gatsby", 2001))
#     bplus_tree.insert(Book("To Kill a Mockingbird", 2002))
#     bplus_tree.insert(Book("Pride and Summer", 2213))
    
#     # Search for books by a keyword
#     keyword = "Summer"
#     results = bplus_tree.search(keyword)
    
#     if isinstance(results, str):
#         print(results)  # Output: Book not found.
#     else:
#         print(f"Books found matching '{keyword}':")
#         for book in results:
#             print(f"Title: {book.title}, Code: {book.location}")


# if __name__ == "__main__":
#     main()
