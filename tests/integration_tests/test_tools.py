from typing import Type

from langchain_dappier.tools import DappierRealTimeSearchTool
from langchain_tests.integration_tests import ToolsIntegrationTests


class TestDappierTool(ToolsIntegrationTests):
    @property
    def tool_constructor(self) -> Type[DappierRealTimeSearchTool]:
        return DappierRealTimeSearchTool

    @property
    def tool_constructor_params(self) -> dict:
        # if your tool constructor instead required initialization arguments like
        # `def __init__(self, some_arg: int):`, you would return those here
        # as a dictionary, e.g.: `return {'some_arg': 42}`
        return {"ai_model_id": "am_01j06ytn18ejftedz6dyhz2b15"}

    @property
    def tool_invoke_params_example(self) -> dict:
        """
        Returns a dictionary representing the "args" of an example tool call.

        This should NOT be a ToolCall dict - i.e. it should not
        have {"name", "id", "args"} keys.
        """
        return {"query": "who won the last french open"}
