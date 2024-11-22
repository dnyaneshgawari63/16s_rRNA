import pandas as pd
data = pd.read_csv("D:/FDS/Projects/16s_rRNA/DiabImmune_Metagenomic_sequencing_assay.txt", sep="\t")
data.to_csv("microbiome.csv", index=False)
df = pd.read_csv("D:/FDS/Projects/16s_rRNA/microbiome.csv")
print(df.head())
print(df.dtypes)
