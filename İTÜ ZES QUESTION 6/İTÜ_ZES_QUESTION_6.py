#Codes
import random

class Person:        
                                            
    def __init__(self,name = "Not Specified.",surname = "Not Specified."):
        
        self.name = name
        self.surname = surname
    
    def print_name(self):
        print(self.name)
        
    def print_surname(self):
        print(self.surname)

    def enter_name(self,name = "Not Specified."):
        self.name = name
    def enter_surname(self,surname = "Not Specified."):
        self.surname = surname
        
    def __str__(self):
        return "Name:{}  Surname:{}".format(self.name,self.surname)


class Passenger(Person):    
    
    def __init__(self,name = "Not Specified.",surname = "Not Specified.",cash = 0, ticket = False):
        
        super().__init__(name,surname)    
        self.cash = max(0,cash)
        self.ticket = ticket
    
    def buyTicket(self,ticket_price):
        
        if not self.ticket:       
            if self.cash >= ticket_price:
                new_cash = self.cash - ticket_price
                self.cash = new_cash
                self.ticket = True
                print(f"{self.name} bought a ticket and {self.name}'s cash is {new_cash} left.")
            else:
                print(f"{self.name} does not have enough cash to buy a ticket. {self.name} can buy a ticket after earn more money.")
        else:
            print(f"{self.name} has already ticket.")
    
    def how_many_cash(self):
        print(self.cash)

    def has_ticket(self):
        return self.ticket
    

class Astronaut(Person):
    
    def __init__(self,name = "Not Specified.",surname = "Not Specified.",numMissions = 0):
        
        super().__init__(name,surname)
        self.numMissions = numMissions
     
    def complete_mission(self):
        self.numMissions += 1
        print(f"{self.name} completed another mission and the number of missions are {self.numMissions}")



class Mission:
    
    numMissions = 0
    
    def __init__(self,name = "Not Specified.",missionNumber = 0 ,cost = 0 ,faultProbability = 0 ,completed = False):
        
        if len(name) == 5 and name[0].isalpha() and name[1].isalpha() and name[2] == '-' and name[3].isdigit() and name[4].isdigit():
            pass
        else:
            print("Invalid mission name. Please, use default name. For instance: 'AA-00'.")
            name = "it is invalid name."
        
        if faultProbability > 100:
            print("it is invalid probability.")
            faultProbability = "Enter probability again."
        else:
            pass
        
        self.name = name
        self.missionNumber = Mission.numMissions + 1
        Mission.numMissions += 1        
        self.cost = cost
        self.faultProbability = faultProbability
        self.completed = completed
        self.passengers = []
        self.crew = []
        
    def addSpaceShipStaff(self,staff):
        
        if isinstance(staff, Passenger):
            
            if staff.has_ticket():
                self.passengers.append(staff)
            else:
                print(f"Passenger {staff.name} does not have a ticket. Cannot add to the mission.")
                
        elif isinstance(staff, Astronaut):
            self.crew.append(staff)
            
    def execute_mission(self):
        random_number = random.randint(0, 100)
        
        if random_number > self.faultProbability:
            self.completed = True
            for astronaut in self.crew:
                astronaut.complete_mission()
            print("Mission successful.")
            for astronaut in self.crew:
                print(f"{astronaut.name} has completed {astronaut.numMissions} missions.")
        else:
            self.completed = False
            print("Mission failed.")
                    
    def iscompleted(self):
        return self.completed
    
    def calculate_profit(self, ticket_price):
        if self.completed:
            profit = len(self.passengers) * ticket_price - self.cost
            print(f"The profit of Company is {profit}.") 
            return profit
        else:
            profit = -self.cost
            print(f"The profit of Company is {profit}.")  
            return profit
        
    def get_mission_number(self):
        return self.missionNumber   
    
    def show_crew_passengers(self):
        print("\nCrew:")
        for i in self.crew:            
            print(i)
            
        print("\nPassengers:")
        for j in self.passengers:            
            print(j)            
      
        
class Agency:
    
    def __init__(self,name = "Not Specified.",cash = 0,ticketPrice = 0):
        self.name = name
        self.cash = cash
        self.ticketPrice = ticketPrice
        self.completedMissions = []
        self.nextMissions = []

    def add_mission(self, mission):
        self.nextMissions.append(mission)

    def execute_next_mission(self,mission):
        
        if not self.nextMissions:
            print("No missions available to execute.")
        else:
            mission = self.nextMissions.pop(0)
            mission_result = mission.iscompleted()

        if mission_result:
            self.completedMissions.append(mission)
            self.cash += mission.calculate_profit(self.ticketPrice)
        else:            
            self.cash += mission.calculate_profit(self.ticketPrice)
        
    def agency_info(self):
        print(f"Agency Name: {self.name}")
        print(f"Current Cash: {self.cash}")
        print(f"Ticket Price: {self.ticketPrice}")
        print("\nNext Missions:")
        for mission in self.nextMissions:                                          
            print(f"Mission {mission.get_mission_number()}: {mission.name}, Cost: {mission.cost}")           
        print("\nCompleted Missions:")
        for mission in self.completedMissions:
            print(f"Mission {mission.get_mission_number()}: {mission.name}, Cost: {mission.cost}")
           
            
#Examples
person1 = Person()
person1.enter_name("Yekta")
person1.enter_surname("Doganay")
person1.print_name()
person1.print_surname()
print(person1)

passenger1 = Passenger("Yekta","Doganay",1000)
passenger1.buyTicket(500)
passenger1.how_many_cash()
print(passenger1.has_ticket())
passenger2 = Passenger("Yusuf","Doganay",600)
passenger2.buyTicket(500)
print(passenger2.has_ticket())
passenger3 = Passenger("Aysegul","Doganay",400)
passenger3.buyTicket(500)
print(passenger3.has_ticket())

astronaut1 = Astronaut("Yekta","Doganay",2)
astronaut1.complete_mission()

missions1 = Mission("AB-21",cost=250,faultProbability=50)
missions1.addSpaceShipStaff(astronaut1)
missions1.addSpaceShipStaff(passenger1)
missions1.addSpaceShipStaff(passenger2)

missions1.execute_mission()
missions1.calculate_profit(500)
missions1.show_crew_passengers()
print("\n")

missions2 = Mission("YD-34", cost=250, faultProbability=50)
missions2.execute_mission()
missions2.addSpaceShipStaff(astronaut1)
missions2.addSpaceShipStaff(passenger1)
missions2.addSpaceShipStaff(passenger2)
missions3 = Mission("AD-03", cost=250, faultProbability=50)
missions3.execute_mission()
missions3.addSpaceShipStaff(astronaut1)
missions3.addSpaceShipStaff(passenger1)
missions3.addSpaceShipStaff(passenger2)

print("\n")
agency1 = Agency("NASA",12000,500)
agency1.add_mission(missions2)
agency1.add_mission(missions3)
agency1.agency_info()
print("\n")
agency1.execute_next_mission(missions2)
agency1.execute_next_mission(missions3)
print("\n")
agency1.agency_info()