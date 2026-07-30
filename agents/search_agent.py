from typing import List

from models.job import Job
from sources.remoteok import RemoteOKSource
from sources.github_jobs import GitHubJobs


class SearchAgent:

    def __init__(self):
        self.sources = [
            RemoteOKSource(),
            GitHubJobs(),
        ]

        self.career_keywords = [
            "intern",
            "internship",
            "graduate",
            "junior",
            "entry",
            "apprentice",
            "trainee",
        ]

        self.tech_keywords = [
            "python",
            "software",
            "developer",
            "engineer",
            "machine learning",
            "artificial intelligence",
            "ai",
            "data",
            "backend",
            "frontend",
            "full stack",
            "sql",
            "aws",
            "docker",
            "tensorflow",
            "pytorch",
            "llm",
        ]

    def search(self) -> List[Job]:

        all_jobs = []

        for source in self.sources:

            jobs = source.search()

            for job in jobs:

                text = (
                    job.title + " " +
                    job.company + " " +
                    job.description
                ).lower()

                has_career_keyword = any(
                    word in text for word in self.career_keywords
                )

                has_tech_keyword = any(
                    word in text for word in self.tech_keywords
                )

                if has_career_keyword or has_tech_keyword:
                    all_jobs.append(job)

        return all_jobs