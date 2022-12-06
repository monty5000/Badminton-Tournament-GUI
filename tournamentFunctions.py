# file holding functions
import os
import PySimpleGUI as sg
import json
from templateTournamentVars import icon_shuttle as shuttleIcon
from templateTournamentVars import icon_warning as warningIcon
from matchProcessingClass import PairData
from groupGeneratorFunctions import pr1_colour, pr2_colour, pr3_colour, pr4_colour, pr5_colour


combo_score_list_15 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
combo_score_list_21 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
combo_score_list_30 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30]

logExtra = os.path.basename(__file__)


def update_group_results(log, parent_window, active_group_list, workingDict):
    """ Updates all group results summaries

    Notes:
        required on load of tournament data
        this is NOT the table, this is the results summary above the table

    :param log: logging object
    :param parent_window: sg window object for calling parent
    :param active_group_list: list of active groups ["GRP1", "GRP2", "GRP5"]
    :param workingDict: working dictionary for all tournament data

    """
    data = workingDict

    try:
        max_score = int(data["tournament"]["max_game_points"])
        grp_size1 = int(data["GRP1"]["config"]["grp_size"])
        grp_size2 = int(data["GRP2"]["config"]["grp_size"])
        grp_size3 = int(data["GRP3"]["config"]["grp_size"])
        grp_size4 = int(data["GRP4"]["config"]["grp_size"])
        grp_size5 = int(data["GRP5"]["config"]["grp_size"])
        grp_size6 = int(data["GRP6"]["config"]["grp_size"])
        grp_size7 = int(data["GRP7"]["config"]["grp_size"])
        grp_size8 = int(data["GRP8"]["config"]["grp_size"])

        if (max_score == 15):
            min_winning_score = 15
        elif (max_score == 21):
            min_winning_score = 21
        elif (max_score == 30):
            min_winning_score = 21
        else:
            min_winning_score = 21  # set a default to 21

        log.info("::[%s]::'update_group_results' active group list %s" % (logExtra, (str(active_group_list))))

        for i in active_group_list:
            temp_scores_list = scores_list_generator2(log, i, data)
            log.info("::[%s]::'update_group_results' scores list for %s" % (logExtra, (i + str(temp_scores_list))))
            # temp_scores_list of format [(2, 21, 21, 9, 21, 20), (21,10, 21, 2, 0, 0), (0, 0, 0, 0, 0, 0)]
            if temp_scores_list:
                # if group i match 1 has changed from default there must be a score entered
                if temp_scores_list[0] != (0, 0, 0, 0, 0, 0):
                    match1_display_tuple = add_score_result(log, temp_scores_list[0],
                                                            min_score_to_win=min_winning_score)
                    # example match tuple: (True, (2, 21, 21, 9, 21, 20), {'net_points': -6, 'net_wins': 1},
                    # {'net_points': 6, 'net_wins': -1}, 'teamA')
                    log.info("::[%s]::'update_group_results' match1 display tuple: %s" %
                             (logExtra, (i + str(match1_display_tuple))))
                    if match1_display_tuple[0]:  # if success
                        update_GRPxMy_display(log, parent_window, match1_display_tuple, i, 1)

                # group i match 2
                if temp_scores_list[1] != (0, 0, 0, 0, 0, 0):
                    match2_display_tuple = add_score_result(log, temp_scores_list[1],
                                                            min_score_to_win=min_winning_score)
                    log.info("::[%s]::'update_group_results' match2 display tuple: %s" %
                              (logExtra, (i + str(match2_display_tuple))))
                    if match2_display_tuple[0]:  # if success
                        update_GRPxMy_display(log, parent_window, match2_display_tuple, i, 2)

                # group i match 3
                if temp_scores_list[2] != (0, 0, 0, 0, 0, 0):
                    match3_display_tuple = add_score_result(log, temp_scores_list[2],
                                                            min_score_to_win=min_winning_score)
                    log.info("::[%s]::'update_group_results' match3 display tuple: %s" %
                              (logExtra, (i + str(match3_display_tuple))))
                    if match3_display_tuple[0]:  # if success
                        update_GRPxMy_display(log, parent_window, match3_display_tuple, i, 3)

                # group i match 4
                if temp_scores_list[3] != (0, 0, 0, 0, 0, 0):
                    match4_display_tuple = add_score_result(log, temp_scores_list[3],
                                                            min_score_to_win=min_winning_score)
                    log.info("::[%s]::'update_group_results' match4 display tuple: %s" %
                              (logExtra, (i + str(match4_display_tuple))))
                    if match4_display_tuple[0]:  # if success
                        update_GRPxMy_display(log, parent_window, match4_display_tuple, i, 4)

                # group i match 5
                if temp_scores_list[4] != (0, 0, 0, 0, 0, 0):
                    match5_display_tuple = add_score_result(log, temp_scores_list[4],
                                                            min_score_to_win=min_winning_score)
                    log.info("::[%s]::'update_group_results' match5 display tuple: %s" %
                             (logExtra, (i + str(match5_display_tuple))))
                    if match5_display_tuple[0]:  # if success
                        update_GRPxMy_display(log, parent_window, match5_display_tuple, i, 5)

                # group i match 6
                if temp_scores_list[5] != (0, 0, 0, 0, 0, 0):
                    match6_display_tuple = add_score_result(log, temp_scores_list[5],
                                                            min_score_to_win=min_winning_score)
                    log.info("::[%s]::'update_group_results' match6 display tuple: %s" %
                              (logExtra, (i + str(match6_display_tuple))))
                    if match6_display_tuple[0]:  # if success
                        update_GRPxMy_display(log, parent_window, match6_display_tuple, i, 6)

                # group i match 7
                if temp_scores_list[6] != (0, 0, 0, 0, 0, 0):
                    match7_display_tuple = add_score_result(log, temp_scores_list[6],
                                                            min_score_to_win=min_winning_score)
                    log.info("::[%s]::'update_group_results' match7 display tuple: %s" %
                              (logExtra, (i + str(match7_display_tuple))))
                    if match7_display_tuple[0]:  # if success
                        update_GRPxMy_display(log, parent_window, match7_display_tuple, i, 7)

                # group i match 8
                if temp_scores_list[7] != (0, 0, 0, 0, 0, 0):
                    match8_display_tuple = add_score_result(log, temp_scores_list[7],
                                                            min_score_to_win=min_winning_score)
                    log.info("::[%s]::'update_group_results' match8 display tuple: %s" %
                              (logExtra, (i + str(match8_display_tuple))))
                    if match8_display_tuple[0]:  # if success
                        update_GRPxMy_display(log, parent_window, match8_display_tuple, i, 8)

                # group i match 9
                if temp_scores_list[8] != (0, 0, 0, 0, 0, 0):
                    match9_display_tuple = add_score_result(log, temp_scores_list[8],
                                                            min_score_to_win=min_winning_score)
                    log.info("::[%s]::'update_group_results' match9 display tuple: %s" %
                             (logExtra, (i + str(match9_display_tuple))))
                    if match9_display_tuple[0]:  # if success
                        update_GRPxMy_display(log, parent_window, match9_display_tuple, i, 9)

                # group i match 10
                if temp_scores_list[9] != (0, 0, 0, 0, 0, 0):
                    match10_display_tuple = add_score_result(log, temp_scores_list[9],
                                                            min_score_to_win=min_winning_score)
                    log.info("::[%s]::'update_group_results' match10 display tuple: %s" %
                             (logExtra, (i + str(match10_display_tuple))))
                    if match10_display_tuple[0]:  # if success
                        update_GRPxMy_display(log, parent_window, match10_display_tuple, i, 10)

            else:
                log.warning("::[%s]::'update_group_results' found NO scores list %s" % logExtra)

    except Exception as e:
        log.error("::[%s]::'update_group_results' General Exception %s" % (logExtra, str(e)))


def popup_confirm_exit():
    """ Popup window for confirming exit

    :return:
    """
    confirm_exit = False
    layoutConfirmExit = [
        [sg.Text("Do you wish to close the tournament?")],
        [sg.Text("")],
        [sg.Text("Please ensure any updates were saved")],
        [sg.Text("")],
        [sg.B('Yes - Close now', key="EXIT_CONFIRMED")],
        [sg.B('No - Return', key="EXIT_ABORTED")]
    ]
    window = sg.Window("Confirm Exit", layoutConfirmExit, use_default_focus=False, finalize=True, modal=True,
                       icon=shuttleIcon)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "EXIT_CONFIRMED":
            confirm_exit = True
            break
        if event == "EXIT_ABORTED":
            break
    window.close()
    return confirm_exit


def popup_error_input():
    """ Popup window for error input

    :return:
    """
    layoutPopupWarning = [
        [sg.Text("WARNING - ERROR WITH INPUTS")],
        [sg.Text("No updates have been made")],
        [sg.B('OK')]
    ]
    window = sg.Window("Input Error", layoutPopupWarning, use_default_focus=False, finalize=True, modal=True,
                       icon=warningIcon)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "OK":
            break
    window.close()


def popup_exception(exceptionDetail):
    """ Popup window for when exception is encountered

    :param exceptionDetail: Exception information
    :return:
    """
    layoutPopupException = [
        [sg.Text("EXCEPTION ENCOUNTERED")],
        [sg.Text(exceptionDetail)],
        [sg.B('OK')]
    ]
    window = sg.Window("Exception Encountered", layoutPopupException,
                       use_default_focus=False, finalize=True, modal=True, icon=warningIcon)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "OK":
            break
    window.close()

