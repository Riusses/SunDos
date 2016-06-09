def red_carret(request):
    es_actiu=False
    valor=0
    if 'carret' in request.session:
        es_actiu=True
        for id in request.session['carret']:
            valor+=1
    if valor==0:
        es_actiu=False
    return {'carret_ple':es_actiu, 'valor':valor}