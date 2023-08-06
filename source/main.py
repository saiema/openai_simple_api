import argparse
import sys
from actions.ShowHelp import ShowHelp
from actions.ShowVersion import ShowVersion
from actions.ShowModels import ShowModels
from actions.ShowPredefinedPrompts import ShowPredefinedPrompts
from actions.QueryDataCollector import QueryDataCollector
from api.PromptManager import PromptManager
from api.ChatGPT import ChatGPT

parser = argparse.ArgumentParser(add_help=False)
mutually_exclusive_flags = parser.add_mutually_exclusive_group()
mutually_exclusive_flags.add_argument("-h", "--help", action=ShowHelp, default=False)
mutually_exclusive_flags.add_argument("-v", "--version", action=ShowVersion, default=False)
mutually_exclusive_flags.add_argument("-l", "--list-models", action=ShowModels, default=False)
mutually_exclusive_flags.add_argument("-r", "--predefined-prompts", action=ShowPredefinedPrompts,
                                      default=False)
mutually_exclusive_flags.add_argument("-t", "--text", type=str, action=QueryDataCollector)
mutually_exclusive_flags.add_argument("-f", "--file", type=str, action=QueryDataCollector)
parser.add_argument("-c", "--use-chat-completion", type=bool, action=QueryDataCollector)
parser.add_argument("-m", "--model", type=str, action=QueryDataCollector)
parser.add_argument("-p", "--prompt", type=str, action=QueryDataCollector)
parser.add_argument("-o", "--max-tokens", type=int, action=QueryDataCollector)
parser.add_argument("-e", "--temperature", type=float, action=QueryDataCollector)
parser.add_argument("-n", "--n", type=int, action=QueryDataCollector)
parser.add_argument("-b", "--best-of", type=int, action=QueryDataCollector)

if __name__ == '__main__':
    args = parser.parse_args()
    if args.help | args.version | args.list_models | args.predefined_prompts:
        exit(0)
    if args.prompt is not None:
        PromptManager.instance().select_prompt(args.prompt)
        args.text = PromptManager.instance().last_selected_prompt() + args.text
    if args.use_chat_completion is not None:
        ChatGPT.instance().use_chat_completion = args.use_chat_completion
    if args.model is not None:
        if args.model not in ChatGPT.instance().available_models:
            print(f"The model {args.model} is not an available model\n"
                  f"Use --list-models to get a list of available models.", file=sys.stderr)
            exit(1)
        ChatGPT.instance().model = args.model
    if args.max_tokens is not None:
        ChatGPT.instance().max_tokens = args.max_tokens
    if args.temperature is not None:
        ChatGPT.instance().temperature = args.temperature
    if args.n is not None:
        ChatGPT.instance().n = args.n
    if args.best_of is not None:
        ChatGPT.instance().best_of = args.best_of
    print(f"ChatGPT response:\n{ChatGPT.instance().completion(args.text)}")