def popup_file_invalid():
    """ Popup window for invalid file message

    :return:
    """
    layoutPopupFileInvalid = [
        [sg.Text("FILE DATA IS NOT VALID - CHOOSE ANOTHER OR CREATE NEW")],
        [sg.Text("")],
        [sg.B('OK')]
    ]
    window = sg.Window("File Invalid", layoutPopupFileInvalid,
                       use_default_focus=False, finalize=True, modal=True, icon=warningIcon)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "OK":
            break
    window.close()


def popup_new_tournament():
    """ Popup window that allows user to select inputs for new tournament creations

    :return: selection_dict: dictionary holding all tournament data

    """
    # max 8 groups and 4 pairs per group
    # key list matches JSON objects 'GRP1' etc
    key_list = ['GRP1', 'GRP2', 'GRP3', 'GRP4', 'GRP5', 'GRP6', 'GRP7', 'GRP8']
    selection_dict = {}
    temp_value = "0"

    layoutPopupNew = [
        [sg.T("ENTER TOURNAMENT DESCRIPTION:", font="Any 11 bold")],
        [sg.HSep()],
        [sg.InputText(default_text="my tournament", size=(60, 1), key="TOURNAMENT_DESCR")],
        [sg.T("")],
        [sg.T("ENTER POINTS LIMIT:", font="Any 11 bold")],
        [sg.HSep()],
        [sg.T("Max. points per game", text_color="maroon", font="Any 11 bold"),
         sg.Combo(['15', '21', '30'], default_value='21', key='MAX_GAME_POINTS')],
        [sg.T("")],
        [sg.T("SELECT NUMBER OF TEAMS PER GROUP:", font="Any 11 bold")],
        [sg.HSep()],
        [sg.T("Group1", font="Any 10 bold"), sg.Combo(['not used', '3', '4', '5'], default_value='not used',
                                                      key='GRP1')],
        [sg.T("Group2", font="Any 10 bold"), sg.Combo(['not used', '3', '4', '5'], default_value='not used',
                                                      key='GRP2')],
        [sg.T("Group3", font="Any 10 bold"), sg.Combo(['not used', '3', '4', '5'], default_value='not used',
                                                      key='GRP3')],
        [sg.T("Group4", font="Any 10 bold"), sg.Combo(['not used', '3', '4', '5'], default_value='not used',
                                                      key='GRP4')],
        [sg.T("Group5", font="Any 10 bold"), sg.Combo(['not used', '3', '4', '5'], default_value='not used',
                                                      key='GRP5')],
        [sg.T("Group6", font="Any 10 bold"), sg.Combo(['not used', '3', '4', '5'], default_value='not used',
                                                      key='GRP6')],
        [sg.T("Group7", font="Any 10 bold"), sg.Combo(['not used', '3', '4', '5'], default_value='not used',
                                                      key='GRP7')],
        [sg.T("Group8", font="Any 10 bold"), sg.Combo(['not used', '3', '4', '5'], default_value='not used',
                                                      key='GRP8')],
        [sg.T("")],
        [sg.HSep()],
        [sg.B('Submit', key="SUBMIT_NEW", font="Any 12 bold")]
    ]
    window = sg.Window("Create New Tournamment", layoutPopupNew, use_default_focus=False, finalize=True, modal=True,
                       icon=shuttleIcon)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            # if user has not 'submitted' then parent window receives false and can determine this
            selection_dict = False
            break

        if event == "SUBMIT_NEW":

            for i in key_list:
                if values[i] == 'not used':
                    temp_value = "0"
                else:
                    temp_value = values[i]
                selection_dict[i] = temp_value

            selection_dict["tournament_description"] = values["TOURNAMENT_DESCR"]
            selection_dict["max_game_points"] = values["MAX_GAME_POINTS"]
            break

    window.close()
    return selection_dict


def popup_saved(filename):
    layoutSaved = [
        [sg.Text("Current tournament data saved")],
        [sg.Text(filename)],
        [sg.B('OK')]
    ]
    window = sg.Window("Tournament Saved", layoutSaved, use_default_focus=False, finalize=True, modal=True,
                       icon=shuttleIcon)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "OK":
            break
    window.close()


