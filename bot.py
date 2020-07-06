import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
PREFIX = '$'

client = commands.Bot(command_prefix= PREFIX )
client.remove_command( 'help')



#
# prefix for aLL DISCORD commands !
#

# Hello Words
hello_words = ['hello', 'hi' , 'privet' ,'salam','salut']
answer = ['server info']
bye_words = ['bye']
pivas = ['piva','pivas']
ion = ['ion']
mihai = ['misha','mihai','misa']
ghost = ['ghost','gost','lavoar']
nikita = ['nikita']

@client.event
async def on_ready():
	print( 'Bot connected' )
	await client.change_presence( status = discord.Status.online, activity = discord.Game( 'with my life' ) )

@client.event 
async def on_message(message):
	author = message.author
	content = message.content
	channel = message.channel
	print('Channel: {} User: {} MSG >> {}'.format(channel, author, content))

@client.event
async def on_message_delete(message):
	author = message.author
	content = message.content
	channel = message.channel
	print('deleted from {} by {} -- msg >>  {}'.format(channel, author, content))


# Check errors 
@client.event 

async def on_command_error( ctx, error ):
	pass

'''
@client.command( pass_context = True )

async def hello( ctx ):
	author = ctx.message.author
	await ctx.send ( f' { author.mention } Hello. I am your new friend!')
	#await ctx.send ( f' { author.mention } ' +  arg)
'''

# assign role to new users


'''  
test
@client.event

async def on_member_join( member ):
	channel = client.get_channel(719098548737802292)

	role = discord.utils.get( member.guild.roles, id = 724680453642256394 )

	await member.add_roles( role )
	await channel.send( embed = discord.Embed( description = f' User ``{member.name}``, connected!' color = 0x3ec95d))
'''

#Clear messages
@client.command( pass_context = True )
@commands.has_permissions( administrator = True)
async def clear( ctx, amount : int  ):
	await ctx.channel.purge( limit = amount)

	await ctx.send( embed =discord.Embed(description = f':white_check_mark: Deleted {amount} messages', color=0x17e208))
#########################################


#Hello with cleared message
@client.command( pass_context = True )

async def hello( ctx, amount = 1 ):
	await ctx.channel.purge( limit = amount )

	author = ctx.message.author
	await ctx.send( f' Hello { author.mention }')
#########################################


#Kick
@client.command( pass_context = True )
@commands.has_permissions( administrator = True)

async def kick( ctx , member: discord.Member, *, reason = None):
	await ctx.channel.purge( limit = 1 )

	await member.kick( reason = reason )
	await ctx.send( f'kick user { member.mention }')
#########################################

#Ban 
@client.command( pass_context = True )
@commands.has_permissions( administrator = True)

async def ban( ctx, member:discord.Member, *, reason = None):
	await ctx.channel.purge( limit = 1 )

	await member.ban( reason = reason )
	await ctx.send( f'Ban user { member.mention }')

#########################################

#Unban
@client.command( pass_context = True )
@commands.has_permissions( administrator = True)

async def unban( ctx, *,  member):
	await ctx.channel.purge( limit = 1 )

	banned_users = await ctx.guild.bans()
	
	for ban_entry in banned_users:
		user = ban_entry.user
		
		await ctx.guild.unban( user )
		await ctx.send(f'Unbanned user {user.mention}')
		
		return 
#########################################


# Command help
@client.command( pass_context = True )
@commands.has_permissions( administrator = True)

async def help( ctx ):
	await ctx.channel.purge( limit = 1 )
	emb = discord.Embed( title = 'Commands ')
	emb.add_field( name = '{}clear'.format( PREFIX),value = 'Clear chat')
	emb.add_field( name = '{}kick'.format( PREFIX),value = 'kick user')
	emb.add_field( name = '{}ban'.format( PREFIX),value = 'ban user')
	emb.add_field( name = '{}unban'.format( PREFIX),value = 'unban user')

	await ctx.send( embed = emb )


# ------------- Test -------------
@client.command( pass_context = True )
@commands.has_permissions( administrator = True)


async def test ( ctx ):
	emb = discord.Embed( title = '')
#----------------------------------




