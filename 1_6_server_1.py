import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    while True:
        data = s.recv(1024)
        if not data or data.decode('utf-8') == 'close':
            break
        conn.send(data)
    conn.close()



# import socket

# class Server:
#     def __init__(self, ip, port,q_len):
#         self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.s.bind((ip, port))
#         self.s.listen(q_len)
        
#     def run(self):
#         while True:
#             conn, addr = self.s.accept()
#             while True:
#                 data = self.s.recv(1024)
#                 if not data or data.decode('utf-8') == 'close':
#                     break
#                 conn.send(data)
#             conn.close()

# if __name__ == "__main__":
#     serv = Server('0.0.0.0', 2222, 10)