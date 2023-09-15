class RidingTeam:

    all = []

    def __init__(self,horse_name, rider_name):
        self.horse_name = horse_name
        self.rider_name = rider_name
        RidingTeam.all.append(self)
    

    @property
    def horse_name(self):
        return self._horse_name

    @horse_name.setter
    def horse_name(self, horse_name):
        if type(horse_name) == str:
            if 1 <= len(horse_name) <= 15:
                self._horse_name = horse_name
            else:
                raise Exception('Name must be more than 0 characters long.')
        else:
            raise Exception('Name must be a string.')
        

    @property
    def rider_name(self):
        return self._rider_name
    
    @rider_name.setter
    def rider_name(self, rider_name):
        if type(rider_name) is str:
            if 1 <= len(rider_name) <= 15 :
                self._rider_name = rider_name
            else:
                raise ValueError('Name must be more than 0 characters long.')
        else:
            raise TypeError('Name must be a string.')
        

    def registrations(self):
        return [registration for registration in Registration.all if registration.riding_team is self]
    
    def create_registration(self, skier, event):
        return Registration(
            riding_team = self,
            skier = skier,
            event = event
        )
   
   
    def events(self):
        return [registration.event for registration in self.registrations()]

    
    def average_speed(self):
        pass
    
    
    
        



from classes.registration import Registration
