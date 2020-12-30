@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    if reason == None:
        reason = 'Because you were too cutie ^^'

    await ctx.send(f'Banning {member} with the reason **`{reason}`**')
    await member.ban(reason = reason)

@bot.command()
@has_permissions(administrator=True)
async def unban(ctx, id: int = None):
    if id == None:
        await ctx.send('Oopsies but you need an ID!')

    else:
        if len(str(id)) == 18:
            user = await bot.fetch_user(id)
            
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned **{id}**! Welcome back buddy!')

        else:
            await ctx.send(f'Oops! **{id}** doesn\'t seem like a valid ID! Try again!')
