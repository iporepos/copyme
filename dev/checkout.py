# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (C) 2025 The Project Authors
# See pyproject.toml for authors/maintainers.
# See LICENSE for license details.

# IMPORTS
# ***********************************************************************

# Native imports
# =======================================================================
import subprocess
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
        decision = fork(message=s_msg, exit_option="cancel")

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


def black_all():
    subprocess.run(["black", "."])


def main():

    while True:
        subprocess.run(["clear"])

        print("\n")
        print(50 * "=")
        black_all()

        print("\n")
        print(50 * "=")
        subprocess.run(["git", "status"])

        s = fork(message="Add new changes?", exit_option="exit", clear_option=False)

        if s == "exit":
            exiting()
            break

        elif s == "y":
            subprocess.run(["git", "add", "."])
            git_commit()

        elif s == "n":
            continue

        elif s == "clear":
            subprocess.run(["clear"])
            continue


def git_commit():
    while True:
        print("\n")
        print(50 * "-")
        subprocess.run(["git", "status"])
        s = fork(message="Commit changes?", exit_option=None, clear_option=False)

        if s == "y":
            s_msg = "Enter commit message"
            git_msg = user_input(s_msg)
            if git_msg is None:
                print(" >>> Commit aborted.")
                time.sleep(1)
            else:
                subprocess.run(["git", "commit", "-m", f'"{git_msg}"'])
                print(f" >>> '{git_msg}' successfully commited")
                time.sleep(3)
            break

        elif s == "n":
            break

        elif s == "clear":
            subprocess.run(["clear"])
            continue


def exiting():
    print(" >>> exiting ...")
    time.sleep(1)
    subprocess.run(["clear"])


if __name__ == "__main__":

    print("Hello world!")

    # subprocess.run(["git", "tag"])

    main()
