---
name: HW6 Introduction and Methods
overview: Align [docs/hw6/hw6.tex](c:\src\my\uwf-idc6940-capstone\docs\hw6\hw6.tex) with the HW6 assignment in [docs/hw6/intro.md](c:\src\my\uwf-idc6940-capstone\docs\hw6\intro.md) by adding a proper Introduction section (problem definition, context and background, objectives, summary of approach), ensuring Methods explicitly covers data acquisition, models, experimental design, software and tools, and optional ethical considerations, fixing the title and a typo, and saving the plan to the docs/hw6 folder.
todos: []
---

# HW6: Align Introduction and Methods with Assignment

## Reference

- **Assignment:** [docs/hw6/intro.md](c:\src\my\uwf-idc6940-capstone\docs\hw6\intro.md) — develop Introduction and Methods sections (problem definition, context/background, objectives, summary of approach; data, models, experimental design, software/tools, ethics).
- **Deliverable:** [docs/hw6/hw6.tex](c:\src\my\uwf-idc6940-capstone\docs\hw6\hw6.tex) — currently titled "Week 4--5 Progress Report" and structured as Goal/Research Question + Expanded Methods + Dataset/Implementation/Results/Appendix.

## 1. Title and typo

- **Title (line 29):** Change `\title{Week 4--5 Progress Report: Methods, Data, and Implementation}` to reflect HW6, e.g. `\title{Introduction and Methods: Capstone Forecasting Comparison}` (or similar).
- **Typo (line 124):** Change "comprasion" to "comparison" in the LSTM implementation paragraph.

## 2. Restructure into Introduction and Methods

Rename and regroup sections so the document explicitly has **Section 1: Introduction** and **Section 2: Methods** as required by the assignment.

- **Section 1 — Introduction**
- **1.1 Problem definition:** Keep and slightly expand the current "Goal" and "Research Question" (why the problem is significant in time-series/forecasting context). Optionally fold in the current "Problem Definition" paragraph from Expanded Methods here or keep a short cross-reference.
- **1.2 Context and background (new):** Add 1–2 paragraphs reviewing relevant theories and techniques: univariate time-series forecasting, ARIMA (stationarity, AIC/BIC selection), LSTM for sequences, and comparison of classical vs neural approaches. Cite existing bibliography (e.g. \cite{hyndman2006,prabhat2024,forecast_auto_arima,keras_r,keras_timeseries}) and NYC TLC \cite{nyctlc2024}.
- **1.3 Objectives and goals:** Add a short subsection (bullets or one paragraph) stating what the project will accomplish: e.g. produce 14-day forecasts from ARIMA and LSTM, compare them on the same horizon, evaluate with sMAPE and MASE.
- **1.4 Summary of approach:** Add one short paragraph summarizing the pipeline: same daily series, ARIMA + LSTM, same 14-day test window and metrics; full details in Methods.

- **Section 2 — Methods**
- **2.1 Data acquisition and sources:** Merge/refactor current "Data Description", "Preprocessing Plan" (keep \ref{sec:preprocessing} and Appendix reference), and "Dataset and Access" so that origin (NYC TLC), structure (366 days, pickup_date, avg_duration_min), and preprocessing (filter Uber, derive cols, clean, IQR, aggregate to daily CSV) are clearly in one place.
- **2.2 Mathematical or statistical models:** Keep and optionally tighten "Modeling Plan" (ARIMA, LSTM, comparison). Ensure it states why these models are appropriate (univariate series, comparison of classical vs neural).
- **2.3 Experimental design or analytical procedures:** Add or expand a short subsection: chronological train/validation/test split (e.g. last 14 days test, 30 validation), 14-day forecast horizon, and choice of evaluation metrics — state that sMAPE and MASE are used (cite \cite{hyndman2006,prabhat2024}) and briefly why (scale-independent, comparable across methods). Reference Implementation section for step-by-step code.
- **2.4 Software and tools (new):** Add a subsection listing: **Software:** R, Python (PySpark), Quarto; **Libraries:** R — forecast, keras, Metrics, yardstick (and any others used); Python — PySpark; **Computational resources:** e.g. Google Colab for PySpark preprocessing if applicable.
- **2.5 Ethical considerations (optional):** One sentence: public NYC TLC data, no human subjects; no special ethical concerns (or "Not applicable" if preferred).

Sections 3–7 (Dataset and Access if not fully merged, Implementation and Experiments, Results, Issues and Limitations, Next Steps) can remain; adjust section numbers after Introduction/Methods renumbering. Appendices unchanged.

## 3. File and label consistency

- After restructuring, ensure all internal references (e.g. \ref{sec:preprocessing}, \ref{appendix:pyspark}, listing refs) still resolve.
- Ensure bibliography [docs/hw6/hw6.bib](c:\src\my\uwf-idc6940-capstone\docs\hw6\hw6.bib) (or referenced bib file) contains nyctlc2024, hyndman2006, prabhat2024, forecast_auto_arima, keras_r, keras_timeseries.

## 4. Save plan to docs/hw6

- Save this plan as a markdown file in [docs/hw6](c:\src\my\uwf-idc6940-capstone\docs\hw6), e.g. `hw6_introduction_and_methods_plan.md`, so it lives with the assignment and deliverable for reference.

## Order of edits (suggested)

1. Fix title and typo.
2. Insert new Introduction section (1.1–1.4) and rename/restructure so "Project Goal and Research Question" becomes "Introduction" with the four subsections.
3. Rename "Expanded Methods" to "Methods" and add subsections 2.3 (Experimental design), 2.4 (Software and tools), 2.5 (Ethical considerations); merge Data Description/Dataset and Access into 2.1 as needed.
4. Renumber subsequent sections (Dataset and Access optional merge, Implementation, Results, Issues, Next Steps, Appendix).
5. Verify refs and bibliography.
6. Write this plan to docs/hw6/hw6_introduction_and_methods_plan.md (or chosen name).