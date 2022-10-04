class Parkinggarage():

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        # Prevents someone from taking a ticket if spaces are full.
        if len(self.tickets) == 0:
            print("Sorry, there are no available parking spaces.")
        # Pops number from the ticket list and assigns it to the available space, then shows status of all current tickets.
        else:
            availableSpace = self.tickets.pop(0)
            print(f"Please go to your assigned space- #{availableSpace}.")
            print(self.currentTicket)
        # Adds ticket occupied spaces list and sets value to "unpaid"
        self.parkingSpaces.append(availableSpace)
        self.currentTicket[availableSpace] = "unpaid"
    
    def payforParking(self):
        availableSpace = int(input("Please enter the number of your assigned space. "))
        # Does not allow user to pay if there are no spots to pay for.
        if len(self.parkingSpaces) == 0:
            print("There are no occupied parking spaces.")
            return
        # Prevents code from crashing if user enters wrong data.
        if availableSpace not in self.parkingSpaces:
            print("Invalid entry")
            return
        # Prevents user from having to pay twice.
        if self.currentTicket[availableSpace] == "paid":
            print("This ticket has been paid already.")
        # Allows user to "pay" for parking.
        else:
            print("Please pay before leaving the garage.")
            haspaid = input("Please type 'y' to pay.")

            # If user "pays", sets value of ticket to "paid", so that they may leave garage.
            if haspaid.lower() == "y":
                self.currentTicket[availableSpace] = "paid"
                print(f'Your ticket has been {self.currentTicket[availableSpace]}. Please leave within the next 15 minutes.')

    def leaveGarage(self):
        paidSpace = int(input("Please enter the number of your assigned space. "))
        # User cannot leave if they never entered.
        if len(self.parkingSpaces) == 0:
            print("There are no occupied parking spaces.")
            return
        # Prevents code from crashing if user enters wrong data.
        elif paidSpace not in self.parkingSpaces:
            print("Invalid entry. Please try again.")
        # Removes space from list of occupied spaces, adds it back to ticket numbers 
        # list, sorts ticket list back to numerical order, then deletes ticket from 
        # currentTicket dictionary. 
        elif self.currentTicket[paidSpace] == "paid":
            self.parkingSpaces.remove(paidSpace)
            self.tickets.append(paidSpace)
            self.tickets.sort()
            del self.currentTicket[paidSpace]
            print("Thank you for your business. Have a great day!")
        # Redirects user to payment method.
        else:
            print("Your ticket has not been paid. Please pay now.")
            self.payforParking()

# Setting the size of garage we want
desired_size = [1,2,3,4,5,6,7,8,9]
# Making an instance of our class and feeding it the list of tickets, 
# an empty list for spaces, and an empty dictionary for current ticket.
groovygarage= Parkinggarage(desired_size,[],{})

# A function to run all the methods in a cohesive program.
def run():
    while True:
        do = input("Welcome to Groovy Garage! What would you like to do? Park/Pay/Leave/Quit: ")
        if do.lower() == "quit":
            print("Have a great day!")
            break
        elif do.lower() == "park":
            groovygarage.takeTicket()
        elif do.lower() == "pay":
            groovygarage.payforParking()
        elif do.lower() == "leave":
            groovygarage.leaveGarage()
        else:
            print("Invalid entry. Please try again.")

run()