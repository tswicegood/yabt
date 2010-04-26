from distutils.core import setup
import os, sys
sys.path[0:0] = [os.path.join(os.path.dirname(__file__), "src"), ]

from yabt import YABT


# TODO: add classifiers once I have the full list
setup(
    name = "yabt",
    version = YABT.version,
    packages = ["yabt", "yabt.commands"],
    package_dir = {"yabt": "src/yabt", "yabt.commands": "src/yabt/commands"},
    scripts = ["scripts/yabt"],
    author = "Travis Swicegood",
    author_email = "development@domain51.com"
)
