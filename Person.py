class Person:
    """
    Represents a person with basic attributes like name, money, mood, and health rate.
    """
    name =''
    money =0
    mood=''
    health_rate = 0
    
    def __init__(self,name, money,mood,health_rate):
        """
        Initializes a Person instance.

        Args:
            name (str): The name of the person.
            money (float or int): The amount of money the person has.
            mood (str): The mood of the person.
            health_rate (int): The person's health rate (0 to 100).
        """
        self.name = name
        self.money= money
        self.mood = mood
        self.health_rate =health_rate
            
    def sleep(self,hours):
        """ 
        Determines mood based on number of hours slept.

        Args:
            hours (int): Number of sleeping hours.

        Returns:
            str: Mood status ('tired', 'happy', or 'lazy').
        """
        if hours < 7 :
            return 'tired'
        elif hours == 7 :
            return 'happy' 
        else : 
            return 'Lazy'
        
    def eat(self,meals):
        """
        Determines health level based on number of meals eaten.

        Args:
            meals (int): Number of meals the employee ate today.

        Returns:
            str: Health percentage as a string.
        """
        if meals == 3 :
                return '100% hth'
        elif meals == 2 :
                return '75% hth' 
        elif meals == 1 :
                return '50% hth'

    def buy(self,items):
        """
        Deducts money based on the number of items bought.

        Args:
            items (list): A list of items to be purchased.

        Returns:
            str: Summary of the purchase and remaining balance.
        """
        self.money -= len(items)
        return f'you buy {items} , your remain balance is {self.money}'
            