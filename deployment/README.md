# Researchly Abstract Classifier: Deployment

A Streamlit web app that classifies a research abstract as artificial intelligence or classical research. It uses the best model from Questions 1 and 2 (Random Forest with TF-IDF features, test accuracy 0.907, F1 0.759).

## Requirements
- Python 3.9 or newer

## Steps
1. Download this `deployment` folder to your computer.
2. Open a terminal (Anaconda Prompt on Windows) and go to the folder:
   cd "path\to\deployment"
3. Install the libraries:
   pip install -r requirements.txt
4. Start the app:
   streamlit run app.py
5. If asked for an email address, press Enter to skip it.
6. Open http://localhost:8501 in your browser, paste an abstract and click "Classify Abstract".

## Notes
- app.py and best_model.joblib must stay in the same folder.
- To stop the app, press Ctrl + C in the terminal.
- Example abstract and expected result are shown in the screenshots in the outputs folder.
