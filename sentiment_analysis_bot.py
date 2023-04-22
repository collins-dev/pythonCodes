from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

    
    def get_mood(input_text: str, *, threshold: float):
        """
        Analyze the mood of a given text and return a mood object containing the emoji and sentiment
        :input_text: The input text to be analyzed
        :threshold: The statement threshold used for determining the friendly and hostile mood
        :return: A mood object containing the mood and the sentiment polarity.
        """
        sentiment: float = TextBlob(input_text).sentiment.polarity

        # define mood thresholds
        friendly_threshold: float = threshold
        hostile_threshold: float = -threshold

        if sentiment >= friendly_threshold:
            return Mood('😊', sentiment)
        elif sentiment <= hostile_threshold:
            return Mood('😢', sentiment)
        else:
            return Mood('😐', sentiment)

if __name__ == '__main__':
    while True:
        text: str = input('Text: ')
        mood: Mood = Mood.get_mood(text, threshold=0.1)

        print(f'{mood.emoji} ({mood.sentiment})')
