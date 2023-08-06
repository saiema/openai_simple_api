from config import configs


def before_all(context):
    context.config = configs["testing"]()
