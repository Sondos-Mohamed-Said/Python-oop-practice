from Person import Person
from Car import Car
from Office import Office
from Employee import Employee

# implement Person
 
p1 = Person('Ahmed',50,'Happy',7) #name, money,mood,health_rate
print(p1.money)
print(p1.eat(2))
print(p1.sleep(20)) 
print(p1.buy(['Mango','Milk']))


#**************************************************

# implement Car

Sondos_car = Car('fiat 128',70,50) #velocity,fuelRate
print(Sondos_car.name)
print(Sondos_car.velocity) #70
print(Sondos_car.fuelRate) #50
print(Sondos_car.run(80,200))
#print(Sondos_car.run(80,500)) # refuel
print(Sondos_car.stop()) 

#**************************************************

# implement Employee

Sondos_car =Car('BMW',50,50)
Sondos = Employee('Sondos',2000,'happy',5,3,Sondos_car,'Sondos@gmail.com',5000,20)
print(Employee.employeesNum) #2
print(Employee.change_emps_num(100))
print(Employee.employeesNum) #102
print(Sondos.work(5))
Sondos.drive(50)           #fuelRate -= 0.1 * distance 
print(Sondos_car.fuelRate) #45
Sondos.refuel() 
print(Sondos_car.fuelRate) # 145
print(Employee.employeesNum) #1

#**************************************************

# implement Office

employees = [
    {
        "id": 1,
        "name": "Omar",
        "money": 5000,
        "mood": "happy",
        "health_rate": 90,
        "email": "omar@example.com",
        "salary": 7000,
        "distanceToWork": 10,
        "car": {"name": "BMW", "fuel_rate": 70, "velocity": 120}
    },
    {
        "id": 2,
        "name": "Sara",
        "money": 4500,
        "mood": "tired",
        "health_rate": 85,
        "email": "sara@example.com",
        "salary": 6800,
        "distanceToWork": 15,
        "car": {"name": "Kia", "fuel_rate": 80, "velocity": 100}
    }
]


ITI = Office('ITI',employees)
print(ITI.get_all_employees()) #['Omar', 'Sara']
print(ITI.get_employee(2)) # Sara
Samy = {
        "id": 5,
        "name": "Samy",
        "money": 4500,
        "mood": "tired",
        "health_rate": 85,
        "email": "Samy@example.com",
        "salary": 6800,
        "distanceToWork": 20,
        "car": {"name": "Fiat 128", "fuel_rate": 50, "velocity": 100}
    }

ITI.hire(Samy)
print(Employee.employeesNum) 
print(ITI.get_all_employees())
print(Employee.employeesNum) #1
print(ITI.get_employee(5))
print(ITI.get_all_employees())
ITI.fire(2)                      # emp id == 2
print(ITI.get_all_employees())                                                  
print(ITI.check_lateness(5,8))                                  # check_lateness(empId, moveHour)
print(ITI.deduct(5,1000))
print(ITI.reward(5,1000)) 


