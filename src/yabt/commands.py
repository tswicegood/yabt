from yabt.utils import command_factory
import yabt.models
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
            yabt.models.Index(os.path.join(new_path, "index"))
            sys.exit(0)

class Add(CommandOption):
    desc = "Add a new issue"
    cmd = "add"
    help = """usage: yabt add <title>

    <title> A single parameter that describes your new task.  This
            is generally encapsulated in quotes to accept a string.
"""

    def run(self):
        if len(self.caller.options.args) <= 1:
            print get_help('add')
            sys.exit(1)
        else:
            subject = self.caller.options.args[1]
            task = yabt.models.Task()
            task.subject = subject
            task.creator = "Travis Swicegood <travis@domain51.com>"
            task.save()
            # refactor generation of index and path
            index = yabt.models.Index(os.path.join(os.getcwd(),  ".yabt", "index"))
            index.addTask(task)
            index.save()


class Help(CommandOption):
    desc = "Display help for the provide command"
    cmd = "help"
    help = """Isn't that a bit meta?  Seriously, do you think this is Ruby?"""

    def run(self):
        if len(self.caller.options.args) <= 1:
            self.caller.usage()
        else :
            print get_help(self.caller.options.args[1])

class View(CommandOption):
    desc = "View a given bug by its subject"
    cmd = "view"
    help = """usage: yabt view <title>

    <title> A single parameter that identifies a task by its unique subject.
            It is generally encapsulated in quotes.
"""

    def run(self):
        print "Not yet implemented"
        """
        i = yabt.models.IndexFactory()
        task_id = i.get(selc.caller.options.args[1])
        t = yabt.models.TaskFactory().byId(task_id)
        print t
        """

def get_help(class_name):
    c = command_factory(class_name.title())
    return c.help

class List(CommandOption):
    cmd = "list"
    desc = "Display a list of current issues"

    def run(self):
        index = yabt.models.Index(os.path.join(os.getcwd(), ".yabt", "index"))
        for task in index:
            print index.get(task) + "    " + task