def popup_help():
    """ Popup window with help information

    """

    sum_line1 = "This application is intended to allow management of badminton tournament group stages."
    sum_line2 = "Currently up to 8 groups are supported (with 3, 4 or 5 pairs in each group).  A table for each group" \
                " will be shown in order depending on matches, games and points won."
    sum_line3 = "Management of the latter stages (after the groups) is not included as this tends to vary and is" \
                " generally easier to manage."

    start1 = "Select 'New' from the root window and select options. Choose number of groups, the size of each group " \
             "and maximum points per game then select 'Launch Tournament'."

    sav_load1 = "The tournament data can be saved at any time (it will be a .json file)."
    sav_load2 = "As an alternative to creating a new tournament, users can load a previous save then select 'Launch" \
                " Tournament'."

    score1 = "3 options for maximum score per game are supported: 15, 21 and 30. 15 and 21 assume 'no setting' is" \
             " required, i.e. first to the limit wins and does not need '2 clear" \
             " points.'"
    score2 = "30 is more flexible and allows users to set any score up to the 30 limit, however it assumes one score" \
             " is at least 21."
    score3 = "This score limit must be set correctly from the creation of a new tournament (it cannot be changed" \
             " later)."

    oop = "The order of play is usually only of use when there are more groups than courts or for large groups. Users" \
        " can ignore this as needed."

    ans_a1 = "Check carefully the score that was entered, a score is not accepted if any check fails. Every game must" \
             " have a score that is at least the minimum expected to win (see above)."
    ans_a2 = "No draws are permitted. One team cannot win more than 2 games. A single game score is not allowed, it" \
             " must be each game for the match with a minimum of 2 game scores."

    ans_b1 = "Check for popup windows (particularly if using multiple screens), these intentionally block other "\
             "windows until user acknowledges them."

    text_i = "Any 9"    # adjust font params for main text
    text_ii = "Any 6"   # adjust font params for space "" text
    layoutHelp = [
        [sg.T("Summary", font="Any 10 bold")],
        [sg.T(sum_line1, font=text_i)],
        [sg.T(sum_line2, font=text_i)],
        [sg.T(sum_line3, font=text_i)],
        [sg.Text("", font=text_ii)],
        [sg.T("Creating a new tournament", font="Any 10 bold")],
        [sg.T(start1, font=text_i)],
        [sg.Text("", font=text_ii)],
        [sg.T("Saving/Loading", font="Any 10 bold")],
        [sg.T(sav_load1, font=text_i)],
        [sg.T(sav_load2, font=text_i)],
        [sg.Text("", font=text_ii)],
        [sg.T("Score limits", font="Any 10 bold")],
        [sg.T(score1, font=text_i)],
        [sg.T(score2, font=text_i)],
        [sg.T(score3, font=text_i)],
        [sg.Text("", font=text_i)],
        [sg.T("Order of play", font="Any 10 bold")],
        [sg.T(oop, font=text_i)],
        [sg.Text("", font=text_ii)],
        [sg.T("QUESTION:", font="Any 10 bold"), sg.T("Why does entering score give 'ERROR WITH INPUTS'?")],
        [sg.T(ans_a1, font=text_i)],
        [sg.T(ans_a2, font=text_i)],
        [sg.Text("", font=text_ii)],
        [sg.T("QUESTION:", font="Any 10 bold"), sg.T("Why don't Window buttons do anything'?")],
        [sg.T(ans_b1, font=text_i)],
        [sg.Text("", font=text_ii)],
        [sg.B('Close', key="EXIT_HELP")]
    ]

    layoutHelpInColumn = [
        [
            sg.Column(layoutHelp, expand_x=True, expand_y=True, scrollable=True)
        ]
    ]

    window = sg.Window("Help and FAQ", layoutHelpInColumn, use_default_focus=False, modal=True,
                       icon=shuttleIcon, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "EXIT_HELP":
            break
    window.close()


def scores_list_generator2(log, grp, data):
    """ Creates list of tuples of scores for group matches from data

        :param log: logging object
        :param grp: string for group e.g. "GRP1"
        :param data: working dictionary for all tournament data

        """

    scores_match1 = ()
    scores_match2 = ()
    scores_match3 = ()
    scores_match4 = ()
    scores_match5 = ()
    scores_match6 = ()
    scores_match7 = ()
    scores_match8 = ()
    scores_match9 = ()
    scores_match10 = ()
    scores_list = []

    try:
        # example scores tuple: (2, 21, 21, 9, 21, 20)
        scores_match1 = (data[grp]["resultsv2"][grp + "M1Pia"], data[grp]["resultsv2"][grp + "M1Piia"],
                         data[grp]["resultsv2"][grp + "M1Pib"], data[grp]["resultsv2"][grp + "M1Piib"],
                         data[grp]["resultsv2"][grp + "M1Pic"], data[grp]["resultsv2"][grp + "M1Piic"])

        scores_match2 = (data[grp]["resultsv2"][grp + "M2Pia"], data[grp]["resultsv2"][grp + "M2Piia"],
                         data[grp]["resultsv2"][grp + "M2Pib"], data[grp]["resultsv2"][grp + "M2Piib"],
                         data[grp]["resultsv2"][grp + "M2Pic"], data[grp]["resultsv2"][grp + "M2Piic"])

        scores_match3 = (data[grp]["resultsv2"][grp + "M3Pia"], data[grp]["resultsv2"][grp + "M3Piia"],
                         data[grp]["resultsv2"][grp + "M3Pib"], data[grp]["resultsv2"][grp + "M3Piib"],
                         data[grp]["resultsv2"][grp + "M3Pic"], data[grp]["resultsv2"][grp + "M3Piic"])

        scores_match4 = (data[grp]["resultsv2"][grp + "M4Pia"], data[grp]["resultsv2"][grp + "M4Piia"],
                         data[grp]["resultsv2"][grp + "M4Pib"], data[grp]["resultsv2"][grp + "M4Piib"],
                         data[grp]["resultsv2"][grp + "M4Pic"], data[grp]["resultsv2"][grp + "M4Piic"])

        scores_match5 = (data[grp]["resultsv2"][grp + "M5Pia"], data[grp]["resultsv2"][grp + "M5Piia"],
                         data[grp]["resultsv2"][grp + "M5Pib"], data[grp]["resultsv2"][grp + "M5Piib"],
                         data[grp]["resultsv2"][grp + "M5Pic"], data[grp]["resultsv2"][grp + "M5Piic"])

        scores_match6 = (data[grp]["resultsv2"][grp + "M6Pia"], data[grp]["resultsv2"][grp + "M6Piia"],
                         data[grp]["resultsv2"][grp + "M6Pib"], data[grp]["resultsv2"][grp + "M6Piib"],
                         data[grp]["resultsv2"][grp + "M6Pic"], data[grp]["resultsv2"][grp + "M6Piic"])

        scores_match7 = (data[grp]["resultsv2"][grp + "M7Pia"], data[grp]["resultsv2"][grp + "M7Piia"],
                         data[grp]["resultsv2"][grp + "M7Pib"], data[grp]["resultsv2"][grp + "M7Piib"],
                         data[grp]["resultsv2"][grp + "M7Pic"], data[grp]["resultsv2"][grp + "M7Piic"])

        scores_match8 = (data[grp]["resultsv2"][grp + "M8Pia"], data[grp]["resultsv2"][grp + "M8Piia"],
                         data[grp]["resultsv2"][grp + "M8Pib"], data[grp]["resultsv2"][grp + "M8Piib"],
                         data[grp]["resultsv2"][grp + "M8Pic"], data[grp]["resultsv2"][grp + "M8Piic"])

        scores_match9 = (data[grp]["resultsv2"][grp + "M9Pia"], data[grp]["resultsv2"][grp + "M9Piia"],
                         data[grp]["resultsv2"][grp + "M9Pib"], data[grp]["resultsv2"][grp + "M9Piib"],
                         data[grp]["resultsv2"][grp + "M9Pic"], data[grp]["resultsv2"][grp + "M9Piic"])

        scores_match10 = (data[grp]["resultsv2"][grp + "M10Pia"], data[grp]["resultsv2"][grp + "M10Piia"],
                          data[grp]["resultsv2"][grp + "M10Pib"], data[grp]["resultsv2"][grp + "M10Piib"],
                          data[grp]["resultsv2"][grp + "M10Pic"], data[grp]["resultsv2"][grp + "M10Piic"])

        scores_list = [scores_match1, scores_match2, scores_match3, scores_match4, scores_match5, scores_match6,
                       scores_match7, scores_match8, scores_match9, scores_match10]

    except Exception as e:
        log.error("::[%s]::'scores_list_generator2' General Exception:\n%s" % (logExtra, str(e)))
        scores_list = []

    return scores_list


def add_score_result(log, input_score_result, min_score_to_win=21):
    """ Processes input scores for score summary tuple including winner

    Notes, return tuple is format of:  bool, tuple, dict, dict, string
    example return:
    (True, (2, 21, 21, 9, 21, 20), {'net_points': -6, 'net_wins': 1}, {'net_points': 6, 'net_wins': -1}, 'teamA')

    :param log: logging object
    :param min_score_to_win: int for minimum score to win, used in basic validation
    :param input_score_result: tuple of input scores integers e.g. (21, 2, 21, 3, 0, 0)

    :return tuple for result: (success, score_result, team1_summary, team2_summary, winner)

    """

    success = False
    team1_summary = {}  # used for net points and net wins
    team2_summary = {}  # used for net points and net wins
    team1_wins = 0  # number games team 1 has won
    team2_wins = 0  # number games team 2 has won
    team1_net_points = 0
    team2_net_points = 0
    winner = ''
    flag_game3_played = True
    score_result = input_score_result
    log.debug("::[%s]::'add_score_result' input scores tuple:\n%s" % (logExtra, str(score_result)))

    try:

        INPUT_SCORE1 = input_score_result[0]
        INPUT_SCORE2 = input_score_result[1]
        INPUT_SCORE3 = input_score_result[2]
        INPUT_SCORE4 = input_score_result[3]
        INPUT_SCORE5 = input_score_result[4]
        INPUT_SCORE6 = input_score_result[5]

        if (INPUT_SCORE1 > INPUT_SCORE2):
            team1_wins += 1
        else:
            team2_wins += 1

        if (INPUT_SCORE3 > INPUT_SCORE4):
            team1_wins += 1
        else:
            team2_wins += 1

        # only evaluate game 3 if score is 1-1
        if (team1_wins == 1) and (team2_wins == 1):
            if (INPUT_SCORE5 > INPUT_SCORE6):
                team1_wins += 1
            else:
                team2_wins += 1
        else:
            flag_game3_played = False  # game 3 not played and can be 0-0 score
            # if user has incorrectly entered a game 3 score then throw Exception
            if not((INPUT_SCORE5 == 0) and (INPUT_SCORE6 == 0)):
                popup_error_input()
                raise ValueError('Input error in add_score_result')


        team1_net_points = (INPUT_SCORE1 - INPUT_SCORE2 + INPUT_SCORE3 - INPUT_SCORE4 + INPUT_SCORE5 - INPUT_SCORE6)
        team2_net_points = (-INPUT_SCORE1 + INPUT_SCORE2 - INPUT_SCORE3 + INPUT_SCORE4 - INPUT_SCORE5 + INPUT_SCORE6)

        team1_summary["net_points"] = team1_net_points
        team2_summary["net_points"] = team2_net_points

        team1_summary["net_wins"] = team1_wins - team2_wins
        team2_summary["net_wins"] = team2_wins - team1_wins

        if team1_wins == 2:
            winner = "teamA"
        else:
            winner = "teamB"

        # set some error conditions for draws (not allowed)
        if (INPUT_SCORE1 == INPUT_SCORE2):
            popup_error_input()
            raise ValueError('Input error in add_score_result')

        if (INPUT_SCORE3 == INPUT_SCORE4):
            popup_error_input()
            raise ValueError('Input error in add_score_result')

        # only check if game 3 was played
        if flag_game3_played:
            if (INPUT_SCORE5 == INPUT_SCORE6):
                popup_error_input()
                raise ValueError('Input error in add_score_result')

        # check at least 1 score in each game is the minimum score to win
        if ((INPUT_SCORE1 < min_score_to_win) and (INPUT_SCORE2 < min_score_to_win)):
            popup_error_input()
            raise ValueError('Input error in add_score_result')

        if ((INPUT_SCORE3 < min_score_to_win) and (INPUT_SCORE4 < min_score_to_win)):
            popup_error_input()
            raise ValueError('Input error in add_score_result')

        # only check if game 3 was played
        if flag_game3_played:
            if ((INPUT_SCORE5 < min_score_to_win) and (INPUT_SCORE6 < min_score_to_win)):
                popup_error_input()
                raise ValueError('Input error in add_score_result')

        # otherwise all ok and success is True
        success = True

    except ValueError as e:
        # do not popup Exception on ValueError as there is already popup for error input
        log.error("::[%s]::'add_score_result' ValueError Exception: %s" % (logExtra, str(e)))

    except Exception as e:
        log.error("::[%s]::'add_score_result' General Exception: %s" % (logExtra, str(e)))
        popup_exception("Exception in add_score_result\nDetail:\n" + str(e))

    return (success, score_result, team1_summary, team2_summary, winner)


def update_table_for_group(log, parent_window, group_number, workingDict):
    """ Update display table for group

    :param log: logging object
    :param parent_window: sg window object for calling parent
    :param group_number: int for group number
    :param workingDict: working dictionary for all tournament data

    :return: success: bool for success
    """

    success = False

    try:

        # get teams per group
        group_teams = workingDict["GRP" + str(group_number)]["config"]["grp_size"]
        log.debug("::[%s]::'update_table_for_group' teams for this group:%s" % (logExtra, group_teams))

        # create a dictionary for the group with all table data calculated and updated
        my_table_data_dict = process_table(log, workingDict, group_number, int(group_teams))
        log.debug("::[%s]::'update_table_for_group' group table data is:\n\n%s" %
                  (logExtra, (str(my_table_data_dict) + "\n\n")))

        # order the updated table data best to worst
        corrected_table_data_dict = table_order_analyser(log, my_table_data_dict, group_teams)
        log.info("::[%s]::'update_table_for_group' corrected table data is:\n\n%s" %
                (logExtra, (str(corrected_table_data_dict) + "\n\n")))

        # write the corrected data to the table display window
        update_group_table(log, parent_window, group_number, corrected_table_data_dict, int(group_teams))
        success = True

    except Exception as e:
        log.error("'update_table_for_group' General Exception:\n" + str(e))
        success = False

    return success


def process_table(log, workingDict, group, number_teams):
    """ Processes results for a given group to be used in the display table

    Note the pair name order is critical in this - must match GUI

    :param log: logging object
    :param workingDict: working dictionary for all tournament data
    :param group: int for group
    :param number_teams: int for number of teams in the group

    :return tableDict: dictionary of table keys:values

    """

    tableDict = {
        "success": False
    }

    data = workingDict
    group_key = "GRP" + str(group)    # e.g. "GRP1"
    match_key1 = group_key + "M1"     # e.g. "GRP1M1
    match_key2 = group_key + "M2"
    match_key3 = group_key + "M3"
    match_key4 = group_key + "M4"
    match_key5 = group_key + "M5"
    match_key6 = group_key + "M6"
    match_key7 = group_key + "M7"
    match_key8 = group_key + "M8"
    match_key9 = group_key + "M9"
    match_key10 = group_key + "M10"

    # table metrics for each pair in the group
    # minimum of 3, max of 5
    pair1_data = PairData(log, 1)
    pair2_data = PairData(log, 2)
    pair3_data = PairData(log, 3)
    if number_teams > 3:
        pair4_data = PairData(log, 4)
    if number_teams > 4:
        pair5_data = PairData(log, 5)

    try:

        if number_teams == 3:
            # order is 1v2, 3v1, 2v3
            # 1v2
            match1_result_tuple = PairData.create_match_tuple(log, group_key, match_key1, data)
            match_result1 = process_match_result(log, "Pair1", "Pair2", match1_result_tuple)
            log.debug("::[%s]::'process_table' match_result1 is: %s" % (logExtra, str(match_result1)))
            pair1_data.update_from_result(match_result1)
            pair2_data.update_from_result(match_result1)

            # 3v1
            match2_result_tuple = PairData.create_match_tuple(log, group_key, match_key2, data)
            match_result2 = process_match_result(log, "Pair3", "Pair1", match2_result_tuple)
            log.debug("::[%s]::'process_table' match_result2 is: %s" % (logExtra, str(match_result2)))
            pair3_data.update_from_result(match_result2)
            pair1_data.update_from_result(match_result2)

            # 2v3
            match3_result_tuple = PairData.create_match_tuple(log, group_key, match_key3, data)
            match_result3 = process_match_result(log, "Pair2", "Pair3", match3_result_tuple)
            log.debug("::[%s]::'process_table' match_result3 is: %s" % (logExtra, str(match_result3)))
            pair2_data.update_from_result(match_result3)
            pair3_data.update_from_result(match_result3)

            tableDict = pair1_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))
            tableDict = pair2_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))
            tableDict = pair3_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))

            tableDict["success"] = True

        if number_teams == 4:
            # order is 1v2, 3v4, 1v4, 2v3, 1v3, 2v4
            # 1v2
            match1_result_tuple = PairData.create_match_tuple(log, group_key, match_key1, data)
            match_result1 = process_match_result(log, "Pair1", "Pair2", match1_result_tuple)
            log.debug("::[%s]::'process_table' match_result1 is: %s" % (logExtra, str(match_result1)))
            pair1_data.update_from_result(match_result1)
            pair2_data.update_from_result(match_result1)

            # 3v4
            match2_result_tuple = PairData.create_match_tuple(log, group_key, match_key2, data)
            match_result2 = process_match_result(log, "Pair3", "Pair4", match2_result_tuple)
            log.debug("::[%s]::'process_table' match_result2 is: %s" % (logExtra, str(match_result2)))
            pair3_data.update_from_result(match_result2)
            pair4_data.update_from_result(match_result2)

            # 1v4
            match3_result_tuple = PairData.create_match_tuple(log, group_key, match_key3, data)
            match_result3 = process_match_result(log, "Pair1", "Pair4", match3_result_tuple)
            log.debug("::[%s]::'process_table' match_result3 is: %s" % (logExtra, str(match_result3)))
            pair1_data.update_from_result(match_result3)
            pair4_data.update_from_result(match_result3)

            # 2v3
            match4_result_tuple = PairData.create_match_tuple(log, group_key, match_key4, data)
            match_result4 = process_match_result(log, "Pair2", "Pair3", match4_result_tuple)
            log.debug("::[%s]::'process_table' match_result4 is: %s" % (logExtra, str(match_result4)))
            pair2_data.update_from_result(match_result4)
            pair3_data.update_from_result(match_result4)

            # 1v3
            match5_result_tuple = PairData.create_match_tuple(log, group_key, match_key5, data)
            match_result5 = process_match_result(log, "Pair1", "Pair3", match5_result_tuple)
            log.debug("::[%s]::'process_table' match_result5 is: %s" % (logExtra, str(match_result5)))
            pair1_data.update_from_result(match_result5)
            pair3_data.update_from_result(match_result5)

            # 2v4
            match6_result_tuple = PairData.create_match_tuple(log, group_key, match_key6, data)
            match_result6 = process_match_result(log, "Pair2", "Pair4", match6_result_tuple)
            log.debug("::[%s]::'process_table' match_result6 is: %s" % (logExtra, str(match_result6)))
            pair2_data.update_from_result(match_result6)
            pair4_data.update_from_result(match_result6)

            tableDict = pair1_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))
            tableDict = pair2_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))
            tableDict = pair3_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))
            tableDict = pair4_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))

            tableDict["success"] = True

        if number_teams == 5:
            # order: 4v1, 3v2, 3v5, 2v1, 2v4, 1v5, 1v3, 5v4, 5v2, 4v3
            # 4v1
            match1_result_tuple = PairData.create_match_tuple(log, group_key, match_key1, data)
            match_result1 = process_match_result(log, "Pair4", "Pair1", match1_result_tuple)
            log.debug("::[%s]::'process_table' match_result1 is: %s" % (logExtra, str(match_result1)))
            pair4_data.update_from_result(match_result1)
            pair1_data.update_from_result(match_result1)

            # 3v2
            match2_result_tuple = PairData.create_match_tuple(log, group_key, match_key2, data)
            match_result2 = process_match_result(log, "Pair3", "Pair2", match2_result_tuple)
            log.debug("::[%s]::'process_table' match_result2 is: %s" % (logExtra, str(match_result2)))
            pair3_data.update_from_result(match_result2)
            pair2_data.update_from_result(match_result2)

            # 3v5
            match3_result_tuple = PairData.create_match_tuple(log, group_key, match_key3, data)
            match_result3 = process_match_result(log, "Pair3", "Pair5", match3_result_tuple)
            log.debug("::[%s]::'process_table' match_result3 is: %s" % (logExtra, str(match_result3)))
            pair3_data.update_from_result(match_result3)
            pair5_data.update_from_result(match_result3)

            # 2v1
            match4_result_tuple = PairData.create_match_tuple(log, group_key, match_key4, data)
            match_result4 = process_match_result(log, "Pair2", "Pair1", match4_result_tuple)
            log.debug("::[%s]::'process_table' match_result4 is: %s" % (logExtra, str(match_result4)))
            pair2_data.update_from_result(match_result4)
            pair1_data.update_from_result(match_result4)

            # 2v4
            match5_result_tuple = PairData.create_match_tuple(log, group_key, match_key5, data)
            match_result5 = process_match_result(log, "Pair2", "Pair4", match5_result_tuple)
            log.debug("::[%s]::'process_table' match_result5 is: %s" % (logExtra, str(match_result5)))
            pair2_data.update_from_result(match_result5)
            pair4_data.update_from_result(match_result5)

            # 1v5
            match6_result_tuple = PairData.create_match_tuple(log, group_key, match_key6, data)
            match_result6 = process_match_result(log, "Pair1", "Pair5", match6_result_tuple)
            log.debug("::[%s]::'process_table' match_result6 is: %s" % (logExtra, str(match_result6)))
            pair1_data.update_from_result(match_result6)
            pair5_data.update_from_result(match_result6)

            # 1v3
            match7_result_tuple = PairData.create_match_tuple(log, group_key, match_key7, data)
            match_result7 = process_match_result(log, "Pair1", "Pair3", match7_result_tuple)
            log.debug("::[%s]::'process_table' match_result7 is: %s" % (logExtra, str(match_result7)))
            pair1_data.update_from_result(match_result7)
            pair3_data.update_from_result(match_result7)

            # 5v4
            match8_result_tuple = PairData.create_match_tuple(log, group_key, match_key8, data)
            match_result8 = process_match_result(log, "Pair5", "Pair4", match8_result_tuple)
            log.debug("::[%s]::'process_table' match_result8 is: %s" % (logExtra, str(match_result8)))
            pair5_data.update_from_result(match_result8)
            pair4_data.update_from_result(match_result8)

            # 5v2
            match9_result_tuple = PairData.create_match_tuple(log, group_key, match_key9, data)
            match_result9 = process_match_result(log, "Pair5", "Pair2", match9_result_tuple)
            log.debug("::[%s]::'process_table' match_result9 is: %s" % (logExtra, str(match_result9)))
            pair5_data.update_from_result(match_result9)
            pair2_data.update_from_result(match_result9)

            # 4v3
            match10_result_tuple = PairData.create_match_tuple(log, group_key, match_key10, data)
            match_result10 = process_match_result(log, "Pair4", "Pair3", match10_result_tuple)
            log.debug("::[%s]::'process_table' match_result10 is: %s" % (logExtra, str(match_result10)))
            pair4_data.update_from_result(match_result10)
            pair3_data.update_from_result(match_result10)

            tableDict = pair1_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))
            tableDict = pair2_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))
            tableDict = pair3_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))
            tableDict = pair4_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))
            tableDict = pair5_data.update_table_dict(tableDict)
            log.debug("::[%s]::'process_table' tabelDict is: %s" % (logExtra, str(tableDict)))

            tableDict["success"] = True

    except Exception as e:
        log.error("::[%s]::'process_table' General Exception:%s" % (logExtra, str(e)))

    return tableDict


