# Class for tournament window

import os
from pathlib import Path
import json
import PySimpleGUI as sg

from tournamentFunctions import *
from groupGeneratorFunctions import *
from templateTournamentVars import icon_shuttle as shuttleIcon

logExtra = os.path.basename(__file__)

all_group_list = ["GRP1", "GRP2", "GRP3", "GRP4", "GRP5", "GRP6", "GRP7", "GRP8"]
all_group_list_int = [1, 2, 3, 4, 5, 6, 7, 8]

class GuiWindow(object):
    """ Class for GUI root window"""

    def __init__(self, log, version):
        """ Constructor

        Notes:

        :param: log: logging object
        :param: version: string for code version
        """
        self.log = log

        self.log.info("::[%s]:: A new GuiWindow instance is created" % logExtra)

        ################
        # main columns #
        ################
        # 1st column
        column1 = [
            [sg.Text("To start choose 'New' or load from previous save", font=("Any 14"))],
            [sg.HSep()],
            [sg.Button('New', font=('Any 14'), tooltip="Create new tournament")],
            [sg.HSep()],
            [sg.Text("Select previous save: ", font=("Any 14")), sg.Input(size=(40, 1)),
             sg.FileBrowse(key="MY_LOAD_FILE", file_types=(('JSON Files', '*.json'),))],
            [sg.Button('Load Selected', font=("Any 14"))],
            [sg.T("")],
            [sg.HSep()],
            [sg.B("Exit", key="EXIT_HOME", font=("Any 14")), sg.B("Help", button_color="green on white", key="HELP",
                                                                  font=("Any 14"))],
            [sg.HSep()],
            [sg.T("")],
            [sg.T("Martin Burns, ", font='Verdana 9'),
             sg.T("mburns5000@outlook.com", font='Verdana 9', text_color=("Blue"))],
            [sg.T("Check for latest version: ", font='Verdana 9'),
             sg.T("Link to Project URL on GitHub", enable_events=True,
                  tooltip="Click to open project URL in webbrowser", font='Verdana 10 underline', text_color=("Blue"),
                  key="PROJECT_URL")]
        ]

        # 2nd column
        column2 = [
            [sg.T("'Launch Tournament' only available after selecting 'New' or loading a previous save", size=(40, 2),
                  font=('Any 14'), text_color="yellow")],
            [sg.T("")],
            #[sg.B("Launch Tournament", button_color="black on red", font=("Any 14"), disabled=True,
            [sg.B("Launch Tournament", button_color="white on maroon", font=("Any 14"), disabled=True,
                  key="LAUNCH_BUTTON")],
            [sg.T("")],
            [sg.HSep()],
            [sg.T("")],
            [sg.T('Tournament Description:', font=('Any 14'), text_color="yellow"),
             sg.T('No data loaded', font=('Any 13'), key="DATA_DESCRIPTION")],
            [sg.T("")]
        ]

        # ----- Full layout -----
        layout = [
            [
                sg.Column(column1, size=(570, 330)),
                sg.VSeperator(),
                sg.Column(column2, size=(440, 330))
            ]
        ]

        sg.theme("DarkTeal8")

        sg.user_settings_filename(path='.')  # Set the location for the settings file
        self.window = sg.Window("Tournament Root Window || Version:" + version, layout, icon=shuttleIcon)

    def popup_launch_tournament(self, data):
        """ Launch tournament from given data

        :param data: dictionary for current working data
        :return:
        """

        max_score = int(data["tournament"]["max_game_points"])
        self.log.info("::[%s]::'popup_launch_tournament', Live tournament window has max_game_points: %s" %
                      (logExtra, str(max_score)))

        layoutSummaryLeft = [
            [sg.T("")],
            [sg.HSep()],
            [sg.T("TOURNAMENT: ", font="Any 14"), sg.T("", key="DESCRIPTION_MAIN", font="Any 14")],
            [sg.T("(Max. points per game: " + str(max_score) + ")", font="Any 12")],
            [sg.HSep()],
            [sg.T("")],
            [sg.T("Order of Play", font="Any 14", text_color="Black"),
             sg.B("Alternative View", key="ADVANCED_OOP", tooltip="Alternative view for order of play", )],
            [sg.T("")],
            [sg.Multiline("", text_color="White", size=(60, 200), key="ORDER_OF_PLAY")]
        ]

        layoutSummaryRight = [
            [sg.T("")],
            [sg.B("Refresh Player List", font="Any 14", key="REFRESH_PLAYER_SUMMARY",
                  tooltip="Updates player list below", )],
            [sg.HSep()],
            [sg.T("")],
            [sg.T("Pairing Summary", font="Any 14", text_color="Black")],
            [sg.T("")],
            [sg.Multiline("", text_color="White", size=(60, 20), key="PLAYER_SUMMARY")]
        ]

        layoutMain = [
            [
                sg.Column(layoutSummaryLeft),
                sg.VSeperator(),
                sg.Column(layoutSummaryRight)
            ]
        ]

        layoutUnused1 = [
            [sg.T("This group is unused")]
        ]
        layoutUnused2 = [
            [sg.T("This group is unused")]
        ]
        layoutUnused3 = [
            [sg.T("This group is unused")]
        ]
        layoutUnused4 = [
            [sg.T("This group is unused")]
        ]
        layoutUnused5 = [
            [sg.T("This group is unused")]
        ]
        layoutUnused6 = [
            [sg.T("This group is unused")]
        ]
        layoutUnused7 = [
            [sg.T("This group is unused")]
        ]
        layoutUnused8 = [
            [sg.T("This group is unused")]
        ]

        # if result is False (failure encountered) then set a default layoutGroup1
        layoutGroup1 = generate_GRP(self.log, 1, (data["GRP1"]["config"]["grp_size"]))
        if not layoutGroup1:
            layoutGroup1 = [
                [sg.T("Default - Group1")]
            ]

        layoutGroup2 = generate_GRP(self.log, 2, (data["GRP2"]["config"]["grp_size"]))
        if not layoutGroup2:
            layoutGroup2 = [
                [sg.T("Default - Group2")]
            ]

        layoutGroup3 = generate_GRP(self.log, 3, (data["GRP3"]["config"]["grp_size"]))
        if not layoutGroup3:
            layoutGroup3 = [
                [sg.T("Default - Group3")]
            ]

        layoutGroup4 = generate_GRP(self.log, 4, (data["GRP4"]["config"]["grp_size"]))
        if not layoutGroup4:
            layoutGroup4 = [
                [sg.T("Default - Group4")]
            ]

        layoutGroup5 = generate_GRP(self.log, 5, (data["GRP5"]["config"]["grp_size"]))
        if not layoutGroup5:
            layoutGroup5 = [
                [sg.T("Default - Group5")]
            ]

        layoutGroup6 = generate_GRP(self.log, 6, (data["GRP6"]["config"]["grp_size"]))
        if not layoutGroup6:
            layoutGroup6 = [
                [sg.T("Default - Group6")]
            ]

        layoutGroup7 = generate_GRP(self.log, 7, (data["GRP7"]["config"]["grp_size"]))
        if not layoutGroup7:
            layoutGroup7 = [
                [sg.T("Default - Group7")]
            ]

        layoutGroup8 = generate_GRP(self.log, 8, (data["GRP8"]["config"]["grp_size"]))
        if not layoutGroup8:
            layoutGroup8 = [
                [sg.T("Default - Group8")]
            ]

        # set all group tabs to default of unused
        group1_tab = sg.Tab('Unused', layoutUnused1, background_color='Grey')
        group2_tab = sg.Tab('Unused', layoutUnused2, background_color='Grey')
        group3_tab = sg.Tab('Unused', layoutUnused3, background_color='Grey')
        group4_tab = sg.Tab('Unused', layoutUnused4, background_color='Grey')
        group5_tab = sg.Tab('Unused', layoutUnused5, background_color='Grey')
        group6_tab = sg.Tab('Unused', layoutUnused6, background_color='Grey')
        group7_tab = sg.Tab('Unused', layoutUnused7, background_color='Grey')
        group8_tab = sg.Tab('Unused', layoutUnused8, background_color='Grey')

        # if set active then use active layout
        if data["GRP1"]["config"]["active"]:
            group1_tab = sg.Tab('Group 1', layoutGroup1)
        if data["GRP2"]["config"]["active"]:
            group2_tab = sg.Tab('Group 2', layoutGroup2)
        if data["GRP3"]["config"]["active"]:
            group3_tab = sg.Tab('Group 3', layoutGroup3)
        if data["GRP4"]["config"]["active"]:
            group4_tab = sg.Tab('Group 4', layoutGroup4)
        if data["GRP5"]["config"]["active"]:
            group5_tab = sg.Tab('Group 5', layoutGroup5)
        if data["GRP6"]["config"]["active"]:
            group6_tab = sg.Tab('Group 6', layoutGroup6)
        if data["GRP7"]["config"]["active"]:
            group7_tab = sg.Tab('Group 7', layoutGroup7)
        if data["GRP8"]["config"]["active"]:
            group8_tab = sg.Tab('Group 8', layoutGroup8)

        tabgrp = [
            [sg.TabGroup([[sg.Tab('Tournament Summary', layoutMain, element_justification='left'),
                           group1_tab, group2_tab, group3_tab, group4_tab, group5_tab, group6_tab, group7_tab,
                           group8_tab]], selected_title_color='yellow', font="Any 14"),
             [sg.B("Save", font="Any 12 bold", size=(14, 1), button_color="#333399", key="LIVE_POPUP_SAVE"),
              sg.B("Close", font="Any 12 bold", size=(14, 1), button_color="#333399", key="LIVE_POPUP_EXIT")]]]

        live_window = sg.Window("Live Tournament", tabgrp, use_default_focus=False, finalize=True, modal=True,
                                icon=shuttleIcon, resizable=True, size=(1300, 700))


        #########################################################################################
        # SECTION: upon launch - update display summary and display table for all active groups #
        #########################################################################################
        # update display summary per active group
        active_group_list = []
        for i in all_group_list:
            if (data[i]["config"]["active"]):
                active_group_list.append(i)
        self.log.info("::[%s]::'popup_launch_tournament' active groups found as: %s" % (logExtra,
                                                                                        str(active_group_list)))

        update_group_results(self.log, live_window, active_group_list, data)

        # update display table per active group
        for i in all_group_list_int:
            temp_grp_key = "GRP" + str(i)
            if (data[temp_grp_key]["config"]["active"]):
                update_table_for_group(self.log, live_window, i, data)
        ###############
        # END SECTION #
        ###############

        ################################################################
        # SECTION: upon launch - update player names for active groups #
        ################################################################
        active_groups = []  # list of int for active groups, used in next step
        for i in all_group_list_int:
            player_names_list = []
            temp_grp_key = "GRP" + str(i)
            if (data[temp_grp_key]["config"]["active"]):
                active_groups.append(i)
                # get player names list for active group from data dictionary
                player_names_list = player_names_from_workingData(self.log, temp_grp_key, data,
                                                                  int(data[temp_grp_key]["config"]["grp_size"]))
                self.log.info("::[%s]::'popup_launch_tournament' player_names_list from data dict for %s:\n%s" %
                              (logExtra, temp_grp_key, str(player_names_list)))
                # update display names, returns data dict with those names updated
                # note this function returns the updated data dict (in this case the input and returned one are the
                # same but this function is called elsewhere and this is needed)
                data = update_display_names(self.log, live_window, player_names_list, i, data)
        ###############
        # END SECTION #
        ###############

        ##################################################
        # SECTION - populate Main tab with order of play #
        ##################################################

        live_window["DESCRIPTION_MAIN"].update(data["tournament"]["description"])

        order_of_play_list = []
        order_of_play_list = create_order_of_play(self.log, data, active_groups)
        self.log.info("::[%s]::'popup_launch_tournament' order of play list from active groups is:\n%s" %
                      (logExtra, str(order_of_play_list)))

        order_of_play_text = ""
        if order_of_play_list:
            for i in order_of_play_list:
                order_of_play_text += "\n" + i + "\n"
            live_window["ORDER_OF_PLAY"].update(order_of_play_text)

        ###############
        # END SECTION #
        ###############

        while True:
            event, values = live_window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == "LIVE_POPUP_EXIT":
                # popup_confirm_exit() only returns True if user confirms at prompt
                exit_tournament = popup_confirm_exit()
                if exit_tournament:
                    break
                else:
                    pass

            if event == "LIVE_POPUP_SAVE":
                popup_save(self.log, data)

            if event == "ADVANCED_OOP":
                adv_order_of_play_list = []
                adv_order_of_play_list = create_order_of_play(self.log, data, active_groups)
                self.log.info("::[%s]::'popup_launch_tournament' alternative oop list created:\n%s" %
                              (logExtra, str(adv_order_of_play_list)))
                popup_advanced_oop(self.log, adv_order_of_play_list, data)

            if event == "REFRESH_PLAYER_SUMMARY":
                # note 'active_groups' is a list of int for active groups
                temp_all_group_text = ""  # to be used updating the sg.Multi element
                for i in active_groups:
                    temp_group_names = []
                    temp_all_group_text += "\n\n*** GROUP: " + str(i) + " ***\n"
                    # 1st arg is format 'GRP1'
                    temp_group_names = player_names_from_workingData(self.log, ("GRP" + str(i)), data,
                                                                     int(data["GRP" + str(i)]["config"]["grp_size"]))

                    # create a human-readable list of names for pairs in each group
                    counter = 0
                    for j in temp_group_names:
                        if counter == 0:
                            temp_all_group_text += ("Pair 1: " + j + ",  ")
                        elif counter == 1:
                            temp_all_group_text += (j + "\n")
                        elif counter == 2:
                            temp_all_group_text += ("Pair 2: " + j + ",  ")
                        elif counter == 3:
                            temp_all_group_text += (j + "\n")
                        elif counter == 4:
                            temp_all_group_text += ("Pair 3: " + j + ",  ")
                        elif counter == 5:
                            temp_all_group_text += (j + "\n")
                        elif counter == 6:
                            temp_all_group_text += ("Pair 4: " + j + ",  ")
                        elif counter == 7:
                            temp_all_group_text += (j + "\n")
                        elif counter == 8:
                            temp_all_group_text += ("Pair 5: " + j + ",  ")
                        elif counter == 9:
                            temp_all_group_text += (j + "\n")
                        else:
                            pass
                        counter += 1

                live_window["PLAYER_SUMMARY"].update(temp_all_group_text)

            #####################################################
            # SECTION - events, update group summary and tables #
            #####################################################
            # Group 1
            if event == "UPDATE_GRP1M1":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 1, 1)
            if event == "UPDATE_GRP1M2":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 1, 2)
            if event == "UPDATE_GRP1M3":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 1, 3)
            if event == "UPDATE_GRP1M4":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 1, 4)
            if event == "UPDATE_GRP1M5":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 1, 5)
            if event == "UPDATE_GRP1M6":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 1, 6)
            if event == "UPDATE_GRP1M7":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 1, 7)
            if event == "UPDATE_GRP1M8":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 1, 8)
            if event == "UPDATE_GRP1M9":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 1, 9)
            if event == "UPDATE_GRP1M10":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 1, 10)

            # Group 2
            if event == "UPDATE_GRP2M1":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 2, 1)
            if event == "UPDATE_GRP2M2":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 2, 2)
            if event == "UPDATE_GRP2M3":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 2, 3)
            if event == "UPDATE_GRP2M4":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 2, 4)
            if event == "UPDATE_GRP2M5":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 2, 5)
            if event == "UPDATE_GRP2M6":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 2, 6)
            if event == "UPDATE_GRP2M7":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 2, 7)
            if event == "UPDATE_GRP2M8":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 2, 8)
            if event == "UPDATE_GRP2M9":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 2, 9)
            if event == "UPDATE_GRP2M10":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 2, 10)

            # Group 3
            if event == "UPDATE_GRP3M1":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 3, 1)
            if event == "UPDATE_GRP3M2":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 3, 2)
            if event == "UPDATE_GRP3M3":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 3, 3)
            if event == "UPDATE_GRP3M4":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 3, 4)
            if event == "UPDATE_GRP3M5":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 3, 5)
            if event == "UPDATE_GRP3M6":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 3, 6)
            if event == "UPDATE_GRP3M7":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 3, 7)
            if event == "UPDATE_GRP3M8":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 3, 8)
            if event == "UPDATE_GRP3M9":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 3, 9)
            if event == "UPDATE_GRP3M10":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 3, 10)

            # Group 4
            if event == "UPDATE_GRP4M1":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 4, 1)
            if event == "UPDATE_GRP4M2":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 4, 2)
            if event == "UPDATE_GRP4M3":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 4, 3)
            if event == "UPDATE_GRP4M4":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 4, 4)
            if event == "UPDATE_GRP4M5":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 4, 5)
            if event == "UPDATE_GRP4M6":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 4, 6)
            if event == "UPDATE_GRP4M7":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 4, 7)
            if event == "UPDATE_GRP4M8":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 4, 8)
            if event == "UPDATE_GRP4M9":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 4, 9)
            if event == "UPDATE_GRP4M10":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 4, 10)

            # Group 5
            if event == "UPDATE_GRP5M1":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 5, 1)
            if event == "UPDATE_GRP5M2":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 5, 2)
            if event == "UPDATE_GRP5M3":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 5, 3)
            if event == "UPDATE_GRP5M4":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 5, 4)
            if event == "UPDATE_GRP5M5":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 5, 5)
            if event == "UPDATE_GRP5M6":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 5, 6)
            if event == "UPDATE_GRP5M7":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 5, 7)
            if event == "UPDATE_GRP5M8":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 5, 8)
            if event == "UPDATE_GRP5M9":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 5, 9)
            if event == "UPDATE_GRP5M10":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 5, 10)

            # Group 6
            if event == "UPDATE_GRP6M1":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 6, 1)
            if event == "UPDATE_GRP6M2":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 6, 2)
            if event == "UPDATE_GRP6M3":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 6, 3)
            if event == "UPDATE_GRP6M4":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 6, 4)
            if event == "UPDATE_GRP6M5":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 6, 5)
            if event == "UPDATE_GRP6M6":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 6, 6)
            if event == "UPDATE_GRP6M7":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 6, 7)
            if event == "UPDATE_GRP6M8":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 6, 8)
            if event == "UPDATE_GRP6M9":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 6, 9)
            if event == "UPDATE_GRP6M10":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 6, 10)

            # Group 7
            if event == "UPDATE_GRP7M1":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 7, 1)
            if event == "UPDATE_GRP7M2":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 7, 2)
            if event == "UPDATE_GRP7M3":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 7, 3)
            if event == "UPDATE_GRP7M4":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 7, 4)
            if event == "UPDATE_GRP7M5":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 7, 5)
            if event == "UPDATE_GRP7M6":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 7, 6)
            if event == "UPDATE_GRP7M7":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 7, 7)
            if event == "UPDATE_GRP7M8":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 7, 8)
            if event == "UPDATE_GRP7M9":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 7, 9)
            if event == "UPDATE_GRP7M10":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 7, 10)

            # Group 8
            if event == "UPDATE_GRP8M1":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 8, 1)
            if event == "UPDATE_GRP8M2":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 8, 2)
            if event == "UPDATE_GRP8M3":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 8, 3)
            if event == "UPDATE_GRP8M4":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 8, 4)
            if event == "UPDATE_GRP8M5":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 8, 5)
            if event == "UPDATE_GRP8M6":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 8, 6)
            if event == "UPDATE_GRP8M7":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 8, 7)
            if event == "UPDATE_GRP8M8":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 8, 8)
            if event == "UPDATE_GRP8M9":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 8, 9)
            if event == "UPDATE_GRP8M10":
                my_result = popup_enter_score(self.log, event, data, max_score=max_score)
                self.process_popup_score(my_result, live_window, data, 8, 10)

            ###############
            # END SECTION #
            ###############

            #################################################
            # SECTION - edit and update players, all groups #
            #################################################
            if event == "GRP1-EDIT-PLAYERS":  # unlocks for editing names
                edit_player_names(self.log, live_window, 1, data)
                self.log.debug("::[%s]::'popup_launch_tournament' Group 1, edit_player_names completed" % logExtra)

            if event == "GRP2-EDIT-PLAYERS":  # unlocks for editing names
                edit_player_names(self.log, live_window, 2, data)
                self.log.debug("::[%s]::'popup_launch_tournament' Group 2, edit_player_names completed" % logExtra)

            if event == "GRP3-EDIT-PLAYERS":  # unlocks for editing names
                edit_player_names(self.log, live_window, 3, data)
                self.log.debug("::[%s]::'popup_launch_tournament' Group 3, edit_player_names completed" % logExtra)

            if event == "GRP4-EDIT-PLAYERS":  # unlocks for editing names
                edit_player_names(self.log, live_window, 4, data)
                self.log.debug("::[%s]::'popup_launch_tournament' Group 4, edit_player_names completed" % logExtra)

            if event == "GRP5-EDIT-PLAYERS":  # unlocks for editing names
                edit_player_names(self.log, live_window, 5, data)
                self.log.debug("::[%s]::'popup_launch_tournament' Group 5, edit_player_names completed" % logExtra)

            if event == "GRP6-EDIT-PLAYERS":  # unlocks for editing names
                edit_player_names(self.log, live_window, 6, data)
                self.log.debug("::[%s]::'popup_launch_tournament' Group 6, edit_player_names completed" % logExtra)

            if event == "GRP7-EDIT-PLAYERS":  # unlocks for editing names
                edit_player_names(self.log, live_window, 7, data)
                self.log.debug("::[%s]::'popup_launch_tournament' Group 7, edit_player_names completed" % logExtra)

            if event == "GRP8-EDIT-PLAYERS":  # unlocks for editing names
                edit_player_names(self.log, live_window, 8, data)
                self.log.debug("::[%s]::'popup_launch_tournament' Group 8, edit_player_names completed" % logExtra)

            if event == "GRP1-UPDATE-PLAYERS":
                # for some reason moving this to a separate function has issues with keys and button requiring pressed
                # twice, perhaps issues with live_window.read(), live_window.refresh() or live_window.finalize()
                player_input_keys = generate_player_keys_inputs(self.log, "GRP1",
                                                                int(data["GRP1"]["config"]["grp_size"]))
                self.log.debug("::[%s]::'popup_launch_tournament' Player input keys GRP1 are:%s" %
                               (logExtra, str(player_input_keys)))
                player_input_values = []
                for i in player_input_keys:
                    player_input_values.append(values[i])
                self.log.debug("::[%s]::'popup_launch_tournament' Player input values GRP1 are:%s" %
                               (logExtra, str(player_input_values)))
                for i in player_input_keys:
                    live_window[i].update(visible=False)
                live_window["GRP1-UPDATE-PLAYERS"].update(visible=False)
                live_window["GRP1-EDIT-PLAYERS"].update(visible=True)
                # update display names, returns data dict with those names updated
                data = update_display_names(self.log, live_window, player_input_values, 1, data)

            if event == "GRP2-UPDATE-PLAYERS":
                player_input_keys = generate_player_keys_inputs(self.log, "GRP2",
                                                                int(data["GRP2"]["config"]["grp_size"]))
                self.log.debug("::[%s]::'popup_launch_tournament' Player input keys GRP2 are:%s" %
                               (logExtra, str(player_input_keys)))
                player_input_values = []
                for i in player_input_keys:
                    player_input_values.append(values[i])
                self.log.debug("::[%s]::'popup_launch_tournament' Player input values GRP2 are:%s" %
                               (logExtra, str(player_input_values)))
                for i in player_input_keys:
                    live_window[i].update(visible=False)
                live_window["GRP2-UPDATE-PLAYERS"].update(visible=False)
                live_window["GRP2-EDIT-PLAYERS"].update(visible=True)
                # update display names, returns data dict with those names updated
                data = update_display_names(self.log, live_window, player_input_values, 2, data)

            if event == "GRP3-UPDATE-PLAYERS":
                player_input_keys = generate_player_keys_inputs(self.log, "GRP3",
                                                                int(data["GRP3"]["config"]["grp_size"]))
                self.log.debug("::[%s]::'popup_launch_tournament' Player input keys GRP3 are:%s" %
                               (logExtra, str(player_input_keys)))
                player_input_values = []
                for i in player_input_keys:
                    player_input_values.append(values[i])
                self.log.debug("::[%s]::'popup_launch_tournament' Player input values GRP3 are:%s" %
                               (logExtra, str(player_input_values)))
                for i in player_input_keys:
                    live_window[i].update(visible=False)
                live_window["GRP3-UPDATE-PLAYERS"].update(visible=False)
                live_window["GRP3-EDIT-PLAYERS"].update(visible=True)
                # update display names, returns data dict with those names updated
                data = update_display_names(self.log, live_window, player_input_values, 3, data)

            if event == "GRP4-UPDATE-PLAYERS":
                player_input_keys = generate_player_keys_inputs(self.log, "GRP4",
                                                                int(data["GRP4"]["config"]["grp_size"]))
                self.log.debug("::[%s]::'popup_launch_tournament' Player input keys GRP4 are:%s" %
                               (logExtra, str(player_input_keys)))
                player_input_values = []
                for i in player_input_keys:
                    player_input_values.append(values[i])
                self.log.debug("::[%s]::'popup_launch_tournament' Player input values GRP4 are:%s" %
                               (logExtra, str(player_input_values)))
                for i in player_input_keys:
                    live_window[i].update(visible=False)
                live_window["GRP4-UPDATE-PLAYERS"].update(visible=False)
                live_window["GRP4-EDIT-PLAYERS"].update(visible=True)
                # update display names, returns data dict with those names updated
                data = update_display_names(self.log, live_window, player_input_values, 4, data)

            if event == "GRP5-UPDATE-PLAYERS":
                player_input_keys = generate_player_keys_inputs(self.log, "GRP5",
                                                                int(data["GRP5"]["config"]["grp_size"]))
                self.log.debug("::[%s]::'popup_launch_tournament' Player input keys GRP5 are:%s" %
                               (logExtra, str(player_input_keys)))
                player_input_values = []
                for i in player_input_keys:
                    player_input_values.append(values[i])
                self.log.debug("::[%s]::'popup_launch_tournament' Player input values GRP5 are:%s" %
                               (logExtra, str(player_input_values)))
                for i in player_input_keys:
                    live_window[i].update(visible=False)
                live_window["GRP5-UPDATE-PLAYERS"].update(visible=False)
                live_window["GRP5-EDIT-PLAYERS"].update(visible=True)
                # update display names, returns data dict with those names updated
                data = update_display_names(self.log, live_window, player_input_values, 5, data)

            if event == "GRP6-UPDATE-PLAYERS":
                player_input_keys = generate_player_keys_inputs(self.log, "GRP6",
                                                                int(data["GRP6"]["config"]["grp_size"]))
                self.log.debug("::[%s]::'popup_launch_tournament' Player input keys GRP6 are:%s" %
                               (logExtra, str(player_input_keys)))
                player_input_values = []
                for i in player_input_keys:
                    player_input_values.append(values[i])
                self.log.debug("::[%s]::'popup_launch_tournament' Player input values GRP6 are:%s" %
                               (logExtra, str(player_input_values)))
                for i in player_input_keys:
                    live_window[i].update(visible=False)
                live_window["GRP6-UPDATE-PLAYERS"].update(visible=False)
                live_window["GRP6-EDIT-PLAYERS"].update(visible=True)
                # update display names, returns data dict with those names updated
                data = update_display_names(self.log, live_window, player_input_values, 6, data)

            if event == "GRP7-UPDATE-PLAYERS":
                player_input_keys = generate_player_keys_inputs(self.log, "GRP7",
                                                                int(data["GRP7"]["config"]["grp_size"]))
                self.log.debug("::[%s]::'popup_launch_tournament' Player input keys GRP7 are:%s" %
                               (logExtra, str(player_input_keys)))
                player_input_values = []
                for i in player_input_keys:
                    player_input_values.append(values[i])
                self.log.debug("::[%s]::'popup_launch_tournament' Player input values GRP7 are:%s" %
                               (logExtra, str(player_input_values)))
                for i in player_input_keys:
                    live_window[i].update(visible=False)
                live_window["GRP7-UPDATE-PLAYERS"].update(visible=False)
                live_window["GRP7-EDIT-PLAYERS"].update(visible=True)
                # update display names, returns data dict with those names updated
                data = update_display_names(self.log, live_window, player_input_values, 7, data)

            if event == "GRP8-UPDATE-PLAYERS":
                player_input_keys = generate_player_keys_inputs(self.log, "GRP8",
                                                                int(data["GRP8"]["config"]["grp_size"]))
                self.log.debug("::[%s]::'popup_launch_tournament' Player input keys GRP8 are:%s" %
                               (logExtra, str(player_input_keys)))
                player_input_values = []
                for i in player_input_keys:
                    player_input_values.append(values[i])
                self.log.debug("::[%s]::'popup_launch_tournament' Player input values GRP8 are:%s" %
                               (logExtra, str(player_input_values)))
                for i in player_input_keys:
                    live_window[i].update(visible=False)
                live_window["GRP8-UPDATE-PLAYERS"].update(visible=False)
                live_window["GRP8-EDIT-PLAYERS"].update(visible=True)
                # update display names, returns data dict with those names updated
                data = update_display_names(self.log, live_window, player_input_values, 8, data)
            ###############
            # END SECTION #
            ###############

        live_window.close()

    def process_popup_score(self, score_result, parent_window, workingDict, group, match):
        """ Process result received from popup_enter_score to update display and working data

        :param score_result: tuple of tuples for match score e.g. (True, (2, 21, 21, 9, 21, 20))
        :param parent_window: sg window object for calling parent
        :param workingDict: working dictionary for all tournament data
        :param group: int for group
        :param match: int for match

        """
        data = workingDict
        group_key = "GRP" + str(group)

        try:
            self.log.info("::[%s]::'process_popup_score', popup_enter_score returned: %s" % (logExtra,
                                                                                             str(score_result[1])))
            if score_result:
                if not ((score_result[0] == "Input Error") or (score_result[0] == False)):
                    data = self.update_GRPxMx_workingDict(data, score_result, group, match)
                    update_group_results(self.log, parent_window, [group_key], data)  # updates group summary display
                    update_table_for_group(self.log, parent_window, group, data)

        except Exception as e:
            self.log.error("::[%s]::'process_popup_score' General Exception: %s" % (logExtra, str(e)))


    def update_GRPxMx_workingDict(self, workingDict, group_results, group, match):
        """ Updates working dictionary values for given group and match

        example group_results either:
         (True, (2, 21, 21, 9, 21, 20), {'net_points': -6, 'net_wins': 1}, {'net_points': 6, 'net_wins': -1}, 'teamA')
        or
        (True, (2, 21, 21, 9, 21, 20))

        depending on where it is called from

        :param workingDict: working dictionary for all tournament data
        :param group_results: tuple
        :param group: int for group
        :param match: int for match

        :return updatedDict: updated dictionary
        """

        data = workingDict
        updatedDict = {}

        group_key = "GRP" + str(group)  # e.g. "GRP1"
        match_key = group_key + "M" + str(match)  # e.g. "GRP1M1"

        try:
            self.log.info("::[%s]::'update_GRPxMx_workingDict' called with match key: %s" % (logExtra, match_key))
            data[group_key]["resultsv2"][match_key + "Pia"] = group_results[1][0]
            data[group_key]["resultsv2"][match_key + "Piia"] = group_results[1][1]
            data[group_key]["resultsv2"][match_key + "Pib"] = group_results[1][2]
            data[group_key]["resultsv2"][match_key + "Piib"] = group_results[1][3]
            data[group_key]["resultsv2"][match_key + "Pic"] = group_results[1][4]
            data[group_key]["resultsv2"][match_key + "Piic"] = group_results[1][5]
            updatedDict = data

        except Exception as e:
            self.log.error("::[%s]::'update_GRPxMx_workingDict' General Exception: %s" % (logExtra, str(e)))

        return updatedDict
