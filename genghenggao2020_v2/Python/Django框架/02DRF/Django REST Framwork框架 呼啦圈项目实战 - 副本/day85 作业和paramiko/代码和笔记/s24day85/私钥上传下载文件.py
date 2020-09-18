import paramiko

private_key = paramiko.RSAKey.from_private_key_file(r'C:/Users/Administrator/.ssh/id_rsa')

transport = paramiko.Transport(('192.168.16.85', 22))
transport.connect(username='root', pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
# sftp.put('/tmp/location.py', '/tmp/test.py')

# 将remove_path 下载到本地 local_path
# sftp.get('remove_path', 'local_path')

transport.close()