#!/usr/bin/env python3

import os

GIT_DIR = os.path.dirname(os.path.realpath(__file__))
HOME_DIR = os.path.expanduser('~')

ANS_DIR = os.path.expanduser('~/.ansible')
CFG_FILE = 'ansible.cfg'
ANS_DIR_FILE = os.path.join(ANS_DIR, CFG_FILE)
ANS_FILE = os.path.expanduser('~/.' + CFG_FILE)
SCRIPT = 'bin/ansp'

TASKS = {}
TASKS['linkdir'] = {
  'args': [GIT_DIR, ANS_DIR],
}
TASKS['linkhomecfg'] = {
  'args': [ANS_DIR_FILE, ANS_FILE],
}
TASKS['linkscript'] = {
  'args': [
    os.path.join(GIT_DIR, SCRIPT),
    os.path.join(HOME_DIR, SCRIPT),
  ]
}

def main(tasks):

  for task in tasks.values():
    make(**task)

  print('run: "sudo -H pip3 install ansible"')

def make(func=os.symlink, args=None, kwargs=None):

  args = args or []
  kwargs = kwargs or {}

  try:
    func(*args, **kwargs)
  except FileExistsError:
    pass

if __name__ == '__main__':
  main(TASKS)
