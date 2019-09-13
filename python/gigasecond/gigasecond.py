from datetime import datetime


def add_gigasecond(moment):
    data = datetime.date(moment)
    segundos = datetime.ctime(data)
    return segundos
