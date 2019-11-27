import paramiko

try:
    client = paramiko.client.SSHClient()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.201.128',
                    username='developer',
                    password='4linux',
                    port='22')
except Exception as e:
    print(e)
    exit()

stdin, stdout, stderr = client.exec_command('ls -la')
if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))