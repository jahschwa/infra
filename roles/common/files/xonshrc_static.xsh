# vim: filetype=xonsh

import sys
import warnings


def main():

  def disable_warnings():

    # https://github.com/xonsh/xonsh/issues/4513#issuecomment-1522724843
    if _version() == '3.6.10':
      warnings.filterwarnings(
        'ignore',
        category=DeprecationWarning,
        module='prompt_toolkit.application.application',
        message='There is no current event loop',
      )

  def env():

    # https://github.com/jan-warchol/selenized/tree/master/other-apps/dircolors
    $LS_COLORS.update({
      'ow': ('BOLD_INVERT_BLUE',),
      'st': ('BLACK', 'BACKGROUND_BLUE'),
      'su': ('BACKGROUND_RED',),
    })

  def path():

    $PATH.add(p'~/bin', front=True, replace=True)

  def ssh():

    if not !(ssh-add -L > /dev/null):
      ssh-add

  def style():

    from xonsh.tools import register_custom_style

    config = {
      'PTK.CompletionMenu': 'bg:ansimagenta ansiblack',
      'PTK.CompletionMenu.Completion.Current': 'bg:ansiblack ansimagenta',
    }

    register_custom_style('jah', config, base='default')
    $XONSH_COLOR_STYLE = 'jah'

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
