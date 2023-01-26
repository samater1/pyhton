class Flight():
    def __init__(self, capacity):
        self.capacity=capacity
        self.pasengers= []
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.pasengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity-len(self.pasengers)
flight = Flight(3)
for person in range(10):
    person = input("name:")
    success = flight.add_passenger(person)
    if success:
        print(f"added {person} to the flight successfuly")
    else:
        print(f"no available seats {person}")
        break

print(flight.pasengers)
