from openai_client import client, MODEL


class WritingAgent:

    def get_writing_style(self):

        with open(
            "data/email.txt",
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    def generate_email(self, request):

        email_history = self.get_writing_style()

        prompt = f"""
You are Aditi.

Below are previous emails written by Aditi.

{email_history}

Write a new email.

REQUEST:

{request}

Use the same:

- professionalism
- tone
- formatting
- greeting style
- sign-off style
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