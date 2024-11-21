import socket
top_server = {'com':'8003','net':'8005'}

if __name__ == '__main__':
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(('localhost', 8002))
    sock1.listen(5)
    print('根域名服务器正在运行~~~~')
    while True:
        connection,address = sock1.accept()
        buf = connection.recv(1024)
        buf = buf.decode()
        str1 = buf
        print("由本地域名服务器发来的域名："+buf)
        buf_split = buf.split(".")
        bufend = len(buf_split)


        binds = top_server.get(buf_split[bufend - 1], 11)

        if binds == 11:
            print("没有该类域名！")
            connection.send('不存在此域名！'.encode())
        else:
            binds=int(binds)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', binds))
            sock.send(str1.encode())

            res = sock.recv(1024)
            res = res.decode()
            binds = str(binds)
            connection.send(res.encode())
            connection.send(binds.encode())###
            if(res!='不存在此域名！'):
                print('在'+buf_split[bufend - 1]+"服务器查找到！已发送给本地域名服务器！")
            else:
                print("未找到该域名信息！已发送给本地域名服务器")
            sock.close()
