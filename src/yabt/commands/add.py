from yabt.commands import CommandOption
from yabt.commands.help import get_help
import yabt.models
import os, sys # TODO: refactor these dependencies out

class Command(CommandOption):
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


