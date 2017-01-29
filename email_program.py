from socket import *
import base64
import time
import sys

################
# Email Program
# Simple utility to send an email via SMTP
################


#initialise file for writing
org_stdout = sys.stdout
file = open("smtplog.txt", "w")
sys.stdout = file

#message details and mail server addr/port number
msg = "\r\n Welcome"
end_msg = "\r\n.\r\n"
mail_server = ("smtp.uq.edu.au", 25)

#creating socket on client side and establishing connection
#to server socket.
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(mail_server)
recv = client_socket.recv(1024)
recv = recv.decode()
print("RX> " + recv)
#error check - if response states service is not ready, print notification.
if recv[:3] != '220':
    print('220 reply not received from server.')

#send encoded helo command from client to server
helo = 'HELO smtp.uq.edu.au\r\n'
client_socket.send(helo.encode())
print("TX> " + helo);

#decode helo command reply from server
recv1 = client_socket.recv(1024)
recv1 = recv1.decode()
print("RX> " + recv1)
#error check - if requested mail action has not been completed, print notification.
if recv1[:3] != '250':
    print('TX> 250 reply not received from server.')

#sending MAIL FROM command to server (sender details)
mail_from = "MAIL FROM:<martin.jacobs@uq.net.au>\r\n"
client_socket.send(mail_from.encode())
print("TX> " + mail_from)
recv2 = client_socket.recv(1024)
recv2 = recv2.decode()
print("RX> "+recv2)
#error check - if requested mail action has not been completed, print notification.
if recv2[:3] != '250':
    print('TX> 250 reply not received from server.')

#sending RCPT TO command to server (receiver details)
rcpt_to = "RCPT TO:<martin.jacobs@uq.net.au>\r\n"
client_socket.send(rcpt_to.encode())
print("TX> " + rcpt_to)
recv3 = client_socket.recv(1024)
recv3 = recv3.decode()
print("RX> "+recv3)
#error check - if requested mail action has not been completed, print notification.
if recv3[:3] != '250':
    print('TX> 250 reply not received from server.')

#sending DATA command to server
data = "DATA\r\n"
client_socket.send(data.encode())
print("TX> " + data)
recv4 = client_socket.recv(1024)
recv4 = recv4.decode()
print("RX> "+recv4)
#error check - to see if mail has started input or not
if recv4[:3] != '354':
    print('354 reply not received from server.')

#message contents
subject = "Subject: Testing For Assignment 1\r\n\r\n"
client_socket.send(subject.encode())

print("TX> " + subject)
print("TX> " + msg)
print("TX> " + end_msg)

client_socket.send(msg.encode())
client_socket.send(end_msg.encode())

#receives reply message from server once '.' has been sent
recv_msg = client_socket.recv(1024)
print("RX> "+recv_msg.decode())
#error check - to see if mail action has been completed ok or not
if recv_msg[:3] != '250':
    print('250 reply not received from server.')

#send QUIT command to ask server to close the connection
quit = "QUIT\r\n"
client_socket.send(quit.encode())
print("TX> " + quit)
recv5 = client_socket.recv(1024)
print("RX> " + recv5.decode())
#error check - to see if connection has closed or not
if recv5[:3] != '221':
    print('221 reply not received from server.')

#close the file and socket
sys.stdout = org_stdout
file.close()
client_socket.close()
