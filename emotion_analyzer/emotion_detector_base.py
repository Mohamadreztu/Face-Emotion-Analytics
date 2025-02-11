from abc import ABC, abstractmethod


class EmotionDetectorBase(ABC):
    @abstractmethod
    def detect_emotion(self):
        pass