def table_order_analyser(log, tableDict, teams):
    """ Analyses table data to derive correct pair positions

    Note:
    Position determined from wins then net games then net points and finally a tie breaker
    Use multiplier to weight accordingly:
        wins x 1000000
        net games x 10000
        net points x 10
        tie-breaker x 1 (add 5 to pair1, 4 to pair2, 3 to pair3 etc so there is never a draw)


    Example dict input:

    {'success': True, 'pair1_wins': 1, 'pair1_games_for': 2, 'pair1_games_against': 0, 'pair1_pts_for': 42,
     'pair1_pts_against': 10, 'pair1_net_games': 2, 'pair1_net_pts': 32, 'pair1_position': 1, 'pair2_wins': 0,
      'pair2_games_for': 0, 'pair2_games_against': 2, 'pair2_pts_for': 10, 'pair2_pts_against': 42,
       'pair2_net_games': -2, 'pair2_net_pts': -32, 'pair2_position': 2, 'pair3_wins': 0, 'pair3_games_for': 0,
        'pair3_games_against': 0, 'pair3_pts_for': 0, 'pair3_pts_against': 0, 'pair3_net_games': 0,
         'pair3_net_pts': 0, 'pair3_position': 3}

    :param log: logging object
    :param tableDict: input dictionary table data (unordered)
    :param teams: string for number teams in this group, expects "3", "4" or "5"
    :return updated_tableDict: dictionary of table keys:values
    """
    updated_tableDict = tableDict
    totals_list = []        # list of the weighted scores
    position_dict = {}      # uses key of weighted score and value indicating the associated pair

    try:
        teams = int(teams)

        pair1_total = (tableDict["pair1_wins"]*1000000) + (tableDict["pair1_net_games"]*10000) +\
                      (tableDict["pair1_net_pts"]*10) + 5
        position_dict[str(pair1_total)] = "pair1_position"

        pair2_total = (tableDict["pair2_wins"] * 1000000) + (tableDict["pair2_net_games"] * 10000) + \
                      (tableDict["pair2_net_pts"]*10) + 4
        position_dict[str(pair2_total)] = "pair2_position"

        pair3_total = (tableDict["pair3_wins"] * 1000000) + (tableDict["pair3_net_games"] * 10000) + \
                      (tableDict["pair3_net_pts"]*10) + 3
        position_dict[str(pair3_total)] = "pair3_position"

        if teams > 3:
            pair4_total = (tableDict["pair4_wins"] * 1000000) + (tableDict["pair4_net_games"] * 10000) + \
                          (tableDict["pair4_net_pts"] * 10) + 2
            position_dict[str(pair4_total)] = "pair4_position"

        if teams > 4:
            pair5_total = (tableDict["pair5_wins"] * 1000000) + (tableDict["pair5_net_games"] * 10000) + \
                          (tableDict["pair5_net_pts"] * 10) + 1
            position_dict[str(pair5_total)] = "pair5_position"


        # add all totals to the list and reverse sort, highest to lowest
        totals_list.append(pair1_total)
        totals_list.append(pair2_total)
        totals_list.append(pair3_total)
        if teams > 3:
            totals_list.append(pair4_total)
        if teams > 4:
            totals_list.append(pair5_total)

        totals_list.sort(reverse=True)

        log.debug("::[%s]::'table_order_analyser' weighted totals list is: %s" % (logExtra, str(totals_list)))

        # set position 1, 2 and 3 (4 and 5 as needed)
        # totals_list is an ordered list of all the scores and str of each score is a key in the position_dict
        # example position_dict: {"123456": "pair3_position", "100": "pair1_position", "-123": "pair2_position"}
        position1_key = position_dict[str(totals_list[0])]      # may find "pair3_position"
        updated_tableDict[position1_key] = 10                   # sets the correct position in the returned dict

        position2_key = position_dict[str(totals_list[1])]
        updated_tableDict[position2_key] = 20

        position3_key = position_dict[str(totals_list[2])]
        updated_tableDict[position3_key] = 30

        if teams > 3:
            position4_key = position_dict[str(totals_list[3])]
            updated_tableDict[position4_key] = 40

        if teams > 4:
            position5_key = position_dict[str(totals_list[4])]
            updated_tableDict[position5_key] = 50

    except Exception as e:
        log.error("::[%s]::'table_order_analyser' General Exception:%s" % (logExtra, str(e)))

    return updated_tableDict


