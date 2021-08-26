import csv

time = input("Time: ").lower()

print("-"*100)
print("Data\tMandante\tVisitante")

with open("C:\\Users\\augus\OneDrive\Documentos\\archive\\campeonato-brasileiro-full.csv", 'r', encoding="utf-8") as arquivo:

    results = csv.reader(arquivo)

    for line in results:
        tokens = line[0].split(';')

        data = tokens[2]
        mandante = tokens[5].lower()
        visitante = tokens[6].lower()
        golsMandante = tokens[9]
        golsVisitante = tokens[10]

        ano = data.split('-')[0]

        if (ano == "2014" or ano == "2015") and (visitante == time or mandante == time):
            print("-"*100)
            print(f"{data}\t|{mandante}= {golsMandante}\t|{visitante}= {golsVisitante}")


