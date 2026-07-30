import re


POSITIVE_KEYWORDS = {
    "python": ("Python", 15),
    "machine learning": ("Machine Learning", 20),
    "artificial intelligence": ("Artificial Intelligence", 20),
    "deep learning": ("Deep Learning", 15),
    "llm": ("LLM", 20),
    "openai": ("OpenAI", 20),
    "tensorflow": ("TensorFlow", 15),
    "pytorch": ("PyTorch", 15),
    "data science": ("Data Science", 18),
    "data engineer": ("Data Engineering", 15),
    "software engineer": ("Software Engineering", 15),
    "software developer": ("Software Development", 15),
    "backend": ("Backend Development", 10),
    "frontend": ("Frontend Development", 10),
    "full stack": ("Full Stack Development", 12),
    "sql": ("SQL", 10),
    "aws": ("AWS", 10),
    "azure": ("Azure", 10),
    "gcp": ("Google Cloud", 10),
    "docker": ("Docker", 8),
    "kubernetes": ("Kubernetes", 12),
    "linux": ("Linux", 8),
    "git": ("Git", 5),
    "java": ("Java", 10),
    "javascript": ("JavaScript", 10),
    "typescript": ("TypeScript", 10),
    "react": ("React", 12),
    "node.js": ("Node.js", 10),
    "node": ("Node.js", 10),
    "golang": ("Go", 10),
    "go": ("Go", 10),
    "c++": ("C++", 12),
    "c#": ("C#", 12),
    ".net": (".NET", 10),
    "pandas": ("Pandas", 10),
    "numpy": ("NumPy", 10),
    "scikit": ("Scikit-Learn", 12),
    "nlp": ("Natural Language Processing", 15),
    "computer vision": ("Computer Vision", 15),
    "generative ai": ("Generative AI", 20),
    "rag": ("Retrieval-Augmented Generation", 20),
    "langchain": ("LangChain", 20),
}


NEGATIVE_KEYWORDS = {
    "sales": -30,
    "marketing": -30,
    "cashier": -60,
    "chef": -50,
    "nurse": -50,
    "accounting": -35,
    "recruiter": -25,
    "human resources": -30,
    "warehouse": -40,
    "driver": -40,
}


EXACT_MATCH = {
    "ai",
    "go",
    "git",
    "sql",
    "aws",
    "gcp",
}


SENIOR_KEYWORDS = {
    "senior": -20,
    "staff": -25,
    "lead": -20,
    "principal": -30,
    "architect": -20,
    "manager": -15,
    "director": -35,
    "vp": -40,
    "head": -30,
}


class RankingAgent:

    def rank(self, jobs):

        for job in jobs:

            score = 0
            reasons = []
            tech_matches = []

            text = (
                f"{job.title} "
                f"{job.company} "
                f"{job.description}"
            ).lower()

            # ---------------------------------
            # Career Level Bonuses
            # ---------------------------------

            if re.search(r"\bintern(ship)?\b", text):
                score += 40
                reasons.append("Internship")

            if re.search(r"\bgraduate\b|\bnew grad\b", text):
                score += 30
                reasons.append("Graduate Program")

            if re.search(r"\bjunior\b", text):
                score += 25
                reasons.append("Junior Position")

            if re.search(r"\bentry[- ]?level\b", text):
                score += 20
                reasons.append("Entry Level")

            if re.search(r"\bapprentice(ship)?\b", text):
                score += 35
                reasons.append("Apprenticeship")

            if re.search(r"\btrainee(ship)?\b", text):
                score += 25
                reasons.append("Trainee")

            # ---------------------------------
            # Penalize Senior Roles
            # ---------------------------------

            for keyword, penalty in SENIOR_KEYWORDS.items():

                if re.search(rf"\b{re.escape(keyword)}\b", text):
                    score += penalty

            # ---------------------------------
            # Technical Skills
            # ---------------------------------

            for keyword, (display_name, value) in POSITIVE_KEYWORDS.items():

                if keyword in EXACT_MATCH:

                    found = re.search(
                        rf"\b{re.escape(keyword)}\b",
                        text,
                    )

                else:

                    found = keyword in text

                if found:

                    score += value

                    if display_name not in tech_matches:
                        tech_matches.append(display_name)

                    if display_name not in reasons:
                        reasons.append(display_name)

            # Standalone AI abbreviation

            if (
                re.search(r"\bai\b", text)
                and "Artificial Intelligence" not in tech_matches
            ):

                score += 15

                tech_matches.append(
                    "Artificial Intelligence"
                )

                reasons.append(
                    "Artificial Intelligence"
                )

            # ---------------------------------
            # Negative Keywords
            # ---------------------------------

            for keyword, penalty in NEGATIVE_KEYWORDS.items():

                if keyword in text:
                    score += penalty

            # ---------------------------------
            # Reward Skill Density
            # ---------------------------------

            if len(tech_matches) >= 8:
                score += 15
            elif len(tech_matches) >= 5:
                score += 10

            # ---------------------------------
            # Prevent Non-Tech Jobs
            # ---------------------------------

            if len(tech_matches) == 0:
                score = min(score, 40)

            # ---------------------------------
            # Remote Bonus
            # ---------------------------------

            if job.remote:

                score += 10

                if "Remote" not in reasons:
                    reasons.append("Remote")

            # ---------------------------------
            # Clamp Score
            # ---------------------------------

            score = max(0, min(score, 100))

            job.score = score

            job.reason = (
                ", ".join(reasons)
                if reasons
                else "No strong indicators"
            )

            # ---------------------------------
            # AI Summary
            # ---------------------------------

            summary = []

            career_items = [
                "Internship",
                "Graduate Program",
                "Junior Position",
                "Entry Level",
                "Apprenticeship",
                "Trainee",
            ]

            for item in career_items:

                if item in reasons:
                    summary.append(item.lower())

            if tech_matches:

                summary.append(
                    "technical skills including "
                    + ", ".join(tech_matches)
                )

            if job.remote:
                summary.append("remote work")

            if summary:

                job.ai_summary = (
                    "Strong match because it includes "
                    + ", ".join(summary)
                    + "."
                )

            else:

                job.ai_summary = (
                    "General career opportunity."
                )

        jobs.sort(
            key=lambda job: (
                job.score,
                len(job.reason.split(", "))
            ),
            reverse=True,
        )

        return jobs