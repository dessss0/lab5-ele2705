
from commands.acceleration import acceleration
from utils.error_handling import not_implemented


def get_command(command_str):

    if command_str == "acceleration":
        return acceleration
   
   
    else:
        return not_implemented(command_str)
    
