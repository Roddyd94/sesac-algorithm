from collections import defaultdict
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pokemon = []
pokemon_dict = defaultdict()

for i in range(N):
    name = input().rstrip()
    pokemon.append(name)
    pokemon_dict[name] = i + 1

for i in range(M):
    input_string = input().rstrip()

    if input_string[0] >= "0" and input_string[0] <= "9":
        input_num = int(input_string)
        print(pokemon[input_num - 1])
        continue

    print(pokemon_dict[input_string])
