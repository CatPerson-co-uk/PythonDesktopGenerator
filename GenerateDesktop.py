import os

Dname = input("Name Of Desktop File: ") + ".desktop"
Comment = input("(Optional) Comment: ")
Aname = "Name=" + input("Name Of Application: ")
Exec = "Exec=" + input("Path To Executable/Application: ")
Version = input("(Optional) Version: ")

 
fp = open(Dname, "a")
fp.write("[Desktop Entry]\n")

if Version != "":
	fp.write("Version=" + Version + "\n")

if Comment != "":
	fp.write("Comment=" + Comment +  "\n")

fp.write(Aname + "\n")
fp.write(Exec + "\n")
fp.close()

os.system("sudo mv " + Dname + " /usr/share/applications")

print("Created .desktop And Moved To /usr/share/applications")
