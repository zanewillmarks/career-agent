from dataclasses import dataclass, field
from typing import List


@dataclass
class Job:
    title: str
    company: str
    source: str
    url: str

    location: str = "Unknown"

    remote: bool = False
    paid: bool = False

    internship: bool = False
    graduate: bool = False
    apprenticeship: bool = False
    fellowship: bool = False

    training: bool = False
    mentorship: bool = False
    international: bool = False

    description: str = ""

    tags: List[str] = field(default_factory=list)

    score: float = 0.0
    reason: str = ""
    training_score: int = 0
    career_score: int = 0
    ai_summary: str = ""