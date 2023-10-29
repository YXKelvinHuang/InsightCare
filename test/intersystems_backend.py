# Required libraries
from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine, text, DateTime, insert, MetaData, Table, Column, Integer, PrimaryKeyConstraint, \
    String
import ssl

from sqlalchemy.exc import SQLAlchemyError

# Configure TLS
# PEM file contents as a string
pem_file_contents = """
-----BEGIN CERTIFICATE-----
MIIEqTCCA5GgAwIBAgIUB2JSTkrUmcf2RaXfb5fgT9oAaQMwDQYJKoZIhvcNAQEL
BQAwgZkxCzAJBgNVBAYTAlVTMRYwFAYDVQQIDA1NYXNzYWNodXNldHRzMQswCQYD
VQQHDAJVUzEhMB8GA1UECgwYSW50ZXJzeXN0ZW1zIENvcnBvcmF0aW9uMQ8wDQYD
VQQLDAZTUUxhYVMxMTAvBgNVBAMMKGE5MjBmY2RmMGY0MTAxMDNhY2JiMDEyNjBl
ZGFjNDYzYy1kYXRhLTAwHhcNMjMxMDI4MDE1NTA4WhcNMjQxMDI3MDE1NTA4WjCB
mTELMAkGA1UEBhMCVVMxFjAUBgNVBAgMDU1hc3NhY2h1c2V0dHMxCzAJBgNVBAcM
AlVTMSEwHwYDVQQKDBhJbnRlcnN5c3RlbXMgQ29ycG9yYXRpb24xDzANBgNVBAsM
BlNRTGFhUzExMC8GA1UEAwwoYTkyMGZjZGYwZjQxMDEwM2FjYmIwMTI2MGVkYWM0
NjNjLWRhdGEtMDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKzwBjDQ
FrSBTcLCRcQ1TjIV6fQxq6o9wGh3Oe+NfjVtRuW28ghE7oWL0fiXqvyjDruNY/cH
uREi20qubBH2fIV8RGW3Jrbo9dQEfn4pR9oCOFLBMfW1rETEbQLD3lyvvt3ya1jQ
fB8luK/X7fQhHNUsfufBvPUfuwshMY9u71JW22aB7uEkY3DmPyPyKikCKGmdm6bc
QV9rBSYXNA0c2dGYChB/idQ4n5t8jDKNHxyJmar/WJEvE2M/8N3LZeU/qYsIz9ng
0EEVB307WI6DEd8PWT+hGe3oBZmgNVGu96MiNVIy8774oksAFHysUwIbr13R63Ns
4Njvub03Oiuv9j0CAwEAAaOB5jCB4zAdBgNVHQ4EFgQUJWp1bhUY/OcMri/wYQoV
Ds7owcQwHwYDVR0jBBgwFoAUJWp1bhUY/OcMri/wYQoVDs7owcQwDwYDVR0TAQH/
BAUwAwEB/zCBjwYDVR0RBIGHMIGEgihhOTIwZmNkZjBmNDEwMTAzYWNiYjAxMjYw
ZWRhYzQ2M2MtZGF0YS0wgglsb2NhbGhvc3SCTWs4cy1iMmU2Nzc0Yi1hZTY1MTk2
NC1lYTdmMTc5MzZjLTE2OTdkMDAwNWJmYWI3ODIuZWxiLnVzLWVhc3QtMS5hbWF6
b25hd3MuY29tMA0GCSqGSIb3DQEBCwUAA4IBAQCUhi9rCSjhF5TsmgbUHngkr6em
Zgaaf4IeNnxVtJhr8ZKv8n0po7xls7/3clAN4iNuZVe9Cz99L7oOxpE6LNSp5HKr
TyBZ8zZ2o7CFvTidCOIJqyMUFhDYDi1852dZ/kpkK4pRdrKmGCjFsuFjGG95hLKA
uIm/0BuLlpzwGh7pXT28K1L4wpvHoHKJHP79pO/beZGPqtuRFJqaVxdLz0XF4Lam
WtjGNNUtE885dmYPrBuIfg/LCEr9Y1vYUzHt+yN03VmdPZ9xXyApkFVTlaEyORCx
2/Q/zfODYF7uqEI2/WyWy/YUpCUoecHm9k250VSC4dvSqGbAvdkAqWnJSsr2
-----END CERTIFICATE-----
"""

