# -*- coding: utf-8 -*-
"""Shortcut runner for builders/build_solutions.py"""
import os
import subprocess
import sys

if __name__ == '__main__':
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'builders', 'build_solutions.py')
    sys.exit(subprocess.run([sys.executable, script]).returncode)
