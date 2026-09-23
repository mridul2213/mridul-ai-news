from datetime import datetime
from typing import List, Optional

from ollama import chat
from pydantic import BaseModel, Field


class EmailIntroduction(BaseModel):
    greeting: str
    introduction: str


class RankedArticleDetail(BaseModel):
    digest_id: str
    rank: int
    relevance_score: float
    title: str
    summary: str
    url: str
    article_type: str
    reasoning: Optional[str] = None


class EmailDigestResponse(BaseModel):
    introduction: EmailIntroduction
    articles: List[RankedArticleDetail]
    total_ranked: int
    top_n: int

    def to_markdown(self) -> str:
        md = f"{self.introduction.greeting}\n\n"
        md += f"{self.introduction.introduction}\n\n---\n\n"

        for article in self.articles:
            md += f"## {article.title}\n\n"
            md += f"{article.summary}\n\n"
            md += f"Read more: {article.url}\n\n---\n\n"

        return md


EMAIL_PROMPT = """
You write friendly AI news email introductions.

Return ONLY:

GREETING: ...
INTRODUCTION: ...
"""


class EmailAgent:

    def __init__(self, user_profile: dict):
        self.model = "llama3.2:3b"
        self.user_profile = user_profile

    def generate_introduction(self, ranked_articles: List):

        name = self.user_profile["name"]
        current_date = datetime.now().strftime("%B %d, %Y")

        if not ranked_articles:
            return EmailIntroduction(
                greeting=f"Hey {name}, here is your AI news digest for {current_date}.",
                introduction="No articles were available today."
            )

        titles = []

        for idx, article in enumerate(ranked_articles[:10]):
            if isinstance(article, dict):
                title = article.get("title", "Untitled")
            else:
                title = article.title

            titles.append(f"{idx+1}. {title}")

        article_list = "\n".join(titles)

        prompt = f"""
Create an introduction.

Name: {name}
Date: {current_date}

Articles:
{article_list}
"""

        try:
            response = chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": EMAIL_PROMPT},
                    {"role": "user", "content": prompt}
                ]
            )

            text = response["message"]["content"]

            greeting = ""
            intro = ""

            for line in text.splitlines():
                if line.startswith("GREETING:"):
                    greeting = line.replace("GREETING:", "").strip()

                if line.startswith("INTRODUCTION:"):
                    intro = line.replace("INTRODUCTION:", "").strip()

            if greeting == "":
                greeting = f"Hey {name}, here is your AI news digest for {current_date}."

            if intro == "":
                intro = "Here are today's AI news articles ranked for you."

            return EmailIntroduction(
                greeting=greeting,
                introduction=intro
            )

        except Exception:
            return EmailIntroduction(
                greeting=f"Hey {name}, here is your AI news digest for {current_date}.",
                introduction="Here are today's AI news articles ranked for you."
            )

    def create_email_digest_response(
        self,
        ranked_articles: List[RankedArticleDetail],
        total_ranked: int,
        limit: int = 10
    ) -> EmailDigestResponse:

        top_articles = ranked_articles[:limit]

        return EmailDigestResponse(
            introduction=self.generate_introduction(top_articles),
            articles=top_articles,
            total_ranked=total_ranked,
            top_n=limit
        )