import streamlit as st
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS board (
        board_id INTEGER PRIMARY KEY AUTOINCREMENT,
        이름 VARCHAR(255) NOT NULL,
        리뷰 TEXT NOT NULL
    )
''')
conn.commit()

# 팀 소개
def team_intro():
    st.header("우리 팀 소개")
    st.write("""
    우리는 혁신적인 서비스를 제공하는 팀입니다. 다양한 분야에서 경험을 가진 전문가들이 모여,
    고객에게 최고의 경험을 선사하기 위해 노력하고 있습니다.
    """)

# 서비스 소개
def service_intro():
    st.header("우리가 만든 서비스")
    st.write("""
    우리의 서비스는 사용자에게 실용적이고 편리한 기능을 제공합니다. 직관적인 인터페이스와
    효율적인 문제 해결을 위해 항상 최선을 다하고 있습니다.
    """)

# def guestbook():
#     st.header("사용자 후기")
    
#     # 후기 저장용 리스트 (세션 상태 사용)
#     if 'reviews' not in st.session_state:
#         st.session_state.reviews = []
    
#     # 후기 작성 폼
#     with st.form(key='review_form'):
#         user_name = st.text_input("이름")
#         user_review = st.text_area("후기 작성")
#         submit_button = st.form_submit_button("후기 제출")
        
#         if submit_button:
#             if user_name and user_review:
#                 # 세션에 후기 저장 (새로운 후기 먼저 추가)
#                 st.session_state.reviews.insert(0, {'name': user_name, 'review': user_review})
#                 st.success("후기가 제출되었습니다!")
#                 # DB에 저장
#                 cursor.execute("INSERT INTO board (이름, 리뷰) VALUES (?, ?)", (user_name, user_review))
#                 conn.commit()  # DB 변경 사항 저장
#             else:
#                 st.error("이름과 후기를 모두 작성해 주세요.")
    
#     # 제출된 후기 표시 (새로운 후기 먼저 표시)
#     st.write("### 제출된 후기들")
#     # DB에서 정보 가져오기
#     cursor.execute("SELECT * FROM board")
#     all_review = cursor.fetchall()

#     # 결과를 이름과 리뷰로 변수 선언하여 출력
#     for idx, row in enumerate(all_review):
#         name = row[1]  # 첫 번째 열은 '이름'
#         review = row[2]  # 두 번째 열은 '리뷰'
#         st.write(f"💛 {name}님: {review}")
        
#         # 각 후기에 편집과 삭제 버튼 추가
#         col1, col2 = st.columns([1, 1])
        
#         with col1:
#             edit_button = st.button("편집", key=f"edit_{idx}")
#         with col2:
#             delete_button = st.button("삭제", key=f"delete_{idx}")

#         if delete_button:

        
#         #print('리뷰:',all_review)

#     # for idx, review in enumerate(st.session_state.reviews):
#     #     st.write(f"- {review['name']}님: {review['review']}")
        
#     #     # 각 후기에 편집과 삭제 버튼 추가
#     #     col1, col2 = st.columns([1, 1])
#     #     with col1:
#     #         edit_button = st.button("편집", key=f"edit_{idx}")
#     #     with col2:
#     #         delete_button = st.button("삭제", key=f"delete_{idx}")
        
#         # '삭제' 버튼 클릭 시 해당 후기 삭제
#         if delete_button:
#             del st.session_state.review
#             cursor.execute("DELETE FROM board WHERE id = ?", (row[0],))  # id로 삭제
#             conn.commit()  # 변경 사항 저장
#             st.success(f"{name}님의 후기가 삭제되었습니다!")
#             st.experimental_rerun()  # 페이지를 새로고침하여 후기 목록을 갱신

#         # # '편집' 버튼 클릭 시 후기 수정
#         # if edit_button:
#         #     edited_name = st.text_input("이름", value=review['name'], key=f"edit_name_{idx}")
#         #     edited_review = st.text_area("후기 작성", value=review['review'], key=f"edit_review_{idx}")
#         #     save_button = st.button("저장", key=f"save_{idx}")
            
#         #     if save_button:
#         #         st.session_state.reviews[idx] = {'name': edited_name, 'review': edited_review}
#         #         st.success("후기가 수정되었습니다!")
#         #         st.experimental_rerun()  # 페이지를 새로고침하여 수정된 후기를 반영

def new_geustbook():
    st.header("사용자 후기")
        # 후기 작성 폼
    with st.form(key='review_form'):
        user_name = st.text_input("이름")
        user_review = st.text_area("후기 작성")
        submit_button = st.form_submit_button("후기 제출")
    
    if submit_button:
        if user_name and user_review:
            st.success("소중한 후기 감사합니다")
            #DB에 저장하기
            cursor.execute("INSERT INTO board (이름, 리뷰) VALUES (?, ?)", (user_name, user_review))
            # DB 변경 사항 저장
            conn.commit()
        else:
            st.error("이름과 후기를 모두 작성해 주세요.")

        # 제출된 후기 표시 (새로운 후기 먼저 표시)
    st.write("### 제출된 후기들")
    # DB에서 정보 가져오기
    cursor.execute("SELECT * FROM board")
    all_review = cursor.fetchall()

        # 결과를 이름과 리뷰로 변수 선언하여 출력
    for idx, row in enumerate(all_review):
        review_id = row[0]
        name = row[1]  # 첫 번째 열은 '이름'
        review = row[2]  # 두 번째 열은 '리뷰'
        st.write(f"💛 {name}님: {review}")

        left_column, right_column = st.columns(2)


        edit_button = left_column.button("편집", key=f"edit_{idx}")
        delete_button = right_column.button("삭제", key=f"delete_{idx}")

    # 삭제 버튼 클릭 시 리뷰 삭제
        if delete_button:
            cursor.execute("DELETE FROM board WHERE board_id = ?", (review_id,))
            conn.commit()  # 변경사항을 DB에 적용
            st.write(f"{name}님의 리뷰가 삭제되었습니다.")
            st.rerun()  # 페이지 새로 고침


    

# Streamlit 페이지 구조
def main():
    st.title("우리 서비스 웹페이지")
    
    # 각 섹션 호출
    team_intro()
    service_intro()
    new_geustbook()

if __name__ == "__main__":
    main()
