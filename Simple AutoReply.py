PluginName = "Simple AutoReply"
Description = "When a message is received, a predefined message is sent back to the user"
def onMessage(sender, Message, user):
    Log("Received message from: " + sender + " The account: " + user + " received this message")
    sendMessage(sender, "I am currently using LegendaryClient :)")
