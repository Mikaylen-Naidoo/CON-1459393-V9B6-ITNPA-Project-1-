# CON-1459393-V9B6 ITNPA Project 1: Researchly Research Analytics

Mikaylen Naidoo

This project builds a text mining system for research documents.

- **Q1:** Data loading, text denoising, feature engineering and a baseline classifier
- **Q2:** Model comparison, performance enhancement and a Streamlit web app
- **Q3:** Summarisation of research articles (TextRank and TF-IDF)
- **Q4:** LDA topic modelling with an interactive pyLDAvis map

## Repository contents

| Folder or file | Contents |
|---|---|
| `Project_Documentation.pdf` | Project documentation (Questions 1 to 4) |
| `Datasets/` | research_abstracts.json and research_1.txt to research_5.txt |
| `CODE and OUTPUTS/` | Notebooks showing the flow of analytics for Questions 1 to 4, with outputs |
| `deployment/` | Streamlit web app, model, requirements and deployment README |

## Key results

- Best classifier: Random Forest with TF-IDF features (test accuracy 0.907, F1 0.759)
- LDA found 4 topics: reliability and Cronbach's alpha, triangulation, mixed methods, and developmental research

## How to run

1. Open the notebooks in Jupyter and run each from top to bottom.
2. To run the web app, follow the steps in `deployment/README.md`.
