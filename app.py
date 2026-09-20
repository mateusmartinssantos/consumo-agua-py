'''
    app: Consumo de água 
    opções:
    Comercial
    Casa
    Apartamento

Implemente a classificação de acordo com as seguintes regras de negócio: o Se o tipo for "comercial", exibir:
"Tarifa comercial aplicada – consulte o plano corporativo."
Se o tipo for "apartamento" e o consumo for menor que 10 𝑚3 , exibir: "Consumo econômico – excelente controle de água!"
Se o tipo for "apartamento" ou for "casa" com consumo de até 25 𝑚3 , exibir: "Consumo moderado – dentro do padrão residencial."
Em qualquer outro caso (consumo acima do limite residencial), exibir: "Consumo excessivo – adote medidas de economia e verifique vazamentos.
'''
from sqlmodel import case


tipo = input("Digite o tipo de consumo (Comercial, Casa, Apartamento): ")
consumo = float(input("Digite o consumo de água em metros cúbicos: "))

match tipo:
    case "Comercial" | "comercial":
        print("Tarifa Comercial - consulte o plano coorporativo.")

    case "Apartamento" | "apartamento" if consumo <= 10:
        print("Tarifa economica -  excelente controle de água!")

    case "Apartamento" | "apartamento" if consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")

    case "Casa" | "casa" if consumo <= 10:
            print("Tarifa economica -  excelente controle de água!")

    case "Casa" | "casa" if consumo <= 25:
            print("Consumo moderado – dentro do padrão residencial.")
    case _: 
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

    
    