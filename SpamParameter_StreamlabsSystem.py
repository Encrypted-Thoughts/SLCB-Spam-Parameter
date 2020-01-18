#---------------------------
#   Import Libraries
#---------------------------
import codecs
import json
import os
import re
import sys

#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Spam Parameter"
Website = "https://www.twitch.tv/EncryptedThoughts"
Description = "Parameter ($spam) to be used in custom commands that will duplicate and spam the input message to chat. See readme.txt for use instructions."
Creator = "EncryptedThoughts"
Version = "1.0.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")
ReadMe = os.path.join(os.path.dirname(__file__), "README.txt")

#---------------------------------------
# Classes
#---------------------------------------
class Settings(object):
    def __init__(self, SettingsFile=None):
        if SettingsFile and os.path.isfile(SettingsFile):
            with codecs.open(SettingsFile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        else:
            self.EnableDebug = True

    def Reload(self, jsondata):
        self.__dict__ = json.loads(jsondata, encoding="utf-8")
        return

    def Save(self, SettingsFile):
        try:
            with codecs.open(SettingsFile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, encoding="utf-8")
            with codecs.open(SettingsFile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8')))
        except:
            Parent.Log(ScriptName, "Failed to save settings to file.")
        return

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    global ScriptSettings
    ScriptSettings = Settings(SettingsFile)
    ScriptSettings.Save(SettingsFile)
    return

#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
#---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):

    regex = "\$spam\(\s*(discord|stream)\s*,\s*[0-9]+\s*,\s*[0-9]+\s*,\s*(true|false)\s*,.*\)" # !spam(string,number,number,bool,string)

    item = re.search(regex, parseString)

    if item is None:
        return parseString

    if ScriptSettings.EnableDebug:
        Parent.Log(ScriptName, "Oh boy! Spam parameter detected: " + item.group())

    rawArguments = item.group().strip()[6:][:-1]
    args = rawArguments.split(",")
        
    chatType = args[0]
    spamCount = int(args[1])
    maxLength = int(args[2])
    allowPartialMessage = args[3]
    inputMessage = ""

    #allow , in final parameter in case the message needs to contain one
    currentArg = 4
    while currentArg < len(args):
        if currentArg > 4:
            inputMessage += ","
        inputMessage += args[currentArg]
        currentArg += 1

    if chatType == "stream" and maxLength > 400:
        maxLength = 400
    if chatType == "discord" and maxLength > 1795:
        maxLength = 1795

    spam = ""

    if ScriptSettings.EnableDebug:
        Parent.Log(ScriptName, "Vomits Info -> chatType: " + chatType + " spamCount: " + str(spamCount) + " maxLength: " + str(maxLength) + " allowPartialMessage: " + str(allowPartialMessage) + " inputMessage: " + inputMessage)
    
    while len(spam) <= maxLength:
        if allowPartialMessage == "false" and (len(spam) + len(inputMessage) + 1) > maxLength:
            break                
        spam += " " + inputMessage

    if len(spam) > maxLength:
        spam = spam[:maxLength - len(SpamText)]

    parseString = parseString.replace(item.group(), spam)

    if ScriptSettings.EnableDebug:
        Parent.Log(ScriptName, "Spam text generated, PROCEEDING TO SPAM! (evil laughter)")

    count = 0
    while count < spamCount:
        send_message(spam, chatType)
        count += 1

    if ScriptSettings.EnableDebug:
        Parent.Log(ScriptName, "Spamming completed... Back to the shadows I go...")

    return 

#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return

#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return

def send_message(message, chatType):
    if chatType:
        if chatType == "discord":
            Parent.SendDiscordMessage(message)
        else:
            Parent.SendStreamMessage(message)
    else:
        Parent.SendStreamMessage(message)

def openreadme():
    os.startfile(ReadMe)