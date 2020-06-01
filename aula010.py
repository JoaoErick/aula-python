from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    #print(data_atual)
    #print(data_atual.strftime('%d/%m/%Y'))
    #print(data_atual.strftime('%H:%M:%S'))
    #print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    #print(data_atual.strftime('%c'))

    #print(data_atual.day)
    #print(data_atual.month)
    #print(data_atual.year)
    #print(data_atual.hour)
    #print(data_atual.minute)
    #print(data_atual.date())

    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta')
    print(tupla[data_atual.weekday()]) #Dia da semana traduzido
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)

    nova_data = data_convertida - timedelta(days=365, hours=2) #subtraindo um ano e 2 horas
    print(nova_data)

    data_atual = datetime.now()
    resultado = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(type(resultado))
def trabalhando_com_date():
    data_atual = date.today()
    #print(data_atual) #formato americano
    #print(data_atual.strftime('%d/%m/%y')) #formato brasileiro com ano em dois dígitos
    #print(data_atual.strftime('%d/%m/%Y')) #formato brasileiro com ano em quatro dígitos
    print(data_atual.strftime('%A %B %Y')) #Dia, mês e ano por extenso.

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario)
    print(horario_str)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()