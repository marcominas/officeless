#!/usr/bin/python
# -*- coding: utf-8 -*

from re import search

from slackclient import SlackClient

from officeless.tip import do_valid_action
from officeless import COMMAND_LIST
from settings import get_slack_bot_token

MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
officeless_bot_id = None

slack_client = SlackClient(get_slack_bot_token())


def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and "subtype" not in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == officeless_bot_id:
                return message, event["channel"]
    return None, None


def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    default_response = "Not sure what you mean. Try *{}*.".format(", ".join(COMMAND_LIST))
    action, *params = command.split()
    response = None

    if action in COMMAND_LIST:
        response = do_valid_action(action, params)
    text = response or default_response
    slack_client.api_call("chat.postMessage", channel=channel, text=text)
