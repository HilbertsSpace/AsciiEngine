from utils.exceptions import ValidationError

class AsciiObject(object):
    def __init__(self, raw_user_input):
        self.validate_user_input_is_func(raw_user_input)
        self.raw_user_input = raw_user_input

    def validate_user_input_is_func(self, raw_user_input):
        """todo"""
        if raw_user_input[:5] != "func(" or raw_user_input[-1] != ")":
            raise ValidationError("User input needs to be a func")
