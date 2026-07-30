from agents.search_agent import SearchAgent
from agents.ranking_agent import RankingAgent
from agents.summary_agent import SummaryAgent
from agents.dedup_agent import DedupAgent
from agents.export_agent import ExportAgent


def main():

    # Search jobs
    search = SearchAgent()
    jobs = search.search()

    # Remove duplicates
    dedup = DedupAgent()
    jobs = dedup.deduplicate(jobs)

    # Rank jobs
    ranking = RankingAgent()
    jobs = ranking.rank(jobs)

    # Create summaries
    summary = SummaryAgent()
    jobs = summary.summarize(jobs)

    # Export results
    exporter = ExportAgent()
    exporter.export(jobs)

    print(f"\nFound {len(jobs)} job(s)\n")

    for job in jobs:
        print(f"⭐ Score: {job.score}/100")
        print(f"Reason: {job.reason}")
        print(f"Summary: {job.ai_summary}")
        print(f"Title: {job.title}")
        print(f"Company: {job.company}")
        print(f"Source: {job.source}")
        print(f"Remote: {job.remote}")
        print(f"URL: {job.url}")
        print("-" * 40)


if __name__ == "__main__":
    main()