def update_group_table(log, parent_window, group, updated_tableDict, number_teams):
    """ Updates the group table sg.Table in the relevant group tab in the Live Tournament window

    Notes:

    Example input updated_tableDict:

    {'success': True, 'pair1_wins': 1, 'pair1_games_for': 2, 'pair1_games_against': 0, 'pair1_pts_for': 42,
     'pair1_pts_against': 10, 'pair1_net_games': 2, 'pair1_net_pts': 32, 'pair1_position': 10, 'pair2_wins': 0,
      'pair2_games_for': 0, 'pair2_games_against': 2, 'pair2_pts_for': 10, 'pair2_pts_against': 42,
       'pair2_net_games': -2,'pair2_net_pts': -32, 'pair2_position': 20, 'pair3_wins': 0, 'pair3_games_for': 0,
        'pair3_games_against': 0,'pair3_pts_for': 0, 'pair3_pts_against': 0, 'pair3_net_games': 0,
         'pair3_net_pts': 0, 'pair3_position': 30}

    Prepare update for table in the format:
    window["GRP1_TABLE"].update([[1, 0, 3, 0, 0, 0, 0, 0], [2, 0, 4, 0, 0, 0, 0, 0], [3, 0, 5, 0, 0, 0, 0, 0]])

    where table is defined as:

    [sg.Table([[1, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0]],
                      ['Pair', 'Match Wins', 'Net Games', 'Net Points', 'Games Won', 'Games Lost', 'Points for',
                       'Points against'], row_height=40, alternating_row_color="#cccc00", header_text_color="green",
                      num_rows=3, key="GRP1_TABLE")],

    :param log: logging object
    :param parent_window: sg window object for calling parent
    :param group: int for group e.g "GRP1"
    :param updated_tableDict: table data as dict
    :param number_teams: int for number of teams in the group
    :return success : bool for success
    """
    d = updated_tableDict
    success = False
    list_row_pair1 = []
    list_row_pair2 = []
    list_row_pair3 = []
    list_row_pair4 = []
    list_row_pair5 = []
    update_list = []

    try:
        table_key = "GRP" + str(group) + "_TABLE"       # e.g. "GRP1_TABLE"

        list_row_pair1 = [1, d['pair1_wins'], d['pair1_net_games'], d['pair1_net_pts'], d['pair1_games_for'],
                          d['pair1_games_against'], d['pair1_pts_for'], d['pair1_pts_against']]
        list_row_pair2 = [2, d['pair2_wins'], d['pair2_net_games'], d['pair2_net_pts'], d['pair2_games_for'],
                          d['pair2_games_against'], d['pair2_pts_for'], d['pair2_pts_against']]
        list_row_pair3 = [3, d['pair3_wins'], d['pair3_net_games'], d['pair3_net_pts'], d['pair3_games_for'],
                          d['pair3_games_against'], d['pair3_pts_for'], d['pair3_pts_against']]
        if number_teams > 3:
            list_row_pair4 = [4, d['pair4_wins'], d['pair4_net_games'], d['pair4_net_pts'], d['pair4_games_for'],
                              d['pair4_games_against'], d['pair4_pts_for'], d['pair4_pts_against']]
        if number_teams > 4:
            list_row_pair5 = [5, d['pair5_wins'], d['pair5_net_games'], d['pair5_net_pts'], d['pair5_games_for'],
                              d['pair5_games_against'], d['pair5_pts_for'], d['pair5_pts_against']]

        # set rows according to position in input dictionary
        if (d['pair1_position'] == 10):
            update_list.append(list_row_pair1)
        elif (d['pair2_position'] == 10):
            update_list.append(list_row_pair2)
        elif (d['pair3_position'] == 10):
            update_list.append(list_row_pair3)
        elif 'pair4_position' in d:
            if d['pair4_position'] == 10:
                update_list.append(list_row_pair4)
            elif 'pair5_position' in d:
                if d['pair5_position'] == 10:
                    update_list.append(list_row_pair5)
            else:
                pass
        else:
            pass

        if (d['pair1_position'] == 20):
            update_list.append(list_row_pair1)
        elif (d['pair2_position'] == 20):
            update_list.append(list_row_pair2)
        elif (d['pair3_position'] == 20):
            update_list.append(list_row_pair3)
        elif 'pair4_position' in d:
            if d['pair4_position'] == 20:
                update_list.append(list_row_pair4)
            elif 'pair5_position' in d:
                if d['pair5_position'] == 20:
                    update_list.append(list_row_pair5)
            else:
                pass
        else:
            pass

        if (d['pair1_position'] == 30):
            update_list.append(list_row_pair1)
        elif (d['pair2_position'] == 30):
            update_list.append(list_row_pair2)
        elif (d['pair3_position'] == 30):
            update_list.append(list_row_pair3)
        elif 'pair4_position' in d:
            if d['pair4_position'] == 30:
                update_list.append(list_row_pair4)
            elif 'pair5_position' in d:
                if d['pair5_position'] == 30:
                    update_list.append(list_row_pair5)
            else:
                pass
        else:
            pass

        if (d['pair1_position'] == 40):
            update_list.append(list_row_pair1)
        elif (d['pair2_position'] == 40):
            update_list.append(list_row_pair2)
        elif (d['pair3_position'] == 40):
            update_list.append(list_row_pair3)
        elif 'pair4_position' in d:
            if d['pair4_position'] == 40:
                update_list.append(list_row_pair4)
            elif 'pair5_position' in d:
                if d['pair5_position'] == 40:
                    update_list.append(list_row_pair5)
            else:
                pass
        else:
            pass

        if (d['pair1_position'] == 50):
            update_list.append(list_row_pair1)
        elif (d['pair2_position'] == 50):
            update_list.append(list_row_pair2)
        elif (d['pair3_position'] == 50):
            update_list.append(list_row_pair3)
        elif 'pair4_position' in d:
            if d['pair4_position'] == 50:
                update_list.append(list_row_pair4)
            elif 'pair5_position' in d:
                if d['pair5_position'] == 50:
                    update_list.append(list_row_pair5)
            else:
                pass
        else:
            pass

        log.info("::[%s]::'update_group_table'::' update table list for %s" %
                  (logExtra, (table_key + " is: \n" + str(update_list))))
        parent_window[table_key].update(update_list)

        success = True

    except Exception as e:
        log.error("::[%s]::'update_group_table' General Exception: %s" % (logExtra, str(e)))

    return success


