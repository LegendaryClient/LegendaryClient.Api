PluginName = "Simple AutoReply"
Description = "When a message is received, a predefined message is sent back to the user"
def onMessage(sender, Message):
    Log("Received message from" + sender)
    sendMessage(sender, "I am currently using LegendaryClient :)")
