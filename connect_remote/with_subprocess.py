import subprocess
import sys

HOST="10.116.47.99"
USERNAME= "mdmsadmin"
PASSWORD= "monaco1234"
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="uname -a"

# ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
#                        shell=False,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE)
# result = ssh.stdout.readlines()
# if result == []:
#     error = ssh.stderr.readlines()
#     print >>sys.stderr, "ERROR: %s" % error
# else:
#     print result

import shlex
import subprocess

HOST="10.116.47.99"
USERNAME= "mdmsadmin"
PASSWORD= "monaco1234"
cmd = "ssh {} 'cd scripts; python -u get_details.py --web_server'".format(HOST)

subprocess.call(shlex.split(cmd))