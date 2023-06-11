def linearSearch(sortedBooks, differentWords):
    foundBooks = []
    for book in sortedBooks:
        bookTitle = book.lower().split()[0]  # Get the first word of the book title
        if bookTitle in differentWords:
            foundBooks.append(book)
    return foundBooks

# Example usage
sortedBooks = ["Fine Men on Ice", "Great Expectations", "Summer of '69", "Winter's Tale", "Daydreams and Nightmares", "Time Travelers", "Lenovo Time"]
differentWords = ["fine", "great", "summer", "winter", "day", "night", "time"]

foundBooks = linearSearch(sortedBooks, differentWords)

print("The different words are:")
for word in differentWords:
    print("- " + word)

print()
if foundBooks:
    print("Books found:")
    for book in foundBooks:
        print("-", book)
else:
    print("No books found")