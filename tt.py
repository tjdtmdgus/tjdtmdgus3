# import streamlit as st
# import turtle
# import numpy as np
# import matplotlib.pyplot as plt


# fig, ax = plt.subplots()

# a = 2
# b = -5
# c = 3
# d = -7

# x = []
# y = []
# for i in range(-100,101):
#     x.append(i)
#     y.append(a*i**3 + b*i**2 + c*i + d)



# color = st.radio('색을 선택하시오.',('red', 'green', 'blue'))
# plt.plot(x, y, color = color)
# st.pyplot(fig)

# x = [-10, -9, -8, -7, -6]

# cc = st.radio('선의 색을 선택하시오',['red', 'green', ])

# st.image('rabbit.jpg')

import streamlit as st
import os
os.system('cls')

col1, col2 = st.columns(2)
with col1:
    st.image('성승현.jpg',)
with col2:
    st.write('(저는 이런 사람 입니다!)')
    '전화번호 010-8448-9323'
    '주소-xxxx시xxx-xxx'
    '다양한 실무 경험과 문제 해결 능력을 가지고 있음 '
    '꾸준한 자기개발'
    '도전을 두려워하지 않고 항상 새로운 도전을 이어가는 사람'
    '항상 준비하고 대기하면 주어진일을 완벽하게 실행하는 사람'
    '절대 혼자 나아가지 않고 주변에 모두와 함께 나아가는 성실한 일꾼'
import sys
sys.exit()

import streamlit as st