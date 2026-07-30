from models.job import Job


class DedupAgent:

    def deduplicate(self, jobs):

        seen = set()
        unique = []

        for job in jobs:
            key = (
                job.title.lower(),
                job.company.lower()
            )

            if key not in seen:
                seen.add(key)
                unique.append(job)

        return unique