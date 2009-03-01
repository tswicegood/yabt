from yabt.commands import CommandOption
from yabt.utils import command_factory

class Command(CommandOption):
    desc = "Display help for the provide command"
    cmd = "help"
    help = """Isn't that a bit meta?  Seriously, do you think this is Ruby?"""

    def run(self):
        if len(self.caller.options.args) <= 1:
            self.caller.usage()
        else :
            print get_help(self.caller.options.args[1])

def get_help(class_name):
    c = command_factory(class_name)
    return c.help


