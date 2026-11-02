# EPL Goal Prediction Mini Project

## Dataset audit
Five distinct supplied seasons were verified using the football-season labels and fixture dates:
- 2022-23: 380 matches (2022-08-05 to 2023-05-28)
- 2023-24: 380 matches (2023-08-11 to 2024-05-19)
- 2024-25: 380 matches (2024-08-16 to 2025-05-25)
- 2025-26: 380 matches (2025-08-15 to 2026-05-24)
- 2026-27: 80 matches (2026-08-21 to 2026-10-25)

Total: **1,600 matches** and **3,200 team-match observations**.
The 2026-27 season is ongoing and currently contributes 80 matches. No duplicate season was retained.

## Experiment
- Training: 2022-23, 2023-24, 2024-25 and 2025-26 (1,520 matches).
- Test: 2026-27 (80 matches).
- Rolling form: previous five matches only, updated after each fixture.
- Model: Poisson GLM and Negative Binomial GLM; L2-regularized Poisson pipeline for app.
- Validation: chronological TimeSeriesSplit on training data.

## Files
- `football_poisson.ipynb`: executed analysis notebook
- `app.py`: Streamlit prediction app
- `football_goal_model.joblib`: trained prediction pipeline
- `report.docx`: project report
- `slides.pptx`: presentation
- `viva_prep.md`: viva Q&A
- `data/`: five raw season files
- `plots/`: EDA and model diagnostics
- CSV/JSON outputs: cleaned data, metrics, comparisons and calibration

## Run
```bash
pip install -r requirements.txt
jupyter notebook football_poisson.ipynb
streamlit run app.py
```

## Actual results
- Mean total goals per match: 2.9450
- Home IRR: 1.2125
- Training variance/mean ratio: 1.0788
- Pearson dispersion: 0.9353
- NB2 alpha (method of moments): 0.053378
- W/D/L accuracy on 2026-27: 0.4625
