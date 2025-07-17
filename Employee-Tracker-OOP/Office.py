from Employee import Employee
class Office:
    """
    Represents an office that manages employees.
    """
    name = ''
    employees = []
   
    def __init__(self,name,employees):
        """
        Initialize the office with a name and a list of employee data dictionaries.
        """
        self.name = name
        for emp_data in employees:
            emp = Employee(name=emp_data["name"],
            money=emp_data["money"],
            mood=emp_data["mood"],
            health_rate=emp_data["health_rate"],
            id=emp_data["id"],
            car=emp_data["car"],
            email=emp_data["email"],
            salary=emp_data["salary"],
            distanceToWork=emp_data["distanceToWork"]
            
        )
            
        self.employees.append(emp)
    
    
            
    def get_all_employees(self):
        """
        Return a list of employee names.
        """
        names = []
        for emp in self.employees:
          names.append(emp.name) 
        return names  


    def get_employee(self,empId):
        """
        Return details of a specific employee by ID.
        """
        for emp in self.employees:
            if emp.id == empId:
                 return f"Employee {emp.name} found with ID {empId}"
            
        return f"No employee found with ID {empId}"
        
        
    def hire(self,emp_data): # automatic id based on last id in dic
        """
        Hire a new employee from a dictionary of data.
        """
        emp = Employee(
            id=emp_data["id"],
            name=emp_data["name"],
            salary=emp_data["salary"],
            email=emp_data["email"],
            mood=emp_data["mood"],
            money=emp_data["money"],
            health_rate=emp_data["health_rate"],
            car=emp_data["car"],
            distanceToWork=emp_data["distanceToWork"]
        )
        self.employees.append(emp)
        return f"Added {emp.name} with ID {emp.id}"

    

        
    def fire(self,empId):
        """
        Remove an employee from the list by ID.
        """
        for emp in self.employees:
            if emp.id == empId:
                self.employees.remove(emp)
                return f"Employee with ID {empId} has been deleted."
                
        return f"No employee found with ID {empId}."


    @staticmethod
    def calculate_lateness(self,targetHour , moveHour, distance, velocity):
        """
        Check if arrival time is late based on movement hour, distance, and car velocity.
        """
        way_time = distance / velocity  
        arrive_hour = moveHour + way_time
        if arrive_hour <= targetHour:
            return 'Not late'
        else:
            return 'late'
                
    def check_lateness(self,empId, moveHour):
        """
        Check lateness of an employee and adjust salary accordingly.
        """
        for emp in self.employees:
            if emp.id == empId:
                if (Office.calculate_lateness(self,9, moveHour, emp.distanceToWork, emp.car['velocity'])) == 'Not late':
                    emp.salary += 10
                    return f'salary increased now <<< {emp.salary}'
                else:
                    emp.salary -= 10
                    return f'salary decreased now <<< {emp.salary}'
        
    def deduct(self,empId, deduction):
        """
        Deduct amount from employee salary.
        """
        for emp in self.employees:
                if emp.id == empId:
                    emp.salary -= deduction
                    return f'Sorry , you have a deduction {deduction} your salary now is {emp.salary}'
                    
    def reward(self,empId, reward):
        """
        Add reward to employee salary.
        """
        for emp in self.employees:
            if emp.id == empId:
                emp.salary += reward
                return f'Congrats , you have a reward {reward} your salary now is {emp.salary}'
                
    
    
