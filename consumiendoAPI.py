import requests as req

datos = {'nombre':'Jorge', 'apellido':'Miralles'}
resp = req.post('http://localhost:5000/guardar/', data=datos)
print(resp.text)