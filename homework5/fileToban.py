#Heres ip's needed to check for 
login_logs = [
    {"ip": "192.168.1.15", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "root", "status": "success"},
    {"ip": "192.168.1.15", "user": "root", "status": "failed"},
    {"ip": "192.168.1.15", "user": "admin", "status": "success"},
    {"ip": "172.16.0.5", "user": "ubuntu", "status": "success"},
    {"ip": "192.168.1.15", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "admin", "status": "failed"},
    {"ip": "203.0.113.8", "user": "root", "status": "failed"},
    {"ip": "203.0.113.8", "user": "root", "status": "failed"},
    {"ip": "203.0.113.8", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "root", "status": "success"}
]

def block_ip(ip_address):
    #declare the variable for firewall 
    firewall = 1

    #simulate blocking the IP on 3 firewalls 
    while firewall <= 3:

        print("Blocking", ip_address, "on Firewall", firewall)
       
        firewall += 1


def analize_logs(logs):

    #creating empty dict for failed ip
    failedlog_count = {}

    #Loop through every log entry in the logs list
    for curLog in logs:

        #check if log is failed
        if curLog["status"] == "failed":

            ip = curLog["ip"]

            if ip in failedlog_count:
                failedlog_count[ip] += 1

            else:
                failedlog_count[ip] = 1
    
    banned_ip = []

    '''
      Loop through the dictionary of failed login counts,
      if an IP has 3 or more failed login attempts 
      add the IP to the banned list
    '''
    for ip, count in failedlog_count.items():

        if count >= 3:
            banned_ip.append(ip)

            block_ip(ip)

    #return list of banned ip's
    return banned_ip


analize_logs(login_logs)

