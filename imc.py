def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25:
        return "Peso adequado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def obter_recomendacao(classificacao):
    recomendacoes = {
        "Baixo peso": "É recomendado procurar um médico para avaliação criteriosa do resultado. Pode indicar um estado de consumo do organismo, com poucas reservas e riscos associados.",
        "Peso adequado": "Tudo indica que está tudo bem, mas é importante avaliar outros parâmetros da composição corporal, para compreender se estão dentro do recomendado.",
        "Sobrepeso": "O sobrepeso está associado ao risco de doenças como diabetes e hipertensão. Consulte um médico e reveja hábitos para reverter o quadro.",
        "Obesidade grau I": "É importante buscar orientação médica e nutricional para entender melhor o seu caso, mesmo que os exames estejam normais.",
        "Obesidade grau II": "Indica um quadro de obesidade mais evoluído. Mesmo com exames laboratoriais dentro da normalidade, não se deve atrasar a busca por orientação médica e nutricional.",
        "Obesidade grau III": "Nesse ponto, a chance de já estarmos diante de outras doenças associadas é mais elevada. É fundamental buscar orientação médica."
    }
    return recomendacoes.get(classificacao, "")

def main():
    print("Calculadora de IMC")
    
    while True:
        try:
            peso = float(input("Digite seu peso em kg: "))
            altura = float(input("Digite sua altura em metros: "))
            
            if peso <= 0 or altura <= 0:
                raise ValueError("Peso e altura devem ser valores positivos.")
            
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)
            recomendacao = obter_recomendacao(classificacao)
            
            print(f"\nSeu IMC é: {imc:.2f}")
            print(f"Classificação: {classificacao}")
            print(f"Recomendação: {recomendacao}")
            
            break
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()