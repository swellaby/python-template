from invoke import task
import platform
import os
from shutil import rmtree
# Insert module name on the below line
from  import __version__


def black(c, check):
    cmd = f"black . --line-length=79 {'--check' if check is True else ''}"
    return c.run(cmd)


@task(aliases=["f"])
def format(c):
    return black(c, False)


@task(aliases=["cf", "fc"])
def check_format(c):
    return black(c, True)


@task()
def clean_test_reports(c):
    rmtree(".test-reports/", ignore_errors=True)
    if os.path.exists(".coverage"):
        os.remove(".coverage")


@task(aliases=["cl"], pre=[clean_test_reports])
def clean(c):
    pass


@task(aliases=["t"], pre=[clean])
def test(c):
    return c.run("pytest")


@task(aliases=["roc"])
def reopen_coverage(c):
    path = ".test-reports/coverage/unit/html/index.html"
    operating_system = platform.system()
    if operating_system == "Linux":
        return c.run("xdg-open " + path)
    elif operating_system == "Windows":
        return c.run("cmd.exe /C start " + path)
    else:
        return c.run("open " + path)


@task(aliases=["oc", "c"], pre=[test], post=[reopen_coverage])
def open_coverage(c):
    pass


@task(aliases=["l", "lp"])
def lint(c):
    return c.run("pycodestyle .")


@task(aliases=["pv", "sv"])
def print_version(c):
    return print(__version__)
