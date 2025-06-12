#estrutura de decisao composta
#if elif else

estado = input('digite  seu estado civil')

if estado == 'solteiro':
    print('voce é uma pessoa livre de relacionamento')
elif estado == 'casado':
    print('voce é uma pessoa comprometida ao relacionamento')
elif estado == 'divorciado':
    print('voce ta no love mas deu ruim')
elif estado == 'viuvo':
    print('infelizmente voce perdeu uma pessoa querida')
else:
    print('voce digitou algo incorreto')
