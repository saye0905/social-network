class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
    
    pass # Delete this line to implement the Person class


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both people don't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friends_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friends_names)}")
    
    pass # Delete this line to implement the SocialNetwork class
network = SocialNetwork()

# Add people
for name in ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"]:
    network.add_person(name)

# Add friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")  # Edge case
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Print network
network.print_network()


# """
#Design Memo – Social Network Graph

#A graph is the ideal data structure for modeling a social network because relationships are dynamic and bidirectional. Each person is a node, and each friendship is an edge connecting two nodes. This structure allows efficient traversal, querying, and updates as friendships form or dissolve.

#Lists or trees would not work as well. Lists are linear and don’t capture the complexity of mutual relationships. Trees enforce hierarchical structure, which doesn’t reflect the peer-to-peer nature of friendships. Graphs, especially adjacency lists, allow us to store each person and their connections flexibly.

#While building this system, I noticed that adding friends is efficient using adjacency lists, but printing the network requires iterating through each person and their friends. This trade-off is acceptable because social networks prioritize fast updates and flexible connections over sorted or hierarchical data.

#This assignment helped me understand how abstract data structures like graphs can power real-world applications. It also reinforced the importance of choosing the right structure based on the problem’s nature. I’m excited to explore backend development next, where these principles will extend to databases and APIs.
