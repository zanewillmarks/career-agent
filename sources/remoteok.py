import requests

from models.job import Job
from sources.base import JobSource


class RemoteOKSource(JobSource):

    def search(self):

        print("Connecting to RemoteOK...")

        jobs = []

        try:
            response = requests.get(
                "https://remoteok.com/api",
                headers={
                    "User-Agent": "Career-Agent"
                },
                timeout=15
            )

            response.raise_for_status()

            data = response.json()

            # The first item contains metadata, so skip it
            for item in data[1:]:

                jobs.append(
                    Job(
                        title=item.get("position", "Unknown"),
                        company=item.get("company", "Unknown"),
                        source="RemoteOK",
                        url=item.get("url", ""),
                        remote=True,
                        description=item.get("description", ""),
                        tags=item.get("tags", [])
                    )
                )

        except Exception as e:
            print(f"RemoteOK error: {e}")

        return jobs