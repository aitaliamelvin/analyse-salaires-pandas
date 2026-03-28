import pandas as pd
import os
dossier = os.path.dirname(__file__)
fichier = os.path.join(dossier, "data.csv")
df = pd.read_csv(fichier)
print(df)

print(df["Nom"])

print(df["Salaire"].mean())

print(df[df["Age"] > 30])

df["Salaire_annuel"] = df["Salaire"] * 12
print(df)

print(df.groupby("Departement")["Salaire"].mean())

print("\n=== SALAIRE MOYEN ===")
print(df["Salaire"].mean())

print("\n=== SALAIRE MAX ===")
print(df["Salaire"].max())

print("\n=== + de 30 ANS ===")
print(df[df["Age"] > 30])

print("\n=== SALAIRE MOY DEPT ===")
print(df.groupby("Departement")["Salaire"].mean())

moyennes = df.groupby("Departement")["Salaire"].mean()
print(moyennes)
print("\nDept le mieux payé : ", moyennes.idxmax())

max_salaire = df["Salaire"].max()
personne = df[df["Salaire"] == max_salaire]
print(personne)


