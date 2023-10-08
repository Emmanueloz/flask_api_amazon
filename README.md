# Api de Amazon con una aplicación en flask

Para iniciar el proyecto, primero hay que crear el entorno virtual

[Repositorio](https://github.com/Emmanueloz/flask_api_amazon)

```
python -m venv .venv
```

Y activarlo
**Linux**

```bash
source .venv/bin/activate
```

```powershell
. \.venv\Script\activate
```

Instalar las dependencias del _requirements.txt_

```bash
pip install -r requirements.txt
```

Copiar el archivo `.env_example` en la carpeta app con el nombre de `.env`.

```bash
cp app/.env_example .env
```

Llenar la variables de entorno, estos datos los consigues en la api de [Amazon_Data_Extractor](https://rapidapi.com/thanush2112/api/amazon_data_extractor/), es necesario iniciar sesión
