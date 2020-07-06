#!/usr/bin/env python

import subprocess
import sys

# cmd="ssh edenchou@localhost"
# result = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(result)

HOST="edenchou@localhost"
# Ports are handled in ~/.ssh/config since we use OpenSSH
# COMMAND="uname -a"
# cmd="sshpass -p 'pinklemonade' ssh edenchou@localhost"
#ssh = subprocess.Popen(['sshpass', '-p', 'pinklemonade', 'ssh', '-T', 'edenchou@localhost'],                      
#                       stdin=subprocess.PIPE, stdout=subprocess.PIPE)

str="password"
encode=str.encode(encoding='UTF-8',errors='strict')
ssh = subprocess.Popen(['sshpass', '-p', 'password', 'ssh', '-T', 'edenchou@localhost'],                      
                       stdin=subprocess.PIPE, stdout=subprocess.PIPE)

command="cd /Users/edenchou/documents/comp_projects\nls -l\n"
out, err = ssh.communicate(command.encode('utf-8'))
print(out.decode())


#result = ssh.stdout.readlines()
#if result == []:
 #   error = ssh.stderr.readlines()
  #  print >>sys.stderr, "ERROR: %s" % error
#else:
 #   print(result)







