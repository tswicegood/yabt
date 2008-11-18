import optparse
import yabt.commands
from yabt.utils import command_factory

class Options(object) :
    def __init__(self):
        self.parser = optparse.OptionParser()
        self.parser.add_option('-v', '--version')
        self.options, self.args = self.parser.parse_args()

class YABT(object) :
    version = 0.1
    def __init__(self, options):
        self.options = options

    def run(self):
        if len(self.options.args) > 0  :
            klass = command_factory(self.options.args[0].title())
            klass(self).run()
        else:
            self.usage()

    def usage(self):
        print """%s

Usage: yabt <command> <options>

Commands:
%s

You can get additional information by typing: yabt help <command>"""\
        % (self.version_line(), self.display_commands())


    def version_line(self):
        return "Yet-Another-Bug-Tracker v%s" % self.version

    def display_commands(self):
        ret = []
        for class_name in dir(yabt.commands):
            try:
                klass = command_factory(class_name)
                ret.append("%10s - %s" % (klass.cmd, klass.desc))
            except AttributeError, e:
                pass
        return "\n".join(ret)


