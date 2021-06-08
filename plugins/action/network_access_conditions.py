from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from urllib.parse import quote
from ansible_collections.cisco.ise.plugins.module_utils.ise import (
    ISESDK,
    ise_argument_spec,
)

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present", "absent"]),
    conditionType=dict(type="str"),
    isNegate=dict(type="bool"),
    name=dict(type="str"),
    id=dict(type="str"),
    description=dict(type="str"),
    dictionaryName=dict(type="str"),
    attributeName=dict(type="str"),
    attributeId=dict(type="str"),
    operator=dict(type="str"),
    dictionaryValue=dict(type="str"),
    attributeValue=dict(type="str"),
    children=dict(type="list"),
    hoursRange=dict(type="dict"),
    hoursRangeException=dict(type="dict"),
    weekDays=dict(type="list"),
    weekDaysException=dict(type="list"),
    datesRange=dict(type="dict"),
    datesRangeException=dict(type="dict"),
))

required_if = [
    ("state", "present", ["id", "name"], True),
    ("state", "absent", ["id", "name"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NetworkAccessConditions(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            condition_type=params.get("conditionType"),
            is_negate=params.get("isNegate"),
            name=params.get("name"),
            id=params.get("id"),
            description=params.get("description"),
            dictionary_name=params.get("dictionaryName"),
            attribute_name=params.get("attributeName"),
            attribute_id=params.get("attributeId"),
            operator=params.get("operator"),
            dictionary_value=params.get("dictionaryValue"),
            attribute_value=params.get("attributeValue"),
            children=params.get("children"),
            hours_range=params.get("hoursRange"),
            hours_range_exception=params.get("hoursRangeException"),
            week_days=params.get("weekDays"),
            week_days_exception=params.get("weekDaysException"),
            dates_range=params.get("datesRange"),
            dates_range_exception=params.get("datesRangeException"),
        )

    def get_object_by_name(self, name):
        try:
            result = self.ise.exec(
                family="network_access_conditions",
                function="get_network_access_condition_by_name",
                params={"name": quote(name)}
            ).response
        except Exception as e:
            result = None
        return result

    def get_object_by_id(self, id):
        try:
            result = self.ise.exec(
                family="network_access_conditions",
                function="get_network_access_condition_by_id",
                params={"id": quote(id)}
            ).response
        except Exception as e:
            result = None
        return result

    def exists(self):
        result = False
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        if id:
            if self.get_object_by_id(id):
                result = True
        elif name:
            if self.get_object_by_name(name):
                result = True
        return result

    def create(self):
        result = self.ise.exec(
            family="network_access_conditions",
            function="create_network_access_condition",
            params=self.new_object,
        ).response
        return result

    def update(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if id:
            result = self.ise.exec(
                family="network_access_conditions",
                function="update_network_access_condition_by_id",
                params=self.new_object
            ).response
        elif name:
            result = self.ise.exec(
                family="network_access_conditions",
                function="update_network_access_condition_by_name",
                params=self.new_object
            ).response
        return result

    def delete(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if id:
            result = self.ise.exec(
                family="network_access_conditions",
                function="delete_network_access_condition_by_id",
                params=self.new_object
            ).response
        elif name:
            result = self.ise.exec(
                family="network_access_conditions",
                function="delete_network_access_condition_by_name",
                params=self.new_object
            ).response
        return result


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        ise = ISESDK(self._task.args)
        obj = NetworkAccessConditions(self._task.args, ise)

        state = self._task.args.get("state")

        response = None

        if state == "present":
            if obj.exists():
                response = obj.update()
                ise.object_updated()
            else:
                response = obj.create()
                ise.object_created()

        elif state == "absent":
            if obj.exists():
                response = obj.delete()
                ise.object_deleted()
            else:
                ise.object_already_absent()

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result