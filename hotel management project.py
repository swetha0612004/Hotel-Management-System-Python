#hotel management system with datatypes
# Dictionary (dict) - stores room details
# Key: room number (int)
# Value: another dictionary with type, price, status

rooms:dict={
    101: {"type":"single","price":"1000","status":"avaliablity"},
    102: {"type":"double","price":"3000","status":"availabilty"},
    103: {"type":"twin room","price":"4000","status":"availabilty"},
    104: {"type":"deluxe","price":"3000","status":"availabilty"}
}

# Dictionary to store customers
# Key: phone number (str)
# Value: another dict (customer name and booked room)
customers: dict = {
    "9876543210": {"name": "Swetha", "room": None}
}



#function to show available room
def show_rooms() -> None:
    print("\n--- Available Rooms ---")
for num,info in rooms.items():  # num: int, info: dict
       if info["status"]=="available":
             print(f"Room {num} - {info['type']} - ₹{info['price']}/night")
print()

   # Function to add a new customer
def add_customer() -> None:
    name: str = input("Enter customer name: ")
    phone: str = input("Enter phone number: ")
    customers[phone] = {"name": name, "room": None}
    print(" Customer added!\n")

 # Function to book a room
def book_room() -> None:
    phone: str = input("Enter customer phone number: ")
    if phone not in customers:
        print(" Customer not found! Add customer first.\n")
        return
show_rooms()
room_no: int = int(input("Enter room number to book: "))

if room_no in rooms and rooms[room_no]["status"] == "available":
        rooms[room_no]["status"] = "booked"        # str
        customers[phone]["room"] = room_no         # int
        print(f"Room {room_no} booked for {customers[phone]['name']}!\n")
else:
        print(" Room  available!\n")


        

# Function to check out
def check_out() -> None:
    phone: str = input("Enter customer phone number: ")

    if phone in customers and customers[phone]["room"]:
        room_no: int = customers[phone]["room"]
        rooms[room_no]["status"] = "available"
        customers[phone]["room"] = None
        print(f" {customers[phone]['name']} checked out! Room {room_no} is now available.\n")
    else:
        print(" No active booking for this customer.\n")

# Main menu (loop)
def main() -> None:
    while True:
        print("=== HOTEL MANAGEMENT SYSTEM ===")
        print("1. Show Available Rooms")
        print("2. Add Customer")
        print("3. Book Room")
        print("4. Check Out")
        print("5. Exit")

        choice: str = input("Enter choice: ")  # str

        if choice == '1':
            show_rooms()
        elif choice == '2':
            add_customer()
        elif choice == '3':
            book_room()
        elif choice == '4':
            check_out()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print(" Invalid choice!\n")

# Run the program
if __name__ == "__main__":
    main()



          