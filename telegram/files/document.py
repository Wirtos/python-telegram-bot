#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2020
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains an object that represents a Telegram Document."""

from telegram import PhotoSize, TelegramObject


class Document(TelegramObject):
    """This object represents a general file (as opposed to photos, voice messages and audio files).

    Attributes:
        file_id (:obj:`str`): Access identifier for this file.
        file_unique_id (:obj:`str`): Unique identifier for this file.
        thumb (:class:`telegram.PhotoSize`): Optional. Document thumbnail.
        file_name (:obj:`str`): Original filename.
        mime_type (:obj:`str`): Optional. MIME type of the file.
        file_size (:obj:`int`): Optional. File size.
        bot (:class:`telegram.Bot`): Optional. The Bot to use for instance methods.

    Args:
        file_id (:obj:`str`): Access identifier for this file.
        file_unique_id (:obj:`str`): Unique identifier for this file.
        thumb (:class:`telegram.PhotoSize`, optional): Document thumbnail as defined by sender.
        file_name (:obj:`str`, optional): Original filename as defined by sender.
        mime_type (:obj:`str`, optional): MIME type of the file as defined by sender.
        file_size (:obj:`int`, optional): File size.
        bot (:class:`telegram.Bot`, optional): The Bot to use for instance methods.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    """
    _id_keys = ('file_id',)

    def __init__(self,
                 file_id,
                 file_unique_id,
                 thumb=None,
                 file_name=None,
                 mime_type=None,
                 file_size=None,
                 bot=None,
                 **kwargs):
        # Required
        self.file_id = str(file_id)
        self.file_unique_id = str(file_unique_id)
        # Optionals
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.bot = bot

        self._id_attrs = (self.file_id,)

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        data = super(Document, cls).de_json(data, bot)

        data['thumb'] = PhotoSize.de_json(data.get('thumb'), bot)

        return cls(bot=bot, **data)

    def get_file(self, timeout=None, **kwargs):
        """Convenience wrapper over :attr:`telegram.Bot.get_file`

        Args:
            timeout (:obj:`int` | :obj:`float`, optional): If this value is specified, use it as
                the read timeout from the server (instead of the one specified during creation of
                the connection pool).
            **kwargs (:obj:`dict`): Arbitrary keyword arguments.

        Returns:
            :class:`telegram.File`

        Raises:
            :class:`telegram.TelegramError`

        """
        return self.bot.get_file(self.file_id, timeout=timeout, **kwargs)
