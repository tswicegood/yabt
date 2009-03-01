import yabt.commands
import dircache
import sys
import os.path

def command_factory(name):
    exec('from yabt.commands.%s import Command' % name)
    return Command

# TODO allow multiple "paths" for custom commands
def find_commands():
    commands = []
    for path in sys.path:
        command_path = os.path.join(path, "yabt/commands")
        if os.path.exists(command_path) is False:
            continue

        for file in dircache.listdir(command_path):
            if file[-3:] == ".py" and file[0:1] != "_":
                commands.append(file[0:-3])
    return commands

