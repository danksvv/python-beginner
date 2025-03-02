# modules with os, sys and plataform
import sys
import os
import platform

# printer path to the file

print(os.path)

# printer name operating system

print(os.name)

# printer system information

print(sys.platform)

# current working directory path
#
print(os.getcwd())

# change directory

# os.chdir("..")

# print(os.getcwd())

# list directory
#
# print(os.listdir())
#
# os.mkdir("new_dir")
#
# os.chdir("new_dir")
#
# print(os.getcwd())

# finish a execution of the program

# sys.exit()

print(sys.modules)

print(sys.version)

print(sys.version_info)

print(platform.architecture())

print(platform.machine())

print(platform.processor())

print(platform.platform())

print(platform.system())

print(platform.uname())
