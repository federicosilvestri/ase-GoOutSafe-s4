from .table import Table

class Reservation:

    def __init__(self, user, table, timestamp, start_time, active = True, end_time = None):
        self.user = user
        self.table = table
        self.timestamp = timestamp
        self.start_time = start_time
        #Automatically end_time will be set as start_time + 3 hours
        self.end_time =  start_time + 10800


    def setActive(self, active):
        self.active = active

    def isActive(self):
        return self.active


    