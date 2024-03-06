#imports
import writer

#Banner
print("""
   ___ _           __  ____  __ _  _____         _ 
  / __(_)___ __ ___\ \/ /  \/  | ||_   _|__  ___| |
 | (__| (_-</ _/ _ \>  <| |\/| | |__| |/ _ \/ _ \ |
  \___|_/__/\__\___/_/\_\_|  |_|____|_|\___/\___/_|
                                                   
""")

print("CiscoXMLTool Version 1.0")
print("/////////////////////////////////////////////////\n")

#Startup Dialouge
optionChose = int(input("Please select what configuration you'll need\n1) XMLDefault\n2) Phone Config\n3) Dialplan\nSelection: "))
print('\n')

#Create XMLDefault File
if (optionChose == 1):
    print("Beginning XMLDefault Creation")
    serverIP = str(input("Please type your PBX server IP address in x.x.x.x format: "))
    modelNumber = str(input("Please type ONLY the model number of the cisco phone you're using: "))
    versionNumber = str(input("Please type the whole name of the configuration file preceeding the file extention: "))
    writer.xmldefault(serverIP, modelNumber, versionNumber)

#Create PhoneSpecific Config
if (optionChose == 2):
    print("Beginning Phone Configuration")
    macAddress = str(input("Please type the MAC address of the Cisco IP phone without any special characters: "))
    sshUser = str(input("Please type phone SSH Username: "))
    sshPass = str(input("Please type phone SSH Password: "))
    ntpServerIP = str(input("Please type your NTP server IP address in x.x.x.x format: "))
    pbxIP = str(input("Please type your PBX server IP address in x.x.x.x format: "))
    ext = str(input("Please type the extention number: "))
    extPass = str(input("Please type the extention's password: "))
    ver = str(input("Please type the whole name of the configuration file preceeding the file extention: "))
    writer.phoneConfig(macAddress, sshUser, sshPass, ntpServerIP, pbxIP, ext, extPass, ver)

#Create gneric dialplan file
if (optionChose == 3):
    print("Creating default dialplan.xml")
    writer.dialplan()