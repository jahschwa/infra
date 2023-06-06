# vim: filetype=xonsh

import sys
import warnings


def main():

  def silence_prompt_toolkit():
  
    if _version() != '3.6.10':
      return

    warnings.filterwarnings(
      'ignore',
      category=DeprecationWarning,
      module='prompt_toolkit.application.application',
      message='There is no current event loop',
    )
  
  def _version():
  
    return '.'.join(
      map(
        str,
        (getattr(sys.version_info, name) for name in ('major', 'minor', 'micro')),
      )
    )

  for (name, func) in sorted(locals().items()):
    if not name.startswith('_'):
      func()


main()
del main
