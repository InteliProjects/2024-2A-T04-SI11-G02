from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel
import warnings
from tensorflow.keras.models import load_model  # type: ignore

app = FastAPI()

# Carregar o modelo Keras
try:
    model = load_model('modelo_fraude_final.h5')  # Caminho do modelo Keras
    print("Modelo Keras carregado com sucesso.")
except (ValueError, FileNotFoundError, ModuleNotFoundError) as e:
    warnings.warn(f"Erro ao carregar o modelo Keras: {str(e)}")
    model = None

# Definir a estrutura dos dados que serão recebidos
class ConsumoInput(BaseModel):
    dados: list

@app.post("/predict")
async def predict(consumo_input: ConsumoInput):
    try:
        # Verificar se o modelo foi carregado corretamente
        if model is None:
            raise HTTPException(status_code=500, detail="Modelo não foi carregado corretamente.")

        # Log para verificar os dados recebidos
        print("Dados recebidos para predição:", consumo_input.dados)

        # Converter os dados recebidos para um DataFrame
        df = pd.DataFrame(consumo_input.dados)

        # Verificar se o DataFrame possui alguma coluna indesejada
        if 'MATRICULA' in df.columns:
            df = df.drop(columns=['MATRICULA'])

        # Fazer predições utilizando o modelo Keras
        predictions = model.predict(df)
        print("Predições realizadas com o modelo Keras.")

        # Adicionar coluna de predição ao DataFrame original
        df['fraude_predita'] = predictions.flatten()

        # Converter para um formato serializável
        return {"predictions": df.to_dict(orient="records")}

    except Exception as e:
        print(f"Erro no endpoint /predict: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao obter predição: {str(e)}")