import requests

cookies = {
    '__cf_bm': 'bA6g.RXiSErSc.16hGKEUED_ZWfFVIK0lk2IsYal5_8-1708528070-1.0-AZ1zoils4szufExfHEv16HO9pGLkJMr0uyOjm0+WvR34GSqzXnjknH7UMhf8JDootP3Dspu/OaD56N5L+q5ErRM=',
    'auth.strategy': 'cookie',
    'auth._token_expiration.cookie': 'false',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjYyZDEwNWI5YmY4NGNlMmM5N2U0Yjc3MCIsImVtYWlsIjoiamVzdXNjb3J0ZXoxNjM4QGdtYWlsLmNvbSIsInN1YnNjcmlwdGlvbiI6eyJuYW1lIjoiTGlmZXRpbWUgQW1pZ28iLCJwcmljZSI6IjI5OS45OSIsImRheXMiOiI5OTk5OTkiLCJ0cmlhbCI6ZmFsc2UsImVtYWlsIjoiamVzdXNjb3J0ZXoxNjM4QGdtYWlsLmNvbSIsInN0YXJ0X2RhdGUiOiIyMDIyLTExLTE4VDEwOjQ5OjE3LjcwMFoiLCJlbmRfZGF0ZSI6IjQ3NjAtMTAtMTRUMTA6NDk6MTcuNzAwWiIsInN0YXR1cyI6ImFjdGl2ZSIsIl9pZCI6IjYzNzFlNmY0M2FhNTQ2ZTVhNTU3N2U1YSIsInVwZGF0ZWRfYXQiOiIyMDIyLTExLTE4VDEwOjQ5OjE3LjcwMVoiLCJjcmVhdGVkX2F0IjoiMjAyMi0xMS0xOFQxMDo0OToxNy43MDFaIiwicGxhbl9pZCI6MywiX192IjowLCJzeW5jZWRfYXQiOiIyMDIzLTA1LTEyVDE5OjA2OjI4Ljg1MloifSwiaWQiOiI2MmQxMDViOWJmODRjZTJjOTdlNGI3NzAifSwiaWF0IjoxNzA4NTI4MDkwLCJleHAiOjE3MTExMjAwOTB9.AuKB6-6AJ273hTQ4J_7oWa6rANcCQ4KVpfgN6B3RTYI',
    'auth._token.cookie': 'true',
}

headers = {
    'authority': 'dashboard.footyamigo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
    # 'cookie': '__cf_bm=bA6g.RXiSErSc.16hGKEUED_ZWfFVIK0lk2IsYal5_8-1708528070-1.0-AZ1zoils4szufExfHEv16HO9pGLkJMr0uyOjm0+WvR34GSqzXnjknH7UMhf8JDootP3Dspu/OaD56N5L+q5ErRM=; auth.strategy=cookie; auth._token_expiration.cookie=false; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjYyZDEwNWI5YmY4NGNlMmM5N2U0Yjc3MCIsImVtYWlsIjoiamVzdXNjb3J0ZXoxNjM4QGdtYWlsLmNvbSIsInN1YnNjcmlwdGlvbiI6eyJuYW1lIjoiTGlmZXRpbWUgQW1pZ28iLCJwcmljZSI6IjI5OS45OSIsImRheXMiOiI5OTk5OTkiLCJ0cmlhbCI6ZmFsc2UsImVtYWlsIjoiamVzdXNjb3J0ZXoxNjM4QGdtYWlsLmNvbSIsInN0YXJ0X2RhdGUiOiIyMDIyLTExLTE4VDEwOjQ5OjE3LjcwMFoiLCJlbmRfZGF0ZSI6IjQ3NjAtMTAtMTRUMTA6NDk6MTcuNzAwWiIsInN0YXR1cyI6ImFjdGl2ZSIsIl9pZCI6IjYzNzFlNmY0M2FhNTQ2ZTVhNTU3N2U1YSIsInVwZGF0ZWRfYXQiOiIyMDIyLTExLTE4VDEwOjQ5OjE3LjcwMVoiLCJjcmVhdGVkX2F0IjoiMjAyMi0xMS0xOFQxMDo0OToxNy43MDFaIiwicGxhbl9pZCI6MywiX192IjowLCJzeW5jZWRfYXQiOiIyMDIzLTA1LTEyVDE5OjA2OjI4Ljg1MloifSwiaWQiOiI2MmQxMDViOWJmODRjZTJjOTdlNGI3NzAifSwiaWF0IjoxNzA4NTI4MDkwLCJleHAiOjE3MTExMjAwOTB9.AuKB6-6AJ273hTQ4J_7oWa6rANcCQ4KVpfgN6B3RTYI; auth._token.cookie=true',
    'dnt': '1',
    'if-none-match': 'W/"57dcc-Bd1p2q7CF8L5fdmVh5ucbSaWAgs"',
    'referer': 'https://dashboard.footyamigo.com/fixtures',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

response = requests.get('https://dashboard.footyamigo.com/api/fixtures/18957251', cookies=cookies, headers=headers)
if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)