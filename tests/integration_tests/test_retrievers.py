from typing import Type

from langchain_tests.integration_tests import (
    RetrieversIntegrationTests,
)

from langchain_dappier.retrievers import DappierRetriever


class TestDappierRetriever(RetrieversIntegrationTests):
    @property
    def retriever_constructor(self) -> Type[DappierRetriever]:
        """Get an empty vectorstore for unit tests."""
        return DappierRetriever

    @property
    def retriever_constructor_params(self) -> dict:
        return {"data_model_id": "dm_01jagy9nqaeer9hxx8z1sk1jx6"}

    @property
    def retriever_query_example(self) -> str:
        """
        Returns a dictionary representing the "args" of an example retriever call.
        """
        return "latest tech news"
