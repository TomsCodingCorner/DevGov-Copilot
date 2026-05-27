conda create -n DevGov python=3.11 -y
conda activate DevGov

pip install fastapi uvicorn typer python-dotenv requests pydantic openai httpx rich pytest