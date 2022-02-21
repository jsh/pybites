#!/usr/bin/env python3

import shutil

REPO="."
GIT_DIR=".git"
shutil.rmtree(GIT_DIR, ignore_errors=True)
