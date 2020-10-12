import socket
from clientThread import ClientThread
HOST = '127.0.0.1'
PORT = 65435
client = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)
print('Server is listening...')
while True:
    conn, addr = s.accept() 
    try:
        print('Connected by', addr)
        client.append(ClientThread(conn, addr, client))
        client[-1].start()
    except Exception as e:
        print(e)
conn.close()
