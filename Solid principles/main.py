class TicketReservation:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "pending"

    def add_ticket(self, ticket_type: str, quantity: int, price: float) -> None:
        self.items.append(ticket_type)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for quantity, price in zip(self.quantities, self.prices):
            total += quantity * price
        return total

    def confirm_reservation(self, payment_type: str):
        if payment_type == "debit":
            print("Processing debit payment type")
            self.status = "confirmed"
        elif payment_type == "credit":
            print("Processing credit payment type")
            self.status = "confirmed"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")

reservation = TicketReservation()

ticket_type = input("What type of ticket do you want? (Standard/VIP/Economy): ").capitalize()
quantity = int(input("How many tickets do you want? "))
payment_type = input("Enter payment type (debit/credit): ")

if ticket_type == "Standard":
    price = 50
elif ticket_type == "Vip":
    price = 100
elif ticket_type == "Economy":
    price = 20
else:
    raise ValueError("Invalid ticket type")

reservation.add_ticket(ticket_type, quantity, price)
print("Ticket added successfully!")

print(f"Total price: ${reservation.total_price()}")

reservation.confirm_reservation(payment_type)
