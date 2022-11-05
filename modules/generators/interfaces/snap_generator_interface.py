from abc import ABCMeta, abstractmethod
from typing import Dict, Union


class ISnapGenerator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate_snap(snap_id: str, **options: Dict[str, Union[str, int]]) -> bytes:
        """creates snaps based on the raw snap passed to the instance"""
        ...
