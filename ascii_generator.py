from utils.exceptions import ValidationError

class AsciiObject(object):
    def __init__(self, func, rotation_axis, x_bound, y_bound, step_size):
        self.validate_user_func(func)
        self.raw_user_func = func

        self.rotation_axis = rotation_axis
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.step_size = step_size

    def validate_user_func(self, raw_user_input):
        """todo"""
        if raw_user_input[:5] != "func(" or raw_user_input[-1] != ")":
            raise ValidationError("User input needs to be a func")
