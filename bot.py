import discord # Discord API Wrapper 


token = "YOUR TOKEN HERE" 
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
    if message.content == "!test": 
        print("Received test command!") 
        await client.send_message(message.channel, "Hello, " + message.author.name) 
        
        
# Connect the client to Discord 
client.run(token)