from datetime import datetime


class MemoryLogger:

    @staticmethod
    def save_conversation(question, answer):

        with open(
            "data/chat_history.txt",
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"\n\n[{datetime.now()}]\n"
            )

            file.write(
                f"QUESTION:\n{question}\n\n"
            )

            file.write(
                f"ANSWER:\n{answer}\n"
            )