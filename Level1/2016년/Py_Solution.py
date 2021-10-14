def solution(a, b):
    yo = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    if a < 2:
        return yo[b % 7]
    else:
        for item in range(0,a-1):
            days += month[item]
        days += b
        return yo[days % 7]