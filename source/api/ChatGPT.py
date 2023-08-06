import openai
from typing import Dict
import config


class ChatGPT:
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
            ChatGPT._instance = self
            self._secret_api_key = config.current_config.secret_key()
            openai.api_key = self._secret_api_key
            self._use_chat_completion = config.current_config.default_use_chat_completion()
            self._model = config.current_config.default_model()
            self._max_tokens = config.current_config.default_max_tokens()
            self._temperature = config.current_config.default_temperature()
            self._n = config.current_config.default_n()
            self._best_of = config.current_config.default_best_of()

    def _default(self):
        self._secret_api_key = config.current_config.secret_key()
        openai.api_key = self._secret_api_key
        self._use_chat_completion = config.current_config.default_use_chat_completion()
        self._model = config.current_config.default_model()
        self._max_tokens = config.current_config.default_max_tokens()
        self._temperature = config.current_config.default_temperature()
        self._n = config.current_config.default_n()
        self._best_of = config.current_config.default_best_of()

    def reset_to_defaults(self) -> None:
        self._default()

    @property
    def use_chat_completion(self) -> bool:
        """
        :return: If the endpoint to use is either chat completion or just completion
        """
        return self._use_chat_completion

    @use_chat_completion.setter
    def use_chat_completion(self, use_chat_completion: bool):
        self._use_chat_completion = use_chat_completion

    @property
    def model(self) -> str:
        """
        :return: ID of the model to use.
        """
        return self._model

    @model.setter
    def model(self, model: str):
        self._model = model

    @property
    def max_tokens(self) -> int:
        """
        The maximum number of tokens to generate in the completion.
        The token count of your prompt plus max_tokens cannot exceed the model's context length.
        :return: The maximum number of tokens to generate in the completion.
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens: int):
        self._max_tokens = max_tokens

    @property
    def temperature(self) -> float:
        """
        What sampling temperature to use, between 0 and 2.
        Higher values like 0.8 will make the output more random, while lower values
        like 0.2 will make it more focused and deterministic.
        :return: The sampling temperature to use.
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: float):
        self._temperature = temperature

    @property
    def n(self) -> int:
        """
        How many completions to generate for each prompt.

        ---

        **Note: Because this parameter generates many completions, it can quickly
        consume your token quota. Use carefully and ensure that you have reasonable
        settings for max_tokens.**
        :return: How many completions to generate for each prompt.
        """
        return self._n

    @n.setter
    def n(self, n: int):
        self._n = n

    @property
    def best_of(self) -> int:
        """
        Generates best_of completions server-side and returns the "best"

        When used with n, best_of controls the number of candidate completions
        and n specifies how many to return – best_of must be greater than n.

        ---

        **Note: Because this parameter generates many completions,
        it can quickly consume your token quota. Use carefully and
        ensure that you have reasonable settings for max_tokens.**

        :return: How many completions will be considered to return the best of those.
        """
        return self._best_of

    @best_of.setter
    def best_of(self, best_of: int):
        self._best_of = best_of

    def secret_key(self, secret_key: str) -> None:
        self._secret_api_key = secret_key
        openai.api_key = secret_key

    @property
    def available_models(self) -> [str]:
        """
        Lists the available models to be used with the completion api.

        :return: The list of available models.
        """
        models = openai.Model.list()
        return [model['id'] for model in models['data']]

    def completion(self, prompt: str) -> Dict:
        if self.use_chat_completion:
            return openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": f"{prompt}"}],
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                n=self.n
            )
        return openai.Completion.create(
            model=self.model,
            prompt=prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            n=self.n,
            best_of=self.best_of
        )


'''
{
  "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
  "object": "text_completion",
  "created": 1589478378,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nThis is indeed a test",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 7,
    "total_tokens": 12
  }
}

'''
