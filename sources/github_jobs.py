from models.job import Job


class GitHubJobs:

    def search(self):

        print("Connecting to GitHub Jobs...")

        jobs = []

        jobs.append(
            Job(
                title="Open Source AI Internship",
                company="GitHub",
                source="GitHub",
                url="https://github.com",
                remote=True,
                internship=True,
                training=True,
                description="AI internship contributing to open source."
            )
        )

        jobs.append(
            Job(
                title="Machine Learning Fellow",
                company="GitHub",
                source="GitHub",
                url="https://github.com",
                remote=True,
                fellowship=True,
                description="Machine learning fellowship."
            )
        )

        return jobs