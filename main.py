from agents.orchestrator_agent import OrchestratorAgent
from agents.memory_logger import MemoryLogger

agent = OrchestratorAgent()

print("\n🤖 Personal AI Twin Activated")
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    response = agent.process_query(question)

    print("\nTwin:")
    print(response)
    print()

    # Save every conversation
    MemoryLogger.save_conversation(
        question,
        response
    )