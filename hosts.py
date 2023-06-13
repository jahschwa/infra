#!/usr/bin/env python3

from argparse import ArgumentParser
from collections import defaultdict
import json
import socket


GROUPS = {
  'home': ['area11', 'osmc', 'shinkiro', 'sibylpad'],
}


def main(host, list_all):

  groups = {}
  all_hosts = set()
  for (group, hosts) in GROUPS.items():
    groups[group] = sorted(hosts)
    all_hosts.update(hosts)

  groups['all'] = {'children': ['ungrouped'] + list(groups)}

  groups['_meta'] = {'hostvars': {}}
  for host in all_hosts:
    config = groups['_meta']['hostvars'].setdefault(host, {})
    if host == socket.gethostname():
      config['ansible_connection'] = 'local'

  print(json.dumps(groups, indent=4, sort_keys=True))


def get_args():

  ap = ArgumentParser()
  add = ap.add_argument

  add('--host')
  add('--list', action='store_true', dest='list_all')

  return ap.parse_args()


if __name__ == '__main__':
  main(**vars(get_args()))
