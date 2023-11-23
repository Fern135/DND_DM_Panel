from datetime import datetime

def get_current_time_24():
    """Get the current time in 24-hour format."""
    return datetime.now().strftime("%H:%M:%S")

def get_current_time_12():
    """Get the current time in 12-hour format."""
    return datetime.now().strftime("%I:%M:%S %p")