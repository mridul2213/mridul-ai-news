from typing import Optional
from ollama import chat
from pydantic import BaseModel


class DigestOutput(BaseModel):
    title: str
    summary: str


PROMPT = """You are an expert AI news analyst specializing in summarizing
technical articles, research papers, and video content about artificial intelligence.

Your role is to create concise, informative digests that help readers quickly
understand the key points and significance of AI-related content.

Guidelines:
- Create a compelling title of 5-10 words
- Write a 2-3 sentence summary
- Highlight the main points and why they matter
- Focus on useful insights and implications
- Use clear and accessible language
- Maintain technical accuracy
- Avoid marketing fluff
"""


class DigestAgent:

    def __init__(self):
        self.model = "llama3.2:3b"
        self.system_prompt = PROMPT

    def generate_digest(
        self,
        title: str,
        content: str,
        article_type: str
    ) -> Optional[DigestOutput]:

        try:
            user_prompt = f"""
Create a digest for this {article_type}.

Title:
{title}

Content:
{content[:8000]}

Return the result in exactly this format:

TITLE: <short title>
SUMMARY: <2-3 sentence summary>
"""

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

            title_result = ""
            summary_result = ""

            for line in result.splitlines():
                if line.startswith("TITLE:"):
                    title_result = line.replace("TITLE:", "", 1).strip()
                elif line.startswith("SUMMARY:"):
                    summary_result = line.replace("SUMMARY:", "", 1).strip()

            if not title_result:
                title_result = title

            if not summary_result:
                summary_result = result.strip()

            return DigestOutput(
                title=title_result,
                summary=summary_result
            )

        except Exception as e:
            print(f"Error generating digest: {e}")
            return None