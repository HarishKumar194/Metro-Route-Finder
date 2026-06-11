from metro_graph import MetroGraph

def create_metro():
    metro = MetroGraph()

    metro.add_edge("Central", "Egmore", 5)
    metro.add_edge("Egmore", "Nungambakkam", 4)
    metro.add_edge("Nungambakkam", "Kodambakkam", 3)
    metro.add_edge("Kodambakkam", "Guindy", 6)
    metro.add_edge("Guindy", "Airport", 8)
    metro.add_edge("Egmore", "Park Town", 2)
    metro.add_edge("Park Town", "Guindy", 10)

    return metro
