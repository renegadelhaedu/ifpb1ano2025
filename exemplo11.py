#Desenvolva um algoritmo em python que receba do usuário o nome, a idade e a quantidade de graus dos seus óculos. A cada ano, o grau aumenta 0,3. O programa deve calcular e exibir a quantidade de graus dos óculos em 7 anos do usuário.
nome = input('digite seu nome')
idade = int(input('digite sua idade'))
grau = float(input('digite os graus do seu oculos'))

grau_final = grau + 0.3 * 7

print('em 7 anos', nome, 'usara oculos com grau igual a ', grau_final)