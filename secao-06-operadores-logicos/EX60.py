verdadeiro_a = True
verdadeiro_b = True
falso_c = False

resultado_expressao_a = verdadeiro_a or (falso_c and not verdadeiro_b)
resultado_expressao_b = (verdadeiro_a or verdadeiro_b) and (verdadeiro_a and falso_c)

print('A=V, B=V, C=F')
print(f'a) A ou C e não B: {"Verdadeiro" if resultado_expressao_a else "Falso"}')
print(f'b) (A ou B) e (A e C): {"Verdadeiro" if resultado_expressao_b else "Falso"}')
