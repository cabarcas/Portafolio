import requests

response = requests.get('https://api.github.com')

if response.status_code == 200:
    print("¡La instalación fue un éxito! GitHub API respondió correctamente.")
else:
    print(f"Algo falló. Código de estado: {response.status_code}")
