import re
import os
import socket
import admin

def recon(host, directory, filename):
    file = open(directory+"/"+filename, "rw+")
    lines = file.readlines()

    #open_ports = an array with: port no, service
    open_ports = []


    for line in lines:
        if "open" in line:
            port_number = re.findall("^[0-6]?[0-9]?[0-9]?[0-9]?[0-9]", line)
            current_port = port_number[0]
            open_ports.append(current_port)
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            port = int(current_port)
            s.connect( (host, port) )

            if "http" in line:
                print "---> Detected HTTP port open at port", current_port
                s.send("GET / HTTP/1.1\r\n\r\n")
                received = s.recv(300)

                admin.write_to_file(directory, "httpresult.txt", received)
                print("FILE httpresult.txt CREATED.")

            elif "ssh" in line:
                print "---> Detected SSH port open at port", current_port
                s.send("SSH-2.0-OpenSSH_7.6\r\n")
                #print("Received from host: ", s.recv(300))
                act = raw_input("---> Do you want to try to ssh in now? y/n  ")
                if "y" in act:
                    username = raw_input("---> With what username? Leave blank for root.  ")
                    if username == "":
                        username = "root"
                    os.system("ssh "+username+"@"+host)

            elif "ftp" in line:
                print "---> Detected FTP port open at port", current_port
                act = raw_input("---> Do you want to try to telnet in now? y/n  ")
                if "y" in act:
                    os.system("telnet "+host+" "+current_port)

    file.close()
    print "--->  SUMMARY: The following ports are open: \n", open_ports