# User mute
@client.command( pass_context = True )
@commands.has_permissions( administrator = True)

async def user_mute( ctx, member:discord.Member):
	await ctx.channel.purge( limit = 1)
	mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute')

	await member.add_roles( mute_role )
	await ctx.send(f'Y {member.mention},cant send messages!')




# send pm msg
@client.command()
@commands.has_permissions( administrator = True)
async def  send_m( ctx, member:discord.Member,arg ):
	await member.send(f'>>> Message from : {ctx.author.name}')
	await member.send(arg)


# send pm private msg	
@client.command()
@commands.has_permissions( administrator = True)
async def  send_pm( ctx, member:discord.Member, *, arg):
	await ctx.channel.purge( limit = 1)
	await member.send(arg)
'''
# random fucntie
@client.command()
async def random( ctx ,member:discord.Member,* , value):
	await ctx.channel.purge( limit = 1 )
	value = random.randint(0, 100)
	await ctx.send( f'{ author.mention } rolled ' + value)
'''
#-----------------------------------------------------------------------------
# bot responses 
@client.event

async def on_message( message ):
	await client.process_commands(message)
	msg = message.content.lower()
	if msg in hello_words:
		await message.channel.send('Hi, what do u need?')
	#if msg in answer:
		#await message.channel.send('Neferions server!')
	if msg in bye_words:
		await message.channel.send('Bye, good luck!')
	if msg in pivas:
		await message.channel.send('Derji pivo pareni')
	if msg in ion:
		await message.channel.send('Ion loh')
	if msg in mihai:
		await message.channel.send('Domnul Mihail, timlider pi zavod, rilax')
	if msg in ghost:
		await message.channel.send('Ghost ciotkii pareni')
	if msg in nikita:
		await message.channel.send('Nikita nacinaiusii goul, officer pda, rabotyaga')




#voice bot

@client.command( pass_context = True )
async def join(ctx):
  global voice
  channel = ctx.message.author.voice.channel
  voice = get(client.voice_clients, guild = ctx.guild)

  if voice and voice.is_connected():
    await voice.move_to(channel)
  else:
    voice = await channel.connect()
    await ctx.send(f'Bot connected to : {channel}')


@client.command( pass_context = True )
async def leave(ctx):
  channel = ctx.message.author.voice.channel
  voice = get(client.voice_clients, guild = ctx.guild)

  if voice and voice.is_connected():
    await voice.disconnect()
  else:
    voice = await channel.connect()
    await ctx.send(f'Bot left : {channel}')


@client.command()
async def play(ctx, *, url : str ):
	song_there = os.path.isfile('song.mp3')

	try:
		if song_there:

			os.remove('song.mp3')
			print('[log] Deleted file')
	except PermissionError:
		print('[log] Cant delete file')
	await ctx.send('Wait please ^^')

	voice = get(client.voice_clients, guild = ctx.guild)

	ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
            }],
        }

	with youtube_dl.YoutubeDL(ydl_opts)  as ydl:
		print('[log] Loading music...')
		ydl.download([url])

	for file in os.listdir('./'):
		if file.endswith('.mp3'):
			name = file
			print(f'[log] Changed file : {file}')
			os.rename(file,'song.mp3')
	voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log] {name}, song was played!'))
	voice.source = discord.PCMVolumeTransformer(voice.source)
	voice.source.volume = 1

	songname = name.rsplit('-', 2)
	await ctx.send(f'Playing now : {songname[0]}')

@client.command(pass_context=True)
async def pause(ctx):
       voice.pause()

@client.command(pass_context=True)
async def resume(ctx):
       voice.resume()

@client.command(pass_context=True)
async def stop(ctx):
       voice.stop()
       
#-----------------------------------------------------------------------------
# errors 
@clear.error
async def clear_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.channel.purge( limit = 1)
		await ctx.send(f'{ ctx.author.name }, write amount !!!')
	if isinstance( error, commands.MissingPermissions):
		await ctx.channel.purge( limit = 1)
		await ctx.send(f'{ ctx.author.name }, No permissions!')


# Connect / get token

token = open ( 'token.txt' , 'r' ).readline()

client.run( token )