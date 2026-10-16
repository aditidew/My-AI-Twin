import os


class MemoryAgent:

    def __init__(self):

        self.memory_path = "data"

        self.memory_files = {
            "resume": "resume.txt",
            "projects": "projects.txt",
            "personality": "personality.txt",
            "goals": "goals.txt",
            "learning": "learning.txt",
            "linkedin": "linkedin.txt"
        }

    def get_memory(self, memory_type):

        try:

            if memory_type not in self.memory_files:
                return "Memory type not found."

            file_name = self.memory_files[memory_type]

            full_path = os.path.join(
                self.memory_path,
                file_name
            )

            with open(
                full_path,
                "r",
                encoding="utf-8"
            ) as file:

                return file.read()

        except Exception as e:
            return str(e)
