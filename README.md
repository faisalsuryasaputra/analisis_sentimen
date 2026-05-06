# 📊 Ruangguru App Review Sentiment Analysis using Deep Learning

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15+-orange)
![Deep Learning](https://img.shields.io/badge/Model-LSTM%20%26%20GRU-success)

## 📌 Project Description
This project is a Natural Language Processing (NLP) implementation designed to analyze user sentiment from reviews of the Indonesian EdTech platform, Ruangguru, on the Google Play Store. It aims to extract insights regarding User Experience (UX) to better understand students' pain points and satisfaction levels when using the digital learning application.

The Deep Learning model developed in this project successfully categorizes review text into three sentiment classes: **Positive, Neutral, and Negative**.

## ✨ Key Features
- **Independent Data Scraping:** Collected over 10,000 real user reviews directly from the Google Play Store using the `google-play-scraper` library.
- **Imbalanced Data Handling:** Utilized an Oversampling technique (RandomOverSampler) to ensure a balanced sentiment class distribution prior to model training.
- **Multi-Scheme Architecture Experiments:** Conducted 3 different training schemes to compare and evaluate model performance:
  1. **Scheme 1:** LSTM (Train/Test Split 80:20)
  2. **Scheme 2:** GRU (Train/Test Split 80:20)
  3. **Scheme 3:** LSTM (Train/Test Split 90:10)
- **High Accuracy:** Achieved a testing accuracy of over **96%** using the LSTM architecture, optimized with a `Dropout` layer and sequence *pre-padding* technique.

## 🛠️ Technologies Used
- **Programming Language:** Python
- **Model Framework:** TensorFlow / Keras
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning Utilities:** Scikit-Learn, Imbalanced-Learn
- **Scraping Tool:** Google Play Scraper

## 📂 Repository Structure
```text
├── dataset_ruangguru.csv              # Scraped review dataset (>10,000 rows)
├── scraping_ruangguru.py              # Python script to extract data from Play Store
├── Proyek_Analisis_Sentimen_Ruangguru.ipynb  # Main notebook containing preprocessing, training, & evaluation
├── requirements.txt                   # List of library dependencies to run the project
└── README.md                          # Project documentation

```
🚀 How to Run Locally
Clone this repository

Bash
git clone [https://github.com/faisalsuryasaputra/analisis-sentimen-ruangguru.git](https://github.com/faisalsuryasaputra/analisis-sentimen-ruangguru.git)
cd analisis-sentimen-ruangguru
Create a Virtual Environment (Optional but recommended)

Bash
python -m venv env
source env/bin/activate  # For Mac/Linux
# env\Scripts\activate   # For Windows


3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
Run the Scraping Script (If you want to fetch the latest data)

Bash
python scraping_ruangguru.py
Open the Model Training Notebook
Run Jupyter Notebook or upload the .ipynb file to Google Colab (highly recommended to use T4 GPU acceleration) to view the training process and inference interactively.

📈 Evaluation Results
The model was evaluated using the Accuracy metric. The best performing model was the LSTM architecture in Scheme 1 with an 80/20 data split ratio, which yielded:

Testing Accuracy: 96.67%

The model successfully and accurately predicted new inference text (e.g., distinguishing technical complaints like "force close" as Negative sentiment, and praise for learning features as Positive sentiment).

👤 Author
Faisal Surya Saputra
