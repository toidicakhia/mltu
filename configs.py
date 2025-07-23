import os
from datetime import datetime

from mltu.configs import BaseModelConfigs


class ModelConfigs(BaseModelConfigs):
    def __init__(self):
        super().__init__()
        self.model_path = os.path.join("Models/captcha")
        self.vocab = ""
        self.height = 128
        self.width = 128
        self.max_text_length = 0
        self.batch_size = 64
        self.learning_rate = 1e-3
        self.train_epochs = 20
        self.train_workers = 20