from abc import ABC, abstractmethod
from typing import List

from models.job import Job


class JobSource(ABC):

    @abstractmethod
    def search(self) -> List[Job]:
        """Return a list of Job objects."""
        pass