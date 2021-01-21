class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls):
    exceptions_list = []
    for i in func_ls:
        msg = 'ok!'
        try:
            i()
        except Exception as e:
            msg = str(e)
        exceptions_list.append(ExceptionProxy(msg, i))
    return exceptions_list
