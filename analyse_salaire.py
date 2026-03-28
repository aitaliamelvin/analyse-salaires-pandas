import pandas as pd
import os
dossier = os.path.dirname(__file__)
fichier = os.path.join(dossier, "data.csv")
df = pd.read_csv(fichier)

def salaire_moyen(df):
    return df["Salaire"].mean()

def salaire_max(df):
    return df["Salaire"].max()

def plus_de_30_ans(df):
    return df[df["Age"] > 30]

def moyenne_par_departement(df):
    return df.groupby("Departement")["Salaire"].mean()

def departement_mieux_paye(df):
    moyennes = moyenne_par_departement(df)
    return moyennes.idxmax()

def personne_mieux_payee(df):
    max_salaire = df["Salaire"].max()
    return df[df["Salaire"] == max_salaire]

print("\n=== ANALYSE SALAIRE ===")
print("Salaire moyen : ", salaire_moyen(df))
print("Salaire max : ", salaire_max(df))
print("\nPlus de 30 ans : ", plus_de_30_ans(df))
print("\nMoyenne par département :\n", moyenne_par_departement(df))
print("\nDépartement le mieux payé : ", departement_mieux_paye(df))
print("\nPersonne(s) la/les mieux payée(s) :\n", personne_mieux_payee(df))

