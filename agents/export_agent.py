import pandas as pd

from typing import List
from models.job import Job


class ExportAgent:

    def export(self, jobs: List[Job]):

        data = []

        for job in jobs:
            data.append({
                "Score": job.score,
                "Title": job.title,
                "Company": job.company,
                "Reason": job.reason,
                "Summary": job.ai_summary,
                "Source": job.source,
                "Remote": job.remote,
                "Location": job.location,
                "URL": job.url
            })

        df = pd.DataFrame(data)

        df.to_csv("output/jobs.csv", index=False)

        print("\n✅ Jobs exported to output/jobs.csv")