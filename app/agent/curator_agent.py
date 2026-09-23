from typing import List
from ollama import chat
from pydantic import BaseModel, Field


class RankedArticle(BaseModel):
    digest_id: str = Field(description="The ID of the digest")
    relevance_score: float = Field(
        description="Relevance score from 0.0 to 10.0",
        ge=0.0,
        le=10.0
    )
    rank: int = Field(
        description="Rank position, 1 is most relevant",
        ge=1
    )
    reasoning: str = Field(
        description="Brief explanation of why this article is relevant"
    )


class RankedDigestList(BaseModel):
    articles: List[RankedArticle]


CURATOR_PROMPT = """
You are an expert AI news curator.

Your job is to rank AI news articles for a specific user.

Consider:
1. Relevance to the user's interests
2. Technical value
3. Novelty and significance
4. User's expertise level
5. Practical usefulness

For every article:
- Give a relevance score from 0.0 to 10.0
- Give a unique rank
- Give a short reason

IMPORTANT:
Return ONLY valid JSON.

Use exactly this format:

{
  "articles": [
    {
      "digest_id": "article id",
      "relevance_score": 8.5,
      "rank": 1,
      "reasoning": "Short explanation"
    }
  ]
}
"""


class CuratorAgent:
    def __init__(self, user_profile: dict):
        self.model = "llama3.2:3b"
        self.user_profile = user_profile
        self.system_prompt = self._build_system_prompt()

    def _build_system_prompt(self) -> str:
        interests = "\n".join(
            f"- {interest}"
            for interest in self.user_profile["interests"]
        )

        preferences = self.user_profile["preferences"]

        pref_text = "\n".join(
            f"- {key}: {value}"
            for key, value in preferences.items()
        )

        return f"""
{CURATOR_PROMPT}

User Profile:

Name:
{self.user_profile["name"]}

Background:
{self.user_profile["background"]}

Expertise Level:
{self.user_profile["expertise_level"]}

Interests:
{interests}

Preferences:
{pref_text}
"""

    def rank_digests(self, digests: List[dict]) -> List[RankedArticle]:

        if not digests:
            return []

        digest_list = "\n\n".join(
            [
                f"ID: {digest['id']}\n"
                f"Title: {digest['title']}\n"
                f"Summary: {digest['summary']}\n"
                f"Type: {digest['article_type']}"
                for digest in digests
            ]
        )

        user_prompt = f"""
Rank these {len(digests)} AI news articles for the user.

{digest_list}

Return one ranking for every article.
"""

        try:
            response = chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )

            result = response["message"]["content"]

            print("Curator response received.")
            print("Llama ranking response:")
            print(result)

            import json

            data = json.loads(result)

            ranked_articles = [
                RankedArticle(**article)
                for article in data["articles"]
            ]

            ranked_articles.sort(key=lambda x: x.rank)

            return ranked_articles

        except Exception as e:
            print(f"Error ranking digests: {e}")

            return [
                RankedArticle(
                    digest_id=digest["id"],
                    relevance_score=5.0,
                    rank=index,
                    reasoning="Fallback ranking because AI ranking could not be parsed."
                )
                for index, digest in enumerate(digests, start=1)
            ]