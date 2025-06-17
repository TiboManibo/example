import streamlit as st
#import pandas as pd
#import numpy as np
import random

from numpy.random import choice

#title
st.title("ROCK PAPER SCISSORS")
#sidebar
button1=st.button('Rock')
button2=st.button('Paper')
button3=st.button('scissors')
def opponent_choice():
    opponent = random.randint(1, 3)
    options={1:'Rock',2:'Paper',3:'Scissors'}
    oppch=options[opponent]
    opp=opponent
    return oppch,opp
if button1:
    choice=1
elif button2:
    choice=2
elif button3:
    choice=3
winning=[[1,3],[2,1],[3,2]]
result=None
if button1 or button2 or button3:
    opponent,enemigo=opponent_choice()
    st.text(f'your opponent selected {opponent}')
    #st.text(f'enemigo{enemigo}')
    comb=[choice,enemigo]
    if choice==enemigo:
        st.text('Empate babas')
        result='empate'
    elif comb== winning[0] or comb==winning[1] or comb==winning[2]:
        st.text('you win')
        result='win'
    else:
        st.text('you lose')
        result='lose'
        st.image(https://www.google.com/imgres?q=burro%20tonto%20dibujo&imgurl=https%3A%2F%2Fih1.redbubble.net%2Fimage.880069275.7702%2Fflat%2C750x%2C075%2Cf-pad%2C750x1000%2Cf8f8f8.jpg&imgrefurl=https%3A%2F%2Fwww.redbubble.com%2Fes%2Fi%2Fposter%2FBurro-tonto-de-Bumble-Bea%2F40377702.LVTDI&docid=H3cWqZH7VUbMYM&tbnid=ZZW7oM-X7Vr9-M&vet=12ahUKEwiq3rLwvPmNAxUHnokEHVDeKLwQM3oFCIkBEAA..i&w=750&h=1000&hcb=2&ved=2ahUKEwiq3rLwvPmNAxUHnokEHVDeKLwQM3oFCIkBEAA.jpg)
st.text('calla idiota')
#two player





#dropdown_name=st.selectbox('names of people',options=['CJ','Fidel','Gremlin'])
#button
#button =st.button('greet me')
#if button:
 #   st.write(f'welcome mr{name},you are {age} old')
#st.write(f'you selected {dropdown_name}')
#st.subheader('Random Data Chart')
#data=pd.DataFrame(np.random.randn(5,3),columns=["A","B","C"])
#st.dataframe(data=data)
#st.line_chart(data)
