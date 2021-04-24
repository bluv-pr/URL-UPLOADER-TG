#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    #TRChatBase(update.from_user.id, update.text, "/help")
    update_channel = Config.UPDATE_CHANNEL

    if update_channel:

        try:

            user = await bot.get_chat_member(update_channel, update.chat.id)

            if user.status == "kicked":

               await update.reply_text(" Sorry, You are **B A N N E D**")

               return

        except UserNotParticipant:

            #await update.reply_text(f"Join @{update_channel} To Use Me")

            await update.reply_text(

                text="**Oh Dear In Order To Use Me Join My Update Channnl 🤭**",

                reply_markup=InlineKeyboardMarkup([

                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]

              ])

            )

            return

        else:
            await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["me"]))
async def get_me_info(bot, update):
    # logger.info(update)
    #TRChatBase(update.from_user.id, update.text, "/me")
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text(" Sorry, You are **B A N N E D**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="**Oh Dear In Order To Use Me Join My Update Channnl 🤭**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, plan_type, expires_at),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    #TRChatBase(update.from_user.id, update.text, "/start")
    update_channel = Config.UPDATE_CHANNEL

    if update_channel:

        try:

            user = await bot.get_chat_member(update_channel, update.chat.id)

            if user.status == "kicked":

               await update.reply_text(" Sorry, You are **B A N N E D**")

               return

        except UserNotParticipant:

            #await update.reply_text(f"Join @{update_channel} To Use Me")

            await update.reply_text(

                text="**Oh Dear In Order To Use Me Join My Update Channnl 🤭**",

                reply_markup=InlineKeyboardMarkup([

                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]

              ])

            )

            return

        else:
          await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    #TRChatBase(update.from_user.id, update.text, "/upgrade")
    update_channel = Config.UPDATE_CHANNEL

    if update_channel:

        try:

            user = await bot.get_chat_member(update_channel, update.chat.id)

            if user.status == "kicked":

               await update.reply_text(" Sorry, You are **B A N N E D**")

               return

        except UserNotParticipant:

            #await update.reply_text(f"Join @{update_channel} To Use Me")

            await update.reply_text(

                text="**Oh Dear In Order To Use Me Join My Update Channnl 🤭**",

                reply_markup=InlineKeyboardMarkup([

                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]

              ])

            )

            return

        else:
           await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
