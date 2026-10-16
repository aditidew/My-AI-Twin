from agents.memory_agent import MemoryAgent
from openai_client import client, MODEL


class PersonalityAgent:

    def __init__(self):
        self.memory_agent = MemoryAgent()

    def introduce_yourself(self):

        resume = self.memory_agent.get_memory("resume")

        personality = self.memory_agent.get_memory("personality")

        goals = self.memory_agent.get_memory("goals")

        linkedin = self.memory_agent.get_memory("linkedin")

        prompt = f"""
You are Aditi Dewangan.

Below is information about yourself.

RESUME:
{resume}

PERSONALITY:
{personality}

GOALS:
{goals}

LINKEDIN:
{linkedin}

Introduce yourself in first person.

Talk about:
- who you are
- skills
- interests
- goals
- learning journey

Respond naturally.
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