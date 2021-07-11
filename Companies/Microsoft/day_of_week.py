def days_of_week(day, k):
    days_map = {'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3, 'fri': 4, 'sat': 5,
                'sun': 6, 0: 'mon', 1: 'tue', 2: 'wed', 3: 'thu', 4: 'fri', 5: 'sat', 6: 'sun'}

    return days_map[(days_map[day] + k) % 7]


print(days_of_week('wed', 2)) # => 'fri'
print(days_of_week('sat', 23)) # => 'mon'