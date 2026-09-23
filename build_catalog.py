# -*- coding: utf-8 -*-
"""Shortcut runner for builders/build_catalog.py"""
import os
import subprocess
import sys

if __name__ == '__main__':
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'builders', 'build_catalog.py')
    sys.exit(subprocess.run([sys.executable, script]).returncode)
