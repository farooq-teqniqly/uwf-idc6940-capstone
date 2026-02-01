# Capstone Project: Trip Duration Forecasting and Prediction

## Project Overview

This capstone project develops and evaluates forecasting methods for Uber trip durations: it compares an ARIMA approach with an LSTM model on the same data and horizon (ARIMA content is included in the narrative via excerpts from prior work; the capstone does not formally extend the unpublished STA6856 report).

## Project Scope and Goals

### Primary Focus

- **Trip Duration Forecasting and Prediction**: The capstone focuses on developing and evaluating both time-series forecasting models and ML-based prediction models for Uber trip durations in New York City
- **Comparative Analysis**: Compare the performance of time-series forecasting (ARIMA) with ML-based prediction (LSTM) on the same data and metrics

### Previous Work

- Previous time-series analysis was completed using ARIMA models for daily average Uber trip durations
- Previous work is documented in: `uwf-sta6856/finalproject/docs/finalproject-report.tex`
- Previous work used NYC TLC data aggregated to daily averages (365 data points for 2024)

### Current Capstone Scope

1. **Time-Series Forecasting**: Include ARIMA methodology (via excerpts in the narrative) and compare with LSTM for trip duration forecasting
2. **ML-Based Prediction**: Develop machine learning models for trip duration prediction
3. **Performance Comparison**: Compare accuracy and performance of time-series vs ML methods
4. **Data Source**: Use Uber ride-sharing data from NYC TLC (not yellow taxi data)

### Out of Scope

- **Charging Optimization**: Charging optimization for electric ride-hailing fleets is NOT in scope for this capstone
  - While accurate trip duration predictions could potentially benefit charging optimization frameworks in future work, that integration is outside the capstone scope
  - Charging optimization might be a side benefit but is not the main focus

## Data Details

- **Source**: NYC Taxi and Limousine Commission (TLC) - Uber ride-sharing data
- **Note**: The capstone uses Uber ride-sharing data, NOT yellow taxi data (which is used in some related papers)
- **Previous preprocessing**: Used PySpark to aggregate 200+ million records to daily averages

## Methodology

### Time-Series Approach

- Includes ARIMA methodology (via excerpts in the narrative; same data as prior work; do not cite STA6856)
- Focuses on temporal patterns and historical trends
- Uses daily aggregated trip duration data

### Machine Learning Approach

- Develops ML models to capture complex non-linear relationships
- Considers multiple factors: temporal patterns, origin-destination pairs, demand volatility, congestion
- Feature engineering informed by stochastic demand modeling

### Comparison Framework

- Evaluate both approaches on the same dataset
- Compare accuracy metrics and performance
- Identify strengths and limitations of each approach

## Key Insights from Related Work

- Temporal patterns (daily, weekly, seasonal) are important for trip duration prediction
- Stochastic customer demand affects trip durations through congestion and demand volatility
- Multi-scale temporal modeling (different decision horizons) may benefit both time-series and ML approaches
- Anticipative planning based on historical patterns is valuable for forecasting

## Project Context

- **Course**: UWF IDC6940 Capstone
- **Previous Course**: UWF STA6856 (Time Series Analysis)
- **Related Papers**: Ma et al. (2024) on coordinated vehicle dispatching and charging scheduling (provides methodological insights but focuses on charging optimization, which is out of scope)

## Important Notes

- When discussing this project, remember that charging optimization is NOT part of the capstone scope
- The focus is purely on trip duration forecasting/prediction and comparing time-series vs ML methods
- Data source is Uber ride-sharing data from NYC TLC, not yellow taxi data
- The project uses the same data as prior ARIMA work, includes excerpts of that methodology in the narrative (no citation of the unpublished report), and adds LSTM and a formal comparison

### Clarification: relationship to STA6856 work

- **This capstone does not technically extend the work in STA6856.** The STA6856 final project report is not officially published. The capstone uses the same data (daily average trip duration for 2024) and **includes relevant excerpts** from that work (problem definition, data description, ARIMA methodology, preprocessing, forecast table/figure) in the narrative—but does **not cite or explicitly mention** the STA6856 report in the body or bibliography. Present ARIMA content in the capstone as your own methods/results. The capstone **adds** an LSTM model and a formal comparison (ARIMA vs LSTM on sMAPE and MASE). Do not describe the capstone as "extending" prior time-series work or STA6856; use "compares", "adds", or "develops and evaluates" instead.

## Writing Style and Grammar Preferences

When writing academic documents for this capstone project, follow these style and grammar preferences:

### Academic Tone and Terminology

- Use **"this capstone"** or **"the capstone"** (not "this study") when referring to the capstone project itself (e.g., "This capstone compares ARIMA and LSTM", "The capstone predicts daily average trip duration")
- Use "this study" when referring to *other* work being reviewed in the literature (e.g., "This study addresses", "the study by Prabhat et al.")
- Use past tense when describing what authors did: "The authors used" not "The authors use"
- Use "Although" instead of "While" in formal contexts (e.g., "Although this capstone focuses" not "While the paper focuses")

### Structure and Clarity

- Use enumerated lists (LaTeX `\begin{enumerate}`) for multiple items instead of semicolons or commas
- Break up long sentences for clarity
- Use "and then" instead of just "then" for sequential actions (e.g., "develop models and then compare")

### Article Usage

- Use definite articles consistently: "the four benchmark approaches" not "four benchmark approaches"
- Use "the" before specific nouns: "the total profit", "the service rates", "the charging waiting times"

### Terminology

- Use "nonlinear" (one word) instead of "non-linear" (hyphenated)
- Use "the duration of a trip" in some contexts for precision, not just "trip durations"
- Use "day-ahead" (hyphenated) consistently
- Use "discrete-event" (hyphenated) for simulation frameworks

