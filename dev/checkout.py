# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (C) 2025 The Project Authors
# See pyproject.toml for authors/maintainers.
# See LICENSE for license details.
"""
todo: docstring

"""
# IMPORTS
# ***********************************************************************

# Native imports
# =======================================================================
import subprocess
import sys
import time


# FUNCTIONS
# =======================================================================


def fork(message="Chose action", exit_option="exit", clear_option=True):
    s_prefix = f" >>> {message}"
    s_opt = "[y][n]"
    ls = ["y", "n"]

    if exit_option is not None:
        s_opt = s_opt + f"[{exit_option}]"
        ls = ls + [exit_option]

    if clear_option:
        s_opt = s_opt + f"[clear]"
        ls = ls + ["clear"]

    s = f"{s_prefix} {s_opt}: "

    s_inp = None
    while True:
        s_inp = input(s).strip().lower()
        if s_inp in ls:
            break

    return s_inp


def user_input(message="Enter input"):
    s_inp = None
    s = f" >>> {message}: "
    while True:
        print("\n")
        s_inp = input(s).strip()
        s_msg = f"Confirm input: '{s_inp}' ?"
        decision = fork(message=s_msg, exit_option="cancel", clear_option=False)

        if decision == "y":
            print(" >>> input confirmed.")
            break
        elif decision == "cancel":
            print(" >>> input cancelled.")
            s_inp = None
            break
        elif decision == "n":
            print(" >>> input restarted.")
            continue
        elif decision == "clear":
            subprocess.run(["clear"])
            print(" >>> input restarted.")
            continue

    return s_inp


def run_style():
    print("\n")
    print(50 * "=")
    print("Black style")
    subprocess.run(["black", "."])
    return None


def build_docs():
    print("\n")
    print(50 * "=")
    print("Sphinx docs")
    subprocess.run([sys.executable, "-m", "dev.docs"])
    time.sleep(3)
    return None


def run_tests():
    print("\n")
    print(50 * "=")
    print("Unit tests")

    subprocess.run([sys.executable, "-m", "dev.tests"])

    time.sleep(3)
    return None


def handle_commit():
    while True:
        print("\n")
        print(50 * "-")
        subprocess.run(["git", "status"])
        s = fork(message="Commit changes?", exit_option=None, clear_option=False)

        if s == "y":
            s_msg = "Enter commit message"
            git_msg = user_input(s_msg)
            if git_msg is None:
                print(" >>> Commit cancelled.")
                time.sleep(1)
            else:
                subprocess.run(["git", "commit", "-m", f'"{git_msg}"'])
                print(f" >>> '{git_msg}' successfully commited.")
                time.sleep(3)
            break

        elif s == "n":
            break


def handle_tag():

    while True:
        print("\n")
        print(50 * "-")
        print("Current tags:")
        subprocess.run(["git", "tag"])

        s = fork(message="Enter new tag?", exit_option=None, clear_option=False)

        if s == "y":
            s_msg = "Enter new tag in vX.Y.Z format"
            stag = user_input(s_msg)

            if stag is None:
                print(" >>> Tagging cancelled.")
                time.sleep(1)

            else:
                tag_msg = f"Release {stag[1:]}"
                subprocess.run(["git", "tag", "-a", stag, "-m", tag_msg])
                print(f" >>> '{stag}' successfully added")
                print("Updated tags:")
                subprocess.run(["git", "tag"])
                time.sleep(3)

            break

        elif s == "n":
            break

        elif s == "clear":
            subprocess.run(["clear"])
            continue


def handle_push():
    while True:
        print("\n")
        print(50 * "-")
        print("Publish")

        s = fork(
            message="Publish main branch to remote?",
            exit_option=None,
            clear_option=True,
        )

        if s == "y":
            subprocess.run(["git", "push", "origin", "main"])
            print(f" >>> main branch successfully published")
            time.sleep(1)
            subprocess.run(["git", "push", "origin", "--tags"])
            print(f" >>> tags successfully published")
            time.sleep(1)

            break

        elif s == "n":
            print(f" >>> publishing cancelled")
            break

        elif s == "clear":
            subprocess.run(["clear"])
            continue


def exiting():
    print(" >>> exiting ...")
    time.sleep(1)
    subprocess.run(["clear"])


def main():

    while True:
        subprocess.run(["clear"])
        print("\n")
        print(50 * "#")
        print("CHECK OUT")
        print("\n")

        s = fork("Build Docs and Run Tests?", "exit", False)
        if s == "y":

            build_docs()
            run_tests()

        elif s == "exit":
            exiting()
            break

        run_style()

        print("\n")
        print(50 * "=")
        print("Git Tags")
        subprocess.run(["git", "tag"])

        print("\n")
        print(50 * "=")
        print("Git Status")
        subprocess.run(["git", "status"])
        print("\n\n")
        s = fork(
            message="Add/commit/push new changes?",
            exit_option="exit",
            clear_option=False,
        )

        if s == "exit":
            exiting()
            break

        elif s == "y":
            subprocess.run(["git", "add", "."])
            handle_commit()
            handle_tag()
            handle_push()

        elif s == "n":
            continue

        elif s == "clear":
            subprocess.run(["clear"])
            continue


# SCRIPT
# ***********************************************************************
if __name__ == "__main__":

    main()
