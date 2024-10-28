'''
The python calendar module allows us to generate calendars. The functions and classes defined in the calendar module use an idealized calendar. By default, these calendars have Monday as the first day of the week and Sunday as the last (the European convention).
'''

import calendar

year = 2024

print("\nCalendars for the year", year)

for month in range(1, 13):
  print("\nCalendar for", calendar.month_name[month], year)
  
  print("-" * 20)
  
  print("Month:", calendar.month_name[month])
  print("Year:", year)
  
  print('\n' + calendar.month(year, month))
  
  print("-" * 20)
  
  print("This is the calendar for", calendar.month_name[month], "in the year", year)
  
  print()

print("End of calendars for the year", year)