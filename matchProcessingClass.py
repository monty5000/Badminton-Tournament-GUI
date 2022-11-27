# class for match processing functions

import os
logExtra = os.path.basename(__file__)


class PairData(object):
    """ Class for match metrics for a given pair"""

    def __init__(self, log, pair):
        """ Constructor

        Notes:

        :param: log: logging object
        :param: pair: int for pair number
        """
        self.log = log
        self.pair_number = pair
        self.wins = 0
        self.games_for = 0
        self.games_against = 0
        self.pts_for = 0
        self.pts_against = 0
        self.net_games = -99
        self.net_pts = -999
        self.position = pair        # set initially to the pair number to ensure all pairs different

        self.log.debug("::[%s]:: A new PairData instance is created for pair %d" % (logExtra, self.pair_number))

    @staticmethod
    def create_match_tuple(log, group_key, match_key, data):
        """ Creates simple tuple for match

        Notes:
            Relates back to JSON definition where two pairs in any match Pi and Pii and potentially 3 games per match
            a, b, and c

         :param log: logging object
         :param group_key: string for group key e.g. "GRP1"
         :param match_key: string for match key e.g. "GRP1M1
         :param data: working dictionary for all tournament data

         :return result_tuple: tuple of scores for match
         """
        try:
            result_tuple = (data[group_key]["resultsv2"][match_key + "Pia"],
                            data[group_key]["resultsv2"][match_key + "Piia"],
                            data[group_key]["resultsv2"][match_key + "Pib"],
                            data[group_key]["resultsv2"][match_key + "Piib"],
                            data[group_key]["resultsv2"][match_key + "Pic"],
                            data[group_key]["resultsv2"][match_key + "Piic"])

        except Exception as e:
            log.error("::[%s]::'create_match_tuple' General Exception:%s" % (logExtra, str(e)))
            result_tuple = (0, 0, 0, 0, 0, 0)

        return result_tuple

    def update_from_result(self, match_result):
        """ Updates the pair data from a given match result

        Notes:
            Example match_result dictionary
             {'Pair3': {'game_wins': 2, 'game_losses': 0, 'points_for': 42, 'points_against': 3}, 'Pair1':
              {'game_wins': 0, 'game_losses': 2, 'points_for': 3, 'points_against': 42}, 'winner': 'Pair3'}

        :param match_result: dictionary for match result
        :return:
        """

        pair_str = "Pair" + str(self.pair_number)   # example creates 'Pair1'

        try:

            self.games_for += match_result[pair_str]['game_wins']
            self.games_against += match_result[pair_str]['game_losses']
            self.pts_for += match_result[pair_str]['points_for']
            self.pts_against += match_result[pair_str]['points_against']
            self.net_games = self.games_for - self.games_against
            self.net_pts = self.pts_for - self.pts_against
            if match_result['winner'] == pair_str:
                self.wins += 1

        except Exception as e:
            self.log.error("::[%s]::'update_from_result' General Exception:%s" % (logExtra, str(e)))

    def update_table_dict(self, table_dict):
        """ Updates table dictionary with pair results

        :param table_dict: dictionary to be updated
        :return:
        """

        key_part = 'pair' + str(self.pair_number) + "_"    # example creates 'pair1_'

        try:

            table_dict[key_part + 'wins'] = self.wins
            table_dict[key_part + 'games_for'] = self.games_for
            table_dict[key_part + 'games_against'] = self.games_against
            table_dict[key_part + 'pts_for'] = self.pts_for
            table_dict[key_part + 'pts_against'] = self.pts_against
            table_dict[key_part + 'net_games'] = self.net_games
            table_dict[key_part + 'net_pts'] = self.net_pts
            table_dict[key_part + 'position'] = self.position

            return table_dict

        except Exception as e:
            self.log.error("::[%s]::'update_table_dict' General Exception: %s" % (logExtra, str(e)))
            table_dict = {
                "success": False
            }
            return table_dict
