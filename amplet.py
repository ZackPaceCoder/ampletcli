import sys
import os

print("Amplet running version of PYTHON: " + sys.version)

while True:
  x = input(os.getlogin() + "$>>")
  args = x.split(" ")
  if os.path.isfile(os.path.join("amplet",args[0])):
    dat = __import__(os.path.join("amplet",args[0]))
    dat.amplet(args)
