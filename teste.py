import csv

print("-"*100)
print("Data\tMandante\tVisitante")
print("-"*100)

with open("C:\\Users\\augus\OneDrive\Documentos\\archive\\campeonato-brasileiro-full.csv", 'r') as arquivo:

    results = csv.reader(arquivo)

    for line in results:
        tokens = line[0].split(';')

        data = tokens[2]
        mandante = tokens[5]
        visitante = tokens[6]

        if(data.split('-')[0] == "2014"):
            print("-"*100)
            print(f"{data}\t|{mandante}\t|{visitante}")



