import paramiko

def ssh_user_password_check(host: str, port: int, username: str, password: str):
    """
    Checks whether the given username and password authenticates
    properly.
    """
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    try:
        client.connect(host, port=port, username=username, password=password)
        return True
    except:
        return False
