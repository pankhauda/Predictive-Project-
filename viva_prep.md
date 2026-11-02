# Viva Preparation — EPL Goals Prediction using Poisson and Negative Binomial Regression

## 1. Why are goals count data?

Goals are non-negative integer counts, concentrated at low values.

## 2. Why not ordinary linear regression?

It can predict negative goals and does not model count variance.

## 3. What is predictive analytics?

Using historical data and models to estimate future outcomes.

## 4. Descriptive vs predictive vs prescriptive?

Describe what happened; predict what may happen; recommend actions based on predictions.

## 5. What is a GLM?

A generalized linear model combines a response distribution, linear predictor and link function.

## 6. What is the Poisson PMF?

P(Y=y)=exp(-λ)λ^y/y!, for non-negative integer y.

## 7. What is the Poisson mean and variance?

Both equal λ.

## 8. Why use a log link?

It guarantees positive expected counts and gives multiplicative interpretations.

## 9. How are coefficients estimated?

By maximizing the likelihood of the observed goal counts.

## 10. What is an IRR?

The exponentiated coefficient; it is the multiplicative change in expected goals.

## 11. How interpret home IRR?

An IRR of 1.20 means expected scoring is 20% higher at home, holding other predictors fixed.

## 12. What is overdispersion?

Conditional variance exceeds the conditional mean.

## 13. How check dispersion?

Variance/mean and Pearson chi-square divided by residual degrees of freedom.

## 14. What is Negative Binomial regression?

A count model with an extra dispersion parameter allowing variance above the mean.

## 15. What is NB2 variance?

Var(Y|X)=μ+αμ².

## 16. Why compare AIC?

AIC balances model fit with complexity; lower is preferred for comparable models.

## 17. What is maximum likelihood estimation?

Choosing parameters that make observed data most likely under the model.

## 18. What is target leakage?

Using information unavailable at prediction time, such as the current match result in rolling form.

## 19. Why use a chronological split?

It mimics forecasting future matches and avoids training on future data.

## 20. What is TimeSeriesSplit?

Cross-validation in which training folds precede their validation folds.

## 21. RMSE vs MAE?

RMSE penalizes large errors more; MAE is average absolute error.

## 22. What is regularization?

A penalty that shrinks coefficients to reduce overfitting.

## 23. Why include team and opponent?

They represent differences in scoring strength and defensive strength.

## 24. What happens to new teams absent from training?

They receive a baseline/reference effect; no team-specific historical effect is available.

## 25. What are model limitations?

Missing injuries, line-ups, transfers, tactical changes and player quality; the current test set is small.

## 26. Ethical considerations?

Communicate uncertainty, avoid guarantees and do not encourage harmful gambling.

## 27. Possible future improvements?

Dixon-Coles, Elo ratings, xG, bivariate Poisson and zero-inflated models if justified.

