# 🤖 ML Regression Project

## 📚 Overview
This project demonstrates the use of a regression algorithm to predict outcomes based on a dataset. The trained model is served via a Flask API, and a simple frontend allows users to input data and view predictions.

The dataset used in this project is from the **UCI Machine Learning Repository** and contains energy efficiency data for buildings. The goal is to predict **heating load (y1)** and **cooling load (y2)** based on several building features.

---

## 📝 **Key Features**
- Regression Model (e.g., Linear Regression, Decision Tree)  
- Flask API serving model predictions  
- Frontend interface for user interaction  
- Model evaluation and performance metrics

---

## 🔎 **Dataset**
The dataset used in this project is from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/242/energy+efficiency). 
It contains eight attributes (features, denoted as X1 to X8) and two responses (outcomes, denoted as y1 and y2).

**Features:**
- **X1**: Relative Compactness  
- **X2**: Surface Area  
- **X3**: Wall Area  
- **X4**: Roof Area  
- **X5**: Overall Height  
- **X6**: Orientation  
- **X7**: Glazing Area  
- **X8**: Glazing Area Distribution

**Responses:**
- **y1**: Heating Load  
- **y2**: Cooling Load

The aim of the project is to use the eight features to predict **heating load** and **cooling load**.

---

## 🚀 **How to Run**

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/ml-regression-project.git
   cd ml-regression-project
