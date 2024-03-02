'''
write a program to validate whether a given string represents a valid IP address

'''

# IP address valid or invalid

try:
    ip="192.168.0.1"
    ip_number=[i for i in range(0,255)]

    ip_len=len(ip.split("."))
    ip_count=0

    for IP in ip.split("."):
        if int(IP) in ip_number:
            ip_count+=1

    if  ip_count == ip_len == 4:
        print("IP address valid")
    else:
        print("IP address Invalid")

except Exception as e:
    print('IP address is not string')