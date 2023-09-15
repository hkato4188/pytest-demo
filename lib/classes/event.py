class Event:

    all = []

    def __init__(self, capacity, location):
        self.capacity = capacity 
        self.location = location
        Event.all.append(self)

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    
    def capacity(self, capacity):
        if type(capacity) is int and not hasattr(self, "capacity"):
            self._capacity = capacity
        else: 
            raise Exception("Capacity has to be an integer.")

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location)>0 and not hasattr(self, "location"):
            self._location = location
        else:
            raise Exception("Location must be a string, greater than 0 characters long, and cannot be re-assigned.")

    
    def registrations(self):
        return [registration for registration in Registration.all if registration.event == self]

    
    def skiers(self):
        return list(set([registration.skier for registration in Registration.all if registration.event == self]))
    
    def num_skiers(self):
        return len(self.skiers())
    
    def riding_teams(self):
        return [registration.riding_team for registration in Registration.all if registration.event == self]

   
    def add_results(self, result):
        pass


    def get_results(self):
        pass



from classes.registration import Registration
