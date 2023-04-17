while True:
      answer1 = input("jogador 1: ").lower()
      answer2 = input("jogador 2: ").lower()
      if (answer1 == 'pedra' and answer2 == 'tesoura'):
          print("\nJogador 1 ganhou!")
      elif (answer1 == 'tesoura' and answer2 == 'papel'):
          print("\nJogador 1 ganhou!")
      elif (answer1 == 'papel' and answer2 == 'pedra'):
          print("\nJogador 1 ganhou!")
      elif (answer1 == 'tesoura' and answer2 == 'pedra'):
          print("\nJogador 2 ganhou!")
      elif (answer1 == 'papel' and answer2 == 'tesoura'):
          print("\nJogador 2 ganhou!")
      elif (answer1 == 'pedra' and answer2 == 'papel'):
          print("\nJogador 2 ganhou!")
      else:
          print("Ninguém ganhou!")

      answer = input('\nDeseja continuar jogando?\n')
      if answer.lower() != 'sim':
        print('\nFim!')
        break
      print()