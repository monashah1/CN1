###########################################
# NYU iD MS02@nyu.edu
###########################################
#import socket module
from socket import *
import sys # In order to terminate the program

#serverPort = 13331
# port forward 13331
def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)

   #server prep
   serverSocket.bind(("",port))
   serverSocket.listen(1)
   #print ('The server is ready to receive')# comment all print statements before submission

   #Fill in end

   while True:
       #Establish the connection
       #print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
       try:
           message = connectionSocket.recv(1024).decode() #Fill in start    #Fill in end
           # filename = message.split()[1]
           #f = open(filename[1:])
           #outputdata = f.read() #Fill in start     #Fill in end
           #f.close()
           
           
           if "HTTP/1.1" in message:
               try:
                   f = open(filename[1:],'rb')
                   f_data = f.read()
                   f.close()

                   # RESponse
                   response_headers = "HTTP/1.1 200 OK\r\n"
                   response_headers += "Server: MyWebServer\r\n"
                   response_headers += "Connection: close\r\n"
                   response_headers += "Content-Type: text/html; charset=UTF-8\r\n"
                   response_headers += f"Content-Length: {len(file_data)}\r\n\r\n"

                    # Send the headers
                   connectionSocket.send(response_headers.encode())

                    # Send the content of the requested file to the client
                   connectionSocket.send(f_data)
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
           #Send one HTTP header line into socket
           #connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())  
           # 200 http OK message


           #
           #Fill in end

           #Send the content of the requested file to the client
           #for i in range(0, len(outputdata)):
            #   connectionSocket.send(outputdata[i].encode())
           #onnectionSocket.send("\r\n".encode())
           #connectionSocket.close()

       #except IOError:
           #Send response message for file not found (404)
           #Fill in start
        #   connectionSocket.send('HTTP/1.1 404 not found \r\n\r\n'.encode())
         #  connectionSocket.close()
           #Fill in end
           #Fill in start

           #Fill in end

   #serverSocket.close()
   #sys.exit()  # Terminate the program after sending the corresponding data

#if __name__ == "__main__":
#   webServer(13331)

