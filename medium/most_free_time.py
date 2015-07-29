"""
Using the Python language, have the function MostFreeTime(strArr) read the strArr parameter being passed which will represent a full day and will be filled with events that span from time X to time Y in the day. The format of each event will be hh:mmAM/PM-hh:mmAM/PM. For example, strArr may be ["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM-09:50AM"]. Your program will have to output the longest amount of free time available between the start of your first event and the end of your last event in the format: hh:mm. The start event should be the earliest event in the day and the latest event should be the latest event in the day. The output for the previous input would therefore be 01:30 (with the earliest event in the day starting at 09:10AM and the latest event ending at 02:45PM). The input will contain at least 3 events and the events may be out of order.

"12:15PM-02:00PM","09:00AM-10:00AM","10:30AM-12:00PM"

"""

def MostFreeTime(strArr):
    def to_minutes(t):
        h, m = map(int, t[:-2].split(':'))
        h = h % 12 + (12 if t[-2] == 'P' else 0)
        return h * 60 + m

    events = sorted([[to_minutes(a) for a in p.split('-')] for p in strArr], key=lambda x:x[0])
    breaks = [(b[0] - b[1]) for b in zip([e[0] for e in events[1:]], [e[1] for e in events[:-1]])]
    return '%02d:%02d' % divmod(max(breaks), 60)


assert MostFreeTime(["12:15PM-02:00PM","09:00AM-10:00AM","10:30AM-12:00PM"]) == '00:30'
# print MostFreeTime(["12:15PM-02:00PM","09:00AM-12:11PM","02:02PM-04:00PM"])

assert MostFreeTime(["12:15PM-02:00PM", "09:00AM-12:11PM", "02:02PM-04:00PM"]) == '00:04'
