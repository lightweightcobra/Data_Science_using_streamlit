import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('41586_2016_Article_BF530367a_Figa_HTML.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

         This app counts the nucleotide composition of query DNA:

***
""")

st.header('Enter the DNA Sequence')



sequence_input = ">DNA Query \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=200)
sequence = sequence.splitlines()
sequence = sequence[1:] 
sequence = ''.join(sequence) 

st.write("""
***
""")

st.header('INPUT(DNA Query)')
sequence

st.header('OUTPUT(DNA Nucleotide Count)')

## Dictionary
st.subheader('1. Print Dictionary')


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

# Result in text format

st.subheader('2. Print Result in Text')

st.write('There are ', X['A'], 'Adenine(A)', 'in the given DNA sequence.')
st.write('There are ', X['T'], 'Thymine(T)', 'in the given DNA sequence.')
st.write('There are ', X['G'], 'Guanine(G)', 'in the given DNA sequence.')
st.write('There are ', X['C'], 'Cytosine(C)', 'in the given DNA sequence.')

# Display Dataframe

st.subheader('3. Display Dataframe')

df = pd.DataFrame({
    'Nucleotide': X_label,
    'Count': X_values
})

st.write(df)

# Display bar chart

st.subheader('4. Display Bar Chart')

bar_chart = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='Count'
)

bar_chart = bar_chart.properties(
    width=alt.Step(80),
)

st.altair_chart(bar_chart)


