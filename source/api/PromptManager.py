class PromptManager:
    """
    A simple prompt manager which will offer predefined prompts plus
    the option to save new custom ones
    """
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if self._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PromptManager._instance = self
            self._custom_prompts: [str] = []

    # noinspection PyMethodMayBeStatic
    def predefined_prompts(self) -> [str]:
        return ["Translate the following text",
                "Correct the syntax of the following text",
                "List some prompts based on the following text (WUUUT?)"
                ]

    def custom_prompts(self) -> [str]:
        return self._custom_prompts

    def select_prompt(self, prompt: str) -> None:
        if prompt not in self._custom_prompts:
            self._custom_prompts.append(prompt)
        self._custom_prompts.remove(prompt)
        self._custom_prompts.append(prompt)

    def last_selected_prompt(self) -> str | None:
        if self._custom_prompts:
            return self._custom_prompts[-1]
        return None

    def clear_custom_prompts(self) -> None:
        self._custom_prompts.clear()
