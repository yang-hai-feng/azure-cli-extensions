# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExperimentUpdateModel(Model):
    """Defines modifiable attributes of an Experiment.

    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param description: The description of the intent or details of the
     Experiment
    :type description: str
    :param enabled_state: The state of the Experiment. Possible values
     include: 'Enabled', 'Disabled'
    :type enabled_state: str or ~azure.mgmt.frontdoor.models.State
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'enabled_state': {'key': 'properties.enabledState', 'type': 'str'},
    }

    def __init__(self, *, tags=None, description: str=None, enabled_state=None, **kwargs) -> None:
        super(ExperimentUpdateModel, self).__init__(**kwargs)
        self.tags = tags
        self.description = description
        self.enabled_state = enabled_state
