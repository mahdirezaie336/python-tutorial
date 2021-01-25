class Proxy:

    def __init__(self, obj):
        self.obj = obj
        self.attr_dict = {}
        self.last_invoked = None

    def __getattr__(self, item):
        if item not in dir(self.obj):
            raise Exception('No Such Method')

        if item not in self.attr_dict.keys():
            self.attr_dict[item] = 0
        self.attr_dict[item] += 1
        self.last_invoked = item

        return getattr(self.obj, item)

    def last_invoked_method(self):
        if self.last_invoked is None:
            raise Exception('No Method Is Invoked')
        return self.last_invoked

    def count_of_calls(self, method_name):
        if method_name not in self.attr_dict.keys():
            return 0
        return self.attr_dict[method_name]

    def was_called(self, method_name):
        if method_name not in self.attr_dict.keys():
            return False
        return True


class Radio():
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel
        
    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on

