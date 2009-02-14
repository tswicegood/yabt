from yabt.commands import CommandOption
import yabt.models
import os, sys

class Command(CommandOption):
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


