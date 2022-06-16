class MockInput:
    def __init__(self, expected_prompt: str, *inputs: str) -> None:
        self.inputs = inputs
        self.expected_prompt = expected_prompt
        self.__call_count = 0

    def get_input(self, prompt: str) -> str:
        if prompt == self.expected_prompt:
            string = self.inputs[self.__call_count]
            if self.__call_count < len(self.inputs):
                self.__call_count += 1
            return string
        return ""
