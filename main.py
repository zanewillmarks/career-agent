import requests

print("===================================")
print(" Internship Hunter AI - Version 1 ")
print("===================================\n")

url = "https://remoteok.com/api"

headers = {
    "User-Agent": "InternshipHunterAI/1.0"
}

try:
    response = requests.get(url, headers=headers, timeout=30)
    jobs = response.json()

    print("Latest Remote Internship / Entry-Level Opportunities:\n")

    count = 0

    for job in jobs:
        if not isinstance(job, dict):
            continue

        title = job.get("position", "")
        company = job.get("company", "")
        tags = job.get("tags", [])

        text = f"{title} {' '.join(tags)}".lower()

        if any(word in text for word in [
            "intern",
            "internship",
            "graduate",
            "junior",
            "entry"
        ]):

            count += 1

            print(f"{count}. {title}")
            print(f"   Company : {company}")
            print(f"   Tags    : {', '.join(tags)}")
            print()

    if count == 0:
        print("No matching internships found today.")

except Exception as e:
    print("Something went wrong:")
    print(e)