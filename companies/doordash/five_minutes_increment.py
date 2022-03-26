"""
# Ref: https://leetcode.com/discuss/interview-question/1387937/Doordash-new-Q

Input - ("mon 10:00 am", mon 11:00 am)
Output - [11005, 11010, 11015...11100]
Output starts with 1 if the day is monday, 2 if tuesday and so on till 7 for sunday
Append 5 min interval times to that till the end time
So here it is 10:05 as first case, so its written as 11005
2nd is 10:10 so its written as 11010
...
...
Stop at 11100

"""

class Time:
    
    def __init__(self, day, hour, minutes, am):
        this.day = day
        this.hour = hour
        this.minutes = minutes
        this.am = am
        
    def equals(self, time):
        if self.day == time.day and self.hour == time.hour and self.minutes == time.minutes and self.am == time.am:
            return True
        else:
            return False
    
    def add(self, minutes):
        if self.minutes + minutes >= 60:
            self.hour += 1
            self.minutes = (self.minutes + minutes) % 60
        
            if self.hour >= 13:
                am = not am
                self.hour = self.hour % 12
                
                if not am:
                    day += 1
        else:
            self.minutes += 5
    
    # mon 10:00 pm -> 110
    def get_numeric(self):
        return 
    
def convert(time_str):
    # time_str: mon 10:00 pm
    info = time_str.split(' ')
    week_of_day = info[0]
    time_info = info[1].split(":")
    hour = time_info[0]
    minutes = time_info[1]
    am = info[2] == 'am'
    return Time(day, hour, minutes, am)
    
    
def get_intervals(start, end):
    result = []
    
    start = convert(start)
    end = convert(end)
    
    while not start.equals(end):
        start.add(5)
        result.append(start)
    
    return result
