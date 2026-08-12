# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 20:26:29 2026

@author: dswda_uscxvt9
"""

import streamlit as st
import movie_module as mo

st.set_page_config(page_title="숏캐스트 - AI 숏드라마 OTT", page_icon="🎥")
st.title("🎥 숏캐스트 (ShortCast)\n")
st.markdown("이곳은 AI가 창조한 새로운 서사를 만나는 AI 숏드라마 전용 OTT입니다.\n")
Select = st.selectbox("모든 카테고리", ['모든 카테고리', '취업/직장', '첫사랑', '판타지', '가족', '학교', '슬픈 연애'], width=130)
mo.category(Select)
if st.button("OST 감상", icon="🎶", icon_position="left", width="stretch"):
    sel_sea = st.selectbox("시즌 선택", ['서로의 온기 시즌1 OST', '서로의 온기 시즌2 OST', '바다 OST'])
    if sel_sea == '서로의 온기 시즌1 OST': 
      st.markdown("서로의 온기 시즌1 OST - 폭풍 속에서 잡은 손\n")
      st.audio("OST_2.mp3", width="stretch")
    elif sel_sea == '서로의 온기 시즌 2 OST':
      st.markdown("서로의 온기 시즌 2 OST - 서로의 온기\n")
      st.audio("OST_3.mp3", width="stretch")
    elif sel_sea == '바다 OST': 
      st.markdown("바다 OST - 바다가 닿을 때까지\n")
      st.audio("OST_1.mp3", width="stretch")
