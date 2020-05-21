# Import Modules
import dbl
import discord
import pyparticle as pp
from discord.ext import commands, tasks
import asyncio
import _thread
from sseclient import SSEClient

# reference to URL with published events
# 'catHere' is the name of the event being published
messages = SSEClient('https://api.particle.io/v1/events/catHere?access_token=PARTICLE_ACCOUNT_TOKEN')

# reference to command listener,
# also specifies prefix to issue bot commands '.'
client = commands.Bot(command_prefix = '.')

#  reference to particle account - should be change to new token
particle = pp.Particle(access_token='PARTICLE_ACCOUNT_TOKEN')

#  reference to list of devices linked to particle account
devices = particle.list_devices()
# particle photon is only device linked, therefore at index 0
device = devices[0]
# print to confirm correct device selected
print('Selected device: %s' % device['name'])

# location of cat
isInside = True
# set to false to prevent continous listening
keepListening = True
# when startStatus != IsInside, the cat has been detected
startStatus = True

# Output to terminal once the bot is ready to process commands
@client.event
async def on_ready():
    print("Bot is ready.")

# Makes web request to call particle function 'lock'
# Activate this function will lock or unlock the cat door
# Usage: .lock
@client.command()
async def lock(context):
    global particle
    particle.call_function(device['id'], 'lock', 10)
    await context.send('Door locked')


# Stops the program contiously checking for changes in cat status
# Usage: .stopListening
@client.command()
async def stopListening(context):
    global keepListening
    keepListening = False
    await context.send('... Listening stopped')


#  Discord output stating cat location
#  Usage: .status
@client.command()
async def status(context):
    global isInside
    if(isInside):  await context.send('Cat is inside.')
    else: await context.send('Cat is outside.')

# Starts cat detection listener
# Usage: .listen
@client.command()
async def listen(context):
    # Discord feedback
    await context.send("Listening...")
    # Start listener on another thread so bot stays responsive during loop
    _thread.start_new_thread(listenLooper, (context,) )
    #  Provide discord feedback on change
    await outputLoop(context)

# Checks once every second if the cat has been detected
async def outputLoop(context):
    global startStatus
    global isInside
    # While user has not ended loop and cat has not been detected
    while(startStatus == isInside & keepListening):
        await asyncio.sleep(1)
        if startStatus != isInside:
            status(context)
            startStatus = isInside

# Continously makes web requests to check published events by particle photon
def listenLooper(context):
    global isInside
    global keepListening
    while keepListening:
        for msg in messages:
            if(str(msg) != ''): 
                isInside = not isInside
                break
            if(not keepListening):
                break
    keepListening = True

# Starts the bot, causing it to join the server
client.run('BOT_TOKEN')