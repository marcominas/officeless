#!/usr/bin/python
# -*- coding: utf-8 -*

from officeless import COMMAND_LIST

tip_title_dict = {
    "1": "Tip number 01 - wired net",
    "2": "Tip number 02 - use virtual resources",
    "3": "Tip number 03 - do remote meetings",
    "4": "Tip number 04 - only one speaks at a time",
    "5": "Tip number 05 - send link at invite",
    "6": "Tip number 06 - work day is to work",
    "7": "Tip number 07 - context is always necessary",
    "8": "Tip number 08 - use a comfortable clothes"
}
tip_dict = {
    "1": "Wired net *** NEED FULL TIP HERE",
    "2": "Use virtual resources *** NEED FULL TIP HERE",
    "3": "Do remote meetings *** NEED FULL TIP HERE",
    "4": "Only one speaks at a time *** NEED FULL TIP HERE",
    "5": "Send link at invite *** NEED FULL TIP HERE",
    "6": "Work day is to work *** NEED FULL TIP HERE",
    "7": "Context is always necessary *** NEED FULL TIP HERE",
    "8": "Use a comfortable clothes *** NEED FULL TIP HERE"
}


def do_valid_action(action, params):
    action = get_officeless_bot_action(action)
    response = "Sure...write some more code then I can do that!"

    if action == "tips":
        response = get_tip_list()
    elif action == "tip":
        response = get_tip(params)
    elif action == "history":
        response = "I don't have your history yet. Sorry."
    elif action == "help":
        response = "Try some of these commands: {commands}".format(commands=", ".join(COMMAND_LIST))

    print("action: {action}".format(action=action))
    return response


def get_officeless_bot_action(action) -> str:
    action = str(action)
    if not action.islower():
        action = action.lower()
    return action


def get_tip_list():
    global tip_title_dict

    response = "These are the available tips until now:\n"
    for tip in tip_title_dict:
        response += " * {tip} - {title}\n".format(tip=tip, title=tip_title_dict[tip])
    return response


def get_tip(params):
    global tip_dict

    response = None
    default_response = "I don't find this tip here. Sorry."
    for param in params:
        if param in tip_dict:
            response = "Tip #{num}: ".format(num=param)
            tip = tip_dict[param]
            response += "{tip}\n\n".format(tip=tip)

    return response or default_response
