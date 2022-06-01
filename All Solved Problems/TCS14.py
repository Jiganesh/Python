from collections import Counter
import calendar

def usingcalendar(datetuple ):
    
    year, month, day = datetuple
    leap_year = True if year%400==0 or (year%100!=0 and year%4==0) else False
    if leap_year : month = 2
    print(calendar.month(year, month))
    
    
    cal_obj = calendar.Calendar()
    last_7_dates = list(cal_obj.itermonthdates(year, month))[-7:]
    print(last_7_dates)
    
    cal_day =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    count = Counter(d.strftime('%A') for d in cal_obj.itermonthdates(year, month) if d.month==month)
    days_of_week = {cal_day[calendar.weekday(year , month, i)] :i for i in range (1, 8)}

    
    def sorting_cal (x):
        return -count[x], days_of_week[x]
    
    cal_day.sort(key=sorting_cal)
    print(cal_day[0])
    

# DONT WRITE BELOW THIS I WAS TESTING CODE 
usingcalendar((2020,10,11))
usingcalendar((2050, 1, 1))