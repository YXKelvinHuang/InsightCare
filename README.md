# MBTIFY
A web application that leverages advanced Natural Language Processing and Machine Learning technologies to administer streamlined and adaptive MBTI personality tests through fewer than 10 short-answer questions.

## Inspiration
Frustrated by the traditional MBTI's barrage of questions? So were we. Introducing MBTIFY: our web application streamlines your MBTI assessment using advanced Natural Language Processing and Machine Learning. Forget the indecision of Likert scales; MBTIFY's conversational AI prompts you with tailored, open-ended questions. Answer naturally—the AI adapts, selecting queries to pinpoint your personality type with ease. Welcome to a smarter, streamlined path to self-discovery.

## What it does
MBTIFY is a web application designed to administer MBTI personality tests in a more efficient and streamlined manner. Unlike traditional MBTI tests that require answering hundreds of questions, MBTIFY aims to achieve accurate results with fewer than 10 short-answer questions. Users can respond to these questions via text or audio input. The application leverages Natural Language Processing (NLP) and Machine Learning (ML) technologies to analyze the answers and determine the user's MBTI type.

## How we built it
Frontend: Reflex for a user-friendly interface.

Voice Recognition: Converts spoken answers to text.

NLP: Cohere and OpenAI analyze responses for emotional and syntactic insights.

ML: Intersystems IntegratedML utilizes 60,000+ Kaggle MBTI questionnaire responses to train a predictive AutoML model. This model interprets Likert scale responses, determining MBTI type with a confidence level. Immediate results are provided if a confidence threshold is met, or the system dynamically selects further clarifying questions.


## Challenges we ran into
Reflex on M1 Macs: Faced compatibility issues with the Reflex UI framework on M1 chipset Macs, requiring optimization for cross-platform functionality.

SQLAlchemy with sqlalchemy-iris: Experienced limitations in integrating SQLAlchemy with the sqlalchemy-iris dialect, leading to custom code solutions for effective database operations.

IRIS Cloud Connectivity: Encountered difficulties in connecting to the IRIS cloud server, necessitating adjustments in network and security settings for reliable deployment.

Model Training Time: The machine learning model training took over 6 hours due to the large dataset and complex algorithms, prompting a need for pipeline optimization to enhance efficiency.

## Accomplishments that we're proud of
Responsive Design: Developed with Reflex for an adaptive user experience.

Real-Time ML Analysis: Intersystems algorithms provide instant MBTI prediction with a confidence indicator using SQL. We infer Likert scores from user responses to our conversational prompts using LLM, then input these as features into our predictive model, thereby combining discriminative with generative AI models.

Smart Questioning: A dynamic question bank evolves based on user inputs, distinguishing similar MBTI profiles through adaptive questioning and iterative model refinements with updated scores.

## What we learned
Stay on Track: Consistently ensure that you are on the right path by periodically reviewing your goals and progress.

Purposeful Implementation: Before committing to a new feature or task, evaluate its significance to avoid exerting effort on non-impactful activities.

## What's next for MBTIFY
Audio Transcribing: Our roadmap includes the implementation of an advanced audio transcribing feature. This will allow us to extend our voice recognition capabilities to capture even more nuanced responses from users, further refining our MBTI analysis.

Emotion Detection with HumeAI: We plan to integrate HumeAI technology for real-time emotion detection based on the user's voice. This will add an additional layer of depth to the analysis, enabling us to distinguish between closely matched MBTI types with a greater degree of accuracy.

Optimized Machine Learning Algorithms: We aim to continually fine-tune our existing machine learning models within Intersystem to accommodate these new features, ensuring that our confidence levels and MBTI type predictions are as accurate as possible.

Dynamic Questioning 2.0: Building on our adaptive questioning framework, we will incorporate feedback loops that consider not only the content of the user’s responses but also the detected emotional tone. This will make our question selection even more responsive and targeted.
