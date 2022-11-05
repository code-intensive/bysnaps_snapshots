from abc import ABCMeta, abstractmethod

from models.snap_datas import SnapData


class ISnapDecoder(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def decode_snap(self) -> SnapData:
        """Decodes snaps based on the snap passed to the instance"""
        ...
