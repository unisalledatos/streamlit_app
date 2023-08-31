import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout='wide')

data = pd.DataFrame(np.random.normal(10, 5, size=(1000, 4)), columns=list('ABCD'))
st.title('Proyecto')
st.text("Pequeño resumen acerca del proyecto")

st.header("Descripción general de los datos")

st.dataframe(data.head())


fig, ax = plt.subplot_mosaic("""
                    AAAABB
                    AAAACC
                    AAAADD
""")

ax['A'].hist(data['A'])
#histograma 2
ax['B'].hist(data['B'])
#histograma 3
ax['C'].hist(data['C'])
ax['D'].hist(data['D'])

fig.tight_layout()
#histograma 4
st.pyplot(fig)
#heatmap

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Mean A", round(data['A'].mean(), 2))
with col2:
    st.metric("Mean B", round(data['B'].mean(), 2))
with col3:
    st.metric("Mean C", round(data['C'].mean(), 2))
with col4:
    st.metric("Mean D", round(data['D'].mean(), 2))

fig, ax = plt.subplot_mosaic("""
                    BBAAAAA
                    CCAAAAA
                    DDAAAAA
""")

sns.heatmap(data.corr(), ax=ax['A'])

for ax_ in ['B', 'C', 'D']:
    ax[ax_].scatter(data['A'], data[ax_])

fig.tight_layout()
st.pyplot(fig)

st.header("Construcción de clústers")

fig, ax = plt.subplots(1, 1)
data.mean().plot(kind='bar', ax=ax)
st.pyplot(fig)

st.header("Conclusiones")
#conclusiones