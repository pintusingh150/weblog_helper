import ipaddress
from parse_log_file import *
import re

cidr_pattern = re.compile('/^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([8-9]|[1-2][0-9]|3[0-2]))$/')

def validate_ip_address(ip_address):
    try:
        if(cidr_pattern.match(ip_address)):

        else:
            ip = ipaddress.ip_address(ip_address)
    except ValueError:
        print("IP/CIDR address {} is not valid,Please enter a valid IP address".format(ip_address)) 

def view_logs_by_ip(ip_address):
    print(ip_address[-3])
    #log_data_frame = read_log_data()
    print(log_data_frame.loc[log_data_frame['ip'] == ip_address])


view_logs_by_ip('157.55.39.180/32')

cidr_pattern = re.compile('/^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([8-9]|[1-2][0-9]|3[0-2]))$/')

def find(ip_address):
    if(cidr_pattern.ma)
