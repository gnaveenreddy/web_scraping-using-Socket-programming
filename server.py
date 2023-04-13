import socket
import requests
import pickle
from bs4 import BeautifulSoup
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
  

def scrape_website(url):
    # Scrape the website using BeautifulSoup
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    #Extract the data you need
    data_str = ""
    cus_list= []
  
    for item in soup.find_all("span", class_="a-size-base"):#a-profile-name class for profile names;#a-price-whole for prices;#a-size-base for ratings;
        data_str = data_str + item.get_text()
        cus_list.append(data_str)
        data_str = ""
    return cus_list
    

HOST = '172.16.173.185'
PORT = 15679

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('Server is listening on port', PORT)

while True:
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    url = client_socket.recv(1024).decode('utf-8')
    print('Received URL:', url)
    data = scrape_website(url)
    data=str(data)
    client_socket.sendall(data.encode())
    client_socket.close()

