import pytest
from langchain.chains import ConversationalRetrievalChain
from langchain.indexes.vectorstore import VectorStoreIndexWrapper

from features.module import create_indexing_dir_data, create_retrieval_chain


def test_create_indexing_dir_data():
    actual = type(create_indexing_dir_data("tests/test_data/"))
    assert actual == VectorStoreIndexWrapper


def test_create_retrieval_chain():
    index = create_indexing_dir_data("tests/test_data/")
    actual = type(create_retrieval_chain(index))

    assert actual == ConversationalRetrievalChain
