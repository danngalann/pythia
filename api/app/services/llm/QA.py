from typing import List

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.schema import Document


class QA:
    def __init__(self):
        self.chain = load_qa_chain(OpenAI(model_name="text-ada-001"), chain_type="stuff")

    def answer(self, question: str, context: List[Document]) -> str:
        return self.chain.run(question=question, input_documents=context)
