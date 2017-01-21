"""
# adapter pattern #
adapter pattern is a 'structural' pattern
"""

class CustomVideoInputJack():
    """ Adaptee class """
    def __init__(self, data):
        self.data = data

    def input(self):
        print("input with: {0}".format(self.data))


class HdmiToCustomInputAdapter():
    """ Adapter class """
    def __init__(self, data):
        data = self._convert_to_custom_input(data) # converted from hdmi to custom
        self.jack = CustomVideoInputJack(data)

    def convert(self):
        self.jack.input()

    def _convert_to_custom_input(self, data):
        return data + " > custom"


if __name__ == '__main__':
    adapter = HdmiToCustomInputAdapter("hdmi")
    adapter.convert()