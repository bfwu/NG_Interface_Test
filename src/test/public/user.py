# -*- coding = utf-8 -*-
import csv
import random

my_file = "C:\\user.csv"
data = csv.reader(file(my_file, "rb"))
c = []
d = []
for user in data:
    c.append(user[0])
    d.append(user[1])


def user():
    #    my_file="C:\\user.csv"
    #    data=csv.reader(file(my_file,"rb"))
    name = c[random.randint(0, len(c))]
    print name
    return name


def password():
    #    my_file="C:\\user.csv"
    #    data=csv.reader(file(my_file,"rb"))
    password = d[random.randint(0, len(d))]
    print password
    return password
