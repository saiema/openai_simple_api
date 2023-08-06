import argparse


class QueryDataCollector(argparse.Action):

    def __init__(self, option_strings, dest, **kwargs):
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if (option_string == "-c") | (option_string == "--use-chat-completion"):
            setattr(namespace, self.dest, bool(values))
        if (option_string == "-t") | (option_string == "--text"):
            setattr(namespace, self.dest, values)
        elif (option_string == "-f") | (option_string == "--file"):
            with open(values, 'r') as file:
                setattr(namespace, 'text', file.read())
        elif (option_string == "-p") | (option_string == "--prompt"):
            setattr(namespace, self.dest, values)
        elif (option_string == "-m") | (option_string == "--model"):
            setattr(namespace, self.dest, values)
        elif (option_string == "-o") | (option_string == "--max-tokens"):
            setattr(namespace, self.dest, int(values))
        elif (option_string == "-e") | (option_string == "--temperature"):
            setattr(namespace, self.dest, float(values))
        elif option_string == "-n":
            setattr(namespace, self.dest, int(values))
        elif (option_string == "-b") | (option_string == "--best-of"):
            setattr(namespace, self.dest, int(values))

