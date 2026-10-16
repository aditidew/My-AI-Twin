from agents.memory_agent import MemoryAgent
from agents.personality_agent import PersonalityAgent
from agents.decision_agent import DecisionAgent
from agents.writing_agent import WritingAgent


class OrchestratorAgent:

    def __init__(self):

        self.memory_agent = MemoryAgent()

        self.personality_agent = PersonalityAgent()

        self.decision_agent = DecisionAgent()

        self.writing_agent = WritingAgent()

    def process_query(self, query):

        query_lower = query.lower()

        if "who are you" in query_lower:

            return self.personality_agent.introduce_yourself()

        elif "email" in query_lower:

            return self.writing_agent.generate_email(
                query
            )

        elif (
            "learn" in query_lower
            or "career" in query_lower
            or "project" in query_lower
        ):

            return self.decision_agent.answer(
                query
            )

        elif "resume" in query_lower:

            return self.memory_agent.get_memory(
                "resume"
            )

        else:

            return self.decision_agent.answer(
                query
            )