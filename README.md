# Hi, I'm Daniel Livingston

**Senior Data Scientist | MS Applied Statistics | Greer, SC**

I build machine learning systems that change business decisions, not just dashboards. I have over a decade of experience in the Finance and Energy sectors, covering the full path from statistical modeling to the data platforms that put those models into production.

My work centers on three things:

* **Decisions, not just metrics.** I tune models to what an error actually costs the business: F2-optimized thresholds when a missed default or engine failure costs more than a false alarm.
* **Models that hold up to scrutiny.** Interpretability (SHAP, linear scorecards), fair-lending compliance (ECOA), and honest reporting of a model's limits.
* **Platforms that scale.** Layered Snowflake architectures, in-warehouse feature engineering with Snowpark, and model registries so work is reproducible across a team.

### Featured Projects

| Project | What it shows |
|---|---|
| **[Predictive Maintenance](https://github.com/livingdw67/cmapss-predictive-maintenance)** | End-to-end Snowflake pipeline (raw → staging → core → marts → feature store) feeding tandem XGBoost classifiers that give early-warning and critical-action alerts for turbofan engine failure. Includes class-imbalance experiments and Snowflake Model Registry. |
| **[Loan Default Prediction](https://github.com/livingdw67/azure-automl-loan-default-prediction)** | Azure AutoML with cost guardrails, ECOA-compliant feature engineering, and an F2-tuned cutoff that catches about 75% of defaults on a held-out test set, validated out of sample. SHAP explains the drivers of risk. |
| **[Tire Industry Report Analyst](https://github.com/livingdw67/michelin-rag)** | LangGraph agent over 1,250 pages of annual reports: hybrid retrieval, verified page citations, calculator-backed comparisons, and layered guardrails. 98% accuracy on a 41-question evaluation; FastAPI + Streamlit, Docker. |
| **[Grid Stress Simulator](https://github.com/livingdw67/grid-stress-simulator)** | Models how IRA-driven heat pump and EV adoption change winter peak load in every South Carolina county, using NREL ResStock data. Found that synchronized off-peak EV charging can create a new midnight peak in cold snaps. |
| **[Vehicle Loan Origination Risk](https://github.com/livingdw67/vehicle-loan-default-risk)** | XGBoost vs. an interpretable logistic scorecard, with a clear-eyed read on the data's predictive ceiling and a roadmap for alternative data. |

### Technical Toolkit

* **Modeling:** XGBoost, scikit-learn, logistic scorecards, clustering, SHAP, class-imbalance methods, threshold optimization
* **Platforms & MLOps:** Snowflake, Snowpark, Azure ML, AWS, MLflow, Docker, CI/CD
* **Languages:** Python, SQL, SAS, R, DAX
* **Applied AI:** RAG, LangChain, vector databases, LLM agents

[daniellivingston.org](https://daniellivingston.org)