def process_match_result(log, pair_nameA, pair_nameB, match_result_tuple):
    """ Processes match result from tuple of scores and pair A and B names

    Example returned dict:
    {'Pair1': {'game_wins': 2, 'game_losses': 0, 'points_for': 42, 'points_against': 3}, 'Pair2': {'game_wins': 0,
     'game_losses': 2, 'points_for': 3, 'points_against': 42}, 'winner': 'Pair1'}

    :param log: logging object
    :param pair_nameA: string for pairA name
    :param pair_nameB: string for pairB name
    :param match_result_tuple: tuple of ints for results e.g. (21, 3, 21, 19, 0, 0)

    :return: match_summary: dict for key match stats

    """
    match_summary = {
        pair_nameA: {"game_wins": 0, "game_losses": 0, "points_for": 0, "points_against": 0},
        pair_nameB: {"game_wins": 0, "game_losses": 0, "points_for": 0, "points_against": 0},
        "winner": ""
    }
    pairA_wins = 0
    pairB_wins = 0
    pairA_pts_for = 0
    pairB_pts_for = 0

    try:
        if(match_result_tuple == (0, 0, 0, 0, 0, 0)):
            log.debug("::[%s]::'process_match_result' process_match_result input tuple was 0, 0, 0, 0, 0, 0" % logExtra)

        else:
            if(match_result_tuple[0] > match_result_tuple[1]):
                pairA_wins += 1
            elif(match_result_tuple[0] < match_result_tuple[1]):
                pairB_wins += 1
            else:
                pass  # should not get here

            if (match_result_tuple[2] > match_result_tuple[3]):
                pairA_wins += 1
            elif (match_result_tuple[2] < match_result_tuple[3]):
                pairB_wins += 1
            else:
                pass  # should not get here

            # below logic works even if game 3 not played and is 0, 0
            if (match_result_tuple[4] > match_result_tuple[5]):
                pairA_wins += 1
            elif (match_result_tuple[4] < match_result_tuple[5]):
                pairB_wins += 1
            else:
                pass  # should not get here

            pairA_pts_for = match_result_tuple[0] + match_result_tuple[2] + match_result_tuple[4]
            pairB_pts_for = match_result_tuple[1] + match_result_tuple[3] + match_result_tuple[5]

            match_summary[pair_nameA]["game_wins"] = pairA_wins
            match_summary[pair_nameA]["game_losses"] = pairB_wins
            match_summary[pair_nameA]["points_for"] = pairA_pts_for
            match_summary[pair_nameA]["points_against"] = pairB_pts_for

            match_summary[pair_nameB]["game_wins"] = pairB_wins
            match_summary[pair_nameB]["game_losses"] = pairA_wins
            match_summary[pair_nameB]["points_for"] = pairB_pts_for
            match_summary[pair_nameB]["points_against"] = pairA_pts_for

            if(pairA_wins)>(pairB_wins):
                match_summary["winner"] = pair_nameA
            elif(pairB_wins)>(pairA_wins):
                match_summary["winner"] = pair_nameB
            else:
                pass    # should not get here

    except Exception as e:
        log.error("::[%s]::'process_match_result' General Exception: %s" % (logExtra, str(e)))

    return match_summary


def update_GRPxMy_display(log, parent_window, group_results, group_string, match):
    """ Updates Group X and Match Y display summary

    Notes:
        example group_results:
         (True, (2, 21, 21, 9, 21, 20), {'net_points': -6, 'net_wins': 1}, {'net_points': 6, 'net_wins': -1}, 'teamA')

    :param log: logging object
    :param parent_window: sg window object for calling parent
    :param group_results: tuple for group results (see Notes)
    :param group_string: string for group e.g. "GRP1"
    :param match: int for match

    :return success: bool for success
    """

    success = False
    grpXmY = ""          # start of key, e.g. GRP1M1

    try:
        grpXmY = group_string + "M" + str(match)
        window = parent_window

        window[grpXmY + "Pia"].update(group_results[1][0])
        window[grpXmY + "Piia"].update(group_results[1][1])
        window[grpXmY + "Pib"].update(group_results[1][2])
        window[grpXmY + "Piib"].update(group_results[1][3])
        window[grpXmY + "Pic"].update(group_results[1][4])
        window[grpXmY + "Piic"].update(group_results[1][5])

        # make applicable winner message visible and the other invisible (in case scores were changed)
        if group_results[4] == "teamA":
            window[grpXmY + "winnerA"].update(visible=True)
            window[grpXmY + "winnerB"].update(visible=False)
        elif group_results[4] == "teamB":
            window[grpXmY + "winnerB"].update(visible=True)
            window[grpXmY + "winnerA"].update(visible=False)
        else:
            pass
        log.info("::[%s]::'update_GRPxMy_display' success with %s" % (logExtra,
                                                                      (group_string + ", match " + str(match))))

        success = True

    except Exception as e:
        log.error("::[%s]::'update_GRPxMy_display' General Exception: %s" % (logExtra, str(e)))

    return success


def player_names_from_workingData(log, group_string, workingDict, number_teams):
    """ Creates list of player names for group from working dict

    :param: log: logging object
    :param workingDict: working dictionary for all tournament data
    :param group_string: e.g. "GRP1"
    :param number_teams: int for number of teams in the group
    :return: player_name_list: list of player names
    """
    player_name_list = []
    grp = group_string

    try:
        player_name_list.append(workingDict[grp]["config"][grp + "_PLAYERA1-DISPLAY"])
        player_name_list.append(workingDict[grp]["config"][grp + "_PLAYERA2-DISPLAY"])
        player_name_list.append(workingDict[grp]["config"][grp + "_PLAYERB1-DISPLAY"])
        player_name_list.append(workingDict[grp]["config"][grp + "_PLAYERB2-DISPLAY"])
        player_name_list.append(workingDict[grp]["config"][grp + "_PLAYERC1-DISPLAY"])
        player_name_list.append(workingDict[grp]["config"][grp + "_PLAYERC2-DISPLAY"])
        if number_teams > 3:
            player_name_list.append(workingDict[grp]["config"][grp + "_PLAYERD1-DISPLAY"])
            player_name_list.append(workingDict[grp]["config"][grp + "_PLAYERD2-DISPLAY"])
        if number_teams > 4:
            player_name_list.append(workingDict[grp]["config"][grp + "_PLAYERE1-DISPLAY"])
            player_name_list.append(workingDict[grp]["config"][grp + "_PLAYERE2-DISPLAY"])

        log.info("::[%s]::'player_names_from_workingData' player display list:%s" % (logExtra, str(player_name_list)))

    except Exception as e:
        log.error("::[%s]::'player_names_from_workingData' General Exception: %s" % (logExtra, str(e)))
        player_name_list = []

    return player_name_list


def update_display_names(log, parent_window, name_list, group, workingDict):
    """ Updates display names for given name list and group

    :param: log: logging object
    :param parent_window: sg window object for calling parent
    :param name_list: list of strings for names
    :param group: int for group
    :param workingDict: working dictionary for all tournament data
    :return workingDict: updated working dictionary for all tournament data

    """

    group_str = "GRP" + str(group)
    display_key_list = []

    try:
        group_teams = int(workingDict[group_str]["config"]["grp_size"])

        log.info("::[%s]::'update_display_names' name list is %s " % (logExtra, str(name_list)))
        display_key_list = generate_player_keys_display(log, group_str, group_teams)
        log.info("::[%s]::'update_display_names' key list is %s " % (logExtra, str(display_key_list)))

        name_counter = 0
        for i in display_key_list:
            parent_window[i].update(name_list[name_counter])
            workingDict[group_str]["config"][i] = name_list[name_counter]
            name_counter += 1
        log.info("::[%s]::'update_display_names' display names updated for %s" % (logExtra, group_str))

    except Exception as e:
        log.error("::[%s]::'update_display_names' General Exception:%s" % (logExtra, str(e)))

    return workingDict


def generate_player_keys_display(log, group_str, number_teams):
    """ generates player display keys for input names from template

    Notes:
        example sg.Text key "GRP2_PLAYERC2-DISPLAY"

    :param log: logging object
    :param group_str: string for part of key e.g. GRP1
    :param number_teams: int for number of teams in the group

    :return: player_display_keys : list of strings for player names
    """
    player_display_keys = []

    if number_teams == 3:
        player_template_keys = ["_PLAYERA1-DISPLAY", "_PLAYERA2-DISPLAY", "_PLAYERB1-DISPLAY", "_PLAYERB2-DISPLAY",
                                "_PLAYERC1-DISPLAY", "_PLAYERC2-DISPLAY"]
    elif number_teams == 4:
        player_template_keys = ["_PLAYERA1-DISPLAY", "_PLAYERA2-DISPLAY", "_PLAYERB1-DISPLAY", "_PLAYERB2-DISPLAY",
                                "_PLAYERC1-DISPLAY", "_PLAYERC2-DISPLAY", "_PLAYERD1-DISPLAY", "_PLAYERD2-DISPLAY"]
    else:
        player_template_keys = ["_PLAYERA1-DISPLAY", "_PLAYERA2-DISPLAY", "_PLAYERB1-DISPLAY", "_PLAYERB2-DISPLAY",
                                "_PLAYERC1-DISPLAY", "_PLAYERC2-DISPLAY", "_PLAYERD1-DISPLAY", "_PLAYERD2-DISPLAY",
                                "_PLAYERE1-DISPLAY", "_PLAYERE2-DISPLAY"]

    try:
        for i in player_template_keys:
            player_display_keys.append(group_str + i)

    except Exception as e:
        log.error("::[%s]::'generate_player_keys_display' General Exception:%s" % (logExtra, str(e)))

    return player_display_keys


