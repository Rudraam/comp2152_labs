#sys.operations.py
import platform
import socket
import os
print(f"Machine type: " , platform.machine())
print(f"CPU architecture: ", platform.architecture())

socket.setdefaulttimeout(50)
print(f"CPU Architecture: " , {socket.getdefaulttimeout()})
print(f"OS Type: " , {os.name})
print(f"OS system: " , {platform.system()})


print(f"Current PID: {os.getpid()}" )
