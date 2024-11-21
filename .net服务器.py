import socket
#/net服务器
net_server={'edu.net':'8006'}
if __name__ == '__main__':
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(('localhost', 8005))
    sock1.listen(5)
    print('net域名服务器正在运行~~~~')
    while True:
        connection,address = sock1.accept()
        buf = connection.recv(1024)
        buf = buf.decode()
        print("由根域名服务器发来的域名："+buf)
        ip = net_server.get(buf, 11)

        str=buf
        buf_split = buf.split(".")
        bufend = len(buf_split)
        s = buf_split[bufend-2]+'.'+buf_split[bufend-1]

        ip = net_server.get(s, 11)
        if ip==11:
            connection.send('不存在此域名！'.encode())
            print("不存在此域名！已返回信息！")
        else:
            ip = int(ip)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', ip))
            sock.send(str.encode())

            res = sock.recv(1024)
            res = res.decode()
            connection.send(res.encode())
            if (res != '不存在此域名！'):
                print('在' + buf_split[bufend - 1] + "服务器查找到！已发送给根域名服务器！")
            else:
                print("未找到该域名信息！已发送给根域名服务器")
            sock.close()