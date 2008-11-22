from yabt.utils import command_factory
import os, sys

class CommandOption(object):
    desc = "undefined"
    help = "not yet defined"

    def __init__(self, caller):
        self.caller = caller

    def run(self):
        print "Not yet implemented"

class Init(CommandOption):
    desc = "Initialize a new YABT filesystem"
    cmd = "init"
    help = """usage: yabt init

This initializes a YABT filesystem inside the .yabt directory if one does
not exist.
"""

    def run(self):
        """
        @todo add ability to pass in --dir parameter
        """
        new_path = os.path.join(os.getcwd(), ".yabt")
        if os.path.exists(new_path):
            print "YABT filesystem already initialized in " + new_path
            sys.exit(1)
        else:
            os.mkdir(new_path)
            print "YABT filesystem initialized in " + new_path
            sys.exit(0)

class Add(CommandOption):
    desc = "Add a new issue"
    cmd = "add"
    help = """usage: yabt add <title>

Options:
    Some options should go here
"""


class Help(CommandOption):
    desc = "Display help for the provide command"
    cmd = "help"
    help = """Isn't that a bit meta?  Seriously, do you think this is Ruby?"""

    def run(self):
        if len(self.caller.options.args) <= 1:
            self.caller.usage()
        else :
            print get_help(self.caller.options.args[1])

def get_help(class_name):
    c = command_factory(class_name.title())
    return c.help

class List(CommandOption):
    cmd = "list"
    desc = "Display a list of current issues"

