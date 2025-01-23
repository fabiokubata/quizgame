#Projeto HandsOn  Fábio Kubata / 08/2024    
#São questões de conhecimento geral, onde as questões irão gerar uma pontuação. Bora lá ?

print("Bem vindo ao QUIZ do portfólio de Fabio Kubata")
user_answer = input("Vamos começar o jogo? Digite S para iniciar ")

if user_answer != "S":
    quit()

score = 0

print ("Então vamos lá, lembre de apenas digitar a letra da opcao em maiusculo") 
print("Qual é o elemento com maior potencial de condutividade da tabela periódica? \n (A) Osmium \n (B) Alumínio \n (C) Prata \n (D) Cobre ") #Questao 1
answer1 = input ("Resposta:")
if answer1 == "C":
    print ("Parabens, acertou")
    score = score + 1
else:
    print ("Desculpe, a resposta está incorreta. \n A Resposta correta é C, Prata")

print("Qual a somatória de lados opostos de um dado? \n (A) 6 \n (B) 7 \n (C) 8 \n (D) 9 ") #Questao 2
answer1 = input ("Resposta:")
if answer1 == "B":
    print ("Parabens, acertou")
    score = score + 1
else:
    print ("Desculpe, a resposta está incorreta. \n A Resposta correta é B, 7")

print("Quem foi o cientista que formulou a lei gravitacional? \n (A) Albert Einstein \n (B) Isaac Newton \n (C) Neil Degrasse Tyson \n (D) Nikola Tesla ") #Questao 3
answer1 = input ("Resposta:")
if answer1 == "B":
    print ("Parabens, acertou")
    score = score + 1
else:
    print ("Desculpe, a resposta está incorreta. \n A Resposta correta é B, Isaac Newton")

print("Qual destes é considerado o pai da aviação no Brasil? \n (A) Santos Dumont \n (B) Fabio Kubata \n (C) Arthur Laurentiz \n (D) Jaime ") #Questao 4
answer1 = input ("Resposta:")
if answer1 == "A":
    print ("Parabens, acertou")
    score = score + 1
else:
    print ("Desculpe, a resposta está incorreta. \n A Resposta correta é A, Santos Dummont")

print("Qual o apelido que o Exército Expedicionário Brasileiro ganhou durante a Segunda Guerra Mundial? \n (A) O Brasil não participou da Segunda Guerra \n (B) Tropa sem fuzil \n (C) Os Amarelinhos \n (D) Cobras Fumantes ")
answer1 = input ("Resposta:")
if answer1 == "D":
    print ("Parabens, acertou")
    score = score + 1
else:
    print ("Desculpe, a resposta está incorreta. \n A Resposta correta é D, Santos Dummont")

print (f" Nosso QUIZ terminou, sua pontuação foi de: {score}/5 Kubata Points")