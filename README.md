# DataSensei: Your Data Science Q&A System

Welcome to **DataSensei**, the intelligent Q&A system designed to provide answers to all your data science questions. Trained on comprehensive data science books, DataSensei offers precise and insightful responses to enhance your data science learning and research.


## Introduction

DataSensei is an advanced question-answering RAG system tailored for the data science community. Whether you are a beginner or an expert, DataSensei helps you find answers to your data science queries quickly and efficiently.

## Features

- **Comprehensive Knowledge**: Uses number of data science books to retrieve information.
- **Vector Database**: Utilizes Chroma vector database for efficient information retrieval based on semantic similarity.
- **Accurate Responses**: Provides precise answers to your data science questions.
- **User-Friendly Interface**: Easy to interact with and get the information you need.

## Screenshot

Here’s a preview of DataSensei:

![data_sensei](https://github.com/Abhidyum/rag_datasensei/assets/94860032/a10be58f-a32e-4240-9a6d-836c033e6ebb)


## Installation

To set up DataSensei on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abhidyum/rag_datasensei.git
    cd rag_datasensei
    ```
   
2. **Download the quantized Llama 2 model**:
    Download `llama-2-7b-chat.ggmlv3.q4_0.bin` from the following link: [Llama 2 Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)
    
    Place the downloaded model file in the `model` directory of your project.





3. **Install the necessary dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

## Usage

Once the application is running, you can start asking your data science questions directly through the interface. Here’s a simple example:

1. **Start the application**:
    ```bash
    python app.py
    ```

2. **Ask a question**:
    Enter your data science question in the input field and press enter or press "Ask" button.
    
    Example:
    ```
    What is the difference between supervised and unsupervised learning?
    ```

3. **Receive an answer**:
    DataSensei will process your question and provide a detailed answer.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to us:

- **Email**: tyagiabhidyum@gmail.com
- **GitHub**: [abhidyum](https://github.com/abhidyum)
