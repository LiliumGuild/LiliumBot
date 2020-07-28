# LiliumBot

A bot for the Lilium Discord. 

## Features Wanted

- General Command Prompts.
- LFG Finder
- Event Scheduler 

## General Command Prompts.

Simply put, The users should be able to type some command and recieve some response. Most of the basic commands are already implemented using [Cogs](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html). Basically we can separate all the type of commands by file. So one file for General Commands, one for suggestion commands and one for Admin commands (working on that atm)
This just keeps things tidy.

## LFG Finder

This will be a 2 parter relating to the general command prompts. Users should be able to set a role for themselves (Tank, Healer, Damage) and users with a role should be able to create a group finder for Dungeons.

For example if someone with the role damage types !Library a message should pop up along the lines of:

<User> is looking for a group for <Dungeon>

Tank    Healer    Damage
0/1     0/1       1/3
---     ---       ---

  
It would also display the names of the people who want to join under the role

People who are also looking to do the Library should be notified. We can do this with Roles too.


## Event Scheduler

This will probably be the the hardest to implement. It may be better to just hardcode any upcoming events. As the raid will be everyday. 


## .gitignore files

There are 2 files that are to be kept local. secrets.py and config.py

### secrets.py
This is where we store our discord token.
Stored as a string

    DISCORD_TOKEN = ""
    
### config.py
This is where we store the config for the different channels. This is currently used for storing the discord channel keys but will also store more information in future like message cooldown timer. Stored as an int

    OFFICER_CHANNEL = 
    EVENT_CHANNEL = 
    MEDIA_CHANNEL = 
    GRAPHIC_CHANNEL =  
    RAID_CHANNEL = 
    RECRUITMENT_CHANNEL = 
 
