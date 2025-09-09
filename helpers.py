# some helper functions and classes

class ModInpText(UIInputText):
    """ input text with nr to have possibility
    to deactivate it
    """
    def __init__(self, nr, **kwargs):
        self.nr=nr
        super().__init__(**kwargs)


