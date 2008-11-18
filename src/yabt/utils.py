import yabt.commands

def command_factory(name):
    exec('k = yabt.commands.%s' % name)
    return k
