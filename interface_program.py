#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Program class.
- Class data, pre-work for insert data;
- Class Interface, allow us to display each step of program.
"""

from requests_mysql import (MySqlConnector)
from constantes import (NO_RECORD)


class Interface():
    """
    This class allows us to generate data from sql request for the user interface.
    """

    def __init__(self):

        self.list_valid_input = ''

    def display(self, info_pre_data, info_post_data, request=None, display_result='Yes'):
        """
        This method allows us to display each steps of the interface program, and apply SQL request.
        """

        self.list_valid_input = []

        print(info_pre_data)

        if request is not None and display_result == 'Yes':
            for row in request:
                print(*row, sep=' : ')
                self.list_valid_input.append(str(row[0]))
            if len(request) == 0:
                print('\n', NO_RECORD)

        elif request is not None and display_result == 'No':
            request

        print(info_post_data)
