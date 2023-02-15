from langchain.docstore.document import Document
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain

from fastapi import Form, File, UploadFile

from pypdf import PdfReader

async def POST(document: UploadFile = File()):
    print('WHAT')
    print('COOL')

    pdf_reader = PdfReader(document.file)
    docs = []
    for i, page in enumerate(pdf_reader.pages):
        text = page.extract_text()
        metadata = {"source": document.filename, "page": i}
        docs.append(Document(page_content=text, metadata=metadata))

    llm = OpenAI(temperature=0)

    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)

    return {
        "file_size": len(document.file.read()),
        "summary": f"{summary}<br/><br/>Your welcome!",
    }
