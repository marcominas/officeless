#!/usr/bin/python
# -*- coding: utf-8 -*

from time import sleep

from settings import RTM_READ_DELAY
from officeless.bot import slack_client
from officeless.bot import handle_command
from officeless.bot import parse_bot_commands


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running! ^C exit.")
        officeless_bot_id = slack_client.api_call("auth.test")["user_id"]
        looping = True
        while looping:
            try:
                cmd, chn = parse_bot_commands(slack_client.rtm_read())
                if cmd:
                    handle_command(command=cmd, channel=chn)
                sleep(RTM_READ_DELAY)
            except KeyboardInterrupt:
                looping = False
                print('Exiting gracefully.')
    else:
        print("Connection failed. Exception traceback printed above.")
