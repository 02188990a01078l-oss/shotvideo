# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 20:26:29 2026

@author: dswda_uscxvt9
"""

import streamlit as st
import movie_module as mo

st.set_page_config(page_title="숏캐스트 - AI 숏드라마 OTT", page_icon="🎥")
st.title("🎥 숏캐스트 V2.5\n")
st.markdown("이곳은 AI가 창조한 새로운 서사를 만나는 AI 숏드라마 전용 OTT입니다.\n")
sel_upd = st.selectbox("업데이트 정보", ['보기', 'V2.5'])

if sel_upd == '보기':
  st.write("\n")
elif sel_upd == 'V2.5':
  st.markdown("- 모든 카테고리에 'OST 듣기' 기능 추가\n")
  st.markdown("- 모든 카테고리에 '업데이트 정보' 추가\n")
  if st.button("닫기", width=130):
    st.rerun()
Select = st.selectbox("모든 카테고리", ['모든 카테고리', '취업/직장', '첫사랑', '판타지', '가족', '학교', '슬픈 연애'], width=130)
mo.category(Select)
