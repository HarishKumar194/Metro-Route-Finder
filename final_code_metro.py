from sample_data import create_metro

def main():
    metro = create_metro()

    print("\n🚇 Metro Route Finder (Dijkstra Algorithm)")
    print("----------------------------------------")

    start = input("Enter source station: ")
    end = input("Enter destination station: ")

    dist, parent = metro.dijkstra(start, end)
    path = metro.get_path(parent, start, end)

    if not path:
        print("\n❌ No route found!")
        return

    distance = dist[end]
    fare = metro.calculate_fare(distance)

    print("\n✅ SHORTEST ROUTE FOUND")
    print("------------------------")
    print("Route:", " -> ".join(path))
    print(f"Total Distance: {distance} km")
    print(f"Estimated Fare: ₹{fare}")

if __name__ == "__main__":
    main()