question_mapping = {
    "You regularly make new friends.": "MakeNewFriends",
    "You spend a lot of your free time exploring various random topics that pique your interest": "ExploreTopics",
    "Seeing other people cry can easily make you feel like you want to cry too": "EmpathyCry",
    "You often make a backup plan for a backup plan.": "BackupPlans",
    "You usually stay calm, even under a lot of pressure": "CalmUnderPressure",
    "At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know": "SocialIntroversion",
    "You prefer to completely finish one project before starting another.": "SingleTasking",
    "You are very sentimental.": "Sentimental",
    "You like to use organizing tools like schedules and lists.": "OrganizeTools",
    "Even a small mistake can cause you to doubt your overall abilities and knowledge.": "DoubtByMistake",
    "You feel comfortable just walking up to someone you find interesting and striking up a conversation.": "ConfidentApproach",
    "You are not too interested in discussing various interpretations and analyses of creative works.": "DislikeInterpretation",
    "You are more inclined to follow your head than your heart.": "HeadOverHeart",
    "You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.": "Spontaneous",
    "You rarely worry about whether you make a good impression on people you meet.": "UnworriedImpression",
    "You enjoy participating in group activities.": "EnjoyGroupActivities",
    "You like books and movies that make you come up with your own interpretation of the ending.": "InterpretiveEndings",
    "Your happiness comes more from helping others accomplish things than your own accomplishments.": "HappinessInHelping",
    "You are interested in so many things that you find it difficult to choose what to try next.": "VariedInterests",
    "You are prone to worrying that things will take a turn for the worse.": "WorryWorse",
    "You avoid leadership roles in group settings.": "AvoidLeadership",
    "You are definitely not an artistic type of person.": "NotArtistic",
    "You think the world would be a better place if people relied more on rationality and less on their feelings.": "RationalityOverFeelings",
    "You prefer to do your chores before allowing yourself to relax.": "ChoresFirst",
    "You enjoy watching people argue.": "EnjoyArguments",
    "You tend to avoid drawing attention to yourself.": "AvoidAttention",
    "Your mood can change very quickly.": "MoodSwings",
    "You lose patience with people who are not as efficient as you.": "ImpatientWithInefficiency",
    "You often end up doing things at the last possible moment.": "Procrastinate",
    "You have always been fascinated by the question of what, if anything, happens after death.": "AfterlifeCuriosity",
    "You usually prefer to be around others rather than on your own.": "PrefersCompany",
    "You become bored or lose interest when the discussion gets highly theoretical.": "BoredByTheory",
    "You find it easy to empathize with a person whose experiences are very different from yours.": "EasyEmpathy",
    "You usually postpone finalizing decisions for as long as possible.": "DelayDecisions",
    "You rarely second-guess the choices that you have made.": "ConfidentChoices",
    "After a long and exhausting week, a lively social event is just what you need.": "RechargeSocially",
    "You enjoy going to art museums.": "EnjoyArtMuseums",
    "You often have a hard time understanding other people’s feelings.": "HardToUnderstandFeelings",
    "You like to have a to-do list for each day.": "DailyToDoList",
    "You rarely feel insecure.": "SeldomInsecure",
    "You avoid making phone calls.": "AvoidPhoneCalls",
    "You often spend a lot of time trying to understand views that are very different from your own.": "UnderstandDifferentViews",
    "In your social circle, you are often the one who contacts your friends and initiates activities.": "InitiateSocialContact",
    "If your plans are interrupted, your top priority is to get back on track as soon as possible.": "PlanRecovery",
    "You are still bothered by mistakes that you made a long time ago.": "BotheredByOldMistakes",
    "You rarely contemplate the reasons for human existence or the meaning of life.": "RarelyContemplateExistence",
    "Your emotions control you more than you control them.": "EmotionsControl",
    "You take great care not to make people look bad, even when it is completely their fault.": "ProtectOthersImage",
    "Your personal work style is closer to spontaneous bursts of energy than organized and consistent efforts.": "SpontaneousWorkStyle",
    "When someone thinks highly of you, you wonder how long it will take them to feel disappointed in you.": "FearDisappointment",
    "You would love a job that requires you to work alone most of the time.": "PrefersSoloWork",
    "You believe that pondering abstract philosophical questions is a waste of time.": "Pragmatic",
    "You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.": "PrefersBusyPlaces",
    "You know at first glance how someone is feeling.": "IntuitiveAboutFeelings",
    "You often feel overwhelmed.": "OftenOverwhelmed",
    "You complete things methodically without skipping over any steps.": "Methodical",
    "You are very intrigued by things labeled as controversial.": "IntriguedByControversy",
    "You would pass along a good opportunity if you thought someone else needed it more.": "AltruisticOpportunities",
    "You struggle with deadlines.": "StruggleWithDeadlines",
    "You feel confident that things will work out for you.": "ConfidentOutlook",
    "Personality": "Personality"  # This seems to be the topic or category header, not a question.
}

mbti_mapping = {
    "ISTJ": 0, "ISFJ": 1, "INFJ": 2, "INTJ": 3,
    "ISTP": 4, "ISFP": 5, "INFP": 6, "INTP": 7,
    "ESTP": 8, "ESFP": 9, "ENFP": 10, "ENTP": 11,
    "ESTJ": 12, "ESFJ": 13, "ENFJ": 14, "ENTJ": 15
}

metadata = MetaData()

