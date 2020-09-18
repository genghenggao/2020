import paramiko

transport = paramiko.Transport(('192.168.16.85', 22))
transport.connect(username='root', password='123456')
sftp = paramiko.SFTPClient.from_transport(transport)


# 将location.py 上传至服务器 /tmp/test.py
# sftp.put('wy.txt', '/data/wy.txt')
sftp.get('/data/wy.txt', 'xx.txt')

transport.close()