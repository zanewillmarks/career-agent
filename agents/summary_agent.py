from typing import List
from models.job import Job


class SummaryAgent:

    def summarize(self, jobs: List[Job]) -> List[Job]:

        for job in jobs:

            summary = []

            if job.internship:
                summary.append("internship")

            if job.graduate:
                summary.append("graduate program")

            if job.remote:
                summary.append("remote")

            if job.training:
                summary.append("training")

            if job.mentorship:
                summary.append("mentorship")

            if "python" in job.reason.lower():
                summary.append("Python")

            if "artificial intelligence" in job.reason.lower():
                summary.append("AI")

            if len(summary) == 0:
                job.ai_summary = "General career opportunity."
            else:
                job.ai_summary = (
                    "This opportunity offers "
                    + ", ".join(summary)
                    + "."
                )

        return jobs