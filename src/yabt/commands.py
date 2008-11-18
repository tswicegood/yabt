from yabt.utils import command_factory

class CommandOption(object):
    desc = "undefined"
    help = "not yet defined"

    def __init__(self, caller):
        pass

    def run(self):
        print "Not yet implemented"

class Add(CommandOption):
    desc = "Add a new issue"
    cmd = "add"
    help = """usage: yabt add <title>

Options:
    Some options should go here
"""

    def __init__(self, caller):
        pass

class Help(CommandOption):
    desc = "Display help for the provide command"
    cmd = "help"
    help = """Isn't that a bit meta?  Seriously, do you think this is Ruby?"""

    def __init__(self, caller):
        self.caller = caller

    def run(self):
        if len(self.caller.options.args) <= 1:
            self.caller.usage()
        else :
            klass = command_factory(self.caller.options.args[1].title())
            print klass.help
        

class List(CommandOption):
    cmd = "list"
    desc = "Display a list of current issues"

