import discord
from discord.ext import commands
import asyncio
from classes import donjonInstance
import logging

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='!')
counter = 0
dj_list = []

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.content.startswith('Tu en penses quoi toi mon petit bot ?'):       
        await bot.send_message(message.channel, 'Je préfère clairement celle avec les 4 bières mon cochon...')

@bot.command(pass_context=True)
async def purge(context, number : int):
	"""Clear a specified number of messages in the chat"""
	deleted = await bot.purge_from(context.message.channel, limit=number)
	await bot.send_message(context.message.channel, 'J\'ai supprimé {} messages... c\'est qu\'ça cause pas mal par ici !'.format(len(deleted)))

    
@bot.command(pass_context=True, name='mm+')
async def mmplus(context, *args):
    global dj_list
    global counter
    if len(args) == 0:
        await bot.send_message(context.message.channel, 'Va falloir revoir ta requête gamin... je te filerai un mode d\'emploi à l\'occase')

    elif args[0] == 'create':
        if len(args) != 4:
            await bot.send_message(context.message.channel, 'Créer un appel à la baston en donjon ? Rien de plus simple, demande moi:\n**!mm+ create <clé> <pseudo - ilvl - classe> <heure>** ')
        else:
            dj = donjonInstance(counter, args[1], args[2], args[3])
            counter += 1
            dj_list.append(dj)
            await bot.send_message(context.message.channel, dj.print_full())
    
    elif args[0] == 'tag':
        if len(args) != 6:
            await bot.send_message(context.message.channel, 'S\'inscrire à une bonne castagne ? Fastoche, demande moi:\n**!mm+ tag <djID> <dps/tank/heal> <pseudo> <classe> <ilvl>** ')            

        else:
            ret = dj_list[int(args[1])].add_player(args[2], args[3], args[4], args[5])
            if ret==2:
                bot.send_message(context.message.channel, 'Personnage déjà inscrit !')
            else:
                await bot.send_message(context.message.channel, dj_list[int(args[1])].print_full())

    elif args[0] == 'untag':
        if len(args) != 3:
            await bot.send_message(context.message.channel, 'Tu te dégonfles mon chou ? Pas grave viens prendre une bonne pinte ;)\n**!mm+ untag <djID> <pseudo>** ')            

        else:
            dj_list[int(args[1])].remove_player(args[2])
            await bot.send_message(context.message.channel, dj_list[int(args[1])].print_full())

            



bot.run('NDIyNzkxNzU1MDk2NjUzODM0.DYhKfQ.7P1VOJ1ljsxqVvAUU1dTo0ONuX4')