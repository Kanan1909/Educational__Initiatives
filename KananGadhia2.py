# ------------------ OBSERVER PATTERN ------------------

# Observer interface
class Observer:
    def update(self, is_occupied):
        pass

# AC observer class
class AC(Observer):
    def update(self, is_occupied):
        if is_occupied:
            print("AC turned on.")
        else:
            print("AC turned off.")

# Lights observer class
class Lights(Observer):
    def update(self, is_occupied):
        if is_occupied:
            print("Lights turned on.")
        else:
            print("Lights turned off.")

# Room class that manages observers (AC and Lights) and room status
class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.occupied = False
        self.max_capacity = 0
        self.observers = [AC(), Lights()]

    def set_max_capacity(self, max_capacity):
        if max_capacity > 0:
            self.max_capacity = max_capacity
            print(f"Room {self.room_number} maximum capacity set to {max_capacity}.")
        else:
            print("Invalid capacity. Please enter a valid positive number.")

    def get_room_number(self):
        return self.room_number

    def add_occupants(self, count):
        if count >= 2:
            self.occupied = True
            print(f"Room {self.room_number} is now occupied by {count} persons.")
        else:
            self.occupied = False
            print(f"Room {self.room_number} occupancy insufficient to mark as occupied.")
        self.notify_observers()

    def release_occupants(self):
        self.occupied = False
        print(f"Room {self.room_number} is now unoccupied.")
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.occupied)

    def is_occupied(self):
        return self.occupied


# ------------------ SINGLETON PATTERN ------------------

# Singleton class for managing office configuration and global state
class OfficeManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OfficeManager, cls).__new__(cls)
            cls._instance.rooms = []
        return cls._instance

    def configure_rooms(self, count):
        for i in range(1, count + 1):
            self.rooms.append(Room(i))
        print(f"Office configured with {count} meeting rooms.")

    def get_room(self, room_number):
        if 0 < room_number <= len(self.rooms):
            return self.rooms[room_number - 1]
        else:
            print("Invalid room number.")
            return None


# ------------------ COMMAND PATTERN ------------------

# Command interface
class Command:
    def execute(self):
        pass

# Command for booking a room
class BookRoomCommand(Command):
    def __init__(self, room, start_time, duration):
        self.room = room
        self.start_time = start_time
        self.duration = duration

    def execute(self):
        if not self.room.is_occupied():
            print(f"Room {self.room.get_room_number()} booked from {self.start_time} for {self.duration} minutes.")
            self.room.add_occupants(2)  # Assuming 2 persons to make it occupied
        else:
            print(f"Room {self.room.get_room_number()} is already booked.")

# Command for canceling a room booking
class CancelBookingCommand(Command):
    def __init__(self, room):
        self.room = room

    def execute(self):
        if self.room.is_occupied():
            self.room.release_occupants()
            print(f"Booking for Room {self.room.get_room_number()} cancelled successfully.")
        else:
            print(f"Room {self.room.get_room_number()} is not booked.")


# ------------------ MAIN CLASS ------------------

if __name__ == "__main__":
    office_manager = OfficeManager()

    # Configuring rooms
    office_manager.configure_rooms(3)

    room1 = office_manager.get_room(1)
    room2 = office_manager.get_room(2)

    # Setting room capacities
    room1.set_max_capacity(10)
    room2.set_max_capacity(8)

    # Booking room 1
    book_room1 = BookRoomCommand(room1, "09:00", 60)
    book_room1.execute()

    # Cancel booking for room 1
    cancel_room1 = CancelBookingCommand(room1)
    cancel_room1.execute()

    # Trying to book room 1 again
    book_room1.execute()

    # Invalid cases
    book_room2 = BookRoomCommand(room2, "09:00", 60)
    cancel_room2 = CancelBookingCommand(room2)
    cancel_room2.execute()

    # Test occupancy changes
    room1.add_occupants(0)  # Occupancy less than 2, should not mark as occupied
    room1.add_occupants(3)  # Occupancy of 3, should mark as occupied