def popup_save(log, data):
    """ saves current settings

    convert current dict to JSON and saves

    :param log: logging object
    :param data: dictionary for current working data

    """

    temp_json = ""
    fullSaveFile = ""

    layoutSave = [
        [sg.T("Save current settings and data")],
        [[sg.Input(key='INPUT_FILE_WINDOW', disabled=True, size=(80, 1)), sg.Button('Select File', key="GET_FILE_WINDOW")]],
        [sg.T("Enter filename to enable Save Tournament button", key="SAVE_MESSAGE")],
        [sg.B('Save Tournament', key='SAVE_CURRENT', disabled=True)],
        [sg.Button('Exit', key='EXIT_SAVE')]
    ]

    window = sg.Window("Save Tournamment", layoutSave, use_default_focus=False, finalize=True, modal=True,
                       icon=shuttleIcon)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "EXIT_SAVE":
            break

        if event == "SAVE_CURRENT":
            try:
                # convert working data dictionary to JSON
                temp_json = json.dumps(data, indent=4)
                fullSaveFile = values["INPUT_FILE_WINDOW"]

                with open(fullSaveFile, "w") as f:
                    f.write(temp_json)

                popup_saved(fullSaveFile)
                break

            except Exception as e:
                log.error("::[%s]::'popup_save' General Exception:%s" % (logExtra, str(e)))
                popup_exception("Event was SAVE_CURRENT\nDetail:\n" + str(e))
                break

        if event == "GET_FILE_WINDOW":
            my_filename = sg.popup_get_file("Select File (.json file type will be set automatically)",
                                            history=True, file_types=(('JSON Files', '*.json'),),
                                            save_as=True)

            if my_filename:
                if not (".json" in my_filename):
                    log.info("::[%s]::'popup_save' .json extension added as it was missing from user input filename:%s"
                             % (logExtra, str(my_filename)))
                    my_filename = my_filename + ".json"
                window['INPUT_FILE_WINDOW'].update(my_filename)
                window["SAVE_CURRENT"].update(disabled=False)
                window["SAVE_MESSAGE"].update(visible=False)
                window["INPUT_FILE_WINDOW"].update(disabled=False)

            log.info("::[%s]::'popup_save' - 'file select window' file selected: :%s" % (logExtra, str(my_filename)))

    window.close()


def popup_enter_score(log, event, workingDict, max_score=21,):
    """ window to enter match score

    enter_score_result will be of format:
    (success, score_result, team1_summary, team2_summary, winner): tuple of bool, tuple, dict, dict, string

    note that for min_winning_score that 15 and 21 assume NO SETTING (first to  this max score wins) but if set to 30
    then assumed SETTING is used and 2 clears points to a maximum of 30 is what is required

    event and workingDictionary used to give user better indication of which team is which drop-down selector

    :param: log: logging object
    :param: event: string for button event e.g. "UPDATE_GRP1M1"
    :param workingDict: working dictionary for all tournament data
    :param: max_score: int, kwarg for max points per game
    :return: enter_score_result: False or tuple

    """

    enter_score_result = ["Input Error"]
    log.info("::[%s]::'popup_enter_score' called with input max. score of:%s" % (logExtra, str(max_score)))

    # lookup dictionary for match order, key is g<group size>m<match number>
    # value is list of pairs involved in that match in the correct order ['4', '1']
    # 3 teams play order: 1v2, 3v1, 2v3
    # 4 teams play order: 1v2, 3v4, 1v4, 2v3, 1v3, 2v4
    # 5 teams play order: 4v1, 3v2, 3v5, 2v1, 2v4, 1v5, 1v3, 5v4, 5v2, 4v3
    teams_lookup = {
        "g3m1": [1, 2], "g3m2": [3, 1], "g3m3": [2, 3],
        "g4m1": [1, 2], "g4m2": [3, 4], "g4m3": [1, 4], "g4m4": [2, 3], "g4m5": [1, 3], "g4m6": [2, 4],
        "g5m1": [4, 1], "g5m2": [3, 2], "g5m3": [3, 5], "g5m4": [2, 1], "g5m5": [2, 4],
        "g5m6": [1, 5], "g5m7": [1, 3], "g5m8": [5, 4], "g5m9": [5, 2], "g5m10": [4, 3]
    }
    # lookup for pair colours
    colour_lookup = {1: pr1_colour, 2: pr2_colour, 3: pr3_colour, 4: pr4_colour, 5: pr5_colour}

    try:

        # extract group and match from event: "UPDATE_GRP1M1"
        match_string = event.replace("UPDATE_GRP", "")
        match_list = match_string.split("M")
        group = match_list[0]
        match = match_list[1]
        # find number teams in the group
        group_str = "GRP" + group
        group_teams = workingDict[group_str]["config"]["grp_size"]
        lookup_key = "g" + group_teams + "m" + match
        pair_list = teams_lookup[lookup_key]

        # vars for use in layout below
        pair_i_name = "Pair " + str(pair_list[0])
        pair_ii_name = "Pair " + str(pair_list[1])
        pair_i_colour = colour_lookup[pair_list[0]]
        pair_ii_colour = colour_lookup[pair_list[1]]

        if (max_score == 15):
            combo_score_list = combo_score_list_15
            min_winning_score = 15
        elif (max_score == 21):
            combo_score_list = combo_score_list_21
            min_winning_score = 21
        elif (max_score == 30):
            combo_score_list = combo_score_list_30
            min_winning_score = 21
        # set a default to 21
        else:
            combo_score_list = combo_score_list_21
            min_winning_score = 21

        score_result = (99, 99, 99, 99, 99, 99)  # tuple for reults for all 3 games
        team1_summary = {}  # used for net points and net wins
        team2_summary = {}  # used for net points and net wins
        team1_wins = 0  # number games team 1 has won
        team2_wins = 0  # number games team 2 has won
        team1_net_points = 0
        team2_net_points = 0
        winner = ''
        flag_game3_played = True

        layoutPopupScore = [
            [sg.Text("ENTER SCORE (minimum 2 games)")],
            [sg.T(pair_i_name, text_color=pair_i_colour), sg.T(" v "), sg.T(pair_ii_name, text_color=pair_ii_colour)],
            [sg.HSep()],
            [sg.T('Game1')],
            [sg.Combo(combo_score_list, default_value=0, key='INPUT_SCORE1'),
             sg.Combo(combo_score_list, default_value=0, key='INPUT_SCORE2')],
            [sg.T('Game2')],
            [sg.Combo(combo_score_list, default_value=0, key='INPUT_SCORE3'),
             sg.Combo(combo_score_list, default_value=0, key='INPUT_SCORE4')],
            [sg.T('Game3 (leave as 0 if not played)')],
            [sg.Combo(combo_score_list, default_value=0, key='INPUT_SCORE5'),
             sg.Combo(combo_score_list, default_value=0, key='INPUT_SCORE6')],
            [sg.B('Add Result')]
        ]

        window = sg.Window("Enter Score", layoutPopupScore, use_default_focus=False, finalize=True, modal=True,
                           icon=shuttleIcon, size=(300, 300))

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break
            if event == "Add Result":
                enter_score_result = []  # empty list to append entries to
                score_result = (values['INPUT_SCORE1'], values['INPUT_SCORE2'], values['INPUT_SCORE3'],
                                values['INPUT_SCORE4'], values['INPUT_SCORE5'], values['INPUT_SCORE6'])

                log.info("::[%s]::'popup_enter_score' calling 'add_score_result' with scores:%s" % (logExtra,
                                                                                                     str(score_result)))
                enter_score_result = add_score_result(log, score_result, min_score_to_win=min_winning_score)
                break

    except Exception as e:
        log.error("::[%s]::'popup_enter_score' General Exception:%s" % (logExtra, str(e)))
        enter_score_result = [False]

    window.close()
    return enter_score_result


