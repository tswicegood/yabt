from yabt.commands import CommandOption
import yabt.models
import os # TODO: refactor out dependency

class Command(CommandOption):
    cmd = "list"
    desc = "Display a list of current issues"

    def run(self):
        index = yabt.models.Index(os.path.join(os.getcwd(), ".yabt", "index"))
        for task in index:
            print index.get(task)[0:10] + "    " + task


