class Car:
    name =''
    fuelRate = 0
    velocity = 0

    def __init__(self,name, velocity,fuelRate):
        self.name = name
        if (0 < velocity < 200) and (0 < fuelRate < 100) : # not self.velocity (it refer to 0 above)
            self.velocity = velocity
            self.fuelRate = fuelRate
        else:
            raise ValueError ('velocity must be between 0  200 , fuel_Rate must be between 0  100')
            
    def run(self,velocity,distance):    
        """
        Simulate running the car for a certain distance with given velocity.
        Updates fuel rate and velocity accordingly.
        """    
        self.distance = distance  # save object variable to can access it in any func
        self.fuelRate -= 0.1 * distance 
        self.velocity = velocity
        
        if Car.stop(self):   # what syntax else?
            if self.fuelRate <= 0:
               return f"There is no fuel ,refuel please "
            else:
             return f'you run {distance} m ,your remain fuel is {self.fuelRate}'   
        
    def stop(self):
        """
        Stop the car by setting velocity to 0 and reporting remaining distance.
        """
        self.velocity = 0
        if self.distance :
                print(f"remain distance is {self.distance}") 
                return True
        else:
                print("you arrive the destintation ")   
                return False
         
