import os

Dname = input("Name Of Desktop File: ") + ".desktop"
Aname = "Name=" + input("Name Of Application: ")
Exec = "Exec=" + input("Path To Executable/Application: ")
Comment = input("(Optional) Comment: ")
Version = input("(Optional) Version: ")

 
f = open(Dname, "a")
f.write("[Desktop Entry]\n")

if Version != "":
	f.write("Version=" + Version + "\n")

if Comment != "":
	f.write("Comment=" + Comment +  "\n")

f.write(Aname + "\n")
f.write(Exec + "\n")
f.close()

os.system("sudo mv " + Dname + " /usr/share/applications")

print("Created .desktop And Moved To /usr/share/applications")
