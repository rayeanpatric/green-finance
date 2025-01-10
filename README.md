# Green Finance Optimization Platform

## Project Overview
The **Green Finance Optimization Platform** is designed to enhance Environmental, Social, and Governance (ESG) investment strategies. This platform focuses on **risk assessment** and **investment prediction management** by integrating machine learning models with financial and ESG-related data. The goal is to support sustainable investment decisions, minimize risks, and maximize returns.

---

## Model Used

- **FinBERT-ESG**: A transformer-based model fine-tuned for ESG-related text classification. It helps in calculating ESG scores from project reports.
  - **Model Link**: [FinBERT-ESG on Hugging Face](https://huggingface.co/yiyanghkust/finbert-esg)

- **Llama-3.2-1B-Instruct-IQ3_M**: A transformer-based model utilized for answering specific questions and extracting insights from text data.
  - **Model Path**: [Llama-3.2-1B-Instruct-IQ3_M.gguf](https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF/blob/main/Llama-3.2-1B-Instruct-IQ3_M.gguf)

---

## Project Flow

### 1. Data Collection and Preprocessing
- **Input Sources**:
  - PDF project reports containing financial and ESG data.
  - Extracted textual data from PDF images using OCR.
- **Preprocessing**:
  - Converted PDF pages to images using PyMuPDF.
  - Extracted text from images using Tesseract OCR.

### 2. ESG Score Calculation
- **Model**: FinBERT-ESG
- **Process**:
  - The text extracted from project reports is fed into the FinBERT-ESG pipeline.
  - Outputs include the ESG category and its confidence score.

### 3. Question-Answering System
- **Model**: Llama-3.2-1B-Instruct-IQ3_M
- **Process**:
  - Questions related to project details (e.g., investment amount, project location) are answered using context from the extracted text.

### 4. ROI Calculation
- **Inputs**:
  - ESG category, ESG score, project type, and risk status.
- **Logic**:
  - Base ROI is determined by project type and ESG category.
  - Adjustments are applied based on risk status and ESG score contribution.

### 5. Machine Learning-Based Prediction
- **Model**: Random Forest Regressor
- **Process**:
  - Predicts ROI using preprocessed features from project data.
  - Evaluates model performance using Mean Squared Error (MSE) and R² score.

---

## Backend Overview

### Frameworks and Tools
- **Python**: Core programming language for data preprocessing and modeling.
- **PyMuPDF**: For converting PDF pages into images.
- **Pytesseract**: For extracting text from images.
- **Transformers**: For FinBERT-ESG model integration.
- **Pandas and NumPy**: For data manipulation and analysis.
- **Scikit-learn**: For building and evaluating machine learning models.

### Backend Flow
1. **Data Extraction**:
   - Convert PDF files to images and extract text.
   - **Future Improvement**: Replace Tesseract OCR with LayoutLMv3 for improved accuracy in extracting structured data from documents.
2. **ESG Score Calculation**:
   - Use FinBERT-ESG to determine ESG category and score.
3. **Question-Answering**:
   - Use Llama model to extract project-specific details.
   - **Future Improvement**: Fine-tune Llama with Reinforcement Learning from Human Feedback (RLHF) for domain-specific insights.
4. **ROI Prediction**:
   - Calculate ROI dynamically based on extracted data.
5. **Data Storage**:
   - Save processed data and predictions to CSV files.

---

## Frontend Overview

### Frameworks and Tools
- **React.js**: For building the user interface.
- **Chart.js**: For rendering interactive data visualizations.
- **Material-UI**: To style components and maintain a clean design.

### Features
- **Investment Insights**:
  - View predicted ROI and risk scores for potential investments.
  - Drill-down analysis of ESG factors influencing decisions.
- **ESG Trends**:
  - Real-time updates on sector-specific ESG scores.
  - Correlation between ESG performance and financial success.
- **User-Friendly Interface**:
  - Interactive filters for risk tolerance and ROI preferences.

---

## Deployment

### Steps
1. **Backend Deployment**:
   - Deploy the Python backend on a cloud server (e.g., AWS or Azure).
   - Set up a database (e.g., PostgreSQL) for storing financial and ESG data.
2. **Frontend Deployment**:
   - Host the React.js application on a static site hosting service like Netlify or Vercel.
3. **Model Hosting**:
   - Use Hugging Face Inference API for running the FinBERT-ESG model.
   - Host the Llama model locally or on a dedicated GPU server.
4. **Integration**:
   - Connect backend APIs with the frontend interface.
   - Test the end-to-end functionality.

---

## Future Improvements
- **Incorporate Real-Time Data Streams**: Include real-time ESG updates from news and social media.
- **AI-Driven Recommendations**: Add a feature to suggest investment portfolios based on user preferences.
- **Blockchain for Transparency**: Use blockchain to track and verify ESG compliance for investments.
- **Advanced OCR and NLP Models**: Replace Tesseract OCR with LayoutLMv3 for structured data extraction and improve textual insights.
- **Enhanced QA System**: Fine-tune Llama with RLHF to enhance its ability to answer domain-specific queries.

---

## Conclusion
The **Green Finance Optimization Platform** empowers investors to make sustainable, data-driven decisions. By leveraging advanced machine learning models, the platform provides actionable insights that balance profitability with ethical responsibility.
