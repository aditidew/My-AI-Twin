from agents.memory_agent import MemoryAgent
from openai_client import client, MODEL


class DecisionAgent:

    def __init__(self):
        self.memory_agent = MemoryAgent()

    def answer(self, question):

        goals = self.memory_agent.get_memory("goals")

        learning = self.memory_agent.get_memory("learning")

        personality = self.memory_agent.get_memory("personality")

        projects = self.memory_agent.get_memory("projects")

        prompt = f"""
You are Aditi Dewangan.

Below is information about Aditi.

GOALS:
{goals}

LEARNING HISTORY:
{learning}

PERSONALITY:
{personality}

PROJECTS:
{projects}

Answer the following question exactly
the way Aditi would answer.

Question:
{question}
"""

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content