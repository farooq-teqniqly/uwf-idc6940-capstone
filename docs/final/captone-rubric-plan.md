---
name: Capstone rubric alignment plan
overview: Assess capstone.tex against rubric-final.md and plan updates so the report meets all required sections, rubric criteria, and formatting. The plan is saved as a markdown file in docs/final for reference.
todos: []
---

# Capstone Report Rubric Alignment Plan

## Rubric-to-paper mapping

| Rubric requirement | Current state in [capstone.tex](docs/final/capstone.tex) | Action |
|--------------------|----------------------------------------------------------|--------|
| **Introduction (10 pts)** | Problem, objectives, background, summary present | Minor strengthening (see below) |
| **Methods (30 pts)** | Data, models, design, software, ethics present | Add mathematical formulation; optional hyperparameter sentence |
| **Results (40 pts)** | Figures/tables with captions; comparison table | Add LSTM uncertainty (e.g. SD or range across 5 runs) |
| **Discussion (10 pts)** | No section titled "Discussion"; limitations in "Issues and Limitations" | Add **Discussion** section (interpretation + limitations + implications) |
| **Conclusion and Future Work (10 pts)** | Conclusion present; no explicit Future work | Add **Future work** subsection/paragraph |
| **Formatting** | Title, author, date; bibliography | Add course title to title block; confirm page numbers and citation style |

---

## 1. Introduction (10 points)

**Rubric:** Problem definition (precise; variables, quantities, success), significance and gap, context with citations, objectives, summary of approach.

**Gaps:**

- **Success criterion:** Make "success" explicit (e.g., lower sMAPE/MASE = better; comparison on same test window).
- **Gap:** Briefly state what gap the project addresses (e.g., comparative evaluation of ARIMA vs LSTM on the same urban-mobility series and horizon).

**Planned changes:**

- In Problem Definition (or Significance): Add one sentence defining success (e.g., "Success is measured by lower sMAPE and MASE on the same 14-day holdout.") and one sentence on the gap (e.g., "The project addresses the gap of directly comparing a classical and a neural forecasting approach on the same univariate daily series.").

---

## 2. Methods (30 points)

**Rubric:** Mathematical/statistical formulation when appropriate; appropriateness and rigor; clarity and reproducibility; data acquisition; experimental design (metrics, tuning, validation); software; ethics.

**Gaps:**

- **Mathematical form:** Rubric asks for "objective function, likelihood, loss function, update rules" when appropriate. ARIMA paragraph does not give the ARIMA(p,d,q) form or AIC/BIC; LSTM paragraph does not state loss (MSE) or optimizer (Adam) in mathematical terms.
- **Hyperparameter strategy:** Experimental design asks for "hyperparameter tuning strategy." Paper mentions early stopping and pragmatic choices but not explicitly "no grid search; sequence length, units, dropout fixed."

**Planned changes:**

- **ARIMA:** Add one sentence or inline formula for the model class, e.g. "The model has the form ARIMA(p,d,q) with p,d,q selected by minimizing AIC/BIC" and cite the forecast package. Optionally add the standard ARIMA equation in notation (or reference Hyndman & Athanasopoulos).
- **LSTM:** In the LSTM paragraph, state explicitly: loss function (MSE), optimizer (Adam), and that training minimizes MSE on the training sequences. Optionally one sentence on early stopping (monitor val_loss, patience 15).
- **Experimental design:** In "Experimental Design and Analytical Procedures," add one sentence: "LSTM hyperparameters (sequence length 21, 32 units, dropout 0.2, batch size 16) were fixed; no grid or random search was performed."

---

## 3. Results (40 points)

**Rubric:** Completeness and correctness; quality of figures/tables; sound evaluation (metrics, baselines, validation, **uncertainty and variability**).

**Gaps:**

- **Uncertainty/variability:** Rubric asks for "confidence intervals, error bars, standard deviations, or variability across folds/runs" when relevant. LSTM metrics are the mean of 5 runs but the table has no SD or range; adding variability would strengthen the Results section.

**Planned changes:**

- In Table~\ref{tab:compare}: Add a column or footnote for LSTM giving the standard deviation (or range) of sMAPE and MASE across the 5 runs (e.g. "LSTM: 8.05 ± 0.xx (sMAPE), 2.09 ± 0.xx (MASE)"). If the exact SD values are not available, add a sentence in the Results text stating that LSTM metrics are means of 5 runs and report the approximate range or SD if available; otherwise state "variability across runs was observed but not quantified in the table."
- Optional: Report a naive baseline (e.g. naive one-step sMAPE/MASE on the test window) in text or table for "baseline comparison" if desired.

---

## 4. Discussion (10 points)

**Rubric:** A **Discussion** section: interpretation (tie results to research question), limitations and challenges, implications (contribution, use in decision-making).

**Gaps:**

- The report has **Results**, **Issues and Limitations**, and **Conclusion**, but no section explicitly titled **Discussion**. The rubric expects "Discussion (Meaning and Implications)" with interpretation, limitations, and implications in one place.

**Planned changes:**

