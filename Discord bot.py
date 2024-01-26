import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name} ({bot.user.id})')
    print('---')
    @bot.command(name='hello', help='Say hello')
    async def hello(ctx):
        await ctx.send(f'hello') {ctx.author.name}!')
        async def serverinfo(ctx):
        server = ctx.guild 
        text_channels - len(server.txt_channels)
        voice_channels = len(server.voice_channels)
        member = server.member_count

        info = ( 
        f'Server Name: {server.name}\n'
        f'Server ID: {server.id}\n'
        f'Text Channels: {text_channels}\n'
        f'Voice Channels: {voice_channels}\n'
        f'Member Count: {members}'
        )


        await ctx.send(info)
        

        async def clear(ctx, amount: int):
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f'{amount} message cleared by {ctx.author.mention}', delete after=5)



        @bot.event
        async def on_member_join(member):
           if channel: 
               Welcome_message = f'Welcome {member.mention} to {member.guild.name}!!'
               await channel.send(Welcome_message)



@bot.command(name='kick', help='Kick a member from the server')
@commands.has_permissions(kick_members=True)

async def ban(ctx, member: discord.Member, *, reason='No reason provided'):
            await member.ban(reaon=reason)
            await ctx.send(f'{member.mention} has been banned. Reason is: {reason}')


       @bot.command(name='poll', help='Create a poll with yes/no options')
async def poll(ctx, question, *options):
    reactions = ['👍', '👎']
    poll_message = await ctx.send(f'**Poll:** {question}\n\nOptions: {", ".join(options)}')
    
    for reaction in reactions:
        await poll_message.add_reaction(reaction)




@bot.command(name='botinfo', help='Display information about the bot')
async def botinfo(ctx):
    embed = discord.Embed(title='Bot Information', color=discord.Color.blue())
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(name='Bot Name', value=bot.user.name, inline=True)
    embed.add_field(name='Bot ID', value=bot.user.id, inline=True)
    embed.add_field(name='Servers', value=len(bot.guilds), inline=True)
    embed.add_field(name='Command Prefix', value=bot.command_prefix, inline=True)
    embed.set_footer(text='Bot created by Your Name')
    await ctx.send(embed=embed)

@bot.command(name='roll', help='Roll a dice')
async def roll(ctx, user: discord.User = None):
           
           user = user or ctx.author 
           embed = discord.Embed(title=f'{user.name}/' Avatar', color=discord.Color.blue())
                embed.set_image(url=user.avatar_url)
                await ctx.send(embed=embed)
                @bot.command(name='roll', help='Roll a dice')

                
async def roll(ctx, dice: str):
    import re
    match = re.match(r'(\d+)d(\d+)', dice)
    if match:
        num_dice = int(match.group(1))
        num_sides = int(match.group(2))
        import random
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(rolls)
        await ctx.send(f'Rolling {num_dice} {num_sides}-sided dice: {rolls}\nTotal: {total}')
    else:
        await ctx.send('Invalid dice format. Use the format XdY (e.g., 2d6)')
            
           bot.run ('Your token here')