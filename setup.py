#!/usr/bin/env python3

import os

MY_DIR = os.path.dirname(os.path.realpath(__file__))

HOME_DIR = os.path.expanduser('~/.ansible')
CFG_FILE = 'ansible.cfg'
HOME_DIR_FILE = os.path.join(HOME_DIR, CFG_FILE)
HOME_FILE = os.path.expanduser('~/.' + CFG_FILE)

TASKS = {}
TASKS['linkdir'] = {
  'func': os.symlink,
  'args': [MY_DIR, HOME_DIR],
}
TASKS['linkhomecfg'] = {
  'func': os.symlink,
  'args': [HOME_DIR_FILE, HOME_FILE],
} 

def main(tasks):

  for task in tasks.values():
    make(**task)

def make(func, args=None, kwargs=None):

  args = args or []
  kwargs = kwargs or {}

  try:
    func(*args, **kwargs)
  except FileExistsError:
    pass

if __name__ == '__main__':
  main(TASKS)
