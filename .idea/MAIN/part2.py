def find_lock_combinations():
    for combination in range(1000):
        combination_str = str(combination).zfill(3)  # Pad with leading zeros if necessary
       
        # Check if the current combination matches the correct combination
        if combination_str == "123":  # Replace "123" with the actual correct combination
            return combination_str
   
    return None


# Call the function to find the lock combination
combination = find_lock_combinations()


# Print the output based on the result
if combination:
    print("The correct combination for the lock is:", combination)
else:
    print("No valid combination found.")
