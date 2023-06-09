def calculate_weighted_decision_matrix(matrix, weights):
    scores = []
    for row in matrix:
        weighted_sum = sum(val * weight for val, weight in zip(row, weights))
        scores.append(weighted_sum)
    return scores


# Criteria weights (adjust as needed)
net_worth_weight = 0.4
relationship_weight = 0.3
character_trait_weight = 0.3

# Person data
persons = ['Person A', 'Person B', 'Person C', 'Person D', 'Person E']

# Decision matrix for net worth (values between 0 and 1)
net_worth_matrix = [
    #columns are things related to net worth -> assets, job, income, investment
    [0.8, 0.6, 0.7], #Persona A
    [0.5, 0.7, 0.4], #Person B
    [0.3, 0.4, 0.9], #Person C
    [0.6, 0.3, 0.2], #Person D
    [0.4, 0.5, 0.7]  #Person E
]

# Decision matrix for relationship (values between 0 and 1)
relationship_matrix = [
    [0.8, 0.2, 0.3],
    [0.5, 0.7, 0.4],
    [0.3, 0.4, 0.9],
    [0.6, 0.3, 0.2],
    [0.4, 0.5, 0.7]
]

# Decision matrix for character traits (values between 0 and 1)
character_trait_matrix = [
    [0.7, 0.4, 0.2],
    [0.5, 0.6, 0.3],
    [0.8, 0.2, 0.5],
    [0.4, 0.6, 0.4],
    [0.3, 0.4, 0.7]
]

# Calculate weighted scores for each person
net_worth_scores = calculate_weighted_decision_matrix(net_worth_matrix, [net_worth_weight] * len(net_worth_matrix[0]))
relationship_scores = calculate_weighted_decision_matrix(relationship_matrix, [relationship_weight] * len(relationship_matrix[0]))
character_trait_scores = calculate_weighted_decision_matrix(character_trait_matrix, [character_trait_weight] * len(character_trait_matrix[0]))

# Calculate total scores by summing up the weighted scores
total_scores = [sum(scores) for scores in zip(net_worth_scores, relationship_scores, character_trait_scores)]

# Find the person with the highest total score
person_with_highest_motive = persons[total_scores.index(max(total_scores))]

# Print the results
print("Person with the highest motive:", person_with_highest_motive)
