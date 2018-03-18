import reconnaissance
import os
import admin

# collecting input
host = raw_input("Host to be tested: ")
directory = raw_input("Directory name: ")
nmap_flags = raw_input("Nmap flags: ")

os.system('mkdir '+directory)
print "---> DIRECTORY %s CREATED." % directory
nmap_result = os.popen('nmap '+nmap_flags+" "+host).read()
admin.write_to_file(directory, "nmapresult.txt", nmap_result)
print "---> FILE nmapresult.txt CREATED."

reconnaissance.recon(host, directory, 'nmapresult.txt')