def edit_player_names(log, parent_window, group, workingDict):
    """ Toggles editing for player names in the Group tab, removes option to edit and make update option visible

    :param: log: logging object
    :param parent_window: sg window object for calling parent
    :param group: int for group to prepend to keys
    :param workingDict: working dictionary for all tournament data

    """
    group_str = "GRP" + str(group)
    group_teams = int(workingDict[group_str]["config"]["grp_size"])
    player_template_keys = []
    json_name_keys = []

    if group_teams == 3:
        player_template_keys = ["_PLAYERA1", "_PLAYERA2", "_PLAYERB1", "_PLAYERB2", "_PLAYERC1", "_PLAYERC2"]
        json_name_keys = ["_PLAYERA1-DISPLAY", "_PLAYERA2-DISPLAY", "_PLAYERB1-DISPLAY", "_PLAYERB2-DISPLAY",
                          "_PLAYERC1-DISPLAY", "_PLAYERC2-DISPLAY"]

    elif group_teams == 4:
        player_template_keys = ["_PLAYERA1", "_PLAYERA2", "_PLAYERB1", "_PLAYERB2", "_PLAYERC1", "_PLAYERC2",
                                "_PLAYERD1", "_PLAYERD2"]
        json_name_keys = ["_PLAYERA1-DISPLAY", "_PLAYERA2-DISPLAY", "_PLAYERB1-DISPLAY", "_PLAYERB2-DISPLAY",
                          "_PLAYERC1-DISPLAY", "_PLAYERC2-DISPLAY", "_PLAYERD1-DISPLAY", "_PLAYERD2-DISPLAY"]

    else:
        player_template_keys = ["_PLAYERA1", "_PLAYERA2", "_PLAYERB1", "_PLAYERB2", "_PLAYERC1", "_PLAYERC2",
                                "_PLAYERD1", "_PLAYERD2", "_PLAYERE1", "_PLAYERE2"]
        json_name_keys = ["_PLAYERA1-DISPLAY", "_PLAYERA2-DISPLAY", "_PLAYERB1-DISPLAY", "_PLAYERB2-DISPLAY",
                          "_PLAYERC1-DISPLAY", "_PLAYERC2-DISPLAY", "_PLAYERD1-DISPLAY", "_PLAYERD2-DISPLAY",
                          "_PLAYERE1-DISPLAY", "_PLAYERE2-DISPLAY"]

    temp_player_keys = []
    temp_json_players = []

    # create correct list of keys
    for i in player_template_keys:
        temp_player_keys.append(group_str + i)              # e.g. ["GRP1_PLAYERA1", "GRP1_PLAYERA2" etc

    # sg window key is GRP1_PLAYERA1, json dict has "GRP8_PLAYERA1-DISPLAY": "undefined"
    # populate the sg.window key for the player with the working dict player name
    for i in json_name_keys:
        temp_json_players.append(workingDict[group_str]["config"][group_str + i])

    try:
        parent_window[group_str + "-UPDATE-PLAYERS"].update(visible=True)
        parent_window[group_str + "-EDIT-PLAYERS"].update(visible=False)
        temp_counter = 0
        for i in temp_player_keys:
            parent_window[i].update(visible=True)
            parent_window[i].update(temp_json_players[temp_counter])
            temp_counter += 1

    except Exception as e:
        log.error("::[%s]::'edit_player_names' General Exception:%s" % (logExtra, str(e)))


def generate_player_keys_inputs(log, group_str, number_teams):
    """ generates player keys for input names from template

    Notes:
        example sg.Input key GRP1_PLAYERA1

    :param: log: logging object
    :param group_str: string for part of key e.g. GRP1
    :param number_teams: int for number of teams in the group

    :return: player_inputs_keys : list of strings for player names
    """
    player_inputs_keys = []

    if number_teams == 3:
        player_template_keys = ["_PLAYERA1", "_PLAYERA2", "_PLAYERB1", "_PLAYERB2", "_PLAYERC1", "_PLAYERC2"]
    elif number_teams == 4:
        player_template_keys = ["_PLAYERA1", "_PLAYERA2", "_PLAYERB1", "_PLAYERB2", "_PLAYERC1", "_PLAYERC2",
                                "_PLAYERD1", "_PLAYERD2"]
    else:
        player_template_keys = ["_PLAYERA1", "_PLAYERA2", "_PLAYERB1", "_PLAYERB2", "_PLAYERC1", "_PLAYERC2",
                                "_PLAYERD1", "_PLAYERD2", "_PLAYERE1", "_PLAYERE2"]

    try:
        for i in player_template_keys:
            player_inputs_keys.append(group_str + i)

    except Exception as e:
        log.error("::[%s]::'generate_player_keys_inputs' General Exception:%s" % (logExtra, str(e)))

    return player_inputs_keys


def create_order_of_play(log, workingDict, active_groups):
    """ creates a human-readable order of play list for 'Tournament Summary' tab

    Notes:
    Example of a returned list
        ["GROUP 1 :: Pair 1 v Pair 2", "GROUP 1 :: Pair 3 v Pair 1", "GROUP 1 :: Pair 2 v Pair 3"]

    :param log: logging object
    :param workingDict: working dictionary for all tournament data
    :param active_groups: list of ints for active groups

    :return: play_order
    """

    play_order = []
    d = workingDict
    play_dict = {}      # used to hold all data about games remaing per group

    # working vars - set to default
    grp_size = 0
    grpx = ""
    temp_play_list = []
    temp_play_dict = {}
    games_remaining = 0
    group_adjustment = 0        # used to adjust group total to weight the % remaining

    try:
        for i in active_groups:
            temp_play_list = []
            temp_play_dict = {}
            games_remaining = 0
            grpx = "GRP" + str(i)
            grp_size = int(d[grpx]["config"]["grp_size"])

            if grp_size == 3:
                temp_play_list.append("GROUP " + str(i) + " :: Pair 1 v Pair 2")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 3 v Pair 1")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 2 v Pair 3")
                games_remaining = 3
                group_adjustment = 50

            if grp_size == 4:
                # play order: 1v2, 3v4, 1v4, 2v3, 1v3, 2v4
                temp_play_list.append("GROUP " + str(i) + " :: Pair 1 v Pair 2")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 3 v Pair 4")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 1 v Pair 4")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 2 v Pair 3")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 1 v Pair 3")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 2 v Pair 4")
                games_remaining = 6
                group_adjustment = 20

            if grp_size == 5:
                # play order: 4v1, 3v2, 3v5, 2v1, 2v4, 1v5, 1v3, 5v4, 5v2, 4v3
                temp_play_list.append("GROUP " + str(i) + " :: Pair 4 v Pair 1")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 3 v Pair 2")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 3 v Pair 5")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 2 v Pair 1")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 2 v Pair 4")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 1 v Pair 5")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 1 v Pair 3")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 5 v Pair 4")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 5 v Pair 2")
                temp_play_list.append("GROUP " + str(i) + " :: Pair 4 v Pair 3")
                games_remaining = 10
                group_adjustment = 0

            temp_play_dict["play_list"] = temp_play_list
            temp_play_dict["games_remaining"] = games_remaining
            # with % remaining being of interest, set weighted totals above remaining and further adjust for group
            # number (so not all groups equal) and group size (larger served first)
            temp_play_dict["weighted_total"] = (games_remaining*100) + i + group_adjustment
            temp_play_dict["remaining_metric"] = games_remaining*100
            play_dict[grpx] = temp_play_dict

        log.info("::[%s]::'create_order_of_play' play dictionary is:%s" % (logExtra, str(play_dict)))

        # example play_dict
        # play_dict = {
        #     'GRP1': {'play_list': ['GROUP 1 :: Pair 1 v Pair 3', 'GROUP 1 :: Pair 2 v Pair 4'],
        #              'games_remaining': 6, 'weighted_total': 421, 'remaining_metric': 400},
        #     'GRP2': {'play_list': ['GROUP 2 :: Pair 1 v Pair 3', 'GROUP 2 :: Pair 2 v Pair 4'],
        #              'games_remaining': 6, 'weighted_total': 422, 'remaining_metric': 400}
        # }

        # iterate through the play_dict to find the group with the highest % remaining - set next_grp to this group
        # if working correctly max iterations would be 8 groups x 10 games = 80
        loop_count = 0              # used to exit loop as a maximum value
        while loop_count < 200:
            loop_count += 1
            next_grp = ""    # used for next group to have a match added to the order of play - based on % remaining
            grp_percent_remaining = 0
            sum_games_remaining = 0     # used to exit loop, if sum all games remaining then exit
            for key, value in play_dict.items():
                sum_games_remaining = 0
                if (value['games_remaining']) > 0:
                    sum_games_remaining += value['games_remaining']
                    # grp_percent_remaining and next_grp will be the highest found so far
                    if (value['remaining_metric']/value['weighted_total']) > grp_percent_remaining:
                        grp_percent_remaining = (value['remaining_metric']/value['weighted_total'])
                        next_grp = key
                        #log.debug("::[%s]::'create_order_of_play' finds new highest remaining: %s" % (logExtra, key))

            # if all groups have 0 games remaining exit loop
            if sum_games_remaining == 0:
                log.debug("::[%s]::'create_order_of_play' no games remaining in any group" % logExtra)
                loop_count = 1000

            else:
                success, next_up, play_dict = process_next_match(log, next_grp, play_dict)
                log.debug("::[%s]::'create_order_of_play' next match is: %s" % (logExtra, next_up))
                if success:
                    play_order.append(next_up)


    except Exception as e:
        log.error("::[%s]::'create_order_of_play' General Exception:%s" % (logExtra, str(e)))

    return play_order


def process_next_match(log, group, play_dict):
    """ Updates play dictionary and returns next match
    Notes:
        Need to extract the first line in 'play_list' from relevant group
        Need to reduce games remaining for relevant group
        Need to adjust remaining metric for relevant group
        Example input dictionary
        play_dict = {
                 'GRP1': {'play_list': ['GROUP 1 :: Pair 1 v Pair 3', 'GROUP 1 :: Pair 2 v Pair 4'],
                        'games_remaining': 6, 'weighted_total': 421, 'remaining_metric': 400},
                'GRP2': {'play_list': ['GROUP 2 :: Pair 1 v Pair 3', 'GROUP 2 :: Pair 2 v Pair 4'],
                        'games_remaining': 6, 'weighted_total': 422, 'remaining_metric': 400}
        }

    :param group: string for group of interest (will match key in input dictionary)
    :param play_dict: dictionary for matches per group (see above)

    :return: tuple of bool, str, dict
    """
    success = False
    next_match = ""
    temp_list = []

    try:
        # log.debug("::[%s]::'process_next_match' input dictionary:%s" % (logExtra, str(play_dict)))
        play_dict[group]["games_remaining"] -= 1
        play_dict[group]["remaining_metric"] -= 100
        temp_list = play_dict[group]["play_list"]
        next_match = temp_list.pop(0)
        play_dict[group]["play_list"] = temp_list
        # log.debug("::[%s]::'process_next_match' adjusted dictionary:%s" % (logExtra, str(play_dict)))
        success = True

    except Exception as e:
        log.error("::[%s]::'process_next_match' General Exception:%s" % (logExtra, str(e)))
        success = False
        next_match = ""
        play_dict = {}

    return success, next_match, play_dict

