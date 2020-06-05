# Embedded-Prototype

## Dependencies

# dbl
https://github.com/DiscordBotList/DBL-Python-Library

# discord.py
https://github.com/Rapptz/discord.py

# pyparticle
https://github.com/howardpaget/pyparticle

# sseclient
https://pypi.org/project/sseclient/


## Setup

After installing all dependencies, replace all areas containing "PARTICLE_ACCOUNT_TOKEN" with token of your particle account. You can get this by downloading the particle CLI at https://docs.particle.io/tutorials/developer-tools/cli/ and using the command "particle token list".

"BOT_TOKEN" should be replaced with the token of a discord bot, or you can use my token Njk2MzIzMTIzMTA4MzgwNzAy.XtpacQ.YZlM-Wno2wP70-wfjQntKKzzjfU

System 1 (particle photon/argon) should have particle-code flashed to it.

Install and open Discord on PC or phone.

Make bot join your channel (create an empty channel if you don't have one) by using https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot and replace "CLIENT_ID" with the client id of your bot, or use mine https://discord.com/oauth2/authorize?client_id=696323123108380702&scope=bot

System 2 (Raspberry pi, or PC) should run embedbot.py using "python embedbot.py" or "python3 embedbot.py".

Bot should become available.

You can now issue commands to bot. E.g, 

.help
.listen




