import discord
from .services.trigger_manager import TriggerManager
from .constants import LOGGED_IN_LOG, PROCESSED_LOG, SYSTEM_ERROR
from .exceptions import ValidationException


class SearchBotConnectionView(discord.Client):
    """Short summary.

    This is an event driven view for discord websocket, it
    triggers events based on the actions performed by the
    suscribed user.

    """

    async def on_ready(self):
        """Short summary.

        An onReady event to check if connection is made
        successfully.

        """
        # used print instead of LOG
        print(LOGGED_IN_LOG.format(self.user))

    async def on_message(self, message):
        """Short summary.

        Parameters
        ----------
        message : Discord message object
            it holds the user content and user info.

        Returns
        -------
        def
            Description of returned object.

        """
        try:
            trigger_manager = TriggerManager(message)
            reply, embed = trigger_manager.perform_operation()
            if reply or embed:
                await message.channel.send(reply, embed=embed)
                # used print instead of LOG
                print(
                    PROCESSED_LOG.format(
                        content=message.content, user=message.author.name
                    )
                )
        except ValidationException as e:
            print(str(e))
            await message.channel.send(str(e))
        except Exception as e:
            print(str(e))
            await message.channel.send(SYSTEM_ERROR)
