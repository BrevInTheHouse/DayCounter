start_date1 = input("What is today's date? (dd/mm/yyyy) ")
end_date1 = input("What is the end date? (dd/mm/yyyy) ")

incl_last_day = input("Do you want to include the final day? (y/n) ")
if incl_last_day.lower() == "y":
    last_day_count = 1
else:
    last_day_count = 0

start_date = start_date1.split("/")
end_date = end_date1.split("/")

start_day = int(start_date[0])
start_month = int(start_date[1])
start_year = int(start_date[2])

end_day = int(end_date[0])
end_month = int(end_date[1])
end_year = int(end_date[2])

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (start_year > end_year) or (start_year == end_year and start_month > end_month) or (start_year == end_year and start_month == end_month and start_day > end_day): # check if the date is in the past
    print("Date has already passed")
    
elif start_year == end_year and start_month == end_month and start_day == end_day: # check if the date is today
    print(end_date1 + " is today")
    
else:
    if (start_month < end_month) or (start_month <= end_month and start_day <= end_day):
        years = end_year - start_year
    else:
        years = end_year - start_year - 1
    
    leap_days = years // 4
    if (start_month <= 2 and end_month >= 3 and start_year % 4 == 0) or (start_month <= 2 and start_year % 4 == 0 and end_year > start_year):
        leap_days += 1
    
    year_in_days = (years * 365) + leap_days
    
    if start_month == end_month and start_day <= end_day: # same month
        months = 0
    elif start_month < end_month: # different month same year
        if start_day <= end_day:
            months = end_month - start_month
        else:
            months = end_month - start_month -1
    else: # crossing year
        if start_day < end_day:
            months = 12 - start_month + end_month
        else:
            months = 12 - start_month + end_month - 1
    
    if months == 0:
        month_in_days = 0
    else:
        m = start_month
        month_in_days = 0
        for i in range(start_month, (months + start_month)):
            month_in_days += month_days[m-1]
            m += 1
            if m == 12:
                m = 1
    
    if start_day == end_day:
        days = 0
    
    elif start_day < end_day:
        days = end_day - start_day
    
    else:
        days = month_days[end_month - 2] + end_day - start_day + last_day_count
    
    
    total_days = year_in_days + month_in_days + days
        
    print(end_date1, "is in", years, "years,", months, "months and", days, "days (" + str(total_days) + " days)")