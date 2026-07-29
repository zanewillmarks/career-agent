from models.job import Job


def search_remoteok():
    """
    Temporary placeholder.
    Later this will scrape RemoteOK.
    """

    jobs = [
        Job(
            title="Python AI Intern",
            company="Remote Company",
            source="RemoteOK",
            url="https://remoteok.com",
            remote=True,
            internship=True,
            training=True,
        )
    ]

    return jobs