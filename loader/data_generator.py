class DataGenerator:
    """
    Generate tensor dataset

    Arg(s):
        input_size (int):
        shift (int):
        label_size (int):
    """

    def __init__(self, input_size, shift, label_size):
        self.input_size = input_size
        self.shift = shift
        self.label_size = label_size

    def make_tf_dataset(self, data, feature_cols, label_cols):
        """
        Build a tensorflow dataset

        Arg(s):
            data (pd.DataFrame): 
            feature_cols (list):
            label_cols (list):
        """
        raise NotImplementedError
