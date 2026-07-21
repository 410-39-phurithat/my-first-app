import streamlit as st
st.title("เเอปพลิเคชั่นเเปลงปี พ.ศ. เป็น ค.ศ. ")

bh=st.number_input("กรอก พ.ศ. ที่ต้องการเเปลง",value=2569)
ce=bh-543
st.header(f"ปี ค.ศ. คือ : {ce}")
