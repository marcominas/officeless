#!/usr/bin/python
# -*- coding: utf-8 -*

from os import environ
from _settings import bot_user_oauth_access_token

RTM_READ_DELAY = 1  # 1 second delay between reading from RTM


def get_slack_bot_token():
    bot_token = environ.get('SLACK_OFFICELESS_TOKEN')
    if not bot_token:
        bot_token = bot_user_oauth_access_token
    return bot_token
