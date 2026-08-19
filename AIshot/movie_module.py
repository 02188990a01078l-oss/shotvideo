# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:26:48 2026

@author: dswda_uscxvt9
"""
import streamlit as st
            
def category(sel):
    if sel == "취업/직장":
        st.title("서로의 온기: 여름과 봄\n")
        st.markdown("취업 실패, 위로 , 비교\n")
        st.video("https://youtu.be/FyicCBk1puA?si=1C9F7MV6TV6SYOL-", width=300)
        if st.button("상세 보기", icon="📑", icon_position="left", width=300):
            st.write("서로의 온기: 여름과 봄\n")
            st.markdown("취업 문제로 고민이 많은 여름을 봄이 위로하는 이야기\n")
            if st.button("상세보기 취소", width=130):
                st.rerun()
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown("👍 비슷한 단막극을 추천해드려요!\n")
        if st.button("1. 서로의 온기: 희서와 민우", width=300):
            with st.expander("서로의 온기: 희서와 민우", width=500):
                st.markdown("첫사랑, 취업, 직장, 우연한 만남, 아름다운\n")
                st.markdown("[📑줄거리 보기]\n")
                st.markdown("회사에서 열심히 일해도 욕먹는 서울 생활의 환멸을 느껴 고향으로 돌아온 희서와 민우는 오랜만에 재회한다. 그리고 벌어지는 로맨스 이야기.\n")
                st.write("첫 이야기\n")
                st.video("https://youtu.be/pa8NQJuak4Y?si=SRw8uNX0-4db7sO6")
                st.write("뒷 이야기\n")
                st.video("https://youtu.be/AWXDsw-Lxr0?si=GieVkVAW1VVg55I0")
                if st.button("닫기", width=130):
                    st.rerun()
            
                
    elif sel == "첫사랑":
        st.title("서로의 온기: 희서와 민우\n")
        st.markdown("첫사랑, 취업, 직장, 우연한 만남, 아름다운\n")
        st.write("첫 이야기\n")
        st.video("https://youtu.be/pa8NQJuak4Y?si=jyTqT_cBpjxwAaGn", width=300)
        st.write("딋 이야기\n")
        st.video("https://youtu.be/AWXDsw-Lxr0?si=ymFiGoc4lxMsv7_t", width=300)
        if st.button("상세 보기", icon="📑", icon_position="left", width=300):
            st.write("서로의 온기: 희서와 민우\n")
            st.markdown("회사에서 열심히 일해도 욕먹는 서울 생활의 환멸을 느껴 고향으로 돌아온 희서와 민우는 오랜만에 재회한다. 그리고 벌어지는 로맨스 이야기.\n")
            if st.button("상세보기 취소", width=130):
                st.rerun()
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown("👍 비슷한 단막극을 추천해드려요!\n")
        if st.button("1. 서로의 온기: 여름과 봄", width=300): 
            with st.expander("1. 서로의 온기: 여름과 봄", width=500): 
                st.markdown("취업 실패, 위로 , 비교\n")
                st.markdown("[📑줄거리 보기]\n")
                st.markdown("취업 문제로 고민이 많은 여름을 봄이 위로하는 이야기\n")
                st.video("https://youtu.be/FyicCBk1puA?si=1C9F7MV6TV6SYOL-")
                if st.button("닫기", width=130): 
                    st.rerun()
        st.write("\n")
        st.write("\n")
        st.markdown("🔥 공개 예정 단막극!\n")
        if st.button("1. 서로의 온기 2: 수호와 서진", width=300):
            st.write("아직 업로드 되지 않았습니다!\n")
            
    elif sel == "판타지":
        st.title("서로의 온기: 승과 은\n")
        st.markdown("주술, 비교, 위로\n")
        st.video("https://youtu.be/p49nPjEBF1s?si=G_XVhPWiGtDNCI1c", width=300)
        if st.button("상세 보기", icon="📑", icon_position="left", width=300): 
            st.write("서로의 온기: 승과 은\n")
            st.markdown("주술 능력이 형편 없다며, 동생과 비교하는 아버지에게 슬픈 감정을 느끼는 은을 승이 따뜻한 위로를 건넨다.\n")
            if st.button("상세보기 취소", width=130):
                st.rerun()
        st.write("\n")
        st.write("\n")
        st.markdown("🔥 공개 예정 단막극!\n")
        if st.button("1. 시간의 조각들", width=300):
            st.write("아직 업로드 되지 않았습니다!\n")
            
    elif sel == "가족":
        st.title("서로의 온기: 규남과 수아\n")
        st.markdown("거짓말, 가정 폭력, 언어 폭력, 따뜻한 손길, 위로\n")
        st.video("https://youtu.be/9OubY0llrWE?si=1TpZvgPZaTFacnlX",  width=300)
        if st.button("상세 보기", icon="📑", icon_position="left", width=300): 
            st.write("서로의 온기: 규남과 수아\n")
            st.markdown("아버지의 언어 폭력으로 상처를 받은 규남과 곁에서 따뜻한 손길을 건네주는 단짝 친구 수아의 로맨스가 시작된다.\n 한 편 규남의 어머니 밀자는 쉽지 않은 결정을 내린다.\n")
            if st.button("상세보기 취소", width=130):
                st.rerun()
        st.write("\n")
        st.write("\n")
        st.markdown("🔥 공개 예정 단막극!\n")
        if st.button("1. 서로의 온기 2: 수호와 서진", width=300):
            st.write("아직 업로드 되지 않았습니다!\n")
                
    elif sel == "학교":
        st.title("서로의 온기: 소희와 민석\n")
        st.markdown("친구, 외로움, 고통, 서로의 온기, 따뜻한 손길\n")
        st.video("https://youtu.be/4sAqoEU0IVE?si=avMRS38QliDcBBDd", width=300)
        if st.button("상세 보기", icon="📑", icon_position="left", width=300): 
            st.write("서로의 온기: 소희와 민석\n")
            st.markdown("친구를 사귀지 못해 외롭고, 고통스러운 나날들을 보낸 민석과 그런 민석 곁에 운명같이 찾아온 소희에 로맨스가 시작된다!\n")
            if st.button("상세보기 취소", width=130):
                st.rerun()
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown("👍 비슷한 단막극을 추천해드려요!\n")
        
        vid6, vid7, vid8 = st.columns(3)
        with vid6: 
            if st.button("1. 서로의 온기 2: 소희와 민석", width=300): 
                with st.expander("서로의 온기 2: 소희와 민석", width=500): 
                    st.markdown("친구, 외로움, 고통, 서로의 온기, 따뜻한 손길, 명문고, 사회문제\n")
                    st.markdown("[📑줄거리 보기]\n")
                    st.markdown("2년 동안 친구도 사귀지 못한채 고통스럽고, 슬픈 하루를 보내는 민석과 소희.\n")
                    st.markdown("이 둘의 하루는 참 답답하고, 불쌍하다.\n")
                    st.markdown("그러던 어느날, 계속 사귀지 못한 민석의 용기있는 행동이 나온다.\n")
                    st.video("https://youtu.be/aZCTKxsBdGg?si=8qrcvzPi8GmC1Wz_")
        with vid7:
            if st.button("2. 서로의 온기 2: 지윤과 민식", width=300): 
                with st.expander("서로의 온기 2: 지윤과 민식", width=500): 
                    st.markdown("학교폭력, 위로, 조언, 따뜻한 손길, 사회문제\n")
                    st.markdown("[📑줄거리 보기]\n")
                    st.markdown("2년 동안 학업 시스템이 완벽한 명문 이수고등학교에서 우식 패거리에게 학교폭력을 당한 민식.\n")
                    st.markdown("그런 민식 곁에 용기있는 여학생 지윤이 다가와 따뜻한 위로와 조언을 건네는 이야기.\n")
                    st.video("https://youtu.be/p9J9A_L4Wkc?si=llkGgfybUgItcy8C")
        with vid8:
            if st.button("3. 서로의 온기 2: 서현과 민오", width=300): 
                with st.expander("서로의 온기 2: 서현과 민오", width=500): 
                    st.markdown("학교폭력, 위로, 조언, 따뜻한 손길, 사회문제\n")
                    st.markdown("[📑줄거리 보기]\n")
                    st.markdown("의대를 많이 보내는 명문 일반고 ‘과수고’. 부모님의 기대에 따라 의대 진학을 꿈꾸던 고등학생 민오는 성적의 벽 앞에서 결국 좌절하고, 자신이 무엇을 원하는지도 잃어버린다.\n")
                    st.markdown("그런 민오 곁에 운명처럼 나타난 서현. 두 사람의 만남을 통해 민오는 자신의 진짜 꿈을 찾아가기 시작한다.\n")
                    st.video("https://youtu.be/1KwPgUSdpqg?si=b1SP5P1MavjKYNg_")
                    
    elif sel == "슬픈 연애":
        st.title("서로의 온기: 연서와 규현\n")
        st.markdown("시한부, 든든한 연인, 슬픔, 슬픈 로맨스\n")
        st.video("https://youtu.be/ybV8xMdwCa4?si=WvQ8SLx7mFhAlcWe", width=300)
        if st.button("상세 보기", icon="📑", icon_position="left", width=300): 
            st.write("서로의 온기: 연서와 규현\n")
            st.markdown("29살 어린 나이에 폐암 말기가 걸린 규현과 3개월 동안 옆에서 묵묵히 지키며 사랑을 주는 연서의 슬픈 로맨스가 시작된다.\n")
            if st.button("상세보기 취소", width=130):
                st.rerun()
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown("👍 비슷한 단막극을 추천해드려요!\n")
        if st.button("1. 서로의 온기: 겨울과 가을", width=300):
            with st.expander("서로의 온기: 겨울과 가을", width=500):
                st.markdown("이별, 위로, 따뜻한 곁\n")
                st.markdown("[📑줄거리 보기]\n")
                st.markdown("전 여자친구 '세라'와 이별한 겨울을 가을이 따뜻한 위로를 주는 이야기.\n")
                st.video("https://youtu.be/zO1N7gjzKgE?si=hR4Oror-gwPWjnLh")
                if st.button("닫기", width=130):
                    st.rerun()
                    
    
    elif sel == "모든 카테고리":
        st.title("🆕 최신 AI 숏폼\n")
        st.markdown("서로의 온기 2: 서현과 민오\n")
        st.markdown("입시, 명문고, 의대, 슬픔, 좌절, 운명, 따뜻한, 온기, 위로\n")
        st.video("https://youtu.be/1KwPgUSdpqg?si=b1SP5P1MavjKYNg_", width=300)
        if st.button("상세 보기", icon="📑", icon_position="left", width=300):
            st.markdown("서로의 온기 2: 서현과 민오\n")
            st.markdown("의대를 많이 보내는 명문 일반고 ‘과수고’. 부모님의 기대에 따라 의대 진학을 꿈꾸던 고등학생 민오는 성적의 벽 앞에서 결국 좌절하고, 자신이 무엇을 원하는지도 잃어버린다.\n")
            st.markdown("그런 민오 곁에 운명처럼 나타난 서현. 두 사람의 만남을 통해 민오는 자신의 진짜 꿈을 찾아가기 시작한다.\n")
            if st.button("상세보기 취소", width=130):
                st.rerun()
                        
        st.write("\n")
        st.write("\n")
        sel_sea = st.selectbox("🎶 OST 듣기", ['OST를 선택해보세요!', '서로의 온기 시즌1 OST', '서로의 온기 시즌2 OST', '바다 OST', '시간의 조각들 OST'])
        if sel_sea == 'OST를 선택해보세요!':
            st.write("\n")
        elif sel_sea == '서로의 온기 시즌1 OST': 
            st.markdown("서로의 온기 시즌1 OST - 폭풍 속에서 잡은 손\n")
            st.audio("OST_3.mp3", width="stretch")
        elif sel_sea == '서로의 온기 시즌2 OST':
            st.markdown("서로의 온기 시즌2 OST - 서로의 온기\n")
            st.audio("OST_2.mp3", width="stretch")
        elif sel_sea == '바다 OST': 
            st.markdown("바다 OST - 바다가 닿을 때까지\n")
            st.audio("OST_1.mp3", width="stretch")
        elif sel_sea == '시간의 조각들 OST':
            st.markdown("시간의 조각들 OST - 푸른 시간의 조각\n")
            st.audio("OST_4.mp3", width="stretch")

        
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown("🔥 공개 예정 시리즈 선공개!\n")
        with st.expander("<시간의 조각들> 줄거리\n"):
            st.markdown("시간을 넘나드는 여행자 리온. 그는 시간의 균열 속에 흩어진 ‘시간의 조각’을 찾아 새로운 시대와 사건을 여행한다.\n")
            st.markdown("매 회차 새로운 인물들과 만나고, 각 시대를 잠식하는 어둠과 시간의 괴물에 맞서 싸우며 조각을 하나씩 모아간다.\n")
            st.markdown("하지만 조각이 모일수록 리온은 알게 된다. 시간의 조각에는 이 세계와 자신의 과거를 뒤흔든 비밀이 숨겨져 있다는 것을.\n")
            st.markdown("과연 리온은 모든 시간의 조각을 모으고, 시간에 숨겨진 진실을 밝혀낼 수 있을까?\n")
        
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown("👍 다른 작품도 확인해보세요!\n")
        vid1, vid2 = st.columns(2)
        with vid1: 
            if st.button("1. 서로의 온기 2: 소희와 민석", width=300):
                with st.expander("서로의 온기 2: 소희와 민석", width=500):
                    st.markdown("친구, 외로움, 고통, 서로의 온기, 따뜻한 손길, 명문고, 사회문제\n")
                    st.markdown("[📑줄거리 보기]\n")
                    st.markdown("2년 동안 친구도 사귀지 못한채 고통스럽고, 슬픈 하루를 보내는 민석과 소희.\n")
                    st.markdown("이 둘의 하루는 참 답답하고, 불쌍하다.\n")
                    st.markdown("그러던 어느날, 계속 사귀지 못한 민석의 용기있는 행동이 나온다.\n")
                    st.video("https://youtu.be/aZCTKxsBdGg?si=8qrcvzPi8GmC1Wz_")
                    if st.button("닫기", width=130):
                        st.rerun()
        with vid2: 
            if st.button("2. 서로의 온기: 소희와 민석", width=300): 
                with st.expander("서로의 온기: 소희와 민석", width=500): 
                    st.markdown("친구, 외로움, 고통, 서로의 온기, 따뜻한 손길\n")
                    st.markdown("[📑줄거리 보기]\n")
                    st.markdown("친구를 사귀지 못해 외롭고, 고통스러운 나날들을 보낸 민석과 그런 민석 곁에 운명같이 찾아온 소희에 로맨스가 시작된다!\n")
                    st.video("https://youtu.be/4sAqoEU0IVE?si=avMRS38QliDcBBDd")
                    if st.button("닫기", width=130): 
                        st.rerun()
        
        vid3, vid4 = st.columns(2)
        with vid3:
            if st.button("3. 서로의 온기: 겨울과 가을", width=300):
                with st.expander("서로의 온기: 겨울과 가을", width=500):
                    st.markdown("이별, 위로, 따뜻한 곁\n")
                    st.markdown("[📑줄거리 보기]\n")
                    st.markdown("전 여자친구 '세라'와 이별한 겨울을 가을이 따뜻한 위로를 주는 이야기.\n")
                    st.video("https://youtu.be/zO1N7gjzKgE?si=hR4Oror-gwPWjnLh")
                    if st.button("닫기", width=130):
                        st.rerun()
        
        with vid4:
            if st.button("4. 서로의 온기: 규남과 수아", width=300):
                with st.expander("서로의 온기: 규남과 수아", width=500):
                    st.markdown("거짓말, 가정 폭력, 언어 폭력, 따뜻한 손길, 위로\n")
                    st.markdown("[📑줄거리 보기]\n")
                    st.markdown("아버지의 언어 폭력으로 상처를 받은 규남과 곁에서 따뜻한 손길을 건네주는 단짝 친구 수아의 로맨스가 시작된다.\n 한 편 규남의 어머니 밀자는 쉽지 않은 결정을 내린다.\n")
                    st.video("https://youtu.be/9OubY0llrWE?si=1TpZvgPZaTFacnlX")
                    if st.button("닫기", width=130):
                        st.rerun()
