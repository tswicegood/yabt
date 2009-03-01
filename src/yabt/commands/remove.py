from yabt.commands import CommandOption
from yabt.commands.help import get_help
import yabt.models
import sys
import os

class Command(CommandOption):
    desc = "Remove an existing task"
    cmd = "remove"
    help = """usage: yabt remove <title>

    <title> A single parameter that describes your new task.  This
            is generally encapsulated in quotes to accept a string.
"""

    def run(self):
        try :
            task_name = self.caller.options.args[1]
            task = yabt.models.TaskFactory().find(task_name)
            if task is None:
                print "Unable to find task \"%s\"" % (task_name)
                sys.exit(1)
            task.remove()
            # refactor generation of index and path
            index = yabt.models.Index(os.path.join(os.getcwd(),  ".yabt", "index"))
            index.removeTask(task)
            index.save()
        except IndexError:
            print "Error: must provide a task to remove"
            print get_help('remove')
            sys.exit(1)



