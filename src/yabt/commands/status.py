from yabt.commands import CommandOption
from yabt.commands.help import get_help
import yabt.models

class Command(CommandOption):
    cmd = "status"
    desc = "View and edit the status of tickets"
    # TODO: make statuses configurable
    help = """usage: yabt status [<subject> [<new status>]]

    <subject>    If provided without the optional <new status> it shows the
                 status of the given ticket.  If <new status> is provided, it
                 updates the ticket to have that new status
    <new status> The status you want the ticket to have
"""

    def run(self):
        if len(self.caller.options.args) <= 1:
            print "Error: must supply a title"
            print get_help("status")
            return
        task = yabt.models.TaskFactory().find(self.caller.options.args[1])
        if len(self.caller.options.args) == 3:
            task.status = self.caller.options.args[2]
            task.save()
        print task.subject + "    status: " + task.status

