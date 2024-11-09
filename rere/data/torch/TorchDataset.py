from rere.data.Data import Data
from torch.utils.data import Dataset


class TorchDataset(Data, Dataset):
    def __len__(self):
        pass

    def __getitem__(self, index):
        pass
