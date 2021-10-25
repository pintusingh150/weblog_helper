import argparse
from typing import final
from requests.sessions import session
import ipaddress
from parse_log_file import *

parser = argparse.ArgumentParser(prog='wlh', description='Find the logs for IP/CIDR.')
parser.add_argument('ip', metavar='<ip>', help='Pass IP/CIDR address to search the logs.')
args = parser.parse_args()

def view_logs_ip(ip_address):
    log_df = read_logs()
    search_logs_by_ip(log_df,ip_address)
    

def read_logs():
    log_data_frame = read_log_data()
    return log_data_frame

def search_logs_by_ip(log_data_frame,ip_address):
    if(len(log_data_frame.loc[log_data_frame['ip'] == format(ip_address)]) != 0):
        print(log_data_frame.loc[log_data_frame['ip'] == format(ip_address)])
    else:
        print('No matching Logs found for IP {0}'.format(ip_address))


def view_logs(cidr_range):
    log_df = read_logs()
    try:
        net_address = ipaddress.ip_network(cidr_range)
        for ip_address in net_address:
            print('Searching logs for IP address {0}'.format(ip_address))
            search_logs_by_ip(log_df,ip_address)
    except:
        print('The CIDR/IP {0} provided is not valid.Please provide a valid IP/CIDR'.format(cidr_range))
        exit()


view_logs(args.ip)




        



