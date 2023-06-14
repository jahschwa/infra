# vim: filetype=xonsh

import sys
import warnings


def main():

  def disable_warnings():

    if _version() == '3.6.10':
      warnings.filterwarnings(
        'ignore',
        category=DeprecationWarning,
        module='prompt_toolkit.application.application',
        message='There is no current event loop',
      )

  def path():

    $PATH.add(p'~/bin', front=True, replace=True)

  def _version():

    return '.'.join(
      map(
        str,
        (getattr(sys.version_info, name) for name in ('major', 'minor', 'micro')),
      )
    )

  for (name, func) in sorted(locals().items()):
    if not name.startswith('_') and name[0].islower():
      func()


main()
del main
