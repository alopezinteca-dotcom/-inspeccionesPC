import streamlit as st
import pandas as pd

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(layout="wide")

# =========================================================
# URL EXCEL
# =========================================================

url_excel = "https://eurocontrol2014-my.sharepoint.com/personal/alejandro_lopez_eurocontrol_es/Documents/AXIS/EXCEL%203.4.26%20-%20copia.xlsm?download=1"

# =========================================================
# HEADER
# =========================================================

st.title("📊 Gestor de Inspecciones")
st.caption("Conectado a tu Excel real")

# =========================================================
# REFRESCAR
# =========================================================

if st.button("🔄 Refrescar datos"):
    st.rerun()

# =========================================================
# SELECCIÓN BD
# =========================================================

hoja = st.selectbox(
    "Base de datos",
    ["BD_ASCENSORES_ALIP", "BD_BT_ALIP"]
)

# =========================================================
# CARGAR DATOS
# =========================================================

try:
    df = pd.read_excel(url_excel, sheet_name=hoja)
except:
    st.error("Error cargando Excel")
    st.stop()

# =========================================================
# KPIs
# =========================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Total Registros", len(df))

with c2:
    if "ESTADO_PROCESO" in df.columns:
        st.metric("Pendientes", len(df[df["ESTADO_PROCESO"] == "PENDIENTE"]))

with c3:
    st.metric("Columnas", len(df.columns))

# =========================================================
# FILTROS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    buscar = st.text_input("Buscar")

with col2:
    if "ESTADO_PROCESO" in df.columns:
        estado = st.selectbox(
            "Estado",
            ["Todos"] + list(df["ESTADO_PROCESO"].dropna().unique())
        )
    else:
        estado = "Todos"

with col3:
    tecnico = st.text_input("Técnico")

# =========================================================
# FILTRADO
# =========================================================

df_filtrado = df.copy()

if buscar:
    df_filtrado = df_filtrado[
        df_filtrado.astype(str).apply(
            lambda row: row.str.contains(buscar, case=False).any(),
            axis=1
        )
    ]

if estado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["ESTADO_PROCESO"] == estado]

if tecnico and "INSPECTOR" in df_filtrado.columns:
    df_filtrado = df_filtrado[
        df_filtrado["INSPECTOR"].astype(str).str.contains(tecnico, case=False)
    ]

# =========================================================
# TABLA + DETALLE
# =========================================================

izq, der = st.columns([3, 1])

with izq:
    st.subheader("📋 Inspecciones")
    st.dataframe(df_filtrado, use_container_width=True, height=600)

with der:
    st.subheader("📄 Detalle")

    if not df_filtrado.empty:

        seleccion = st.selectbox(
            "Expediente",
            df_filtrado["EXPEDIENTE"]
        )

        fila = df_filtrado[df_filtrado["EXPEDIENTE"] == seleccion].iloc[0]

        st.write("**Cliente:**", fila.get("TITULAR", ""))
        st.write("**Dirección:**", fila.get("DIRECCIÓN INSPECCIÓN", ""))
        st.write("**Fecha:**", fila.get("FECHA", ""))
        st.write("**Resultado:**", fila.get("RESULTADO", ""))
        st.write("**Estado:**", fila.get("ESTADO_PROCESO", ""))
        st.write("**Técnico:**", fila.get("INSPECTOR", ""))

        st.button("📄 Generar informe")
        st.button("💰 Facturar")
        st.button("⚙️ Procesar")