- **Add a new "Discussion" section** between **Results** and **Issues and Limitations** (or merge "Issues and Limitations" into Discussion as subsections). Recommended structure:
- **4.1 Interpretation:** One short paragraph tying the comparison (Table~\ref{tab:compare}, figures) to the research question: what the similar or slightly better ARIMA performance means for this task (short-horizon, univariate, small data); mention LSTM convergence (Figure~\ref{fig:lstm_loss}) and lack of overfitting.
- **4.2 Limitations:** Either move the current "Issues and Limitations" content here as subsections (small sample, univariate, alignment, library changes, LSTM reproducibility) or keep "Issues and Limitations" as a separate section and in Discussion only summarize and cite it (e.g. "As noted in Section X, limitations include..."). Prefer one clear Discussion section that contains both interpretation and limitations to match the rubric.
- **4.3 Implications:** One short paragraph on contribution (methodological comparison, reproducible pipeline, practical takeaway for urban mobility forecasting) and, if relevant, how results could inform model choice or operations.
- **Section order:** Use either:
- **Results → Discussion** (interpretation + limitations + implications) **→ Conclusion and Future Work**, and remove or shorten the standalone "Issues and Limitations" section by folding it into Discussion; or
- **Results → Discussion** (interpretation + implications) **→ Issues and Limitations** (keep as-is) **→ Conclusion and Future Work**.
- Recommendation: Single **Discussion** section with subsections *Interpretation*, *Limitations*, *Implications*; move current "Issues and Limitations" content into *Limitations*; then keep **Conclusion** separate.

---

## 5. Conclusion and Future Work (10 points)

**Rubric:** Conclusion (restate problem, approach, 1–3 key takeaways); **Future work** (concrete improvements or extensions).

**Gaps:**

- **Future work:** The current Conclusion has no explicit "Future work" paragraph. The rubric requires "concrete improvements or extensions (more data, alternative models, improved evaluation, deployment)."

**Planned changes:**

- Add a **Future work** subsection (or paragraph) at the end of the Conclusion section. Content: (1) extend data if more years of NYC TLC data become available; (2) refine LSTM hyperparameters (sequence length, units, dropout) or run a small grid search; (3) report LSTM variability (e.g. SD across runs) or improve reproducibility; (4) optional: alternative models (e.g. Prophet, other neural architectures) or deployment considerations. Keep to 3–5 concrete bullets or one short paragraph.

---

## 6. Formatting and submission (rubric guidelines)

**Rubric:** Single PDF; consistent formatting; page numbers; in-text citations and bibliography (APA, MLA, or accepted style); labeled figures/tables with in-text reference; **cover page with project title, your name(s), course title, and submission date.**

**Gaps:**

- **Course title:** Not present on the title block. Add course title (e.g. "IDC 6940 Capstone" or as specified by your program) to the title page.
- **Page numbers:** Standard `article` class numbers pages by default; confirm in the built PDF that page numbers appear (e.g. bottom center).
- **Bibliography:** Document uses `\bibliographystyle{plain}` and `\bibliography{capstone}`. Rubric allows "APA, MLA, or another accepted style (consistent throughout)." If the program requires APA/MLA, switch to `apalike` or `plainnat` and ensure [capstone.bib](docs/final/capstone.bib) entries match; otherwise state that "plain" is the chosen style and keep it consistent.
- **Title:** Current title is "Introduction and Methods: Capstone Forecasting Comparison." If the rubric expects a more descriptive project title, consider something like "Comparing ARIMA and LSTM for Short-Term Forecasting of Daily Average Uber Trip Duration in New York City" and keep subtitle if needed.

**Planned changes:**

- Add course title to the title block (e.g. in `\date{}` area or a custom line under `\author`).
- Verify page numbers in the generated PDF.
- Optionally adjust title and bibliography style to match program requirements; otherwise document the choice.

---

## 7. Turnitin and AI (rubric note)

The rubric states: similarity index below 25%; AI-generated content no more than 40%. No edits to the LaTeX are required; the author should run the report through Turnitin and ensure originality and AI-use limits are met before submission.

---

## Implementation order

1. **Formatting:** Add course title; verify page numbers and citation style.
2. **Introduction:** Add success criterion and gap sentence.
3. **Methods:** Add ARIMA/LSTM mathematical formulation and hyperparameter sentence.
4. **Results:** Add LSTM variability (SD or range) to table or text.
5. **Discussion:** Add new Discussion section (Interpretation, Limitations, Implications); merge or reference current Issues and Limitations.
6. **Conclusion:** Add Future work subsection with concrete next steps.
7. **Final pass:** Build PDF, check all figure/table references and that every figure/table is cited in the text.

---

## File to create

Save this plan as **[docs/final/capstone-rubric-plan.md](docs/final/capstone-rubric-plan.md)** (or equivalent name) in the `docs/final` directory so it can be used as a checklist during implementation. In Plan mode the plan is created here; to have the exact file on disk, run the implementation step that writes `docs/final/capstone-rubric-plan.md` with the full plan content.