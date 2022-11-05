from abc import ABCMeta, abstractmethod


class ISnapGenerator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate_snap(snap_id: str, **options) -> bytes:
        """creates snaps based on the raw snap passed to the instance"""
        ...
