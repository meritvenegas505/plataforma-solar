from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():

    # =========================
    # INVERSORES
    # =========================

    df = pd.read_excel("inversores.xlsx", engine="openpyxl")

    # LIMPIAR NOMBRES DE COLUMNAS
    df.columns = df.columns.str.strip()

    # SI NO EXISTE IMAGEN, CREARLA
    if "Imagen" not in df.columns:
        df["Imagen"] = ""

    # NORMALIZAR MARCAS
    df["Marca"] = (
        df["Marca"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # NORMALIZAR MODELOS
    df["Modelo"] = (
        df["Modelo"]
        .astype(str)
        .str.strip()
    )

    # NORMALIZAR IMAGENES
    df["Imagen"] = (
        df["Imagen"]
        .astype(str)
        .str.strip()
    )

    datos = df.to_dict(orient="records")

    marcas = sorted(
        df["Marca"]
        .dropna()
        .unique()
    )



    # =========================
    # MODULOS
    # =========================

    df_mod = pd.read_excel(
        "modulos_combinados.xlsx",
        engine="openpyxl"
    )

    # LIMPIAR NOMBRES DE COLUMNAS
    df_mod.columns = df_mod.columns.str.strip()

    # SI NO EXISTE IMAGEN, CREARLA
    if "Imagen" not in df_mod.columns:
        df_mod["Imagen"] = ""

    # NORMALIZAR MARCAS
    df_mod["Marca"] = (
        df_mod["Marca"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # NORMALIZAR MODELOS
    df_mod["Modelo"] = (
        df_mod["Modelo"]
        .astype(str)
        .str.strip()
    )

    # NORMALIZAR IMAGENES
    df_mod["Imagen"] = (
        df_mod["Imagen"]
        .astype(str)
        .str.strip()
    )

    datos_mod = df_mod.to_dict(orient="records")

    marcas_mod = sorted(
        df_mod["Marca"]
        .dropna()
        .unique()
    )



    # =========================
    # RENDER
    # =========================

    return render_template(
        "index.html",
        datos=datos,
        marcas=marcas,
        datos_mod=datos_mod,
        marcas_mod=marcas_mod
    )



if __name__ == "__main__":
    app.run(debug=True)