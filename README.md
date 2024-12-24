# langchain-dappier

This package contains the LangChain integration with Dappier

## Installation

```bash
pip install -U langchain-dappier
```

And you should configure credentials by setting the following environment variables:

## Retrievers

`DappierRetriever` class exposes chat models from Dappier.

```python
from langchain-dappier import DappierRetriever

retriever = DappierRetriever(
    data_model_id="dm_01jagy9nqaeer9hxx8z1sk1jx6"
)

query = "latest tech news"

retriever.invoke(query)
```
