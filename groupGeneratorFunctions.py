# generates layouts for groups
# requirement is now 1-8 groups of 3-5 teams per group

import os
import PySimpleGUI as sg

logExtra = os.path.basename(__file__)

# used for text colour for pair names
pr1_colour = "white"
pr2_colour = "blue"
pr3_colour = "purple"
pr4_colour = "#006600"  # greenish
pr5_colour = "#990000"

but_sz1 = (14, 1)       # button size for edit and update
but_pad = 10            # button padding for edit and update
but_col = "#663300"     # button colour for edit and update

tab_hd_col = "White"    # table header colour
alt_row_col = "#9494b8"     # table alternating row colour


def generate_GRP(log, grp_number, teams):
    """ Generates layout for group

    Notes:
    :param log: logging object
    :param grp_number: string for group number
    :param teams: string for number teams per group
    :return layoutGRP: list of sg. objects on success, else False
    """

    layoutGRP = False
    grp = str(grp_number)
    teams = str(teams)
    results_column_GRP = []
    player_column_GRP = []

    try:
        log.info("::[%s]::'generate_GRP' grp_number %s teams is: %s" % (logExtra, grp, teams))

        if teams == "3":
            results_column_GRP = [
                [sg.T("GROUP" + grp + " RESULTS", font='Any 13', text_color='black')],
                [sg.HSep()],
                [sg.T("Pair 1", text_color=pr1_colour), sg.T(" v "), sg.T("Pair 2", text_color=pr2_colour),
                 sg.T(" || WINNER Pair1 ||", key="GRP" + grp + "M1winnerA", text_color=pr1_colour, visible=False),
                 sg.T(" || WINNER Pair2 ||", key="GRP" + grp + "M1winnerB", text_color=pr2_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M1Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M1Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M1Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M1Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M1Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M1Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M1")],
                [sg.T("Pair 3", text_color=pr3_colour), sg.T(" v "), sg.T("Pair 1", text_color=pr1_colour),
                 sg.T(" || WINNER Pair3 ||", key="GRP" + grp + "M2winnerA", text_color=pr3_colour, visible=False),
                 sg.T(" || WINNER Pair1 ||", key="GRP" + grp + "M2winnerB", text_color=pr1_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M2Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M2Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M2Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M2Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M2Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M2Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M2")],
                [sg.T("Pair 2", text_color=pr2_colour), sg.T(" v "), sg.T("Pair 3", text_color=pr3_colour),
                 sg.T(" || WINNER Pair2 ||", key="GRP" + grp + "M3winnerA", text_color=pr2_colour, visible=False),
                 sg.T(" || WINNER Pair3 ||", key="GRP" + grp + "M3winnerB", text_color=pr3_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M3Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M3Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M3Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M3Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M3Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M3Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M3")],
                [sg.T("")],
                [sg.T("")]
            ]

            player_column_GRP = [
                [sg.T("PLAYER DETAILS", key="GRP" + grp + "_HEADER", font='Any 13')],
                [sg.HSep()],
                [sg.T("Pair1 Player1:", text_color=pr1_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERA1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERA1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair1 Player2:", text_color=pr1_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERA2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERA2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair2 Player1:", text_color=pr2_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERB1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERB1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair2 Player2:", text_color=pr2_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERB2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERB2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair3 Player1:", text_color=pr3_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERC1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERC1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair3 Player2:", text_color=pr3_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERC2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERC2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.pin(sg.Button('Update Players', key="GRP" + grp + "-UPDATE-PLAYERS", visible=False,
                                  button_color=but_col, size=but_sz1, font='Any 11 bold', pad=but_pad), shrink=True)],
                [sg.pin(sg.Button('Edit Players', key="GRP" + grp + "-EDIT-PLAYERS", visible=True, button_color=but_col,
                                  size=but_sz1, font='Any 11 bold', pad=but_pad), shrink=True)]

            ]

            table_element = [
                [sg.Table([[1, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0]],
                          ['Pair', 'Match Wins', 'Net Games', 'Net Points', 'Games Won', 'Games Lost', 'Points for',
                           'Points against'], row_height=40, alternating_row_color=alt_row_col,
                          header_text_color=tab_hd_col, num_rows=3, key=("GRP" + grp + "_TABLE"))],
                [sg.T("")],
                [sg.T("NOTE: Ranked on 'Match Wins'. If tied consider 'Net Games'. If still tied consider"
                      " 'Net Points'.",
                      font="Courier 9 italic")],
                [sg.HSep()],
                [sg.T("")]

            ]

            # --- GRP layout ---
            layoutGRP = [
                [sg.Column(results_column_GRP, vertical_alignment="Top"),
                 #sg.Column(player_column_GRP, vertical_alignment="Top")],
                 sg.Column(player_column_GRP, vertical_alignment="Top")],
                [sg.Column(table_element)]
            ]




        elif teams == "4":
            # play order: 1v2, 3v4, 1v4, 2v3, 1v3, 2v4
            results_column_GRP_1 = [
                [sg.T("GROUP" + grp + "  RESULTS (Part 1)", font='Any 13', text_color='black')],
                [sg.HSep()],
                [sg.T("Pair 1", text_color=pr1_colour), sg.T(" v "), sg.T("Pair 2", text_color=pr2_colour),
                 sg.T(" || WINNER Pair1 ||", key="GRP" + grp + "M1winnerA", text_color=pr1_colour, visible=False),
                 sg.T(" || WINNER Pair2 ||", key="GRP" + grp + "M1winnerB", text_color=pr2_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M1Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M1Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M1Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M1Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M1Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M1Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M1")],
                [sg.T("Pair 3", text_color=pr3_colour), sg.T(" v "), sg.T("Pair 4", text_color=pr4_colour),
                 sg.T(" || WINNER Pair3 ||", key="GRP" + grp + "M2winnerA", text_color=pr3_colour, visible=False),
                 sg.T(" || WINNER Pair4 ||", key="GRP" + grp + "M2winnerB", text_color=pr4_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M2Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M2Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M2Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M2Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M2Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M2Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M2")],
                [sg.T("Pair 1", text_color=pr1_colour), sg.T(" v "), sg.T("Pair 4", text_color=pr4_colour),
                 sg.T(" || WINNER Pair1 ||", key="GRP" + grp + "M3winnerA", text_color=pr1_colour, visible=False),
                 sg.T(" || WINNER Pair4 ||", key="GRP" + grp + "M3winnerB", text_color=pr4_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M3Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M3Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M3Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M3Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M3Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M3Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M3")],
                [sg.T("")],
                [sg.T("")],
                [sg.T("")],
                [sg.T("")]
            ]

            results_column_GRP_2 = [
                [sg.T("GROUP" + grp + "  RESULTS (Part 2)", font='Any 13', text_color='black')],
                [sg.HSep()],
                [sg.T("Pair 2", text_color=pr2_colour), sg.T(" v "), sg.T("Pair 3", text_color=pr3_colour),
                 sg.T(" || WINNER Pair2 ||", key="GRP" + grp + "M4winnerA", text_color=pr2_colour, visible=False),
                 sg.T(" || WINNER Pair3 ||", key="GRP" + grp + "M4winnerB", text_color=pr3_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M4Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M4Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M4Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M4Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M4Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M4Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M4")],
                [sg.T("Pair 1", text_color=pr1_colour), sg.T(" v "), sg.T("Pair 3", text_color=pr3_colour),
                 sg.T(" || WINNER Pair1 ||", key="GRP" + grp + "M5winnerA", text_color=pr1_colour, visible=False),
                 sg.T(" || WINNER Pair3 ||", key="GRP" + grp + "M5winnerB", text_color=pr3_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M5Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M5Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M5Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M5Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M5Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M5Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M5")],
                [sg.T("Pair 2", text_color=pr2_colour), sg.T(" v "), sg.T("Pair 4", text_color=pr4_colour),
                 sg.T(" || WINNER Pair2 ||", key="GRP" + grp + "M6winnerA", text_color=pr2_colour, visible=False),
                 sg.T(" || WINNER Pair4 ||", key="GRP" + grp + "M6winnerB", text_color=pr4_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M6Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M6Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M6Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M6Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M6Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M6Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M6")],
                [sg.T("")],
                [sg.T("")],
                [sg.T("")],
                [sg.T("")]
            ]

            player_column_GRP = [
                [sg.T("PLAYER DETAILS", key="GRP" + grp + "_HEADER", font='Any 13')],
                [sg.HSep()],
                [sg.T("Pair1 Player1:", text_color=pr1_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERA1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERA1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair1 Player2:", text_color=pr1_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERA2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERA2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair2 Player1:", text_color=pr2_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERB1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERB1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair2 Player2:", text_color=pr2_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERB2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERB2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair3 Player1:", text_color=pr3_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERC1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERC1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair3 Player2:", text_color=pr3_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERC2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERC2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair4 Player1:", text_color=pr4_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERD1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERD1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair4 Player2:", text_color=pr4_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERD2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERD2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.pin(sg.Button('Update Players', key="GRP" + grp + "-UPDATE-PLAYERS", visible=False,
                                  button_color=but_col, size=but_sz1, font='Any 11 bold', pad=but_pad), shrink=True)],
                [sg.pin(sg.Button('Edit Players', key="GRP" + grp + "-EDIT-PLAYERS", visible=True, button_color=but_col,
                                  size=but_sz1, font='Any 11 bold', pad=but_pad), shrink=True)]
            ]

            table_element = [
                [sg.Table([[1, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0],
                           [4, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0, 0, 0], [6, 0, 0, 0, 0, 0, 0, 0]],
                          ['Pair', 'Match Wins', 'Net Games', 'Net Points', 'Games Won', 'Games Lost', 'Points for',
                           'Points against'], row_height=40, alternating_row_color=alt_row_col,
                          header_text_color=tab_hd_col, num_rows=4, key="GRP" + grp + "_TABLE")],
                [sg.T(
                    "NOTE: Ranked on 'Match Wins'. If tied consider 'Net Games'. If still tied consider 'Net Points'.",
                    font="Courier 9 italic")]
            ]

            # --- GRP layout ---
            layoutGRP = [
                [sg.Column(results_column_GRP_1, vertical_alignment="Top"),
                 sg.Column(results_column_GRP_2, vertical_alignment="Top"),
                 sg.Column(player_column_GRP, vertical_alignment="Top")],
                [sg.Column(table_element)]
            ]

        elif teams == "5":
            # play order: 4v1, 3v2, 3v5, 2v1, 2v4, 1v5, 1v3, 5v4, 5v2, 4v3
            results_column_GRP_1 = [
                [sg.T("GROUP" + grp + " RESULTS (Part 1)", font='Any 13', text_color='black')],
                [sg.HSep()],
                [sg.T("Pair 4", text_color=pr4_colour), sg.T(" v "), sg.T("Pair 1", text_color=pr1_colour),
                 sg.T(" || WINNER Pair4 ||", key="GRP" + grp + "M1winnerA", text_color=pr4_colour, visible=False),
                 sg.T(" || WINNER Pair1 ||", key="GRP" + grp + "M1winnerB", text_color=pr1_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M1Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M1Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M1Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M1Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M1Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M1Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M1")],
                [sg.T("Pair 3", text_color=pr3_colour), sg.T(" v "), sg.T("Pair 2", text_color=pr2_colour),
                 sg.T(" || WINNER Pair3 ||", key="GRP" + grp + "M2winnerA", text_color=pr3_colour, visible=False),
                 sg.T(" || WINNER Pair2 ||", key="GRP" + grp + "M2winnerB", text_color=pr2_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M2Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M2Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M2Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M2Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M2Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M2Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M2")],
                [sg.T("Pair 3", text_color=pr3_colour), sg.T(" v "), sg.T("Pair 5", text_color=pr5_colour),
                 sg.T(" || WINNER Pair3 ||", key="GRP" + grp + "M3winnerA", text_color=pr3_colour, visible=False),
                 sg.T(" || WINNER Pair5 ||", key="GRP" + grp + "M3winnerB", text_color=pr5_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M3Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M3Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M3Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M3Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M3Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M3Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M3")],
                [sg.T("Pair 2", text_color=pr2_colour), sg.T(" v "), sg.T("Pair 1", text_color=pr1_colour),
                 sg.T(" || WINNER Pair2 ||", key="GRP" + grp + "M4winnerA", text_color=pr2_colour, visible=False),
                 sg.T(" || WINNER Pair1 ||", key="GRP" + grp + "M4winnerB", text_color=pr1_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M4Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M4Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M4Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M4Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M4Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M4Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M4")],
                [sg.T("Pair 2", text_color=pr2_colour), sg.T(" v "), sg.T("Pair 4", text_color=pr4_colour),
                 sg.T(" || WINNER Pair2 ||", key="GRP" + grp + "M5winnerA", text_color=pr2_colour, visible=False),
                 sg.T(" || WINNER Pair4 ||", key="GRP" + grp + "M5winnerB", text_color=pr4_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M5Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M5Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M5Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M5Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M5Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M5Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M5")]
                ]

            results_column_GRP_2 = [
                [sg.T("GROUP" + grp + " RESULTS (Part 2)", font='Any 13', text_color='black')],
                [sg.HSep()],
                [sg.T("Pair 1", text_color=pr1_colour), sg.T(" v "), sg.T("Pair 5", text_color=pr5_colour),
                 sg.T(" || WINNER Pair1 ||", key="GRP" + grp + "M6winnerA", text_color=pr1_colour, visible=False),
                 sg.T(" || WINNER Pair5 ||", key="GRP" + grp + "M6winnerB", text_color=pr5_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M6Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M6Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M6Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M6Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M6Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M6Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M6")],
                [sg.T("Pair 1", text_color=pr1_colour), sg.T(" v "), sg.T("Pair 3", text_color=pr3_colour),
                 sg.T(" || WINNER Pair1 ||", key="GRP" + grp + "M7winnerA", text_color=pr1_colour, visible=False),
                 sg.T(" || WINNER Pair3 ||", key="GRP" + grp + "M7winnerB", text_color=pr3_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M7Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M7Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M7Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M7Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M7Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M7Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M7")],
                [sg.T("Pair 5", text_color=pr5_colour), sg.T(" v "), sg.T("Pair 4", text_color=pr4_colour),
                 sg.T(" || WINNER Pair5 ||", key="GRP" + grp + "M8winnerA", text_color=pr5_colour, visible=False),
                 sg.T(" || WINNER Pair4 ||", key="GRP" + grp + "M8winnerB", text_color=pr4_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M8Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M8Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M8Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M8Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M8Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M8Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M8")],
                [sg.T("Pair 5", text_color=pr5_colour), sg.T(" v "), sg.T("Pair 2", text_color=pr2_colour),
                 sg.T(" || WINNER Pair5 ||", key="GRP" + grp + "M9winnerA", text_color=pr5_colour, visible=False),
                 sg.T(" || WINNER Pair2 ||", key="GRP" + grp + "M9winnerB", text_color=pr2_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M9Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M9Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M9Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M9Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M9Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M9Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M9")],
                [sg.T("Pair 4", text_color=pr4_colour), sg.T(" v "), sg.T("Pair 3", text_color=pr3_colour),
                 sg.T(" || WINNER Pair4 ||", key="GRP" + grp + "M10winnerA", text_color=pr4_colour, visible=False),
                 sg.T(" || WINNER Pair3 ||", key="GRP" + grp + "M10winnerB", text_color=pr3_colour, visible=False)],
                [sg.T(0, key='GRP' + grp + 'M10Pia'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M10Piia'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M10Pib'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M10Piib'), sg.T(' :: '),
                 sg.T(0, key='GRP' + grp + 'M10Pic'), sg.T('-'), sg.T(0, key='GRP' + grp + 'M10Piic'),
                 sg.B('Update Score', key="UPDATE_GRP" + grp + "M10")]
            ]

            table_element = [
                [sg.Table([[1, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0],
                           [4, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0, 0, 0], [6, 0, 0, 0, 0, 0, 0, 0],
                           [7, 0, 0, 0, 0, 0, 0, 0], [8, 0, 0, 0, 0, 0, 0, 0], [9, 0, 0, 0, 0, 0, 0, 0],
                           [10, 0, 0, 0, 0, 0, 0, 0]],
                          ['Pair', 'Match Wins', 'Net Games', 'Net Points', 'Games Won', 'Games Lost', 'Points for',
                           'Points against'], row_height=40, alternating_row_color=alt_row_col,
                          header_text_color=tab_hd_col, num_rows=5, key="GRP" + grp + "_TABLE")],
                [sg.T(
                    "NOTE: Ranked on 'Match Wins'. If tied consider 'Net Games'. If still tied consider 'Net Points'.",
                    font="Courier 9 italic")]
            ]

            player_column_GRP_1 = [
                [sg.T("PLAYER DETAILS (Part 1)", key="GRP" + grp + "_HEADER", font='Any 11')],
                [sg.T("Pair1 Player1:", text_color=pr1_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERA1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERA1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair1 Player2:", text_color=pr1_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERA2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERA2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair2 Player1:", text_color=pr2_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERB1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERB1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair2 Player2:", text_color=pr2_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERB2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERB2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.pin(sg.Button('Update Players', key="GRP" + grp + "-UPDATE-PLAYERS", visible=False,
                                  button_color=but_col, size=but_sz1, font='Any 11 bold', pad=but_pad), shrink=True)],
                [sg.pin(sg.Button('Edit Players', key="GRP" + grp + "-EDIT-PLAYERS", visible=True, button_color=but_col,
                                  size=but_sz1, font='Any 11 bold', pad=but_pad), shrink=True)]

            ]

            player_column_GRP_2 = [
                [sg.T("PLAYER DETAILS (Part 2)", key="GRP" + grp + "_HEADER", font='Any 11')],
                [sg.HSep()],
                [sg.T("Pair3 Player1:", text_color=pr3_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERC1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERC1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair3 Player2:", text_color=pr3_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERC2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERC2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair4 Player1:", text_color=pr4_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERD1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERD1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair4 Player2:", text_color=pr4_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERD2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERD2", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair5 Player1:", text_color=pr5_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERE1-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERE1", default_text="empty", visible=False),
                        shrink=True)],
                [sg.T("Pair5 Player2:", text_color=pr5_colour),
                 sg.T("", key="GRP" + grp + "_PLAYERE2-DISPLAY")],
                [sg.pin(sg.In(size=(25, 1), key="GRP" + grp + "_PLAYERE2", default_text="empty", visible=False),
                        shrink=True)]
            ]

            # --- GRP layout ---
            layoutGRP = [
                [sg.Column(results_column_GRP_1, expand_y=True),
                 sg.Column(results_column_GRP_2, expand_y=True),
                 sg.Column(player_column_GRP_1, expand_y=True),
                 sg.Column(player_column_GRP_2, expand_y=True),
                 ], [sg.Column(table_element)]
            ]

        else:
            log.warning("::[%s]::'generate_GRP' teams value unexpected, teams is: %s" % (logExtra, str(teams)))
            layoutGRP = False

    except Exception as e:
        log.error("::[%s]::'generate_GRP' General Exception: %s" % (logExtra, str(e)))
        layoutGRP = False

    return layoutGRP

