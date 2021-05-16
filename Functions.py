import json
import os
import bs4 as bs
import urllib.request
import time

commands = [
    {
      "command": "exit",
      "description": "Exits the program"
    },
    {
      "command": "rename",
      "description": "Renames a file"
    }
]

def doesFileExist(file):
  if os.path.exists(file):
    return True
  else:
    return False

def helpFunction():
  helpString = ""
  for x in commands:
      helpString += "\n" + x["command"] + " - " + x["description"]
  print(f'Commands to use: {helpString}')

# os.rename can cause issues due to path issues
def renameFunction():
  whichFile = input('File name: ')
  if not doesFileExist(whichFile):
    return print('This file doesn\'t exist: ' + whichFile, "\a")
  newName = input('New name: ')
  return os.rename(whichFile, newName)

while True:
  inputFromUser = input('What function: ')
  if inputFromUser == 'help':
    helpFunction()
    continue
  elif inputFromUser == 'rename':
    renameFunction()
    continue
  elif inputFromUser == 'exit':
    break
  else:
    print(f'Could\'t get that try doing help')
    continue