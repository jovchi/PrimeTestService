""" RPyc Client

(Python 3.4.2)

Author: Jovaughn Chin
        Jonathan Gonzoph
Date:   11/17/2014

"""


# import rpyc for connection, ipaddress for IP validation
import rpyc
import ipaddress

#ask Client the location/server of the Service he wish to access
IPAddress= input(" What is the location(IP) of the server you wish to access?: ")

#Validate IP address
try:
 ipaddress.ip_address(IPAddress)

except ValueError:
	IPAddress=input("Sorry, wrong input. Please input correct location(IP) of the server you wish to access?: ")

# connect to server
c=rypc.connect(IPAddress,12345) 

# validate input is a number
try:
	num=int(input("What number would you like to check if prime?: " ))
except ValueError:
    num = int(input("Sorry, wrong input. Please input a number: "))

print(c.root.isPrime(num))


