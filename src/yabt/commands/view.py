from yabt.commands import CommandOption
from yabt.commands.help import get_help
import yabt.models

class Command(CommandOption):
    desc = "View a given bug by its subject"
    cmd = "view"
    help = """usage: yabt view <title>

    <title> A single parameter that identifies a task by its unique subject.
            It is generally encapsulated in quotes.
"""

    def run(self):
        if len(self.caller.options.args) <= 1:
            # TODO: should raise an error and let the caller display the error and usage
            print "Error: must supply a title"
            print get_help("view");
            return
        task = yabt.models.TaskFactory().byTitle(self.caller.options.args[1])
        print task;


