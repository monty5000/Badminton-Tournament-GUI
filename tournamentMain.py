# **********************************************************************************************************************
# **********************************************************************************************************************
#
# Name:
#
#   tournamentMain.py
#
# Version:
#
#   version:: TG_0.2, NOTE also update variable 'version' below
#
# Purpose:
#
#   Badminton Tournament GUI using PySimpleGUI
#
# Notes:
#
#   Updated version of tournamentGUI
#
# Author:
#
#   Martin Burns
#
# **********************************************************************************************************************
# **********************************************************************************************************************

#################
# further notes #
#################
# total matches for n even teams is n-1 rounds with n/2 matches per round (2 teams is 1 matches, 4 is 6)
# total matches for n odd teams is n rounds with (n-1)/2 matches per round (3 teams is 3 matches, 5 is 10)
# 3 teams play order: 1v2, 3v1, 2v3
# 4 teams play order: 1v2, 3v4, 1v4, 2v3, 1v3, 2v4
# 5 teams play order: 4v1, 3v2, 3v5, 2v1, 2v4, 1v5, 1v3, 5v4, 5v2, 4v3

##########
# Issues #
##########
# use of expand_x and expand_y seem to have undesirable behaviour in that the element consumes more than the space
# it should
# known bug with toggling element visibility; element position then changes.  Use of 'pin' works but has a bug in that
# it will not inherit the background colour of the element it is pinning


import os
import PySimpleGUI as sg
from pathlib import Path
import json

from devLogger import DevLogger
from tournamentClass import GuiWindow
from tournamentFunctions import *
from templateTournamentVars import templateJSON as templateJSON

# vars
log = DevLogger(print_logging=False, log_level=2)
logExtra = os.path.basename(__file__)
version = "TG_0.2"     # TournamentGUI2 version 0.2

try:

    log.info("::[%s]:: Script is running" % logExtra)
    guiWindow = GuiWindow(log, version)

    while True:
        event, values = guiWindow.window.read()

        if event == "EXIT_HOME" or event == sg.WIN_CLOSED:
            break

        if event == "New":
            # load default JSON into working data dictionary to be updated by popup_new_tournament() window
            workingData = json.loads(templateJSON)
            new_tournament_dict = popup_new_tournament()

            # if popup_new_tournament() window is closed it returns False
            if new_tournament_dict:

                for i in new_tournament_dict:
                    # one of the dict keys is the description, one is max points and the rest are the groups
                    if((i != "tournament_description") and (i != "max_game_points")):
                        if new_tournament_dict[i] == "0":
                            workingData[i]["config"]["active"] = False
                        else:
                            workingData[i]["config"]["active"] = True
                        # set group size
                        workingData[i]["config"]["grp_size"] = new_tournament_dict[i]

                    if i == "tournament_description":
                        workingData["tournament"]["description"] = new_tournament_dict["tournament_description"]

                    if i == "max_game_points":
                        workingData["tournament"]["max_game_points"] = new_tournament_dict["max_game_points"]

                guiWindow.window["DATA_DESCRIPTION"].update(new_tournament_dict["tournament_description"])
                guiWindow.window["LAUNCH_BUTTON"].update(disabled=False)

        if event == 'Load Selected':
            loadFile = values["MY_LOAD_FILE"]
            if Path(loadFile).is_file():
                try:
                    with open(loadFile, "rt", encoding='utf-8') as f:
                        fileContent = f.read()
                        workingData = json.loads(fileContent)

                        # try to parse the validation check, if it does not exist then set to invalid
                        try:
                            load_validation = workingData["tournament"]["validation_check"]
                        except:
                            load_validation = "invalid"

                        if load_validation == "valid":
                            guiWindow.window["DATA_DESCRIPTION"].update(workingData["tournament"]["description"])
                            guiWindow.window["LAUNCH_BUTTON"].update(disabled=False)
                        else:
                            popup_file_invalid()

                except Exception as e:
                    log.error("::[%s]:: Exception caught loading file: %s" % (logExtra, str(e)))
                    popup_exception("Event was Load Selected\nDetail:\n" + str(e))

        if event == "LAUNCH_BUTTON":
            guiWindow.popup_launch_tournament(workingData)

        if event == "HELP":
            popup_help()

    guiWindow.window.close()

except Exception as e:
    log.error("::[%s]:: Exception encountered: %s" % (logExtra, str(e)))
