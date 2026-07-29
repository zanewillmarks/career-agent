from agents.search_agent import SearchAgent


def main():

    agent = SearchAgent()

    jobs = agent.search()

    print(f"\nFound {len(jobs)} job(s)\n")

    for job in jobs:
        print(f"{job.title}")
        print(f"Company: {job.company}")
        print(f"Source: {job.source}")
        print(f"Remote: {job.remote}")
        print("-" * 40)


if __name__ == "__main__":
    main()