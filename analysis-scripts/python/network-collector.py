#!/usr/bin/python

import requests, sys

path = "output/results.txt"

def collect_data(addr):
    return requests.get("https://" + addr).elapsed.total_seconds()

def write_header(condition):
    file = open(path, 'w')
    file.write(condition + "\n")
    file.close()

def save_data(response_buffer):
    file = open(path, 'a')
    file.write(response_buffer)
    file.close()


if len(sys.argv) != 3:
    print len(sys.argv)
    print "Usage: network-collector.py [LOAD BALANCER ADDR] [EXEC CONDITION]"
else:
    load_balancer = sys.argv[1]
    write_header(sys.argv[2])
    data_buffer = ""
    #while loop
    for i in range(10000):
        data_buffer += str(collect_data(load_balancer))
        data_buffer += "\n"
    save_data(data_buffer)

