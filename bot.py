import discord # Discord API Wrapper 
import handler

token = "YOUR TOKEN HERE" 
prefix = "PREFIX" 
# Create new client 
client = discord.Client() 

# Log to console when the client is started 
@client.event 
async def on_ready(): 
    print('Logged in as')
    print(client.user.name) 
    print(client.user.id) 
    print('------') 


# Fires every time a new message is received 
@client.event
async def on_message(message):
    if message.author == client.user: # Don't handle our messages
        return

    # Send the message to the CommandHandler if the message starts with the prefix
    if message.content.startswith(prefix):
        await handler.handle(message)
        
# Connect the client to Discord 
client.run(token)