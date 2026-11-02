
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EPL Goal Predictor", page_icon="⚽", layout="wide")
st.title("⚽ EPL Goals Predictor")
st.caption("Poisson goal model trained on 2022-23 through 2025-26; 2026-27 held out for evaluation.")
bundle=joblib.load("football_goal_model.joblib")
model,teams,forms=bundle["model"],bundle["teams"],bundle["forms"]
c1,c2=st.columns(2)
with c1: home=st.selectbox("Home team",teams,index=teams.index("Arsenal") if "Arsenal" in teams else 0)
with c2:
    away_options=[t for t in teams if t!=home]
    away=st.selectbox("Away team",away_options,index=away_options.index("Liverpool") if "Liverpool" in away_options else 0)
fh,fa=forms[home],forms[away]
xh=pd.DataFrame([{"team":home,"opponent":away,"home":1,"form_scored":fh["form_scored"],"form_conceded":fa["form_conceded"]}])
xa=pd.DataFrame([{"team":away,"opponent":home,"home":0,"form_scored":fa["form_scored"],"form_conceded":fh["form_conceded"]}])
lh,la=float(model.predict(xh)[0]),float(model.predict(xa)[0])
g=np.arange(7); mat=np.outer(stats.poisson.pmf(g,lh),stats.poisson.pmf(g,la))
ph,pd_,pa=np.tril(mat,-1).sum(),np.trace(mat),np.triu(mat,1).sum()
norm=ph+pd_+pa; ph,pd_,pa=ph/norm,pd_/norm,pa/norm
score=np.unravel_index(mat.argmax(),mat.shape)
k1,k2,k3=st.columns(3)
k1.metric(f"{home} expected goals",f"{lh:.2f}")
k2.metric(f"{away} expected goals",f"{la:.2f}")
k3.metric("Most likely score",f"{score[0]}–{score[1]}")
st.subheader("Win / draw / loss probabilities")
p1,p2,p3=st.columns(3)
p1.metric(f"{home} win",f"{ph:.1%}"); p2.metric("Draw",f"{pd_:.1%}"); p3.metric(f"{away} win",f"{pa:.1%}")
fig,ax=plt.subplots(figsize=(8,5))
sns.heatmap(mat,annot=True,fmt=".1%",cmap="Blues",xticklabels=g,yticklabels=g,ax=ax)
ax.set_xlabel(f"{away} goals"); ax.set_ylabel(f"{home} goals")
ax.set_title("Scoreline probability matrix (0–6 goals)")
with st.expander("Show scoreline probability matrix"):
    st.pyplot(fig)
st.caption("Probabilities are model estimates, not guarantees or betting advice. The model assumes independent team goal counts and truncates the displayed matrix at six goals.")
