from yabt.commands import CommandOption
from yabt.commands.help import get_help
import yabt.models
import os, subprocess

class Command(CommandOption):
    cmd = "edit"
    desc = "Edit a provided ticket"
    help = """usage: yabt edit <title>

    <title> A single parameter that identifies a task to edit.

yabt looks in the following locations, in the following order, to find an
editor to launch:
 * EDITOR environment variable
 * Attempts to execute "vi" command
"""

    def run(self):
        if len(self.caller.options.args) <= 1:
            print "Error: must supply a title"
            print get_help("edit")
            return
        task = yabt.models.TaskFactory().find(self.caller.options.args[1])
        if os.getenv("EDITOR") is not None:
            editor = os.getenv("EDITOR")
        else:
            editor = "vi"
        subprocess.call([editor, os.path.join(os.getcwd(), ".yabt", "tickets", task.id)])


