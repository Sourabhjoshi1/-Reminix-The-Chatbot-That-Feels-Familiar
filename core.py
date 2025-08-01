from app.memory import MemoryBank


class ReminixAgent:
    def __init__(self):
        self.memory_bank = MemoryBank()

    def remember(self, content, tags=None, emotion=None):
        return self.memory_bank.add_memory(content, tags, emotion)

    def recall_recent(self, n=5):
        return self.memory_bank.get_recent(n)

    def recall_by_emotion(self, emotion):
        return self.memory_bank.search(emotion=emotion)

    def search_memory(self, keyword):
        return self.memory_bank.search(keyword=keyword)
