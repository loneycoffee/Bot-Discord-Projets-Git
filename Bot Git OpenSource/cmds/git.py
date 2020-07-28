import discord
from discord.ext import commands
import asyncio

class Git(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.bot_id= #id du bot
        self.channel= #channel où sont réceptionnés les projets pour une confirmation
        self.channel_projets_id =  #channel où sont postés les projets
        self.yes = "" #emoji yes
        self.no = "" #emoji no
        self.erreur = "" #emoji erreur
        self.plus = "" #emoji plus
        self.moins = "" #emoji moins
        self.attention ="" #emoji attention

    @commands.Cog.listener()
    async def on_ready(self):
        print('[+] Extension "Projets Git" Activée')

    
    # On_raw_reaction_add pour check la reaction ajoutée sur le channel de vérification

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):

        # Check de la reaction yes

        if payload.channel_id==self.channel and payload.user_id!=self.bot_id and str(payload.emoji)==self.yes:

            channel_projets=self.bot.get_channel(self.channel_projets_id)
            channel = self.bot.get_channel(payload.channel_id)
            user = self.bot.get_user(payload.user_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.clear_reactions()
            embed = msg.embeds[0]
            user_git = self.bot.get_user(int(embed.footer.text))
            await channel_projets.send(f"**Projet Git ❱** {user_git.mention}")
            ok = discord.Embed(color=0xffffff,description=f"{embed.description}")
            ok.set_author(name=f"Projet Git de {user_git}",url=user_git.avatar_url)
            ok.set_thumbnail(url=user.avatar_url)
            ok_embed = await channel_projets.send(embed=ok)
            await channel.send(f"{self.yes} **Acceptation** ❯{user.mention} a validé le projet de **{embed.author.name}** ({embed.footer.text})")
            valid=discord.Embed(color=0xecf0f1,description=f"[Lien du projet dans ce channel](https://discordapp.com/channels/{payload.guild_id}/{payload.channel_id}/{payload.message_id}/)\n[Lien du projet dans le channel des projets](https://discordapp.com/channels/{ok_embed.guild.id}/{ok_embed.channel.id}/{ok_embed.id}/)")
            await channel.send(embed=valid)
            try:
                embed= discord.Embed(description=f"{self.yes} Votre projet Git a été accepté.",color=0x2ecc71)
                await user_git.send(embed=embed)
            except:
                pass

        # Check de la reaction no

        elif payload.channel_id==self.channel and payload.user_id!=self.bot_id and str(payload.emoji)==self.no:

            channel = self.bot.get_channel(payload.channel_id)
            user = self.bot.get_user(payload.user_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.clear_reactions()
            embed = msg.embeds[0]
            user_git = self.bot.get_user(int(embed.footer.text))
            await channel.send(f"{self.no} **Refus** ❯ {user.mention} a refusé le projet de **{embed.author.name}** ({embed.footer.text})")
            refus=discord.Embed(color=0xecf0f1,description=f"[Lien du projet dans ce channel](https://discordapp.com/channels/{payload.guild_id}/{payload.channel_id}/{payload.message_id}/)")
            await channel.send(embed=refus)
            try:
                embed= discord.Embed(description=f"{self.no} Votre projet Git a été refusé.",color=0xe74c3c)
                await user_git.send(embed=embed)
            except:
                pass

    @commands.command()
    async def git(self,ctx,arg:str=None):
        try:
            if arg==None:
                if str(ctx.channel.type)!= "private":
                    await ctx.send(f"<:yes:729375491198550078> ❱ Le tutoriel vous a été envoyé en privé **{ctx.author}** !")
                help=discord.Embed(title="❓ ❯ Comment utiliser le bot ?",description="Hey cette commande a été créer dans le but de permettre le partage de projets git, ci-dessous vous aurez plus d'informations.")
                help.add_field(name="📌 ❯ Critères pour ajouter son projet",
                value=f"• Ils seront à but non-lucratif obligatoirement."
                f"\n\n• Il faudra un repo Git public afin de nous permettre une vérification du projet lors de son développement."
                f"\n\n• Nous nous réservons le droit de refuser n'importe quel projet. Bien sûr la cause vous sera expliquée."
                f"\n\n• Vous ne pourrez faire une demande de projet qu'une fois tous les 2/3 jours"
                f"\n\n• Les projets du type 'serveur minecraft', 'plugin minecraft', 'hacking' et j'en passe seront refusés par défaut.",inline=False)
                help.add_field(name=f"{self.plus} ❯ **Ajouter son projet**",value=f"• **Commande** : !git add\n• **Description** : Cela vous permet l'ajout d'un projet git.",inline=False)
                help.add_field(name=f"{self.moins} ❯ **Annuler son projet**",value=f"{self.attention} Fonctionne uniquement si vous êtes en train d'utiliser la commande !git add\n\n• **Commande** : !git stop\n• **Description** : Cela vous permet d'annuler le projet en cours.\n\n{self.attention} ❯ **Tout abus sera sanctionné.**",inline=False)
                help.set_thumbnail(url="https://pbs.twimg.com/profile_images/962245744848719874/rz6DDZSJ_400x400.png")
                await ctx.author.send(embed=help)
            elif arg=="add":
                if str(ctx.channel.type) == "private":
                    def check(m):
                        if (m.author == ctx.author) and (m.author!=self.bot_id) and ("!git add" not in m.content and "!git" not in m.content and "!git stop" and "!git_stop" and "!git del" not in m.content and "!git_del" not in m.content):
                            return True
                        elif ((m.author == ctx.author) and (m.author!=self.bot_id)) and ("!git stop" in m.content or "!git_stop" in m.content or "!git del" in m.content or "!git_del" in m.content):
                            raise Annulation
                        elif (m.author == ctx.author) and (m.author!=self.bot_id) and ("!git add" in m.content or "!git" in m.content):
                            raise AntiCMD
                        else:
                            pass
                    embed = discord.Embed(description=f"{self.plus} ❯ Projet Git\n\n• Vous venez de commencer à **ajouter** votre projet Git.\n\n{self.moins} ❯ Annuler son projet\n\n• Pour annuler votre projet à tout moment pendant cette commande vous pouvez utiliser la commande **!git stop**",color=0x2ecc71)
                    await ctx.author.send(embed=embed)
                    embed = discord.Embed(description=f"Ecrivez le nom du projet :",color=0xe67e22)
                    await ctx.author.send(embed=embed)
                    nom_projet = await self.bot.wait_for('message', check=check,timeout=60.0)
                    await nom_projet.add_reaction('👌')
                    embed = discord.Embed(description=f"Ecrivez le pseudo du gérant du projet (exemple : bot#0000) :",color=0xe67e22)
                    await ctx.author.send(embed=embed)
                    gerant = await self.bot.wait_for('message', check=check,timeout=60.0)
                    await gerant.add_reaction('👌')
                    embed = discord.Embed(description=f"Ecrivez le but du projet :",color=0xe67e22)
                    await ctx.author.send(embed=embed)
                    but = await self.bot.wait_for('message', check=check,timeout=60.0)
                    await but.add_reaction('👌')
                    embed = discord.Embed(description=f"Ecrivez les personnes recherchées :",color=0xe67e22)
                    await ctx.author.send(embed=embed)
                    recherche = await self.bot.wait_for('message', check=check,timeout=60.0)
                    await recherche.add_reaction('👌')
                    embed = discord.Embed(description=f"Ecrivez le nombre de personnes minimum pour la réalisation du projet :",color=0xe67e22)
                    await ctx.author.send(embed=embed)
                    nombre = await self.bot.wait_for('message', check=check,timeout=60.0)
                    await nombre.add_reaction('👌')
                    embed = discord.Embed(description=f"Ecrivez le lien du Git :",color=0xe67e22)
                    await ctx.author.send(embed=embed)
                    git = await self.bot.wait_for('message', check=check,timeout=60.0)
                    await git.add_reaction('👌')
                    embed = discord.Embed(description=f"**Votre projet Git actuel :**\n\n"
                                                      f"• **Nom du projet :** \n❱ {nom_projet.content}\n\n"
                                                      f"• **Gérant du projet :** \n❱ {gerant.content}\n\n"
                                                      f"• **But du projet :** \n❱ {but.content}\n\n"
                                                      f"• **Type de personnes recherchées :** \n❱ {recherche.content}\n\n"
                                                      f"• **Nombre de personnes minimum pour le projet :** \n❱ {nombre.content}\n\n"
                                                      f"• **Lien du Git :** \n❱ {git.content}",color=0xe67e22)
                    await ctx.author.send(embed=embed)  
                    embed = discord.Embed(description=f"**Voulez-vous envoyer cette demande de projet ?** \n❱ Réagissez avec <:yes:729375491198550078> pour **Oui** ou <:no:729375503684862003> pour **Non**.",color=0xe67e22)
                    msg= await ctx.author.send(embed=embed)
                    await msg.add_reaction(self.yes)
                    await msg.add_reaction(self.no)
                    def check_emoji(reaction, user):
                        emojis=[self.yes,self.no]
                        return user == ctx.author and str(reaction.emoji) in emojis and reaction.message.id==msg.id
                    reaction,user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check_emoji)
                    if str(reaction.emoji) == self.yes:
                        embed= discord.Embed(description=f"Projet Git envoyé !",color=0x2ecc71)
                        await ctx.author.send(embed=embed)
                        channel_projets=self.bot.get_channel(self.channel)
                        embed = discord.Embed(description=f"• **Nom du projet :** \n❱ {nom_projet.content}\n\n"
                                                      f"• **Gérant du projet :** \n❱ {gerant.content}\n\n"
                                                      f"• **But du projet :** \n❱ {but.content}\n\n"
                                                      f"• **Type de personnes recherchées :** \n❱ {recherche.content}\n\n"
                                                      f"• **Nombre de personnes minimum pour le projet :** \n❱ {nombre.content}\n\n"
                                                      f"• **Lien du Git :** \n❱ {git.content}",color=0xf1f2f6)
                        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
                        embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
                        embed.set_footer(text=f"{ctx.author.id}")
                        msg = await channel_projets.send(embed=embed)
                        await msg.add_reaction(self.yes)
                        await msg.add_reaction(self.no)
                    elif str(reaction.emoji) == self.no:
                        embed = discord.Embed(description=f"{self.no} ❱ Vous avez décidé d'annuler votre demande de projet Git.",color=0xe74c3c)
                        await ctx.author.send(embed=embed)
                    else:
                        pass
                else:
                    await ctx.send(f"{self.erreur} ❱ **Erreur :** Commandes uniquement en mp !")
        except asyncio.TimeoutError:
            embed = discord.Embed(description=f"{self.no} ❱ Temps expiré pour faire votre demande, veuillez la refaire.",color=0xe74c3c)
            await ctx.author.send(embed=embed)
        except Annulation:
            embed = discord.Embed(description=f"{self.no} ❱ Vous avez décidé d'annuler votre demande de projet Git.",color=0xe74c3c)
            await ctx.author.send(embed=embed)
        except AntiCMD:
            embed = discord.Embed(description=f"{self.no} ❱ Vous avez essayé d'utiliser une commande en tant qu'argument, dommage ça aurait pu faire crash le bot mais on a tout prévu ^^.",color=0xe74c3c)
            await ctx.author.send(embed=embed)
        except:
            embed = discord.Embed(description=f"{self.erreur} ❱ Erreur : Veuillez vérifier que vous acceptez les messages privés de la part du bot.",color=0xe74c3c)
            await ctx.author.send(embed=embed)


def setup(bot):
    bot.add_cog(Git(bot))


class AntiCMD(Exception):
    pass

class Annulation(Exception):
    pass
