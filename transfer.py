import paramiko

def scp_transfer(remote_host, username, password, remote_file, local_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh.connect(remote_host, username=username, password=password)
        
        scp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        
        scp.get(remote_file, local_path)
        
        print("File transferred successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        scp.close()
        ssh.close()

if __name__ == "__main__":
    remote_host = '192.168.125.108'
    username = 'bhalu'
    password = 'bhalu'
    remote_file = '/home/bhalu/project/capture/test.h264'
    local_path = 'C:/Something New/'

    scp_transfer(remote_host, username, password, remote_file, local_path)
