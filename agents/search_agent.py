from typing import List

from models.job import Job
from sources.remoteok import search_remoteok


class SearchAgent:

    def search(self) -> List[Job]:

        jobs = []

        print("Searching RemoteOK...")

        jobs.extend(search_remoteok())

        return jobs