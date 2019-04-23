# Deep Reinforcement Learning
Desenvolvimento de um Agente Artificial treinado com o algoritmo Deep Q-Learning com auxílio de uma Rede Neural Recorrente LSTM Siamesa
(duas entradas: uma entrada para o texto do estado e outro para as possíveis ações a serem tomadas neste estado corrente).

O Projeto foi realizado levando em conta os seguintes resultados publicados:
* Using Reinforcement Learning to learn how to play text-based games (Mikuláš Zelinka, 2018)
* Language Understanding for Text-based Games using DeepReinforcement Learning (Karthik Narasimhan, Tejas Kulkarni, Regina    Barzilay, 
  2017).
  
O Emulador do jogo foi totalmente desenvolvido por mim. No momento é composto apenas por 14 estados e de transições de estado
determinísticas. 
A escolha de fase de inicialização do jogo já é feita de forma estocástica.



Melhorias a serem implementadas:
* Implementação do algoritmo Double Deep Q-Learning, de forma a tornar o treinamento mais estável.
* Replay de memória de experiência de forma eficiente. Numa próxima implementação, usar Listas de Prioridades, onde a chave de
  prioridade é o TD Error.





