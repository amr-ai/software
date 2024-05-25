from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def calculate_price(self) -> float:
        pass

    @abstractmethod
    def get_quantity(self) -> int:
        pass


class StandardTicket(Ticket):
    def __init__(self, quantity: int):
        self.quantity = quantity

    def calculate_price(self) -> float:
        return 50 * self.quantity

    def get_quantity(self) -> int:
        return self.quantity


class VIPTicket(Ticket):
    def __init__(self, quantity: int):
        self.quantity = quantity

    def calculate_price(self) -> float:
        return 100 * self.quantity

    def get_quantity(self) -> int:
        return self.quantity


class EconomyTicket(Ticket):
    def __init__(self, quantity: int):
        self.quantity = quantity

    def calculate_price(self) -> float:
        return 20 * self.quantity

    def get_quantity(self) -> int:
        return self.quantity


class TicketReservation:
    def __init__(self, ticket_provider):
        self.ticket_provider = ticket_provider
        self.tickets = []
        self.status = "pending"

    def add_ticket(self, quantity: int) -> None:
        ticket = self.ticket_provider.get_ticket(quantity)
        self.tickets.append(ticket)

    def total_price(self) -> float:
        total = 0
        for ticket in self.tickets:
            total += ticket.calculate_price()
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


class TicketProvider(ABC):
    @abstractmethod
    def get_ticket(self, quantity: int) -> Ticket:
        pass


class StandardTicketProvider(TicketProvider):
    def get_ticket(self, quantity: int) -> Ticket:
        return StandardTicket(quantity)


class VIPTicketProvider(TicketProvider):
    def get_ticket(self, quantity: int) -> Ticket:
        return VIPTicket(quantity)


class EconomyTicketProvider(TicketProvider):
    def get_ticket(self, quantity: int) -> Ticket:
        return EconomyTicket(quantity)


reservation = TicketReservation(StandardTicketProvider())

ticket_type = input("What type of ticket do you want? (Standard/VIP/Economy): ").capitalize()
quantity = int(input("How many tickets do you want? "))
payment_type = input("Enter payment type (debit/credit): ")

if ticket_type == "Standard":
    reservation.ticket_provider = StandardTicketProvider()
elif ticket_type == "VIP":
    reservation.ticket_provider = VIPTicketProvider()
elif ticket_type == "Economy":
    reservation.ticket_provider = EconomyTicketProvider()
else:
    raise ValueError("Invalid ticket type")

reservation.add_ticket(quantity)
print("Ticket added successfully!")

print(f"Total price: ${reservation.total_price()}")

reservation.confirm_reservation(payment_type)
