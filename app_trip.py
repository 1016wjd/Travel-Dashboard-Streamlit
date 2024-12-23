import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt
import plotly.express as px 
import streamlit as st

from datetime import datetime, timedelta

####데이터####################################################################################################################################
#데이터 로드
df_search = pd.read_csv('./data/country_search_data_202411.csv')

#데이터 전처리
df_vol = df_search[['continent', 'country', 'keyword', 'base_date', 'volume']]
df_vol['base_date'] = pd.to_datetime(df_vol['base_date'], errors='coerce')
# print(df_vol)


####사이드바####################################################################################################################################
#대륙필터
st.sidebar.title('필터')
select_continent = st.sidebar.multiselect(
    '1번. 여행하고 싶은 대륙을 선택하세요(복수선택가능)',
    ['유럽', '아시아','동아시아', '서아시아', '남아시아', '중앙아시아', '아프리카', '북아메리카', '남아메리카', '중동','오세아니아', '카브리해']
)

# 시작 날짜 및 종료 날짜 설정
start_date = datetime(2024, 11, 1)
end_date = datetime(2024, 11, 30)

#날짜필터
slider_range = st.sidebar.slider(
    "choose range of key column",
    start_date, #최소
    end_date, #최대
    (start_date,end_date), # 기본설정값
    format="MM/DD/YY"
)

#버튼
start_button = st.sidebar.button(
    "filter apply📊" #버튼에 표시될 내용
)
if start_button:
    df_vol = df_vol[df_vol['continent'].isin(select_continent)]
    df_vol = df_vol[(df_vol['base_date'] >= slider_range[0]) & (df_vol['base_date'] <= slider_range[1])]


####함수정의####################################################################################################################################
#라인차트 함수
def make_line_chart(data,x,y,title):
    df_temp = data.groupby(x).agg({y:'sum'}).reset_index()
    fig = px.line(df_temp, x=x, y=y, title=title)
    # fig.show()
    return fig

# 국가별 라인차트
def make_country_line_chart(data,x,y,title):
    fig = px.line(df_vol, x=x, y=y,color='country', title=title)
    # fig.show()
    return fig

#히트맵
def make_heatmap(data,z,title=None):
    fig = px.density_heatmap(data, x='base_date',y='continent',z=z,title=title)
    fig.update_layout(
    xaxis=dict(categoryorder='array', categoryarray=sorted(data['base_date'].unique(), reverse=True))
    )
    return fig


####본문####################################################################################################################################
#제목
st.title('Travel Dashboard🛫🛫')

#전체추이그래프
st.header('여행지추이')
fig_1 = make_line_chart(df_vol, 'base_date', 'volume', '전체검색추이')
st.plotly_chart(fig_1, theme='streamlit',use_container_width = True)

#나라별 검색추이그래프
fig_2 = make_country_line_chart(df_vol, 'base_date', 'volume', '나라별검색추이')
st.plotly_chart(fig_2, theme='streamlit',use_container_width = True)

fig_3 = make_heatmap(df_vol, 'volume', '히트맵')
st.plotly_chart(fig_3, theme='streamlit',use_container_width = True)

# col1, col2 = st.columns([1,1])

# with col1:
#     fig_1 = make_line_chart(df_vol, 'base_date', 'volume', '검색추이')
#     st.plotly_chart(fig_1, theme='streamlit',use_container_width = True, key='chart1')
# with col2:
#     fig_2 = make_country_line_chart(df_vol, 'base_date', 'volume', '나라별검색추이')
#     st.plotly_chart(fig_2, theme='streamlit',use_container_width = True, key='chart2')