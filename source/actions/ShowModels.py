import argparse
from api.ChatGPT import ChatGPT


class ShowModels(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super().__init__(option_strings, dest, nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)
        print(f"Available models:")
        for available_model in ChatGPT().available_models:
            print(f"{available_model}")
