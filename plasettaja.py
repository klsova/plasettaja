import random
import pandas as pd

df = pd.read_csv("osallistujat.csv")

poydat = {
    "Pöytä 1": [],
    "Pöytä 2": []
}

def jaa_istumapaikat(df, poydat):
    vieraat = df.sample(frac=1).reset_index(drop=True)
    
    for i, vieras in vieraat.iterrows():
        if i < 60:
            poydat["Pöytä 1"].append(vieras)
        else:
            poydat["Pöytä 2"].append(vieras)
    return poydat

poydat = jaa_istumapaikat(df, poydat)

for poyta, vieraat in poydat.items():
    print(f"{poyta}:")
    for vieras in vieraat:
        print(f" {vieras['Nimi']} (Email: {vieras['Email']}, Seuruetoive: {vieras['Seuruetoive']} Ruokatoive: {vieras['Ruokatoive']}, Juomatoive: {vieras['Juomatoive']}, Ainejärjestö: {vieras['Ainejärjestö']}, Ilmoittautumisaika: {vieras['Ilmoittautumisaika']})")
    print()
    
def tallenna_istumapaikat(poydat, tiedostonimi):
    with open(tiedostonimi, "w") as f:
        f.write("Pöytä,Nimi,Email,Seuruetoive,Ruokatoive,Juomatoive,Ainejärjestö,Ilmoittautumisaika\n")
        for poyta, vieraat in poydat.items():
            for vieras in vieraat:
                f.write(f"{poyta},{vieras['Nimi']},{vieras['Email']},{vieras['Seuruetoive']},{vieras['Ruokatoive']},{vieras['Juomatoive']}, {vieras['Ainejärjestö']}, {vieras['Ilmoittautumisaika']}\n")
                
tallenna_istumapaikat(poydat, "plase.csv")