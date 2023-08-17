import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import wooldridge as wd
import matplotlib.pyplot as plt
import seaborn as sns

wage = wd.data('wage1')
st.title("First app")
col1, col2, col3 = st.columns(3)


# filtrar los datos

wage = wage.filter(['wage','educ','exper','female','married'])

# limpiar los datos
wage = (wage.replace({'female':{1:'female', 0:'male'},
                     'married':{1:'married', 0:'single'}})
            .rename(columns={'female':'gender',
                             'married':'fam_status'}))

# seleccionar las variables
#st.dataframe(wage)

# métricas

educ_mean = round(wage['educ'].mean(), 2)
wage_mean = round(wage['wage'].mean(), 2)
exper_mean = round(wage['exper'].mean(), 2)

with col1:
    st.metric("Salario", wage_mean)

with col2:
    st.metric("Experiencia", exper_mean)

with col3:
    st.metric("Educación", educ_mean)
# gráficos
# histogramas

col11, col22 = st.columns(2)
with col11:
    fig, ax = plt.subplots(3, 1, figsize=(10, 8))

    ax[0].hist(wage['wage'], bins=40)
    ax[1].hist(wage['educ'], bins=40)
    ax[2].hist(wage['exper'], bins=40)

    st.pyplot(fig)
# boxplot

with col22:
    fig, ax = plt.subplots(1, 2,  sharey=True, figsize=(10, 4))
    sns.scatterplot(data=wage, x='educ', y='wage', hue='gender', ax=ax[0])
    sns.scatterplot(data=wage, x='exper', y='wage', hue='gender', ax=ax[1])

    st.pyplot(fig)

    fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    sns.violinplot(data=wage, x='fam_status', y='wage', hue='gender', ax=ax)

    st.pyplot(fig)