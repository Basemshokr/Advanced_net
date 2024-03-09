import socket


HOST = '127.0.0.1'
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    big_data = b'a' * 2025
    s.sendall(big_data)
    data = s.recv(2024)
    print('البيانات المُستلمة:', data)
