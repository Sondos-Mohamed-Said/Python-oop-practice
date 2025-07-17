from Person import Person

class Employee(Person):
    
    """
    Represents an employee with personal and work-related details.
    Inherits from the Person class.
    """
    id = 0
    car = ''
    email = ''
    salary = 0
    distanceToWork = 0
    employeesNum = 0 # Class variable to count number of employees
    
    def __init__(self,name,money, mood, health_rate
                 ,id,car,email,salary,distanceToWork):
        """
        Initialize an Employee instance.

        Args:
            name (str): Employee's name.
            money (float): Available money.
            mood (str): Current mood.
            health_rate (int): Health rate (0 to 100).
            emp_id (int): Employee ID.
            car (Car): Car object with velocity and fuelRate.
            email (str): Work email address.
            salary (float): Salary amount.
            distance_to_work (float): Distance from home to work in km.
        """
        super(Employee,self).__init__(name,money, mood, health_rate)
        self.id = id
        self.car = car #def __init__(self,name, velocity,fuelRate):
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        Employee.employeesNum += 1

       
        
    def work(self,hours):
        """
        Determines mood based on working hours.

        Args:
            hours (int): Number of working hours.

        Returns:
            str: Work mood ('lazy', 'happy', or 'tired').
        """
        if hours < 8 :
            return 'Lazy'
        elif hours == 8 :
            return 'happy' 
        else :
            return 'tired'
        
    
    def drive(self,distance):
            
        """
        Uses the car to drive a certain distance.

        Args:
            distance (float): Distance to drive.
        """
        self.car.run(self.car.velocity,distance) 
             
        
    
    def refuel(self,gasAmount = 100):
        """
        Refuels the employee's car.

        Args:
            gas_amount (float): Amount of fuel to add. Default is 100.

        Returns:
            float: Updated fuel rate.
        """  
        self.car.fuelRate += gasAmount 
        return self.car.fuelRate
    
    def send_mail():
            pass
        
    @classmethod
    def change_emps_num(cls, num):
        """classmethod which modify the number of Employees in all offices.
        """
        cls.employeesNum += num 