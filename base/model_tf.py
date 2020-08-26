class BaseModelTF:
    """
    TensorFlow base model
    Arg(s):
        config (dict): Configs for model management. Default: None
    """

    def __init__(self, config=None):
        self.config = config
        self.model = None

    def save(self):
        """
        Save the model
        """

    def load(self):
        """
        Load the model
        """

    def build_model(self):
        """
        Build the model
        """
        raise NotImplementedError(
            f'{self.model.__class__.__name__}\'s '
            + '`build_model` is not implemented!'
        )
