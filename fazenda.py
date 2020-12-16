import requests
import time

opcao = input(r'''
     ___          _______    ___      ________   _______ .__   __.  _______       ___      
    /   \        |   ____|  /   \    |       /  |   ____||  \ |  | |       \     /   \     
   /  ^  \       |  |__    /  ^  \   `---/  /   |  |__   |   \|  | |  .--.  |   /  ^  \    
  /  /_\  \      |   __|  /  /_\  \     /  /    |   __|  |  . `  | |  |  |  |  /  /_\  \   
 /  _____  \     |  |    /  _____  \   /  /----.|  |____ |  |\   | |  '--'  | /  _____  \  
/__/     \__\    |__|   /__/     \__\ /________||_______||__| \__| |_______/ /__/     \__\ 
                                                                                           
author: Valtercio Junior
version: 1.0


Biel = 758
Jojo = 759
Lipe = 760
Stéfani = 761

Digite o numero de quem voce escolhe: ''')

cabecalho = {
	'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
	'content-length': '32',
	'content-type': 'application/x-www-form-urlencoded',
	'cookie': '_ga=GA1.2.1527410527.1608140736; _gid=GA1.2.711548222.1608140736; __gads=ID=5cb64b66992770e7:T=1608140738:S=ALNI_MYUB2VFOx1ZuTAApNzfTIyc_0TrJA; ak_bmsc=90CB2F620763C88658F3F40C464AF618B1416C87507A00002E78DA5F57D99B06~plL+mDVUlazJMiOTfrcRcZxfDHfPTp5V1YGjC0v2pprzpq+x9HsAklbnj83ooQsEi5gFxnfmLa2FnycyRpckmT+7ZL0prM8HC53Y6lubKqcBWwjxchqYyRVC0+4hfs3mfL2ARrH18cck8Q/gZE41sD3pLDa1tqfWdjKvr38lFvcVbhOQ+qbJp9PaINV1BSM/iVH9AkWGU0h+2gRdHLkVi7lonvaRfbF9fo/jukHrL+8js=; _abck=AED0FA8CF160FBE4D2901DA1B674F5E5~-1~YAAQh2xBsZ6drRt2AQAAe+2EbQX9g9RQhfNgkgJznm7kYkAreb2VVcv7Ra59zcMTqqw+4FLZpyFrO2LzxqFOpEx56xi4hhCJeBt5PjdnRkNOYoL5XNwTXCeRRg2l4R24WA7O9alJWZXKmXY4Ge1mAG4qPNdW6HiNYG3VY+a04+8gaSiNYdaocYGifmI+cwSyixbz8Z9mrtZvrhetXNSrU83fE4O4gVduklHQFbzv5d3n4VchyNhG70JIxCOW5fVUYH2/o65qxfr0mwXtDwkaBaimvDdImOq8Zt2M7bObbfhfcY/Yf+cdU4A1NX1qUzoeRISB~0~-1~-1; bm_sv=62BBDC9511DC6BBC067E085503851555~Svb3ekDLRtGtIiL4giO1XX4jnXYL7F/0p0/PgEEbP85HZ6UMuhPwEyYj2vJ7p2oM6tkOwk89Az7tduhZYCePC6kE7FoYrnUsIpR7wjRwhyMIYPc+5rd1SV+gQuPSTAisnei4RYlhL2kH/7jOllQZbw==; _gat=1; _dc_gtm_UA-10631407-5=1',
	'dnt': '1',
	'origin': 'https://afazenda.r7.com',
	'referer': 'https://afazenda.r7.com/a-fazenda-12/votacao',
	'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
	'sec-ch-ua-mobile': '?0',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

dados = {
	'voting_id':'302',
	'alternative_id':opcao
}


participantes = {'758':'Biel','759':'Jojo','760':'Lipe','761':'Stéfani'}
with requests.Session() as s:
	while True:
		s.get('https://afazenda.r7.com/a-fazenda-12/votacao')
			
		if s.post('https://voting-vote-producer.r7.com/vote', headers=cabecalho, data=dados).status_code == 200:
			print(f'voto computado participante {participantes[opcao]}')
		else:
			print('voto não aceito')
		time.sleep(9)