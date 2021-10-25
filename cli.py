import argparse
from typing import final
from requests.sessions import session
import ipaddress
from parse_log_file import *
import re

parser = argparse.ArgumentParser(prog='wlh', description='Find the logs for IP/CIDR.')
parser.add_argument('ip', type=str, help='Pass IP/CIDR address to search the logs.')
args = parser.parse_args()

def validate_ip_address(ip_address):
    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        print("IP address {} is not valid,Please enter a valid IP address".format(ip_address))
        exit()

def view_logs(ip_address):
    validate_ip_address(ip_address)
    log_data_frame = read_log_data()
    if(len(log_data_frame) == 0):
        print('No matching Logs found.Please try some other IP/CIDR')
    else:
        print(log_data_frame.loc[log_data_frame['ip'] == ip_address])
        

view_logs(args.ip)




        



