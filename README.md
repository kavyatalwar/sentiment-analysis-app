# 🔮 AI-Driven Sentiment Analysis Application

A live, production-ready web application that leverages state-of-the-art Natural Language Processing (NLP) to evaluate textual sentiment in real time. Built with a focus on high accuracy and low latency, this application serves as the foundation for an advanced business intelligence pipeline.

🌐 **[Live Application Link](https://sentiment-analysis-kavya.streamlit.app/)**

---

## 🚀 Project Overview

This application serves as a clean, intuitive interface for real-time emotional analysis of text. Unlike traditional rule-based sentiment analyzers (such as VADER), this project implements a deep-learning-based transformer architecture capable of decoding linguistic nuances, context shifts, and sarcasm.

### Key Features
* **Context-Aware NLP Engine:** Utilizes a pre-trained RoBERTa model optimized for short and medium-form social/consumer text.
* **Intuitive UI:** Minimalist, user-friendly interface featuring dynamic, color-coded visual feedback based on sentiment classification (+ / - / Neutral).
* **Production Deployment:** Fully containerized and deployed via Streamlit Community Cloud with robust edge-case handling for empty or invalid inputs.

---

## 🛠️ Tech Stack & Architecture

* **Frontend & UI:** Streamlit (Python-based web framework)
* **Machine Learning Framework:** Hugging Face Transformers & PyTorch
* **Core Model:** `cardiffnlp/twitter-roberta-base-sentiment-latest`

---

## 🚧 The Roadmap: This is Just the Beginning

While this interface flawlessly handles single-string manual inputs, **this deployment marks Phase 1 of a significantly larger, data-driven vision.** I am currently developing an extensive upgrade to transform this standalone utility into a **Multi-Dashboard Customer Insights & Product Analytics Platform**.

### Phase 2 Development Pipeline (In Progress):
* **Automated Batch Processing (ETL):** Designing a backend data pipeline using Pandas to ingest large-scale datasets (e.g., thousands of e-commerce product reviews or customer support logs).
* **Data Aggregation & Augmentation:** Appending granular sentiment scores dynamically as relational columns to track brand health metrics over time.
* **Executive BI Dashboards:** Replacing the single-input view with an interactive analytics suite featuring time-series trends, categorical breakdown charts, and cross-filtering mechanisms designed for corporate stakeholders.

---

## 📦 Local Installation & Setup

To run this project locally, ensure you have Python 3.12+ installed, then follow these steps:

1. Clone the repository:
```bash
git clone [https://github.com/kavyatalwar/sentiment-analysis-app.git](https://github.com/kavyatalwar/sentiment-analysis-app.git)
cd sentiment-analysis-app
```

2. Install dependencies:
```Bash
pip install -r requirements.txt
```

3. Launch the Streamlit application:
```Bash
streamlit run app.py
```