mbti = Table(
    'mbti', metadata,
    Column('id', Integer, primary_key=True),
    Column('timestamp', DateTime),
    Column('age', Integer),
    Column('MakeNewFriends', Integer),
    Column('ExploreTopics', Integer),
    Column('EmpathyCry', Integer),
    Column('BackupPlans', Integer),
    Column('CalmUnderPressure', Integer),
    Column('SocialIntroversion', Integer),
    Column('SingleTasking', Integer),
    Column('Sentimental', Integer),
    Column('OrganizeTools', Integer),
    Column('DoubtByMistake', Integer),
    Column('ConfidentApproach', Integer),
    Column('DislikeInterpretation', Integer),
    Column('HeadOverHeart', Integer),
    Column('Spontaneous', Integer),
    Column('UnworriedImpression', Integer),
    Column('EnjoyGroupActivities', Integer),
    Column('InterpretiveEndings', Integer),
    Column('HappinessInHelping', Integer),
    Column('VariedInterests', Integer),
    Column('WorryWorse', Integer),
    Column('AvoidLeadership', Integer),
    Column('NotArtistic', Integer),
    Column('RationalityOverFeelings', Integer),
    Column('ChoresFirst', Integer),
    Column('EnjoyArguments', Integer),
    Column('AvoidAttention', Integer),
    Column('MoodSwings', Integer),
    Column('ImpatientWithInefficiency', Integer),
    Column('Procrastinate', Integer),
    Column('AfterlifeCuriosity', Integer),
    Column('PrefersCompany', Integer),
    Column('BoredByTheory', Integer),
    Column('EasyEmpathy', Integer),
    Column('DelayDecisions', Integer),
    Column('ConfidentChoices', Integer),
    Column('RechargeSocially', Integer),
    Column('EnjoyArtMuseums', Integer),
    Column('HardToUnderstandFeelings', Integer),
    Column('DailyToDoList', Integer),
    Column('SeldomInsecure', Integer),
    Column('AvoidPhoneCalls', Integer),
    Column('UnderstandDifferentViews', Integer),
    Column('InitiateSocialContact', Integer),
    Column('PlanRecovery', Integer),
    Column('BotheredByOldMistakes', Integer),
    Column('RarelyContemplateExistence', Integer),
    Column('EmotionsControl', Integer),
    Column('ProtectOthersImage', Integer),
    Column('SpontaneousWorkStyle', Integer),
    Column('FearDisappointment', Integer),
    Column('PrefersSoloWork', Integer),
    Column('Pragmatic', Integer),
    Column('PrefersBusyPlaces', Integer),
    Column('IntuitiveAboutFeelings', Integer),
    Column('OftenOverwhelmed', Integer),
    Column('Methodical', Integer),
    Column('IntriguedByControversy', Integer),
    Column('AltruisticOpportunities', Integer),
    Column('StruggleWithDeadlines', Integer),
    Column('ConfidentOutlook', Integer),
    Column('Personality', Integer),
    PrimaryKeyConstraint('id', name='mbti_pk')
)


def clean_dataset(file_path):
    # Try reading with utf-8 encoding
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        # If there's a UnicodeDecodeError, try 'cp1252' encoding
        df = pd.read_csv(file_path, encoding='cp1252')

    # Convert column names using the provided mapping
    df.rename(columns=question_mapping, inplace=True)

    # Convert the 'Personality' column to string to ensure .str operations work
    df['Personality'] = df['Personality'].astype(str)

    # Drop rows where 'Personality' column has 'nan' (case insensitive)
    df = df[~df['Personality'].str.lower().str.contains('nan')]

    # Now that we've handled non-numeric 'NAN' values, we can safely convert the column to a numeric type
    # Convert MBTI types to digits using the provided mapping
    df['Personality'] = df['Personality'].map(mbti_mapping)

    # Drop any rows with NaN values that result from unmapped personalities
    df = df.dropna(subset=['Personality'])

    # Overwrite the original CSV file with the cleaned DataFrame
    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Cleaned {len(df)} rows from the '{file_path}' file.")


def split_csv(file_path, number_of_splits=4):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Calculate the size of each split
    split_size = len(df) // number_of_splits

    # Split the DataFrame into parts and save them as new CSV files
    for i in range(number_of_splits):
        start_index = i * split_size
        # If it's the last split, include the remainder
        end_index = None if i == number_of_splits - 1 else (i + 1) * split_size
        split_df = df[start_index:end_index]
        split_df.to_csv(f"{file_path}_part_{i + 1}.csv", index=False)


def insert_data(file_path, conn):
    df = pd.read_csv(file_path)

    df.to_sql("mbti", conn)

    print(f"Inserted {len(df)} rows into the table.")


def connect_to_iris():
    ssl_context = ssl.create_default_context(cadata=pem_file_contents)
    # InterSystems IRIS Cloud SQL connection parameters
    args = {
        'hostname': os.getenv("IRIS_HOSTNAME"),
        'port': "443",
        'namespace': "USER",
        'username': "SQLAdmin",
        'password': os.getenv("IRIS_PASSWORD")
    }
    # Create a sqlalchemy connection to IRIS
    engine = create_engine(
        f"iris://{args['username']}:{args['password']}@{args['hostname']}:{args['port']}/{args['namespace']}",
        connect_args={'sslcontext': ssl_context})

    return engine


engine = connect_to_iris()
conn = engine.connect()

sql = """
    SELECT PREDICT(PredictPersonality) AS PredictedPersonality, \
                      Personality AS ActualPersonality FROM SQLUsert.mbti
"""

response = pd.read_sql(text(sql), conn)

print(response)
