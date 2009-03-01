from distutils.core import setup

# TODO: add classifiers once I have the full list
setup(
    name = "yabt",
    version = "0.1.0",
    packages = ["yabt", "yabt.commands"],
    package_dir = {"yabt": "src/yabt", "yabt.commands": "src/yabt/commands"},
    scripts = ["scripts/yabt"],
    author = "Travis Swicegood",
    author_email = "development@domain51.com"
)
