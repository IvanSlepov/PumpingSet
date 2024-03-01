from datetime import datetime


# Task 9. Date Format
# Create a function format_date() that converts a date formatted as MM/DD/YYYY to YYYY-DD-MM.
# Notes.
# Return value should be a string.
# Examples
#
# format_date("11/12/2019") ➞ "2019-12-11"
# format_date("12/31/2019") ➞ "2019-31-12"
# format_date("01/15/2019") ➞ "2019-15-01"

def format_date(some_date):
    split_date = some_date.split("/")

    month = int(split_date[0])
    day = int(split_date[1])
    year = int(split_date[2])

    require_date_format = datetime(year, month, day)
    return require_date_format.strftime("%Y-%d-%m")
