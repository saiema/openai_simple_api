import os

VERSION: str = "0.0.1"


class Config(object):
    _development: bool = False
    _testing: bool = False
    _debug: bool = False
    _env: str = None
    _secret_key: str = None
    _default_use_chat_completion: bool = False
    _default_model: str = "text-davinci-003"
    _default_max_tokens: int = 16
    _default_temperature: float = 1.0
    _default_n: int = 1
    _default_best_of: int = 1

    def development(self) -> bool:
        """
        :type: bool
        :return: If this is a development configuration or not.
        """
        return self._development

    def testing(self) -> bool:
        """
        :type: bool
        :return: If this is a testing configuration or not.
        """
        return self._testing

    def debug(self) -> bool:
        """
        :type: bool
        :return: Is debug features should be enabled.
        """
        return self._debug

    def env(self) -> str:
        """
        :type: str
        :return: The environment to which this configuration belongs.
        """
        return self._env

    def secret_key(self) -> str:
        """
        :type: str
        :return: The ChatGPT API secret key to use
        """
        return self._secret_key

    def default_use_chat_completion(self) -> bool:
        """
        :type: bool
        :return: The default for using chat completion or just completion by the ChatGPT API manager
        """
        return self._default_use_chat_completion

    def default_model(self) -> str:
        """
        :type: str
        :return: The default model to be used by the ChatGPT API manager
        """
        return self._default_model

    def default_max_tokens(self) -> int:
        """
        :type: int
        :return: The default value for max_tokens used by the ChatGPT API manager
        """
        return self._default_max_tokens

    def default_temperature(self) -> float:
        """
        :type: float
        :return: The default value for temperature used by the ChatGPT API manager
        """
        return self._default_temperature

    def default_n(self) -> int:
        """
        :type: int
        :return: The default value for n used by the ChatGPT API manager
        """
        return self._default_n

    def default_best_of(self) -> int:
        """
        :type: int
        :return: The default value for best_of used by the ChatGPT API manager
        """
        return self._default_best_of


class DevelopmentConfig(Config):
    _development = True
    _debug = True
    _env = "development"
    _secret_key = os.environ.get("SECRET_KEY")


class TestingConfig(Config):
    _development = False
    _testing = True
    _debug = True
    _env = "testing"
    _secret_key = None


configs = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}

current_config: Config = configs["testing"]()
