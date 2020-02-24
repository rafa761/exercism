from datetime import datetime


def add_gigasecond(moment):
    data = datetime.date(moment)
    return datetime.ctime(data)
