import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
import streamlit as st

iris_dataset = load_iris()

# 데이터전처리
df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= iris_dataset.target 


species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 


def mapp_species(x):
    return species_dict[x]

df['species'] = df['species'].apply(mapp_species)
# print(df)

# st.subheader('this is table')
# st.table(df.head())

# st.subheader('this is data frame')
# st.dataframe(df.head())


st.sidebar.title('Iris Species🌸')


# 한개의 종 선택
# select_species = st.sidebar.selectbox(
#     '확인하고 싶은 종을 선택하세요',
#     ['setosa','versicolor','virginica']
# )

# tmp_df = df[df['species'] == select_species]
# st.header(f'[{select_species}] Raw Data')
# st.table(tmp_df.head())

#종선택
select_multi_species = st.sidebar.multiselect(
    '확인하고 싶은 종을 선택하세요 (복수선택가능)',
    ['setosa','versicolor','virginica']
)

# tmp_df = df[df['species'].isin(select_multi_species)]
# st.table(tmp_df)


# Radio/slider
radio_select = st.sidebar.radio(
    'what is key column?',
    ['sepal length', 'sepal width', 'petal length','petal width'],
    horizontal=True
)

slider_range = st.sidebar.slider(
    "choose range of key column",
    0.0, #최소
    10.0, #최대
    (2.5,7.5) # 기본설정값
)

start_button = st.sidebar.button(
    "filter apply📊" #버튼에 표시될 내용
)
if start_button:
    tmp_df = df[df['species'].isin(select_multi_species)]
    tmp_df = tmp_df[(tmp_df[radio_select] >= slider_range[0]) & (tmp_df[radio_select] <= slider_range[1])]
    st.header('Datasey')
    st.table(tmp_df)
    st.sidebar.success("Filter Applied")
    st.balloons()



## 시각화

import plotly.express as px 

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)
# fig.show()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)


#지도 위에 표시될 점 좌표 값을 위도경도에 담습니다 .
base_position =  [37.5073423, 127.0572734]
#중심점의 위도, 경도 좌표를 리스트에 담습니다.

# base_position에, 랜덤으로 생성한 값을 더하여 5개의 좌표를 데이터 프레임으로 생성하였고,
# 컬럼명은 위도 :lat  경도 lon으로 지정하였습니다. 


map_data = pd.DataFrame(
    np.random.randn(5, 1) / [20, 20] + base_position , 
    columns=['lat', 'lon'])
# map data 생성 : 위치와 경도 

print(map_data)

st.code('st.map(map_data)')
# 웹사이트에 어떤 코드인지 표시해주기 
st.subheader('Map of Data ')
# 제목 생성 
st.map(map_data)
# 지도 생성 


