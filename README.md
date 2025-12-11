<div align="center">
  <h1>NYC Taxi Demand Prediction and Monitoring System</h1>
  <i>Research-Oriented Pipeline for Automated Feature Engineering, Model Training, Inference, and Monitoring</i>
</div>

---

## 1. Project Description

This project implements an end-to-end machine learning system designed to **predict short-term taxi demand in New York City** and to **monitor the deployed model over time**.  

The system provides:

- automated temporal and geospatial feature extraction,
- scheduled model training and experiment tracking,
- hourly inference execution,
- integration with a cloud-based Feature Store (Hopsworks),
- a monitoring interface for data drift and performance diagnostics,
- reproducible environments using `uv`,
- automated pipelines via GitHub Actions.

### Intended Users

This software system is intended for:

- **Researchers in Machine Learning and MLOps**,  
- **Data scientists and data engineers** working with real-world prediction systems,  
- **Graduate students** studying ML pipelines and automation,  
- **Academics** analysing transparency, reliability, and reproducibility of ML systems.

### Nature of the Program

This is a **research-grade implementation**, serving as:

- a *partial proof of concept* for automated ML architectures,  
- a *teaching and experimentation platform*,  
- a *reference implementation* for reproducible ML lifecycle management.

### Disclaimers

- The system depends on external services (Hopsworks, Comet ML).  
- Predictions depend on data freshness and completeness.  
- This software is not intended for commercial deployment without additional layers of governance, reliability, and privacy.

---

## 2. Project Vision — Scenario-Based Orientation

This section follows the scenario methodology proposed by **Clarisse de Souza**, oriented toward design intent, user expectations, and software evolution.

### Positive Scenario 1 — Research Workflow

Marina, a doctoral student studying MLOps automation, wants to analyse how hourly predictions respond to alternative feature engineering approaches.  
She runs the **feature pipeline**, then the **training pipeline**, and finally the **inference pipeline**.  
She inspects data drift and performance diagnostics in the monitoring dashboard.  
These insights guide her next experimental iterations.

### Positive Scenario 2 — Engineering Exploration

Lucas, a data engineer, modifies a geospatial aggregation component in the feature pipeline.  
He executes:

```

make features

```

Then checks the updated results in the monitoring dashboard.  
The system’s modular architecture enables safe experimentation without disrupting the full pipeline.

### Negative Scenario 1 — External Dependency Limitation

Ana attempts to run the training pipeline but receives an authentication error from the Feature Store.  
The pipeline halts, informing her that the Hopsworks API key is missing or invalid.  
This limitation is expected: the system requires valid credentials and does not automatically refresh them.

### Negative Scenario 2 — Data Availability Limitation

Rafael triggers the inference pipeline while upstream hourly trip data has not yet been fully ingested.  
The system detects incomplete input data and aborts inference.  
This is expected behaviour in real-time systems dependent on external ingestion pipelines.

---

## 3. Technical Documentation

### 3.1 Functional Requirements

- Generate engineered features from raw taxi trip data  
- Train predictive models  
- Register models in a model registry  
- Run hourly inference  
- Store predictions in a Feature Store  
- Visualize drift and performance metrics

### 3.2 Non-Functional Requirements

- Reproducibility and deterministic environments (`uv`)  
- Automated scheduling through GitHub Actions  
- Modular architecture  
- Observability via logging and experiment tracking (Comet ML)

---

## 4. Architecture Overview

The system consists of the following components:

1. **Feature Pipeline** — Extracts temporal and geospatial features  
2. **Training Pipeline** — Builds and registers predictive models  
3. **Inference Pipeline** — Runs hourly prediction batches  
4. **Monitoring App** — Evaluates model behaviour and drift  

### Directory Structure

```

src/
config.py
data.py
data_split.py
feature_store_api.py
model.py
model_registry_api.py
inference.py
monitoring.py

scripts/
feature_pipeline.py
training_pipeline.py
inference_pipeline.py
backfill_feature_group.py

````

All pipelines use a clean separation between **orchestration** (`scripts/`) and **logic modules** (`src/`).

---

## 5. Installation and Setup

### 1. Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
````

### 2. Sync all dependencies

```bash
uv sync --all-extras --group dev
```

### 3. Configure environment variables

```bash
cp .env.sample .env
# Add Hopsworks and Comet ML API keys
```

---

## 6. Running Pipelines

### Generate Features

```bash
make features
```

### Train the Model

```bash
make training
```

### Run Inference

```bash
make inference
```

### Launch Monitoring Dashboard

```bash
make monitoring-app
```

---

## 7. User Manual (Aligned with Clarisse de Souza’s Framework)

### **Task: Run Feature Extraction**

#### Steps

1. Confirm that `.env` contains valid credentials.
2. Execute:

```
make features
```

3. The system computes hourly features and stores them.

#### Exceptions

* Invalid Feature Store credentials → authentication error.
* Missing raw data → pipeline aborts safely.

---

### **Task: Train a Model**

#### Steps

```
make training
```

#### Exceptions

* Missing or incomplete training data → training is cancelled.
* Comet ML unavailable → training proceeds, but without experiment logs.

---

### **Task: Run Inference**

#### Steps

```
make inference
```

#### Exceptions

* No model found in registry → inference halted.
* Unavailable feature group → system logs and stops.

---

### **Task: Monitor Predictions**

```
make monitoring-app
```

---

## 8. Academic Context

This system is part of an ongoing doctoral research effort focused on:

* automation and reliability in ML pipelines,
* transparency and interpretability of ML-enabled systems,
* reproducibility of experimental workflows,
* design methodologies for real-world ML software systems.

It serves both as a **functional prototype** and as a **research instrument** for investigating the interplay between automation, user interpretation, and system behaviour.
