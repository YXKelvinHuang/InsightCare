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

    MBTI_INITILIZATION = """
        You are a AI designed to help users explore aspects of their personality based on the Myers-Briggs Type Indicator (MBTI). Your responses are insightful, encouraging, and guide users to reflect on their personal preferences and behaviors. You are not here to label but to guide users through a series of open-ended questions that resonate with the core principles of MBTI.

        In your first response, you will (i) introduce the purpose of this interaction, (ii) assure the user of confidentiality, and (iii) ask the user an open-ended question about their personal tendencies or preferences.

        Throughout the conversation:
        (1) You will listen attentively to the user's responses.
        (2) You will ask questions that invite users to share more about their personal tendencies, decision-making processes, and how they interact with the world around them.
        (3) You will provide thoughtful insights and suggest resources for further personal exploration if the user's responses indicate they might be interested in it.

        Your responses should be concise and limited to 2 sentences.
        
        Your responses will be clear and respectful, providing a question at the end to facilitate an open dialogue. Based on the user's expressions and what they say, you will respond in a way that supports their personal growth and self-understanding.
        """
        
    question_mapping_zeroed = {
        "You regularly make new friends.": 0,
        "You spend a lot of your free time exploring various random topics that pique your interest": 0,
        "Seeing other people cry can easily make you feel like you want to cry too": 0,
        "You often make a backup plan for a backup plan.": 0,
        "You usually stay calm, even under a lot of pressure": 0,
        "At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know": 0,
        "You prefer to completely finish one project before starting another.": 0,
        "You are very sentimental.": 0,
        "You like to use organizing tools like schedules and lists.": 0,
        "Even a small mistake can cause you to doubt your overall abilities and knowledge.": 0,
        "You feel comfortable just walking up to someone you find interesting and striking up a conversation.": 0,
        "You are not too interested in discussing various interpretations and analyses of creative works.": 0,
        "You are more inclined to follow your head than your heart.": 0,
        "You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.": 0,
        "You rarely worry about whether you make a good impression on people you meet.": 0,
        "You enjoy participating in group activities.": 0,
        "You like books and movies that make you come up with your own interpretation of the ending.": 0,
        "Your happiness comes more from helping others accomplish things than your own accomplishments.": 0,
        "You are interested in so many things that you find it difficult to choose what to try next.": 0,
        "You are prone to worrying that things will take a turn for the worse.": 0,
        "You avoid leadership roles in group settings.": 0,
        "You are definitely not an artistic type of person.": 0,
        "You think the world would be a better place if people relied more on rationality and less on their feelings.": 0,
        "You prefer to do your chores before allowing yourself to relax.": 0,
        "You enjoy watching people argue.": 0,
        "You tend to avoid drawing attention to yourself.": 0,
        "Your mood can change very quickly.": 0,
        "You lose patience with people who are not as efficient as you.": 0,
        "You often end up doing things at the last possible moment.": 0,
        "You have always been fascinated by the question of what, if anything, happens after death.": 0,
        "You usually prefer to be around others rather than on your own.": 0,
        "You become bored or lose interest when the discussion gets highly theoretical.": 0,
        "You find it easy to empathize with a person whose experiences are very different from yours.": 0,
        "You usually postpone finalizing decisions for as long as possible.": 0,
        "You rarely second-guess the choices that you have made.": 0,
        "After a long and exhausting week, a lively social event is just what you need.": 0,
        "You enjoy going to art museums.": 0,
        "You often have a hard time understanding other people’s feelings.": 0,
        "You like to have a to-do list for each day.": 0,
        "You rarely feel insecure.": 0,
        "You avoid making phone calls.": 0,
        "You often spend a lot of time trying to understand views that are very different from your own.": 0,
        "In your social circle, you are often the one who contacts your friends and initiates activities.": 0,
        "If your plans are interrupted, your top priority is to get back on track as soon as possible.": 0,
        "You are still bothered by mistakes that you made a long time ago.": 0,
        "You rarely contemplate the reasons for human existence or the meaning of life.": 0,
        "Your emotions control you more than you control them.": 0,
        "You take great care not to make people look bad, even when it is completely their fault.": 0,
        "Your personal work style is closer to spontaneous bursts of energy than organized and consistent efforts.": 0,
        "When someone thinks highly of you, you wonder how long it will take them to feel disappointed in you.": 0,
        "You would love a job that requires you to work alone most of the time.": 0,
        "You believe that pondering abstract philosophical questions is a waste of time.": 0,
        "You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.": 0,
        "You know at first glance how someone is feeling.": 0,
        "You often feel overwhelmed.": 0,
        "You complete things methodically without skipping over any steps.": 0,
        "You are very intrigued by things labeled as controversial.": 0,
        "You would pass along a good opportunity if you thought someone else needed it more.": 0,
        "You struggle with deadlines.": 0,
        "You feel confident that things will work out for you.": 0,
    }
    
    def answer(self):
        conversation = [{
            "role": "system",
            "content": self.MBTI_INITILIZATION
        }]
        message  = [{"role": "user", "content": self.question}]

        session = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation if not self.chat_history else message,
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Our chatbot has some brains now!
        answer = ""
        self.chat_history.append((self.question, answer))

        select_questions = f"""
            Based on the following response /"{answer}/" to the question /"{self.question}/",
            select the top 5 most relevant questions whose response can be inferred from this list:
            {self.question_mapping_zeroed.keys()}
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": select_questions}],
        )

        print(response)

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