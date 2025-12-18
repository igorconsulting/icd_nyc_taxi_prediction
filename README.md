<div align="center">
  <h1>NYC Taxi Demand Prediction and Monitoring System</h1>
  <i>A Research-Grade Machine Learning Pipeline for Automated Feature Engineering, Model Training, Inference, and Monitoring</i>
</div>

---

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://icd-nyc-taxi-prediction.streamlit.app/)

## **1. Overview**

This repository implements an end-to-end machine learning system designed to forecast taxi demand in New York City using temporal and geospatial information. The system automates:

* ingestion and transformation of historical trip data,
* construction of engineered temporal features,
* weekly model training and registry management,
* hourly inference pipelines,
* storage of features and predictions in a cloud-based Feature Store (Hopsworks),
* monitoring through a Streamlit-based dashboard,
* reproducible environments via `poetry`,
* continuous execution through GitHub Actions.

The project is part of a **doctoral research effort** focused on the study of automation, reliability, transparency, and interpretability of real-world ML systems.

---

## **2. Intended Audience**

This system is designed for:

* researchers in Machine Learning and MLOps,
* data scientists and engineers implementing automated ML workflows,
* graduate students studying production-oriented ML architecture,
* academics analysing reproducibility, observability, and lifecycle automation.

---

## **3. Nature of the Software**

This implementation serves as:

* a **partial proof of concept** for a reproducible ML pipeline,
* a **functional prototype** suitable for empirical evaluation,
* a **reference architecture** for ML lifecycle management,
* an **experimental platform** for research on model monitoring and automation.

### **Disclaimers**

* The system depends on external services (Hopsworks, CometML).
* The quality of predictions depends directly on data availability and ingestion completeness.
* This implementation is not intended for commercial deployment without additional robustness, governance, and privacy mechanisms.

---

## **4. Architecture**

The system follows a modular and explicit separation of concerns.

### **4.1 Pipeline Components**

1. **Feature Pipeline**
   Extracts hourly features (temporal and spatial aggregations) from raw trip data.

2. **Training Pipeline**
   Trains predictive models, logs the experiment, and registers the model in the Model Registry.

3. **Inference Pipeline**
   Executes hourly predictions, writing results back to the Feature Store.

4. **Monitoring Interface**
   Streamlit dashboard for diagnosing model performance, drift, and operational behaviour.

### **4.2 Directory Structure**

```
src/
    config.py
    data.py
    data_split.py
    feature_store_api.py
    model.py
    model_registry_api.py
    inference.py
    plot.py
    logger.py

scripts/
    feature_pipeline.py
    training_pipeline.py
    inference_pipeline.py
    backfill_feature_group.py

.github/workflows/
    feature_pipeline.yml
    inference_pipeline.yml
    training_pipeline.yml
```

---

## **5. Installation and Environment Setup**

### **Prerequisites**

* Python 3.9
* Poetry ≥ 1.8
* Hopsworks account and project
* Comet ML account (optional but recommended)

### **5.1 Install Poetry**

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Ensure Poetry is available in your PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### **5.2 Install Dependencies**

```bash
poetry install
```

### **5.3 Configure Environment Variables**

```bash
cp .env.sample .env
```

Fill in:

```
HOPSWORKS_PROJECT_NAME="<your_project>"
HOPSWORKS_API_KEY="<your_api_key>"

COMET_ML_API_KEY="<optional>"
COMET_ML_WORKSPACE="<optional>"
COMET_ML_PROJECT_NAME="<optional>"
```

---

## **6. Running the Pipelines**

All pipelines are orchestrated via the Makefile.

### **6.1 Generate Hourly Features**

```bash
make features
```

### **6.2 Train the Predictive Model**

```bash
make training
```

### **6.3 Run Inference (Hourly Predictions)**

```bash
make inference
```

### **6.4 Backfill Historical Data**

```bash
make backfill
```

### **6.5 Launch Monitoring Dashboard**

```bash
make monitoring-app
```

---

## **7. GitHub Actions (Automated Execution)**

The repository includes three automated workflows:

* **feature-pipeline.yml** – runs hourly
* **training-pipeline.yml** – runs weekly
* **inference-pipeline.yml** – runs hourly

Secrets used by the workflows:

```
HOPSWORKS_PROJECT_NAME
HOPSWORKS_API_KEY

COMET_ML_API_KEY
COMET_ML_WORKSPACE
COMET_ML_PROJECT_NAME
```

These must be configured in:

```
GitHub → Settings → Secrets and variables → Actions
```

---

## **8. User Guide**

### **Task: Run Feature Extraction**

**Steps**

1. Ensure environment variables are correctly defined.
2. Execute:

```bash
make features
```

3. Features are written to the Feature Store.

**Possible Issues**

* Invalid API key → authentication error.
* Missing raw data → the pipeline halts safely.

---

### **Task: Train a Model**

```bash
make training
```

**Possible Issues**

* Training data unavailable.
* Comet ML temporarily unreachable.

---

### **Task: Run Inference**

```bash
make inference
```

**Possible Issues**

* Model not found in Model Registry.
* Feature group unavailable.

---

### **Task: Monitor Predictions**

```bash
make monitoring-app
```

Displays drift indicators, historical errors, and diagnostic plots.

---

## **9. Academic Context**

This software is part of a doctoral research project investigating:

* automation in ML pipelines,
* dynamic behaviour of deployed models,
* traceability and reproducibility in computational experiments,
* design methods for machine learning systems that operate in real-world conditions.

The codebase serves both as a functional ML system and as a structured artefact for research on software design, human-AI interpretation, and lifecycle automation.

---

## **10. License**

This project is released for academic and research purposes only.
Redistribution or commercial use requires explicit authorization.

---

## **11. Contact**

For academic inquiries or collaboration:

**Igor Caetano Diniz**
PhD Candidate, PUC-Rio
Machine Learning Engineer
