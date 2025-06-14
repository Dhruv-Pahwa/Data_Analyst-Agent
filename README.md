# 📊 Data Analyst Agent

An intelligent agent powered by **LLaMA-4** (via [Together.ai](https://www.together.ai)) that allows users to upload documents and datasets, analyze them, generate insights, and create visualizations — all through natural language interaction.

---

## 🚀 Overview

The Data Analyst Agent enables:

- ✅ Uploading files (`.csv`, `.xlsx`, `.txt`, `.pdf`, images)
- ✅ Extracting and preprocessing data
- ✅ Generating summary and insights using **LLaMA-4**
- ✅ Creating data visualizations like histograms and correlation heatmaps
- ✅ Answering questions and follow-ups about the data

Built primarily for backend usage, the system can optionally be integrated with a UI (**Streamlit** or **Gradio**).

---

## 💡 Core Technologies

- **Python**
- **Together.ai API** (LLaMA-4 Maverick 17B)
- **pandas, matplotlib, seaborn** (data handling & visualization)
- **PyMuPDF (fitz)** for PDF reading
- **Pillow** for image processing
- **OpenPyXL** for Excel

---

## 📂 Supported File Types

| Format         | Description       |
|----------------|-------------------|
| `.csv`         | Tabular data      |
| `.xlsx`        | Excel sheets      |
| `.txt`         | Plain text        |
| `.pdf`         | Document analysis |
| `.png`, `.jpg` | Images (optional) |

---

## 📦 Installation

### Option 1: Clone and Install

```bash
git clone https://github.com/your-username/data-analyst-agent.git
cd data-analyst-agent
pip install -r requirements.txt
## 🔑 Setup

1. Create an account on [Together.ai](https://www.together.ai)
2. Retrieve your API key from the dashboard.
3. Replace the `TOGETHER_API_KEY` in your code:

```python
TOGETHER_API_KEY = "your_actual_api_key"
