import socket

HOST = '172.16.173.185'
PORT = 15679
# url="https://www.amazon.in/Columbia-Mens-wind-\
# resistant-Glove/dp/B0772WVHPS/?_encoding=UTF8&pd_rd\
# _w=d9RS9&pf_rd_p=3d2ae0df-d986-4d1d-8c95-aa25d2ade606&pf\
# _rd_r=7MP3ZDYBBV88PYJ7KEMJ&pd_rd_r=550bec4d-5268-41d5-\
# 87cb-8af40554a01e&pd_rd_wg=oy8v8&ref_=pd_gw_cr_cartx&th=1"
url="https://www.amazon.in/s?rh=n%3A20538600031&language=en_IN&brr=1&rd=1"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall(url.encode('utf-8'))

data = client_socket.recv(1024).decode('utf-8')
# data=eval(data)
print(data)

client_socket.close()
