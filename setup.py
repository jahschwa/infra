#!/usr/bin/env python3

import os
from pathlib import Path

GIT = Path(__file__).resolve().parent
HOME = Path('~').expanduser()

ANSIBLE = HOME / '.ansible'
CFG = 'ansible.cfg'
CFG_HIDDEN = '.' + CFG

SCRIPTS = Path('bin/ans')
SCRIPT_SUFFIXES = ['p', 'v']

TASKS = {}
TASKS['link_ansible_dir'] = {
  'args': [GIT, ANSIBLE],
}
TASKS['link_home_cfg'] = {
  'args': [ANSIBLE / CFG, HOME / CFG_HIDDEN],
}
for suffix in SCRIPT_SUFFIXES:
  script = SCRIPTS.with_name(SCRIPTS.name + suffix)
  TASKS[f'link_script_{suffix}'] = {
    'args': [GIT / script, HOME / script],
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
