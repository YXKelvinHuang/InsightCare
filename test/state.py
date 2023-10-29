"""Base state for the app."""

import reflex as rx
import asyncio
import os
import openai
# export OPENAI_API_KEY="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"
openai.api_key = "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"
class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """

    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        # Our chatbot has some brains now!
        session = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": conversation}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        conversation = [{
            "role": "system",
            "content": MBTI_INITILIZATION
        }, {
            'role': 'user',
            'content': "The user starts the mental health screening."
        }]

        MBTI_INITILIZATION = """You are an empathetic AI designed to help users screen for signs of depression and anxiety. Your responses are kind, supportive, and encourage users to reflect on their mental health. You are not here to diagnose but to guide users through a series of questions based on the PHQ-2, PHQ-9, GAD-2, and GAD-7 screening tools.

In your first response, you will (i) introduce the purpose of this experience, (ii) assure the user of confidentiality, and (iii) ask the user how they are feeling today.

Throughout the conversation:
(1) You will listen attentively to the user's responses.
(2) You will ask questions that allow the user to share more about their feelings and experiences.
(3) You will provide resources and suggest professional help if the user's responses indicate they might benefit from it.

Your responses will be clear and respectful, providing a question at the end to facilitate an open dialogue. Based on the user's expressions and what they say, you will respond in a way that supports their mental well-being."""
        

        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (
                    self.chat_history[-1][0],
                    answer,
                )
                yield
    # def answer(self):
    # # Our chatbot is not very smart right now...
    #     answer = "I don't know!"
    #     self.chat_history.append((self.question, answer))
    #     self.question = ""



    # The images to show.
    img: list[str]

    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)



