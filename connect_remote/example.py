import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.116.47.99", username='mdmsadmin', password='monaco1234')
_, stdout, _ = ssh.exec_command("echo monaco1234 | sudo -S service process_manager status")
time.sleep(0.5)
result = stdout.readlines()

_, stdout, _ = ssh.exec_command("echo monaco1234 | sudo -i; ls")
result = stdout.readlines()

_, stdout, _ = ssh.exec_command("pwd")
result = stdout.readlines()

_, stdout, _ = ssh.exec_command("cd /; ls")    # multiple commands, change directory before
result = stdout.readlines()

_, stdout, _ = ssh.exec_command("ls")
result = stdout.readlines()
ssh.close()
