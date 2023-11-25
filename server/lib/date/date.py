from datetime import datetime

def get_current_year():
    """Get the current year."""
    return datetime.now().year

def get_current_month():
    """Get the current month."""
    Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return Months[datetime.now().month]

def get_current_day():
    """Get the current day of the month."""
    return datetime.now().day

def get_day_of_week():
    """Get the current day of the week."""
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[datetime.now().weekday()]

def is_leap_year(year):
    """Check if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)