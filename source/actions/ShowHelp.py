import argparse
import config


class ShowHelp(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super().__init__(option_strings, dest, nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, True)
        print(f"Simple ChatGPT API interaction application -- version {config.VERSION}.")
        print(f"Usage:")
        print(f"\t-v|--version\t\t\t\t\t\t\t\t:Shows the current version of this application.")
        print(f"\t-h|--help\t\t\t\t\t\t\t\t\t:Shows this help.")
        print(f"\t-l|--list-models\t\t\t\t\t\t\t:Lists all available models."
              f"\n\t\t(Note that currently only Completion models are supported).")
        print(f"\t-r|--predefined-prompts\t\t\t\t:Lists all predefined prompts.")
        print(f"\t-[-t]ext TEXT [-[-p]rompt PROMPT] [OPTIONS]\t:"
              f"\n\t\tMakes a prompt, using TEXT, through ChatGPT API returning the obtained response,"
              f"\n\t\tif a prompt is provided, the full prompt will be PROMPT followed by TEXT.")
        print(f"\t-[-f]ile FILE [-[-p]rompt PROMPT] [OPTIONS]\t:"
              f"\n\t\tMakes a prompt, using the contents of FILE, through ChatGPT API returning the obtained response,"
              f"\n\t\tif a prompt is provided, the full prompt will be PROMPT followed by the text contained in FILE.")
        print(f"\tThe optional OPTIONS include the following:")
        print(f"\t\t-[-]use-[c]hat-completion\t\t\t\t\t\t:Defines if the ChatGPT api will use"
              f"\n\t\t\tthe chat completion endpoint or just completion,"
              f"\n\t\t\tthe default value is {config.current_config.default_use_chat_completion()}.")
        print(f"\t\t-[-m]odel MODEL\t\t\t\t\t\t:Sets the model to use,"
              f"default value is {config.current_config.default_model()}.")
        print(f"\t\t-[-]max-t[o]kens INT\t\t\t:The maximum number of tokens to generate in the completion."
              f"\n\t\t\tThe token count of your prompt plus max_tokens cannot exceed the model's context length."
              f"\n\t\t\tThe default value is {config.current_config.default_max_tokens()}.")
        print(f"\t\t-[-]t[e]mperature FLOAT(0 - 2)\t:What sampling temperature to use, between 0 and 2. "
              f"\n\t\t\tHigher values like 0.8 will make the output more random, while lower values like 0.2"
              f"\n\t\t\twill make it more focused and deterministic."
              f"\n\t\t\tThe default value is {config.current_config.default_temperature()}.")
        print(f"\t\t-n\t:How many completions to generate for each prompt."
              f"\n\t\t\tNote: Because this parameter generates many completions, it can quickly consume"
              f"\n\t\t\tyour token quota. Use carefully and ensure that you have reasonable settings for max_tokens."
              f"\n\t\t\tThe default value is {config.current_config.default_n()}.")
        print(f"\t\t-[-b]est-of\t:Generates best_of completions server-side and returns the \"best\"."
              f"\n\t\t\tThe default value is {config.current_config.default_best_of()}")
