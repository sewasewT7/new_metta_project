# 🧬 Gene Summary Generator using LLMs and MeTTa

This project uses a Large Language Model (LLM) to generate concise summaries of gene information extracted from structured biological data. It integrates the OpenRouter API, Hyperon, and MeTTa language to enable semantic querying, summarization, and structured reasoning.

## 🚀 Features
- **🔬 Gene Data Summarization**: Using Meta LLaMA-3 via OpenRouter API
- **📁 CSV Export**: Stores each gene's summary alongside its ID
- **🧠 MeTTa Knowledge Base**: Automatically appends summaries into a .metta file for symbolic reasoning
- **🛠️ Hyperon Atom Registration**: Registers custom summarization logic as MeTTa atoms

## 📂 Project Structure

new_MeTTa_project/
├── gene_summary.csv # Stores gene ID and their summaries
├── gene_summary.metta # Contains summaries in MeTTa format
├── llm_summary.py # Main script integrating API and Hyperon atoms
├── .env # Your secret API key for OpenRouter
└── README.md # Project documentation

## 🧪 Requirements
- Python 3.8+
- Hyperon Python bindings
- .env file with OpenRouter API key
- requests, python-dotenv, and hyperon packages

Install requirements:
```bash
pip install requests python-dotenv hyperon
```
🔐 Environment Setup
Create a .env file in the root directory with the following:
OPENROUTER_API_KEY=your_api_key_here
⚙️ How It Works
Extracts structured gene data using MeTTa patterns

Sends the gene data to the LLM via the OpenRouter API

Receives and logs the LLM's 2-sentence summary

Saves outputs in:

gene_summary.csv (tabular format)

gene_summary.metta (MeTTa-compatible structure)

Example .metta output:

metta

(gene_summary (gene ENSG00000128245) "The gene ENSG00000128245 encodes for the YWHAH protein...")

📤 Output Example
CSV:

csv:
ID,Summary
ENSG00000175793,"The gene ENSG00000175793 encodes the protein SFN, also known as stratifin..."
MeTTa:

metta

(gene_summary (gene ENSG00000175793) "The gene ENSG00000175793 encodes the protein SFN...")
📄 License
MIT License. See LICENSE file.

📚 References & Resources
🔗 https://github.com/iCog-Labs-Dev/metta-attention/blob/dev/experiments/utils/logger.py

🔗 https://metta-lang.dev/docs/learn/learn.html

🔗https://github.com/iCog-Labs-Dev/metta-attention/blob/dev/experiments/logger.metta

🔗 Meta AI: LLaMA 3

