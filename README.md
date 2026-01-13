# 📁 File Renamer — CT-e Barcode Scanner

Este projeto lê imagens de **CT-e**, extrai a **chave de acesso (44 dígitos)** a partir do **código de barras** e **renomeia automaticamente os arquivos**, evitando sobrescrita por duplicação (seguindo o padrão do Windows: `(2)`, `(3)`, etc).

---

## ✅ Funcionalidades

- 📷 Leitura de imagens (`.jpg`, `.png`, `.jpeg`, `.bmp`, `.tiff`)
- 🧾 Extração **exclusiva de chaves CT-e válidas (44 dígitos)**
- 🚫 Ignora QR Codes
- 🔁 Tratamento de arquivos duplicados
- 📂 Uso automático da pasta **scanner** na Área de Trabalho
- 🖥️ Geração de **executável (.exe)** para Windows
- 🔕 Executa sem console (modo gráfico)

---

## 🖥️ Requisitos

### Para desenvolvimento

- Windows 10 ou superior (64 bits)
- Python **3.11 (64 bits)**

### Para executar o `.exe`

- Windows 64 bits
- ❌ Não é necessário Python instalado

---

## 📦 Estrutura do Projeto

fileRenamer/
│
├── main.py
├── process_image.py
├── desktop_path.py
├── error_message_box.py
├── file_utils.py
│
├── resources/
│ ├── rename.ico
│ ├── libzbar-64.dll
│ └── libiconv.dll
│
├── requirements.txt
├── README.md
└── .gitignore

---

## 📄 requirements.txt

```txt
opencv-python
pyzbar
pylint
pyinstaller
```

🚀 Passo 1 — Clonar o projeto

git clone https://github.com/SEU_USUARIO/fileRenamer.git
cd fileRenamer

🐍 Passo 2 — Criar ambiente virtual

python -m venv venv

Ativar o ambiente:

# Windows (PowerShell)

venv\Scripts\Activate

Caso o PowerShell bloqueie scripts:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

📚 Passo 3 — Instalar dependências

pip install -r requirements.txt

📂 Passo 4 — Criar a pasta scanner

1. Vá para a Área de Trabalho

2. Crie a pasta scanner

3. Coloque as imagens do CT-e dentro dela

Passo 5 — Executar em modo desenvolvimento

python main.py

🏗️ Passo 6 — Gerar o executável (PyInstaller)

```
python -m PyInstaller --onedir --noconsole ^
--icon=resources/rename.ico ^
--add-binary "resources/libzbar-64.dll;." ^
--add-binary "resources/libiconv.dll;." ^
main.py
```

📁 Passo 7 — Arquivos gerados

Após o build:

dist/
└── main/
├── main.exe
├── libzbar-64.dll
├── libiconv.dll
├── python311.dll
├── cv2/
├── pyzbar/
└── \_internal/

Copie toda a pasta para usar em outros computadores.
