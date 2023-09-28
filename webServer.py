###########################################
# NYU iD MS02@nyu.edu
###########################################
# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    # Listen for incoming connections
    serverSocket.listen(1)

    ##serverSocket.listen(1)
    #print ('The server is ready to receive')# comment all print statements before submission

    #Fill in end

    while True:
    
        # Establish the connection
        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()  # Receive the HTTP request from the client

            # Check if the message contains headers
            if "HTTP/1.1" in message:
                filename = message.split()[1]

                # Open the client requested file.
                try:
                    f = open(filename[1:], 'rb')
                    f_data_CON = f.read()
                    f.close()
                    #Send the content of the requested file to the client
                    #for i in range(0, len(outputdata)):
                    #   connectionSocket.send(outputdata[i].encode())
                    #    connectionSocket.send("\r\n".encode())
                    #connectionSocket.close()
                    # Prepare HTTP response headers
                    response_headers_string = "HTTP/1.1 200 OK\r\n"
                    response_headers_string += "Server: MyWebServer\r\n"
                    response_headers_string += "Connection: close\r\n"
                    response_headers_string += "Content-Type: text/html; charset=UTF-8\r\n"
                    response_headers_string += "Content-Length: {len(f_data_CON)}\r\n\r\n"

                    # Send the headers
                    connectionSocket.send(response_headers_string.encode())

                    # Send the content of the requested file to the client
                    connectionSocket.send(f_data_CON)

                except FileNotFoundError:
                    # Send a 404 Not Found response
                    not_found_response = "HTTP/1.1 404 Not Found\r\n"
                    not_found_response += "Server: MyWebServer\r\n"
                    not_found_response += "Connection: close\r\n\r\n"
                    connectionSocket.send(not_found_response.encode())

            else:
                # Send a response with headers to handle invalid requests
                invalid_response = "HTTP/1.1 400 Bad Request\r\n"
                invalid_response += "Server: MyWebServer\r\n"
                invalid_response += "Connection: close\r\n\r\n"
                connectionSocket.send(invalid_response.encode())

            # Close client socket
            connectionSocket.close()

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    webServer(13331)
   