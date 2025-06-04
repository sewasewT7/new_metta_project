import os
import csv
from datetime import datetime
import requests
from dotenv import load_dotenv
from hyperon.atoms import OperationAtom, S
from hyperon.ext import register_atoms

# Load .env variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables.")

# File paths
csv_path = "gene_summary.csv"
metta_path = "gene_summary.metta"

# Ensure headers exist
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Summary"])

with open(metta_path, 'w') as f:
    f.write(f"; Summary generated on {datetime.now()}\n")

# Function to call LLM
def gene_summarizer(gene_id, gene_data):
    prompt = f"You are an expert biological data summarizer. Here is a structured gene data: {gene_data}. Summarize the data in 2 sentences."
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "meta-llama/llama-3.1-8b-instruct:free",
            "messages": [
                {"role": "system", "content": "You are a biology expert tasked with summarizing gene information."},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        summary = response.json()["choices"][0]["message"]["content"].strip()

        # Write to CSV
        with open(csv_path, 'a', newline='') as f:
            # writer = csv.writer(f)
            # writer.writerow([gene_id, summary])

            csv.writer(f).writerow([gene_id, summary])
            # print(f"Wrote to CSV: {gene_id}, {summary}")  # Debug

        # Append to .metta file
        with open(metta_path, 'a') as f:
            f.write(f'(gene_summary (gene {gene_id}) "{summary}")\n')

        return [S(summary)]
    except Exception as e:
        return [S(f"Error: {str(e)}")]

# Register to Hyperon
@register_atoms(pass_metta=True)
def utils(metta):
    summaryGene = OperationAtom(
        "gene_summarizer",
        lambda gene_id, gene_text: gene_summarizer(gene_id, gene_text),
        ["Atom","Expression","Expression"],
        unwrap=False
    )
    return {r"gene_summarizer": summaryGene}
