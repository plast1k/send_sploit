#!/usr/bin/env python
'''
------------------------------------------------------------------------
********documentation*********
------------------------------------------------------------------------
the script takes NIX* like arguments from the command line which include
a remote address,a remote port,a character and the number of characters
to be send. It then sends these charcters to the IP address in question to the port
specified.   
------------------------------------------------------------------------
########################################################################
'''
import getopt 
import sys
import time
import socket
from socket import *
#create a  socket and send an exploit data over the network given the IP address 
#and the port as command line option
#some global sort of varables here
remote_port=0
remote_address=""
characters=""
char_count=0
#a define some colors in a class just to be flushy
class color:
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PINK = '\033[96m'
    DEFAULT_COLOR = '\033[0m'
#End of color class
#about function
def about():
    print color.DEFAULT_COLOR
    print color.BLUE +"\t###################################################################"
    print color.BLUE +"\t#"+ color.RED +"============++++++"+color.GREEN +" sendsploit.py ver 0.1 "+color.RED +"++++++++++=============="+color.RED +"#"
    color.DEFAULT_COLOR
    print color.BLUE +"\t#"+ color.PINK +"=============++++++++++++++++++++++++++++++++++++++=============="+color.BLUE +"#"
    print color.BLUE +"\t###################################################################"
    print color.DEFAULT_COLOR
#usage function
def usage ():
    print"Usage:./sendsploit.py <options>"
    print"./sendsploit.py -a <address> -p <port> -c <charcter> -n <num_of_chars_2_send>"
    print"               -a          The remote address to exploit"
    print"               -p          The remote port running vulnarable application"
    print"               -c          The character you want to use in fuzzing for vulns"
    print"               -n          These are the number of characters you want to send"
    print"               -h          Simply print this help menu and exit for "
    print"                Example:./sendsploit.py -a 127.0.0.1 -p 22 -c A -n 256 "
    print"                 (this will send 256 'A's to an ssh server at 127.0.0.1)" 
    print"                or ./sendploit.py -h for help"
    print"                please make sure you give all the options"
#get option from the user
if __name__=='__main__':
    if len(sys.argv)<3:
        color.DEFAULT_COLOR
        print color.PURPLE +"you need atleast three arguments"
        color.DEFAULT_COLOR
        about()
        usage()
        sys.exit(0)
    try:
        opts,args=getopt.getopt(sys.argv[1:], 'a:p:c:n:k,h')
    except getopt.GetoptError, e:
        print e
        usage()
        sys.exit(0)
    try:
        for option,argument in opts:
            if option=='-a':
                address=argument
                remote_address=address
            elif option=='-p':
                port=argument
                remote_port=port
            elif option=='-n':
                num_of_chars=argument
                char_count=num_of_chars
            elif option=='-c':
                char=argument
                characters=char
            elif option=='-h':
                usage()
                sys.exit(0)
    except:
        exit(0) 
if int(remote_port)<=0 or remote_address=="":
    usage()
    sys.exit(0)
elif int(char_count)<=0:
    print "You must give the -n option with a value greater than zero"
    usage()    
    sys.exit(0)
#if all is well we go on    
def print_answer():
    print "\nsending",char_count, characters,"s to",remote_address,"on Port",remote_port,"Please Wait......"
    time.sleep(3)
    send_data()
def send_data():
#get the exploit (buggy data) into a good string
    xsploit_data=str(characters)*int(char_count)
#first open the file given and put the data in into a list
    try:
        my_socket=socket(AF_INET,SOCK_STREAM)
        my_socket.connect((remote_address,int(remote_port)))
        my_socket.send(xsploit_data)
        print "your exploit data has been send to",remote_address,"Good luck......."
        #close my sweet socket
        my_socket.close()
    except:
        print "\nSploit FAILED ! check out that the remote host is really up :("
        print "Check out the kind of IP you gave...... its not being checked!"
print_answer()
#END

   
