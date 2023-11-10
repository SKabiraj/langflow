from typing import Optional

from langflow.interface.custom.constants import DEFAULT_CUSTOM_COMPONENT_CODE
from langflow.template.field.base import TemplateField
from langflow.template.frontend_node.base import FrontendNode
from langflow.template.template.base import Template


class CustomComponentFrontendNode(FrontendNode):
    name: str = "CustomComponent"
    display_name: str = "Custom Component"
    beta: bool = True
    template: Template = Template(
        type_name="CustomComponent",
        fields=[
            TemplateField(
                field_type="code",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                value=DEFAULT_CUSTOM_COMPONENT_CODE,
                name="code",
                advanced=False,
                dynamic=True,
            )
        ],
    )
    description: Optional[str] = None
    base_classes: list[str] = []
