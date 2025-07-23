import tensorflow as tf

from ..dataProvider import DataProvider as dataProvider

class DataProvider(dataProvider, tf.keras.utils.Sequence):
    def __init__(self, *args, **kwargs):
        self.workers = kwargs.get("workers", 1)
        self.use_multiprocessing = kwargs.get("use_multiprocessing", False)
        self.max_queue_size = kwargs.get("max_queue_size", 10)
        super().__init__(*args, **kwargs)
