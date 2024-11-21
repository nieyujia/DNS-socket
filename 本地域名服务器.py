import socket

if __name__ == '__main__':
    server_local={'www.taobao.com':'000.000.000.001'}
    history={}

    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(('localhost', 8001))
    sock1.listen(5)
    print('本地域名服务器正在运行~~~~')
    while True:
        connection,address = sock1.accept()
        buf = connection.recv(1024)
        buf = buf.decode()
        print("由本机发来的域名："+buf)
        buf_split = buf.split(".")
        bufend = len(buf_split)###
        log = buf_split[bufend-1]###
        bind = history.get(log,11)



        ip = server_local.get(buf, 11)
        if ip == 11:
            if bind==11:
                print('本地域名服务器不存在此域名，正在向根域名服务器请求......')
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(('localhost', 8002))
                sock.send(buf.encode())
                #
                res = sock.recv(1024)
                res = res.decode()
                binds = sock.recv(1024)###
                binds = binds.decode()###
                binds=int(binds)###
                history[log]=binds###
                server_local[buf]=res
                connection.send(res.encode())
                print("收到顶级域名服务器信息！已发送给本机！")
                connection.close()
            else:
                print('本地域名服务器不存在此域名，但查找到该域名服务器，正在连接......')
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(('localhost', bind))
                sock.send(buf.encode())
                res = sock.recv(1024)
                res = res.decode()
                connection.send(res.encode())
                bind=str(bind)
                print("收到"+bind+"域名服务器信息！已发送给本机！")
                connection.close()
        else:
            connection.send(ip.encode())
            print("在本地域名服务器查找到！已发送给本机！")
            connection.close()









