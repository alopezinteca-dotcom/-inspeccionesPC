import streamlit as st
from docx import Document

st.title("inspeccionesPC")

nombre = st.text_input("Cliente")
direccion = st.text_input("Dirección")

if st.button("Guardar"):
    st.success("Guardado")

if st.button("Generar Word"):
    doc = Document()
    doc.add_heading("Informe", 0)
    doc.add_paragraph(nombre)
    doc.add_paragraph(direccion)

    doc.save("informe.docx")

    with open("informe.docx", "rb") as f:
        st.download_button("Descargar Word", f, file_name="informe.docx")
