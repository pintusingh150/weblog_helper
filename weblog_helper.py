#!/usr/bin/env python3
import argparse
from cli import *

parser = argparse.ArgumentParser(prog='wlh', description='Find the logs for IP/CIDR.')
parser.add_argument('ip', metavar='<ip>', help='Pass IP/CIDR address to search the logs.')
args = parser.parse_args()

view_logs(args.ip)

