# RAG-using-langchain 🔗

**This project aims to implement RAG using LangChain which uses OpenAI API key and Chroma for VectorDB. Using this technique we can build interactive AI applications with personal/enterprise data**

## Install dependencies

1. Do the following before installing the dependencies found in `requirements.txt` file because of current challenges installing `onnxruntime` through `pip install onnxruntime`. 

    ```python
     conda install onnxruntime -c conda-forge
    ```
  
2. Now run this command to install dependenies in the `requirements.txt` file. 

```python
pip install -r requirements.txt
```

3. Install markdown depenendies with: 

```python
pip install "unstructured[md]"
```

## Create database

Create the Chroma DB.

```python
python Create_VectorDB.py
```

## Query the database

Query the Chroma DB.

```python
python Search_Data.py "How does Alice related to Mad Hatter?"
```
