from abc import ABCMeta, abstractmethod


class ISnapGenerator(metaclass=ABCMeta):
    """Snap generator interface."""

    @staticmethod
    @abstractmethod
    def generate_snap(snap_id: str, **options: dict[str, str | int]) -> bytes:
        """Creates snaps based on the raw snap passed to the instance.

        :param snap_id: The snap_id to be used for image bytes generation.

        :param options: Optional keyword arguments for advanced image modification.

        :return: Bytes of the generated snapshot.

        :rtype: bytes.
        """
        ...
