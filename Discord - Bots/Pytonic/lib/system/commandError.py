# Python Responsories
import sys
import traceback
import random as r

#   Asynico Responsories
from asyncio.exceptions import TimeoutError

#   Discord Responsories
import discord as d
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog
from discord.ext.commands.errors import CheckFailure, CommandNotFound, MissingRequiredArgument, BadArgument, MemberNotFound, CommandInvokeError

class ErrorHandler(Cog):

    """
        Copyright (C) 2023  Kristoffer Gjøsund

        A collection of reaction games

        >   Creation Date   : 01.01-23
        >   Last update     : 

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
    """

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_red())

        return

    #   Calls when there is an error
    @Cog.listener()
    async def on_command_error(self, ctx:d.ApplicationContext, error):

        '''
            #   Triggers when an error is raised while invoking a command.Parameters

            #   ctx:    commands.Context
            #   #   The context used for command invocation.

            #   commands.ErrorDictionary
            #   #   The Exception which will be raised.

        '''

       #    Classes initialization
        BadArgs = BadArgument
        timeout = TimeoutError
        roleError = CheckFailure
        NotFound = MemberNotFound
        attribute = AttributeError
        invokeError = CommandInvokeError
        cmdError = ErrorMessageDictionary

        botDM = await self.bot.fetch_user(340540581174575107)
        botmsg = None

        #   Member not found 
        if isinstance(error, NotFound):

            #   Prepare & send the embed
            dictionary = cmdError.ErrorDescriptionDictionary(NotFound)
            self.embed.title = 'Member were not found in the server'
            self.embed.description = dictionary
            await ctx.send(embed= self.embed)

        #   Role not satisified
        elif isinstance(error, roleError):

            # Prepare & send the embed
            dictionary = cmdError.ErrorDescriptionDictionary(roleError)
            self.embed.title = 'Unauthorized Role'
            self.embed.description = dictionary
            await ctx.send(embed=self.embed)

        #   Non Discord errors
        elif isinstance(error, invokeError):

            if isinstance(error.original, timeout):
 
                #   Prepare & Send the message
                timeout = str(timeout)

                self.embed.title = "The Game is over"
                self.embed.description = cmdError.ErrorDescriptionDictionary(timeout[27:39])
                await ctx.send(embed=self.embed)

            elif isinstance(error.original, attribute):

                #   Prepare and send the embed
                errorModule = str(attribute)

                self.embed.title = "Attribute error"
                self.embed.description = cmdError.ErrorDescriptionDictionary(errorModule[8:22])
                await ctx.send(embed=self.embed)

                botmsg = f"Master, there is an error with an {errorModule[8:22]} Error were found. {error.original}"
                await self.bot.send(f'{botmsg}', tts = True)

            elif isinstance(error.original, BadArgs):

                #   Prepare & send the embed
                errorModule = str(BadArgs)
                botmsg = f"Master, There is some  {errorModule} Error were found. {error.original}"

                self.embed.title = "You sent me a Bad Arguments"
                self.embed.description = cmdError.ErrorDescriptionDictionary(errorModule)
                await ctx.send(embed=self.embed)

                await self.bot.send(f'{botmsg}', tts = True)

        else:

            # If none of the above, print it in the terminal
            print('Ignoring exception in command {}:\n\n'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        if botmsg !=None: await botDM.send(f'{botmsg}', tts = True)

        return

class ErrorMessageDictionary():

    def __init__(self) -> None:
        pass

    def ErrorDescriptionDictionary (error, *cmd):

        match error:

            case "CommandNotFound":
                dictionary = {
                                1:'meep morp zeep :(\n',
                                2:'Given command does not exists',
                                3:'Sir, have you drunken to much?',
                                4:'We all do mistakes, sometimes...',
                                5:f'Sir where did you find the "{cmd}" ',
                                6:'Sir, im sorry, could you please repeat the command?',
                                7:'Sir The command has not been impleted in my software',
                                8:'Command Executed, if you see this message, check your spelling.',
                                9:f'I have some good news, sir. Im a good boy. Command already executed {cmd}',
                                10:f'Sir, an error has emerged \"{cmd}\" were not found in bot command dictionary',
                                11:'Sir, you\'ve started the "Self destruction protocol", press "enter" to continue, press "esc" to stop.',
                                12:'0101010001101000011001010010000001100011011011110110110101101101011000010110111001100100001000000110010001101111011001010111001100100000011011100110111101110100001000000110010101111000011010010111001101110100',
                            }

            case "MemberNotFound":

                dictionary = {
                                1:'meep, morp, zeep :(\n',
                                2:'Sir, imagne the member where found\n',
                                3:'Sir, if the error continues, check your spelling \n',
                                4:'I regret to inform you, sir. the selected member can not be found in the dictionary, should i make one? \n',
                                5:'010110010110111101110101001000000100010001101111001000000110111001101111011101000010000001101000011000010111011001100101001000000111010001101000011001010010000001110010011001010111000101110101011010010111001001100101011001000010000001110010011011110110110001100101\n',
                                6:'I\'m the bot version for the 99th emoji !',
                                7:f'Just sent out an APB.',
                                8:'We all do mistakes, this time the user doesn\'t exist',
                            }

            case "CheckFailure":

                dictionary = {
                                1:'meep, morp, zeep :(',
                                2:'Role Authorication failed.',
                            }

            case "MissingRequiredArgument":

                dictionary = {
                                1:'meep, morp, meep :(\n',
                                2:'Sir, i just executed the command with-out any arguments...',
                                3:'Sir, should i just fake it?\n',
                                4:'More infomation would do my job easier..',
                                5:'Still missing some leads..',
                                6:'We all do mistakes. You\'re missing some requred arguments ',
                            }

            case "AttributeError":

                dictionary = {
                                1:'meep, morp, zeep :(\n',
                                2:'Sir, Something went horribly wrong',
                                3:'I found out i didnt want to start after all',
                            }

            case "TimeoutError":

                dictionary = {
                                1:'meep, morp, zeep :(\n',
                                2:'Sir, the BOENG 437 just left the airport',
                                3:'Sir, do you need more time?',
                                4:'The game is over',
                                5:'Try again',
                                6:'I decided to cancel the game.',
                                7:'Never got a response in time',
                            }

        #   Randomize the dictionary
        x = len(dictionary)
        x = r.randrange(1, x)

        return dictionary.get(x)
    #   Update requires
    def CommandNameError(cmd):

        prefix = '?'

        dictionary = {
                        #   Community Module
                        'dnd':f'{prefix}{cmd} (message)',
                        'randint':f'{prefix}{cmd} (integer one) (integer two)',

                        #   Moderator module
                        'poll':f'{prefix}{cmd} (poll Name) (ChannelName)',
                        'online':f'{prefix}{cmd} optional (on/off)',
                        'kick':f'{prefix}{cmd} (MemberName) (reason)',
                        'warn':f'{prefix}{cmd} (MemberName) (reason)',
                        'sush':f'{prefix}{cmd} (MemberName) (1(s / m / d / w / y)) (reason)',
                        'lift':f'{prefix}{cmd} (MemberName)',

                        #   Role Management
                        'dero':f'{prefix}{cmd} (RoleName)',
                        'crero':f'{prefix}{cmd} (RoleName)',
                        'remro':f'{prefix}{cmd} (MemberName) (RoleName)',
                        'sero':f'{prefix}{cmd} (MemberName) (roleName) optional (reason)',

                        #   Channel Management / message management
                        'chdel':f'{prefix}{cmd} (Channel Name)',
                        'chcre':f'{prefix}{cmd} (Channel Name)',
                        'cls':f'{prefix}{cmd} (channelName) (lines)',

                        #   Administrator module
                        'unban':f'{prefix}{cmd} (MemberName)',
                        'announce':f'{prefix}{cmd} (channelName)',
                        'ban':f'{prefix}{cmd} (MemberName) (reason)',
                    }
        return dictionary.get(cmd)
