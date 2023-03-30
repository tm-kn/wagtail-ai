from typing import List


class MockBackend:
    def __init__(self, config):
        pass

    def prompt(self, prompt: str) -> str:
        return "AI! Don't talk to me about AI!"

    def get_embeddings(self, inputs: List[str]) -> List[List[float]]:
        return [[0.1, 0.2, 0.3]]
