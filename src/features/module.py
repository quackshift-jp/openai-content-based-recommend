import os

import openai
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper

load_dotenv(verbose=True)

openai.api_key = os.environ.get("OPENAI_API_KEY")
CHAT_HISTORY = []


def create_indexing_dir_data(dir_path: str) -> VectorStoreIndexWrapper:
    """Load documents and indexing.
    args:
        dir_path (str): directory path of documents.
    return:
        index (VectorStoreIndexWrapper): index of documents.
    """
    loader = DirectoryLoader(dir_path)
    return VectorstoreIndexCreator().from_loaders([loader])


def create_retrieval_chain(
    index: VectorStoreIndexWrapper,
) -> ConversationalRetrievalChain:
    return ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(),
    )


def extract_answer_image_path_from_question(
    retrieval_chain: ConversationalRetrievalChain,
    season: str,
    fashion_color: str,
    genre: str,
    scene: str,
    height: str,
    hair_color: str,
    hair_style: str,
    question: str,
    chat_history: list = CHAT_HISTORY,
) -> str:
    query = f"""
    あなたは、プロのアパレル店員です。
    {hair_color}の男性に、{season}に着る服装を選択して、imageリンクのみを返答してほしい。
    良い服装がない場合は、最も近い服装のimageリンクを返答してほしい。
    客は、{fashion_color}の{genre}な服装を好む傾向にある。
    着用シーンは、{scene}で、{height}向けで、髪型は{hair_style}です。
    男性からの意見として「{question}」という要望をもらっている。
    回答方法としては、imageリンクのみを返答して、他の情報は不要です。

    回答フォーマット：
    imageリンク
    回答例：
    https://drive.google.com/file/d/xxxx/view?usp=drive_link

    """
    response = retrieval_chain({"question": query, "chat_history": chat_history})
    chat_history.append((question, response["answer"]))
    print(chat_history)
    return response["answer"]


if __name__ == "__main__":
    index = create_indexing_dir_data("../images/")
    retrieval_chain = create_retrieval_chain(index)
    print(
        extract_answer_image_path_from_question(
            retrieval_chain,
            "夏",
            "ブラック",
            "シティ系",
            "デート",
            "全ての身長",
            "金髪",
            "ショート",
            "デートプランとして、水族館にも行く。",
        )
    )
