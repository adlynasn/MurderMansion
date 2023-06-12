


#using weighted graph without library
class WeightedGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2, weight):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Nodes must be added to the graph before creating an edge.")
        self.edges[(node1, node2)] = weight

    def get_node_weighted_score(self, node):
        weighted_sum = 0
        for (node1, node2), weight in self.edges.items():
            if node1 == node:
                weighted_sum += weight
        return weighted_sum

def determine_motive_and_person(relationship_graph, character_traits_graph, net_worth_graph):
    motive_categories = ['Financial Gain', 'Revenge', 'Jealousy', 'Power', 'Ambition']
    potential_motives = {}
    
    # Analyze relationships
    for node in relationship_graph.nodes:
        score = relationship_graph.get_node_weighted_score(node)
        if score > 0.8:
            potential_motives[node] = potential_motives.get(node, []) + ['Revenge']
            
    # Analyze character traits
    for node in character_traits_graph.nodes:
        score = character_traits_graph.get_node_weighted_score(node)
        if score > 0.8:
            potential_motives[node] = potential_motives.get(node, []) + ['Power']

    # Analyze net worth and financial factors
    for node in net_worth_graph.nodes:
        score = net_worth_graph.get_node_weighted_score(node)
        if score > 0.5:
            potential_motives[node] = potential_motives.get(node, []) + ['Financial Gain']

    # Determine the most likely motive category
    motive_category_counts = {category: sum(category in categories for categories in potential_motives.values()) for category in motive_categories}
    most_likely_motive_category = max(motive_category_counts, key=motive_category_counts.get)
    
    # Determine the person with the highest motivation
    person_with_highest_motivation = max(potential_motives, key=lambda person: len(potential_motives[person]))

    return most_likely_motive_category, person_with_highest_motivation


# Example usage
relationship_graph = WeightedGraph()
character_traits_graph = WeightedGraph()
net_worth_graph = WeightedGraph()

relationship_graph.add_node("Jones")
relationship_graph.add_node("Jenna")
relationship_graph.add_node("Peter")
relationship_graph.add_node("Penelope")
relationship_graph.add_node("Will")
relationship_graph.add_node("Mr Marshall")

character_traits_graph.add_node("Jones")
character_traits_graph.add_node("Jenna")
character_traits_graph.add_node("Peter")
character_traits_graph.add_node("Penelope")
character_traits_graph.add_node("Will")
character_traits_graph.add_node("Murderer A")


net_worth_graph.add_node("Jones")
net_worth_graph.add_node("Peter")
net_worth_graph.add_node("Jenna")
net_worth_graph.add_node("Penelope")
net_worth_graph.add_node("Will")


#closer the higher the ratio
relationship_graph.add_edge("Jones", "Mr Marshall", 0.7)
relationship_graph.add_edge("Jenna", "Mr Marshall", 0.7)
relationship_graph.add_edge("Penelope", "Mr Marshall", 0.6)
relationship_graph.add_edge("Peter", "Mr Marshall", 0.6)
relationship_graph.add_edge("Will", "Mr Marshall", 0.3)

# Assign a higher weight to indicate higher resemblance/presence of that trait
#compare with a known murderer
character_traits_graph.add_edge("Jones", "Murderer A", 0.9)
character_traits_graph.add_edge("Jenna", "Murderer A", 0.5)
character_traits_graph.add_edge("Penelope", "Murderer A", 0.3)
character_traits_graph.add_edge("Peter", "Murderer A", 0.2)
character_traits_graph.add_edge("Will", "Murderer A", 0.7)


# Compare the networth
# higher 
net_worth_graph.add_edge("Jones", "Jenna", 1.43)
net_worth_graph.add_edge("Jones", "Peter", 20)
net_worth_graph.add_edge("Jones", "Penelope", 2)
net_worth_graph.add_edge("Jones", "Will", 100)
net_worth_graph.add_edge("Jenna", "Peter", 0.035)
net_worth_graph.add_edge("Jenna", "Penelope", 0.2857)
net_worth_graph.add_edge("Jenna", "Will", 7)
net_worth_graph.add_edge("Peter", "Penelope", 10)
net_worth_graph.add_edge("Peter", "Will", 250)
net_worth_graph.add_edge("Penelope", "Will", 50)

most_likely_motive_category, person_with_highest_motivation = determine_motive_and_person(relationship_graph, character_traits_graph, net_worth_graph)

print("The most likely motive category is:", most_likely_motive_category)
print("The person with the highest motivation is:", person_with_highest_motivation)




#running time complexity
# Adding nodes to the graph: O(1)
# Adding edges to the graph: O(1)
# Calculating the score for each node: O(n), where n is the number of edges
# Determining the node with the highest score: O(n), where n is the number of nodes
# Overall, the time complexity of this algorithm is O(n), where n is the number of edges or nodes, whichever is larger.