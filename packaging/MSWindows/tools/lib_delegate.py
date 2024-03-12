#!/usr/bin/env python3
# This file is part of Xpra.
# Copyright (C) 2024 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import os
import sys


def main(argv=()) -> int:
    # add `Xpra/` and `Xpra/lib` to the %PATH%
    # then call the real EXE:
    app_dir, exe_name = os.path.split(argv[0])
    if not exe_name.lower().endswith(".exe"):
        exe_name += ".exe"
    lib_dir = os.path.join(app_dir, "lib")
    paths = os.environ.get("PATH", "").split(os.pathsep)
    for d in (lib_dir, app_dir):
        if d not in paths:
            paths.append(d)
    os.environ["PATH"] = os.pathsep.join(paths)
    actual_exe = os.path.join(lib_dir, exe_name)
    from subprocess import run, STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, STD_ERROR_HANDLE
    args = [actual_exe] + list(argv[1:])
    return run(args, stdin=STD_INPUT_HANDLE, stdout=STD_OUTPUT_HANDLE, stderr=STD_ERROR_HANDLE).returncode


if __name__ == "__main__":
    v = main(sys.argv)
    sys.exit(v)
