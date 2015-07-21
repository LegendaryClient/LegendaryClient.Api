PluginName = "avil2"
Description = "advanced champion stat finder"
def userSendMessage(sender, Message, user):
    if "champName:" in Message:
      Log("Looking for " + Message)
