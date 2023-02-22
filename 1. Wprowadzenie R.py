#tworzenie środowisk wirtualnych - oddzielnych środowisk dla pythona
cd C:\projects 
python -m venv .myenv
.myenv/scripts/activate
deactivate
echo pandas==1.5.1 numpy==1.24.1 > requirements.txt
pip install -r requirements.txt
deactivate