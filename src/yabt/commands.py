class CommandOption(object):
    def __init__(self, caller):
        pass

    def run(self):
        print "Not yet implemented"

class Add(CommandOption):
    desc = "Add a new issue"
    cmd = "add"
    help = """usage: yabt add <title>"""

    def __init__(self, caller):
        pass

class Help(CommandOption):
    desc = "Display help for the provide command"
    cmd = "help"

    def __init__(self, caller):
        self.caller = caller

    def run(self):
        if len(self.caller.options.args) <= 1:
            self.caller.usage()
        else :
            print "Help?  You want help bitch?!"
        

class List(CommandOption):
    desc = "Display a list of current issues"
    cmd = "list"

    def __init__(self, caller):
        pass
