import socket
com_data={'www.edu.net':'000.000.000.004'}
if __name__ == '__main__':
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(('localhost', 8006))
    sock1.listen(5)
    print('com权限域名服务器正在运行~~~~')
    while True:
        connection,address = sock1.accept()
        buf = connection.recv(1024)
        buf = buf.decode()
        print("由com域名服务器发来的域名："+buf)
        ip = com_data.get(buf, 11)
        if ip == 11:
            connection.send('不存在此域名！'.encode())
            print("不存在此域名！已返回信息！")
        else:
            connection.send(ip.encode())
            print("存在此域名！已返回信息！")