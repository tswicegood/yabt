import yabt.commands

def command_factory(name):
    exec('from yabt.commands.%s import Command' % name)
    return Command
