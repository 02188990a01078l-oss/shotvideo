# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 20:26:29 2026

@author: dswda_uscxvt9
"""

import streamlit as st
import movie_module as mo

st.title("🎥 숏캐스트 (ShortCast)\n")
st.markdown("이곳은 AI가 창조한 새로운 서사를 만나는 AI 숏드라마 전용 OTT입니다.\n")
Select = st.selectbox("모든 카테고리", ['모든 카테고리', '취업/직장', '첫사랑', '판타지', '가족', '학교', '슬픈 연애'], width=130)
mo.category(Select)

