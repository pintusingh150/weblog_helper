import ipaddress 

def validate_ip_address(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
    except ValueError:
        print("IP address {} is not valid,Please enter a valid IP address".format(address)) 

def view_logs_by_ip(ip_address):
