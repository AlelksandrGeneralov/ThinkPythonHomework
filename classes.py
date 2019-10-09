class Point(object):
    '''represents a point in 2d space'''


print(Point)
blank = Point()
print(blank)
blank.x = 3.0
blank.y = 4.0


def print_point(p):
    print('(% g, % g)' % (p.x, p.y))


print(print_point(blank))


class Rectangle(object):
    '''represents rectangle with attributes: width, height, corner'''


box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return(p)


centr = find_center(box)
print(print_point(centr))


p1 = Point()
p1.x = 3.0
p1.y = 4.0

import copy

p2 = copy.copy(p1)
print(p2)


class Time(object):
    '''represents a time of a day, attributes: hour, minute, second'''

    def print_time(self):
        return('(%.2d:%.2d:%.2d)' % (self.hour, self.minute, self.second))

    def is_after(self, other):
        return(self.time_to_int() > other.time_to_int())

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return(seconds)

    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return(time.print_time())

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return('(%.2d:%.2d:%.2d)' % (self.hour, self.minute, self.second))

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return(int_to_time(seconds))


time = Time()
time.hour = 5
time.minute = 10
time.second = 15


def print_time(time_object):
    return('(%.2d:%.2d:%.2d)' % (time_object.hour, time_object.minute, time_object.second))


def add_time(t1, t2):
    s = Time()
    s.hour = t1.hour + t2.hour
    s.minute = t1.minute + t2.minute
    s.second = t1.second + t2.second
    if s.second >= 60:
        s.second -= 60
        s.minute += 1
    if s.minute >= 60:
        s.minute -= 60
        s.hour += 1
    return(s)


start = Time()
start.hour = 1
start.minute = 2
start.second = 59

duration = Time()
duration.hour = 2
duration.minute = 58
duration.second = 6

done = add_time(start, duration)
print(print_time(done))


def increment(time, seconds):
    time.second += seconds
    if time.second >= 60:
        time.minute += time.second // 60
        time.second = (time.second % 60) * 60
    if time.minute >= 60:
        time.hour += time.minute // 60
        time.minute = (time.minute % 60) * 60


print(Time.print_time(done))

print(done.print_time())


def time_to_int(self):
    minutes = self.hour * 60 + self.minute
    seconds = minutes * 60 + self.second
    return(seconds)


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return(time.print_time())


print(time_to_int(start))
seconds = time_to_int(start)
print(int_to_time(seconds))
print(start.is_after(duration))
print(time.print_time())
print(time)
print(start + duration)
