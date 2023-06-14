def map_format(l, fmt):
  """
  Map string formatting onto a list
  """

  return [fmt.format(x) for x in l]


class FilterModule:

  def filters(self):

    return {k: v for (k, v) in globals().items() if type(v) != type}
