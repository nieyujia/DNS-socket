import sys
import socket
if __name__ == '__main__':
    local_data={'www.baidu.com':'000.000.000.000'}
    while(1):
        while(1):
            print("请输入域名进行查找：")
            data = input()
            ip = local_data.get(data, 11)
            if(ip!=11):
                print("通过本地缓存查找到该ip地址！地址为："+ip)
                s=input('是否继续查找？（Y继续/其余退出）')
                if(s!='Y'):
                    sys.exit()
                else:
                    continue
            else:
                print('本机未找到！')
                break
        #发送给本地域名服务器

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 8001))
        sock.send(data.encode())
        print ('已发送给本地域名服务器！')
        #接受
        res = sock.recv(1024)
        res = res.decode()
        #增加
        local_data[data]=res
        print('收到结果！'+res)

        s = input('是否继续查找？（Y继续/其余退出）')
        if (s != 'Y'):
            sys.exit()
        else:
            continue
        sock.close()