### Sentence Structure

- Prefer active voice: "This capstone addresses" (for the capstone); "This study addresses" (for other work being reviewed)
- Use more formal phrasing: "have not been adequately addressed" not "has not adequately addressed"
- Separate related ideas into distinct sentences rather than long compound sentences
- Use enumerated lists for clarity when presenting multiple points or contributions

### Consistency

- Maintain consistent terminology throughout (e.g., "time-series forecasting" vs "ML-based prediction")
- Use consistent verb tenses within sections
- Ensure parallel structure in lists and comparisons

## Literature Review Methodology

When conducting literature reviews for this capstone project, follow these guidelines based on Snyder (2019):

### Types of Literature Reviews

Three main approaches are available, depending on the research question:

1. **Systematic Review**
   - Best for: Narrow research questions with specific, measurable effects
   - Characteristics: Systematic search strategy, explicit inclusion/exclusion criteria, quantitative analysis (often meta-analysis)
   - Use when: Synthesizing evidence of specific effects or relationships

2. **Semi-Systematic Review**
   - Best for: Broad topics conceptualized differently across disciplines
   - Characteristics: May or may not be fully systematic, qualitative or mixed-method analysis
   - Use when: Overviewing research areas, tracking development over time, identifying themes

3. **Integrative Review**
   - Best for: Creating new theoretical frameworks or conceptual models
   - Characteristics: Usually not systematic, requires advanced conceptual thinking
   - Use when: Combining perspectives to develop new theories or frameworks

### Four-Phase Review Process

**Phase 1: Design**
- Determine if the review is needed and what contribution it will make
- Define specific research question(s) and select appropriate methodology
- Develop search strategy: search terms, databases, inclusion/exclusion criteria
- Consider the target audience and potential impact

**Phase 2: Conduct**
- Pilot test the review process on a smaller sample
- Use multiple reviewers for quality assurance
- Select articles systematically (read abstracts first, then full texts)
- Document inclusion/exclusion process transparently
- Scan references in selected articles for additional relevant work (if appropriate for methodology)

**Phase 3: Analysis**
- Abstract appropriate information from articles (descriptive, effects/findings, or conceptualizations)
- Choose analysis method appropriate to research question
- Train reviewers to ensure consistency in data abstraction
- Document analysis process clearly

**Phase 4: Writing**
- Clearly communicate motivation and need for the review
- Transparently describe methodology and process
- Present results clearly and explain all findings
- Articulate contribution to the field (beyond mere description)

### Quality Criteria for Literature Reviews

A quality literature review must demonstrate:

1. **Depth and Rigor**: Appropriate strategy for selecting articles and capturing insights
2. **Replicability**: Method described so others can replicate the study
3. **Usefulness**: Valuable for scholars and practitioners
4. **Transparency**: Clear documentation of all decisions and processes

### Common Mistakes to Avoid

1. **Insufficient methodological detail**: Failing to describe search strategy, selection process, and analysis methods
2. **Overly limited search**: Restricting to too few journals, narrow time spans, or excluding relevant fields
3. **Poor presentation of results**: Including tables/figures without explanation or context
4. **Lack of meaningful contribution**: Merely summarizing existing research without providing new insights, frameworks, or evidence

### Application to Capstone Project

For this capstone project's literature reviews:

- **Purpose**: Synthesize existing research on trip duration prediction, time-series forecasting, and ML-based prediction methods
- **Approach**: Likely semi-systematic or integrative, given the interdisciplinary nature of the topic
- **Focus Areas**: 
  - Time-series forecasting methods for transportation data
  - Machine learning approaches for trip duration prediction
  - Comparative studies of forecasting vs ML methods
  - Temporal patterns in ride-hailing data
- **Contribution Goal**: Identify gaps in existing research and establish foundation for comparing time-series and ML approaches
- **Key Requirement**: Go beyond description to provide insights that inform the comparative analysis methodology

## Useful Commands and Tools

### LaTeX Word Count

To count words in a LaTeX file (excluding LaTeX commands, citations, and formatting), use this PowerShell command:

```powershell
$content = Get-Content 'filename.tex' -Raw; $text = $content -replace '\\[a-zA-Z]+\{[^\}]*\}|\$[^\$]*\$|\\cite\{[^\}]*\}|\\section\{[^\}]*\}|\\subsection\{[^\}]*\}|\\begin\{[^\}]*\}|\\end\{[^\}]*\}|\\item|\\textbf|\\cite|\\documentclass|\\usepackage|\\title|\\author|\\date|\\maketitle|\\tableofcontents|\\bibliographystyle|\\bibliography|\\begin|\\end', ''; ($text -split '\s+' | Where-Object { $_ -match '^[a-zA-Z]' }).Count
```

**Usage**: Replace `'filename.tex'` with the actual LaTeX file path. This command:
- Removes LaTeX commands, citations, and formatting
- Counts only actual words (starting with letters)
- Provides an accurate word count for assignment requirements

**Example**: 
```powershell
cd "C:\src\my\uwf-idc6940-capstone\docs\hw3"; $content = Get-Content 'hw3.tex' -Raw; $text = $content -replace '\\[a-zA-Z]+\{[^\}]*\}|\$[^\$]*\$|\\cite\{[^\}]*\}|\\section\{[^\}]*\}|\\subsection\{[^\}]*\}|\\begin\{[^\}]*\}|\\end\{[^\}]*\}|\\item|\\textbf|\\cite|\\documentclass|\\usepackage|\\title|\\author|\\date|\\maketitle|\\tableofcontents|\\bibliographystyle|\\bibliography|\\begin|\\end', ''; ($text -split '\s+' | Where-Object { $_ -match '^[a-zA-Z]' }).Count
```
