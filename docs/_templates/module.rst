{{ name | escape | underline }}

.. currentmodule:: {{ module }}
{% if name == 'ConfigLoader' %}
.. autoclass:: {{ fullname | escape }}
  :exclude-members: order
  :members:

  .. autoattribute:: order
    :no-value:
{% elif name == 'ConfigEnvVarLoader' %}
.. autoclass:: {{ fullname | escape }}
  :exclude-members: order
  :members:
  :show-inheritance:

  .. attribute:: order
    :type: int
    :value: -∞
{% else %}
.. autoclass:: {{ fullname | escape }}
  :show-inheritance:
  :members:
{% endif %}

