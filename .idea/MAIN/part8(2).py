# Criteria weights (adjust as needed)
net_worth_weight = 0.4
relationship_weight = 0.1
character_trait_weight = 0.3

# Person data
persons = ['Jones', 'Jenna', 'Peter', 'Penelope', 'Will']

# Individual net worth, relationship, and character trait values
net_worth_values = [1000000, 700000, 50000, 500000, 10000]
relationship_values = [0.7, 0.8, 0.5, 0.5, 0.3]
character_trait_values = [0.05, 0.5, 0.3, 0.2, 0.4]

# Initialize variables for the person with the highest motive
highest_motive_score = float('-inf')
person_with_highest_motive = None

# Calculate weighted scores and find person with the highest motive
for person, net_worth, relationship, character_trait in zip(persons, net_worth_values, relationship_values, character_trait_values):
    weighted_sum = net_worth_weight * net_worth + relationship_weight * relationship + character_trait_weight * character_trait
    
    if weighted_sum > highest_motive_score:
        highest_motive_score = weighted_sum
        person_with_highest_motive = person

# Print the results
print("Person with the highest motive:", person_with_highest_motive)
