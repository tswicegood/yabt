import optparse
import yabt.commands
import yabt.utils
from yabt.utils import command_factory

class Options(object) :
    def __init__(self):
        self.parser = optparse.OptionParser()
        self.parser.add_option('-v', '--version', action="store_true", dest="version")
        self.options, self.args = self.parser.parse_args()

class YABT(object) :
    version = "0.1.1"
    def __init__(self, options):
        self.options = options

    def run(self):
        if self.options.options.version:
            print self.version_line()
            return
        if len(self.options.args) > 0  :
            klass = command_factory(self.options.args[0])
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
        return "Yet Another Bug Tracker (yabt) v%s" % self.version

    def display_commands(self):
        ret = []
        for command in yabt.utils.find_commands():
            try:
                klass = command_factory(command)
                ret.append("%10s - %s" % (klass.cmd, klass.desc))
            except AttributeError, e:
                pass
        return "\n".join(ret)


