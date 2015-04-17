#!/usr/bin/python

import os
from operator import itemgetter

os.system('clear')

def flights(arrivals):
    return sorted(arrivals,key=itemgetter(2))

voo = [
    ('KLM75', 'Amsterdam', '14:35', '60', '50'),
    ('AF111', 'Paris', '14:20', ' 50', '64'),
    ('LH333', 'Frankfurt', '14:10', '112', '203'),
    ('KLM71', 'Madrid', '14:55', '120', '100'),
    ('TAP103', 'Salvador', '15:20', '174', '210'),
    ('KLM79', 'Sofia','09:30','113','13'),
    ('LH123', 'Berlin', '15:10', '115', '210')]


print (flights(voo))