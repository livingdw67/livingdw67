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
| **[Predictive Maintenance](https://github.com/livingdw67/cmapss-predictive-maintenance)** | Snowflake feature store feeding two XGBoost classifiers that flag turbofan engines 50 and 15 cycles before failure, catching about 91% of failures on held-out engines. A Weibull fleet analysis sets maintenance windows and shows that treating cut-off test engines as ordinary censored data overstates engine life by 5–15%. |
| **[Loan Default Prediction](https://github.com/livingdw67/azure-automl-loan-default-prediction)** | Azure AutoML ensemble with ECOA-compliant features and an F2-tuned cutoff. Out-of-sample validation caught that the original 80% figure came from training data; the corrected cutoff catches about 75% of defaults on a true holdout (AUC 0.76). SHAP explains the risk drivers. |
| **[Tire Industry Report Analyst](https://github.com/livingdw67/michelin-rag)** | LangGraph agent that answers questions over 1,250 pages of tire-maker annual reports and cites the page behind every figure. 98% accuracy on a 41-question evaluation, and it correctly refused 100% of unanswerable, off-topic and prompt-injection questions. FastAPI + Streamlit, Docker. |
| **[Grid Stress Simulator](https://github.com/livingdw67/grid-stress-simulator)** | Simulates how IRA-driven heat pump and EV adoption change winter peak load in every South Carolina county, using NREL ResStock data. Key finding: if every EV starts charging on an 11 PM timer, cold nights produce a new midnight peak higher than today's morning peak. |

### Technical Toolkit

* **Modeling:** XGBoost, scikit-learn, logistic scorecards, clustering, SHAP, class-imbalance methods, threshold optimization
* **Platforms & MLOps:** Snowflake, Snowpark, Azure ML, AWS, MLflow, Docker, CI/CD
* **Languages:** Python, SQL, SAS, R, DAX
* **Applied AI:** RAG, LangChain, vector databases, LLM agents
