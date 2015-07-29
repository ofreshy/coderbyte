"""
Using the Python language, have the function CountingMinutes(str) take the str parameter being passed which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two times. The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320.

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""

# def CountingMinutes(str):
#     def to_24_hours(t):
#         hour, minute, am_pm = t.split(':')[0], t.split(':')[1][:-2], t.split(':')[1][-2:]
#         hour = (int(hour) % 12) + (0 if am_pm == 'am' else 12*60)
#         return hour, int(minute)
#
#     early, later = map(to_24_hours, str.split('-'))
#     return early, later

def CountingMinutes(str):
    from datetime import datetime
    ta, tb  = [datetime.strptime(t, '%I:%M%p') for t in str.split('-')]
    return (tb - ta).min










print CountingMinutes("1:23am-1:08am")

"""
Input = "12:30pm-12:00am"Output = 690
Input = "1:23am-1:08am"Output = 1425
"""
