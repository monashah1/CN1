from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message \r\n This is a SMTP Test Message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) #if you want to ver#ify the script beyond GradeScope
    #mailserver = 'smtp.gmail.com'
    #port = 25
    #mailserver = (mailserver, port)
    #print('The mailserver is ', mailserver)

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    recv0 = clientSocket.recv(1024).decode()

    #print("The variable recv0 is ", recv0)
    #if recv0[:3] != '220':
        #print('recv0 -> 220 reply not received from server.')
    #else:
        #print('Success recv0=', recv0[:3])

    # Send HELO command and #print server response.
    heloCommand = 'HELO Esther\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    #print('After HELO Alice command: ', recv1)
    #if recv1[:3] != '250':
        #print('recv1 -> 250 reply not received from server.')
    #else:
        #print('Success recv1=', recv1[:3])

    # Send MAIL FROM command and #print server response.
    mailFrom = "MAIL From: <mshah2@gmail.com>\r\n"
    clientSocket.send(mailFrom.encode())
    recv3 = clientSocket.recv(1024).decode()

    #print("After MAIL FROM command: ", recv3)
    #if recv3[:3] != '250':
        #print('recv3 -> 250 reply not received from server.')
    #else:
        #print('Success recv3=', recv3[:3])

    # Send RCPT TO command and #print server response.
    rcptCommand = 'RCPT TO: <mshah2@gmail.com>\r\n'
    clientSocket.send(rcptCommand.encode())
    recv4 = clientSocket.recv(1024).decode()

    #print('After RCPT TO command: ', recv4)
    #if recv4[:3] != '250':
        #print('recv4 -> 250 reply not received from server.')
    #else:
        #print('Success recv4=', recv4[:3])

    # Send DATA command and #print server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv5 = clientSocket.recv(1024).decode()

    #print("After DATA command: ", recv5)
    

    # Send message data.
    clientSocket.send(msg.encode())
    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    #recv6 = clientSocket.recv(1024).decode()

    #print("Response after sending message body: ", recv6)
    #if recv6[:3] != '250':
        #print('recv6 -> 250 reply not received from server.')
    #else:
        #print('Success recv6=', recv6[:3])

    # Send QUIT command and get server response.
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv7 = clientSocket.recv(1024).decode()

    
    #clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')