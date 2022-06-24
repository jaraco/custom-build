import setuptools
from distutils import log


class Command(setuptools.Command):
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        log.info("brrrrrrrrr")


def install(dist):
    # This could be protected by a opt-in condition...
    build = dist.get_command_obj("build")
    build.sub_commands = [*build.sub_commands, ("custom-build", None)]
