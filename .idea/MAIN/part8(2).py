class WeightedDecisionMatrix:
    def __init__(self):
        self.data = []

    def add_person(self, net_worth, character_trait, relationship):
        self.data.append([net_worth, character_trait, relationship])

    def get_person_scores(self):
        return [sum(row) for row in self.data]


def determine_highest_motive(matrix):
    scores = matrix.get_person_scores()
    highest_motive_index = scores.index(max(scores))
    return highest_motive_index


# Create a weighted decision matrix
decision_matrix = WeightedDecisionMatrix()

# Add persons with their scores for each criterion
decision_matrix.add_person(0.8, 0.7, 0.8)
decision_matrix.add_person(0.6, 0.6, 0.5)
decision_matrix.add_person(0.9, 0.4, 0.3)
decision_matrix.add_person(0.7, 0.5, 0.6)
decision_matrix.add_person(0.6, 0.8, 0.4)

# Determine the person with the highest motive
highest_motive_index = determine_highest_motive(decision_matrix)

# Print the person with the highest motive
persons = ["Person A", "Person B", "Person C", "Person D", "Person E"]
highest_motive_person = persons[highest_motive_index]
print("The person with the highest motive is:", highest_motive_person)
