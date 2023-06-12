def calculate_weighted_decision_matrix(matrix, weights):
    scores = []
    for row in matrix:
        weighted_sum = sum(val * weight for val, weight in zip(row, weights))
        scores.append(weighted_sum)
    return scores


# Criteria weights (adjust as needed)
net_worth_weight = 0.4
relationship_weight = 0.1
character_trait_weight = 0.3

# Person data
persons = ['Jones', 'Jenna', 'Peter', 'Penelope', 'Will']

# Individual net worth, relationship, and character trait values
net_worth_values = [1000000, 700000, 50000, 500000, 10000]
relationship_values = [0.7, 0.8, 0.5, 0.5, 0.3]
character_trait_values = [0.05, 0.5, 0.5, 0.7, 0.4]

# Decision matrix with net worth, relationship, and character trait as columns
decision_matrix = [
    net_worth_values,
    relationship_values,
    character_trait_values
]

# Calculate weighted scores for each person
scores = calculate_weighted_decision_matrix(decision_matrix, [net_worth_weight, relationship_weight, character_trait_weight])

# Find the person with the highest total score
person_with_highest_motive = persons[scores.index(max(scores))]

# Print the results
print("Person with the highest motive:", person_with_highest_motive)
