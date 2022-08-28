import socket
import re
import webbrowser 
#initializing port number and server adress
PORT= 9000
SERVER= socket.gethostbyname(socket.gethostname())
SERVER=""
ADDRESS= (SERVER, PORT)

SocketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket is made using intenet (IP's) and TCP
SocketServer.bind(ADDRESS) #connecting the previous address with the server
SocketServer.listen(2)

print("The Server is Ready to work")

while True:

    ConnectionSoket, Address= SocketServer.accept() #openning one connection for each call
    Sentence= ConnectionSoket.recv(1024).decode() #socket is going to attempt to receive data, in a buffer size of 1024 bytes at a time.
    print (Address)
    print(Sentence)
    IP= Address[0] #IP is taken from the address
    Port= Address[1] #Port is taken from the address
    URL = Sentence.split()[1] #URL is taken

    if (URL == "/" or URL == "/en"): #   en file 

        #reading HTML file and saving its content in variable
        file = open('main_en.html',encoding="utf8")
        filecode = file.read()
        ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
        ConnectionSoket.send("Content-Type: text/html \r\n".encode())
        ConnectionSoket.send("\r\n".encode()) #ready to send data
        ConnectionSoket.send(filecode.encode())
        file.close()
    
    elif ( URL == "/ar"): #   en file 

        #reading HTML file and saving its content in variable
        file = open('main_ar.html', encoding="utf8")
        filecode = file.read()
        ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
        ConnectionSoket.send("Content-Type: text/html \r\n".encode())
        ConnectionSoket.send("\r\n".encode()) #ready to send data
        ConnectionSoket.send(filecode.encode())
        file.close()
    

        
    elif (URL.endswith('css') or URL.endswith('css/')):
        file = open('StyleSheet1.css',encoding="utf8")
        filecode = file.read()
        ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
        ConnectionSoket.send("Content-Type: text/css \r\n".encode())
        ConnectionSoket.send("\r\n".encode()) #ready to send data
        ConnectionSoket.send(filecode.encode()) #sending css to browser
        file.close()


             
    elif (URL.endswith('css') or URL.endswith('css/')):
        file = open('StyleSheet2.css',encoding="utf8")
        filecode = file.read()
        ConnectionSoket.send("HTTP/1.1 200 OK\r\n".encode())#server response is 200 OK
        ConnectionSoket.send("Content-Type: text/css \r\n".encode())
        ConnectionSoket.send("\r\n".encode()) #ready to send data
        ConnectionSoket.send(filecode.encode()) #sending css to browser
        file.close()





    elif (URL.endswith('P2.jpg') or URL.endswith('P2.jpg/')): #picture of jpg type

        name = URL.split('/')[1] #image name
        type = URL.split('.')[1] #image extention
        ConnectionSoket.send('HTTP/1.1 200 OK\r\n'.encode())#server response is 200 OK
        ConnectionSoket.send(("Content-Type: image/" + type + "\r\n").encode()) #Type of the data content is jpg image so the browser can translate it
        ConnectionSoket.send("\r\n".encode())#ready to send data
        image_os = open(name, 'rb') #opening image info
        imageInfo = image_os.read() #reading image info
        image_os.close() #closing
        ConnectionSoket.send(imageInfo) #sending data to browser

    elif (URL.endswith('P1.png') or URL.endswith('P1.png/')): #picture of jpg type

        name = URL.split('/')[1] #image name
        type = URL.split('.')[1] #image extention
        ConnectionSoket.send('HTTP/1.1 200 OK\r\n'.encode())#server response is 200 OK
        ConnectionSoket.send(("Content-Type: image/" + type + "\r\n").encode()) #Type of the data content is jpg image so the browser can translate it
        ConnectionSoket.send("\r\n".encode())#ready to send data
        image_os = open(name, 'rb') #opening image info
        imageInfo = image_os.read() #reading image info
        image_os.close() #closing
        ConnectionSoket.send(imageInfo) #sending data to browser

 

    elif (URL.endswith('HTMLPage1.html') or URL.endswith('HTMLPage1.html/')):
         # # when requesting /other.html
            file = 'HTMLPage1.html'
            file = open(file,encoding="utf8")
            content = file.read()
            file.close()
            ConnectionSoket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            ConnectionSoket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            ConnectionSoket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            ConnectionSoket.sendall(bytes(content, "UTF-8")) 
               
         
   

              
    elif (URL.endswith('/bzu') ):
      
        #reading HTML error file and saving its content in variable
     
      
        ConnectionSoket.send('HTTP/1.1 307 Temporary Redirect \r\n'.encode())#server response is 404 Not Found
        ConnectionSoket.send(("location: https://ritaj.birzeit.edu/register/ \r\n").encode())#Type of the file content is HTML code so the browser can translate it
        ConnectionSoket.send("\r\n".encode())#ready to send data
        ConnectionSoket.send(("<html>" + "<style> body{background: rgb(186,222,234); background: linear-gradient(180deg, rgba(186,222,234,1) 0%, rgba(186,222,234,1) 100%)} .Div { border:; background-color: #badeea; text-align: center; } </style>" + "<body >" + "<div class=""Div"">" + "<p>" + "IP: " + str(IP) + "</p>" + "<p>" + "Port: " + str(Port) + "</p>" + "</div>" +"<body>"+ "</html>").encode())

        ConnectionSoket.close()

        
                      
    elif (URL.endswith('/go') ):
      
        #reading HTML error file and saving its content in variable
      
        ConnectionSoket.send('HTTP/1.1 307 Temporary Redirect \r\n'.encode())#server response is 404 Not Found
        ConnectionSoket.send(("location: https://google.com \r\n").encode())#Type of the file content is HTML code so the browser can translate it
        ConnectionSoket.send("\r\n".encode())#ready to send data
        ConnectionSoket.send(("<html>" + "<style> body{background: rgb(186,222,234); background: linear-gradient(180deg, rgba(186,222,234,1) 0%, rgba(186,222,234,1) 100%)} .Div { border:; background-color: #badeea; text-align: center; } </style>" + "<body >" + "<div class=""Div"">" + "<p>" + "IP: " + str(IP) + "</p>" + "<p>" + "Port: " + str(Port) + "</p>" + "</div>" +"<body>"+ "</html>").encode())

        ConnectionSoket.close()

                           
    elif (URL.endswith('/cn') ):
      
        #reading HTML error file and saving its content in variable
     
        ConnectionSoket.send('HTTP/1.1 307 Temporary Redirect \r\n'.encode())#server response is 404 Not Found
        ConnectionSoket.send(("location: https://cnn.com\r\n").encode())#Type of the file content is HTML code so the browser can translate it
        ConnectionSoket.send("\r\n".encode())#ready to send data
        ConnectionSoket.send(("<html>" + "<style> body{background: rgb(186,222,234); background: linear-gradient(180deg, rgba(186,222,234,1) 0%, rgba(186,222,234,1) 100%)} .Div { border:; background-color: #badeea; text-align: center; } </style>" + "<body >" + "<div class=""Div"">" + "<p>" + "IP: " + str(IP) + "</p>" + "<p>" + "Port: " + str(Port) + "</p>" + "</div>" +"<body>"+ "</html>").encode())

        ConnectionSoket.close()



    else: #if anything except the above is entered in the URL

        #reading HTML error file and saving its content in variable
        file = open('ERROR.html',encoding="utf8")
        filecode = file.read()
        file.close()
        ConnectionSoket.send('HTTP/1.1 404 Not Found \r\n'.encode())#server response is 404 Not Found
        ConnectionSoket.send(("Content-Type: text/html \r\n").encode())#Type of the file content is HTML code so the browser can translate it
        ConnectionSoket.send("\r\n".encode())#ready to send data
        ConnectionSoket.send(filecode.encode())#sending data
        ConnectionSoket.send(("<html>" + "<style> body{background: rgb(186,222,234); background: linear-gradient(180deg, rgba(186,222,234,1) 0%, rgba(186,222,234,1) 100%)} .Div { border:; background-color: #badeea; text-align: center; } </style>" + "<body >" + "<div class=""Div"">" + "<p>" + "IP: " + str(IP) + "</p>" + "<p>" + "Port: " + str(Port) + "</p>" + "</div>" +"<body>"+ "</html>").encode())

        ConnectionSoket.close()