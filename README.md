# Hi, I'm Daniel Livingston

**Senior Data Scientist · MS Applied Statistics · Greer, SC**

[LinkedIn](https://www.linkedin.com/in/daniel-w-livingston)

I build machine learning systems that change business decisions. I have over a decade of experience in Finance and Energy, from statistical modeling to the data platforms that put models into production.

* **Decisions over metrics.** I tune models to what an error costs the business, such as F2-optimized thresholds when a missed default or engine failure costs more than a false alarm.
* **Models that hold up to scrutiny.** Interpretability (SHAP, linear scorecards), fair-lending compliance (ECOA), and honest reporting of a model's limits.
* **Platforms that scale.** Layered Snowflake architectures, in-warehouse training with Snowpark, and reproducible model deployment across a team.

### Experience

* **TIAA**, Senior Data Scientist (2014–2023): Built predictive models feeding a recommendation system that drove **$36M in incremental revenue**, and productionized a SHAP-explained churn model for wealth advisor management.
* **Duke Energy**, Data Scientist (2024–2025): Built a centralized feature store across structured and unstructured sources that **cut model build time by 50%**.

### Featured Projects

| Project | Result | Stack |
|---|---|---|
| **[Customer Segmentation](https://github.com/livingdw67/snowpark-customer-segmentation)** | Segments 4,261 customers by next-quarter value and buying style, trained entirely inside Snowflake. The top 20% capture 71% of next-quarter revenue, vs. 56% for standard RFM. | Snowpark, scikit-learn, LangGraph |
| **[Predictive Maintenance](https://github.com/livingdw67/cmapss-predictive-maintenance)** | Flags turbofan engines 50 and 15 cycles before failure, catching about 91% of failures on held-out engines. | Snowflake, XGBoost, survival analysis |
| **[Tire Industry Report Analyst](https://github.com/livingdw67/michelin-rag)** | AI agent that answers questions over 1,250 pages of annual reports, citing the page behind every figure. 40 of 41 test questions correct; refused every off-topic and prompt-injection attempt. | LangGraph, FastAPI, Docker |
| **[Loan Default Prediction](https://github.com/livingdw67/azure-automl-loan-default-prediction)** | Catches about 75% of defaults on a true holdout (AUC 0.76) with an ECOA-compliant, F2-tuned model. Caught training-data leakage in the initial estimate. | Azure AutoML, SHAP |
| **[Grid Stress Simulator](https://github.com/livingdw67/grid-stress-simulator)** | Models how heat pump and EV adoption shift winter peak load in every South Carolina county. Finds that an 11 PM EV charging timer creates a new midnight peak above today's morning peak. | NREL ResStock, Streamlit, Plotly |

### Technical Toolkit

* **Modeling:** XGBoost, scikit-learn, logistic scorecards, clustering, survival analysis, SHAP, class-imbalance methods, threshold optimization
* **Platforms & MLOps:** Snowflake, Snowpark, Azure ML, AWS, MLflow, Docker, GitHub Actions
* **Languages:** Python, SQL, SAS, R, DAX
* **Applied AI:** RAG, LangGraph, vector databases, LLM agents, LLM evaluation
* **Certifications:** AWS Certified Machine Learning – Associate (2024)
