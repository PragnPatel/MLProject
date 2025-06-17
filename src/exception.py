# Creating custom exception for the entire project.

import sys
import logging


def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = """
    Error occured in 
    Script        : {0}
    Line          : {1}
    Error Message : {2}
    """.format(file_name, exc_tb.tb_lineno, str(error))



    return error_message


class CustomErrorHandling(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)
    
    def __str__(self):
        return self.error_message
    

