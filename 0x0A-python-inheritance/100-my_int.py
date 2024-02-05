#!/usr/bin/python3
"""My integer module"""


class MyInt(int):
    """class of MyInt that invertes equal and not equal operators"""
    def __eq__(self, integer):
        """inverted equal operator"""
        return super().__ne__(integer)

    def __ne__(self, integer):
        """inverted not equal operator"""
        return super().__eq__(integer)
