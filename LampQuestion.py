#  4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. \
#  Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. \
#  3 Seu objetivo é descobrir qual interruptor controla qual lâmpada.


#  Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

#  Cenário 1: 
#  Tenho 3 salas, a sala da esquerda, a do meio e a da direita. Vamos supor que o ligo o interruptor de cima e o do meio, \
#  e então vou na sala da esquerda e vejo que a luz está ligada, \
#  agora eu sei que 1 desses 2 interruptores liga a luz da sala da esquerda, então volto e ligo o interruptor de cima e o de baixo \
#  vou até a sala do meio, se a luz estiver desligada, quer dizer que o primeiro interruptor corresponde a sala da esquerda, \
#  o segundo a sala do meio e o terceiro a sala da esquerda.

#  Cenário 2:
#  Ligo o primeiro e o segundo interruptor e vou a sala de esquerda, e vejo que a luz está desligada \
#  então já sei que o terceiro interruptor corresponde a sala da esquerda, então eu volto acendo o primeiro interruptor \
#  e vou a sala do meio, se estiver ligado, pertence a ela, se não o primeiro inerruptor corresponde a sala da direita\
#  primeiro interruptor = sala do meio
#  segundo interruptor = sala direita
#  terceiro interruptor = sala da esquerda

#  Existem outros cenários de possiblidades, porém optei por mostrar esses, mas a estratégia que eu usuária seria essa em todas tentativas.