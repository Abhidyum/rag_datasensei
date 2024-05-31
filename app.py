from flask import Flask, request, render_template
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import CTransformers
from utils import load_pdf, text_split, setup_vector_store, load_vector_store, vector_store_exists

app = Flask(__name__)

data_directory = 'data'  # Directory where your PDFs are stored
persist_directory = 'dbase'  # Directory for vector database storage

# Check if the vector store already exists; if not, create it
if vector_store_exists(persist_directory):
    vectordb = load_vector_store(persist_directory)
else:
    extracted_data = load_pdf(data_directory)
    text_chunks = text_split(extracted_data)
    vectordb = setup_vector_store(text_chunks, persist_directory)

retriever = vectordb.as_retriever(search_kwargs={'k': 1})

prompt_template = """
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Give answer within the limit of 300 words.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}

llm = CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin", model_type="llama", config={'max_new_tokens': 512, 'temperature': 0.8})
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True, chain_type_kwargs=chain_type_kwargs)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        result = qa({"query": query})
        answer = result.get('result', 'No answer found.')
    else:
        answer = None
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


