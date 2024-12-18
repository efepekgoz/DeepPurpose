import pandas as pd

# First output data (screening)
screening_data = {
    'Phorbol 12-myristate 13-acetate': 37,
    'Mometasone furoate': 36,
    '[(1S,3S,5Z,7R,8Z,11S,12S,13E,15S,17R,21R,23S,25S)-25-Acetyloxy-1,11,21-trihydroxy-17-[(1R)-1-hydroxyethyl]-5,13-bis(2-methoxy-2-oxoethylidene)-10,10,26,26-tetramethyl-19-oxo-18,27,28,29-tetraoxatetracyclo[21.3.1.13,7.111,15]nonacos-8-en-12-yl] (2E,4E)-octa-2,4-dienoate': 28,
    'Mometasone': 28,
    'Brinzolamide': 23,
    'MK-8033': 22,
    'Azelastine': 22,
    'Clobetasol propionate': 22,
    "N'-(1,1-Dioxothian-4-yl)-5-ethyl-4-oxo-7-[3-(trifluoromethyl)phenyl]thieno[3,2-c]pyridine-2-carboximidamide": 22,
    'Androstanolone': 22,
    'Dorzolamide, (+/-)-(cis)-': 22,
    '2-(Phosphonomethyl)pentanedioic acid': 21,
    'Detrothyronine': 21,
    'Modrefen': 21,
    'Olaparib': 19,
    '[(6S,8S,9S,10S,11R,13S,14S,16S,17S)-17-(2-Chloroacetyl)-6,9-difluoro-11-hydroxy-10,13,16-trimethyl-3-oxo-6,7,8,11,12,14,15,16-octahydrocyclopenta[a]phenanthren-17-yl] propanoate': 19,
    'Tacrolimus': 19,
    "(Z)-N'-((6-Bromoimidazo[1,2-a]pyridin-3-yl)methylene)-N,2-dimethyl-5-nitrobenzenesulfonohydrazide": 19,
    'Olcegepant': 18,
    '(8R,10R,13S,14S,17R)-13-Ethyl-17-ethynyl-17-hydroxy-1,2,6,7,8,9,10,11,12,14,15,16-dodecahydrocyclopenta[a]phenanthren-3-one': 18,
    '2-[(3R,5R,6S)-5-(3-Chlorophenyl)-6-(4-chlorophenyl)-3-methyl-1-[(2S)-3-methyl-1-propan-2-ylsulfonylbutan-2-yl]-2-oxopiperidin-3-yl]acetic acid': 18,
    'Levonorgestrel': 18,
    'Adavosertib': 18,
    '[(6S,8S,9S,10S,11R,13S,14S,17S)-17-(2-Acetyloxyacetyl)-6,9-difluoro-11-hydroxy-10,13-dimethyl-3-oxo-6,7,8,11,12,14,15,16-octahydrocyclopenta[a]phenanthren-17-yl] butanoate': 18,
    'Progestoral': 18,
    'Cerdulatinib': 17,
    'Indatraline': 17,
    'Clobetasone butyrate': 17,
    '6-Chloro-9-((4-methoxy-3,5-dimethylpyridin-2-yl)methyl)-9H-purin-2-amine': 17,
    'Eticlopride': 17,
    'GW0742': 17,
    'Bupranolol': 16,
    '2-[2-Methoxy-4-(4-methyl-1-piperazinyl)anilino]-5,11-dimethyl-6-pyrimido[4,5-b][1,4]benzodiazepinone': 16,
    'Zolmitriptan': 16,
    'MK-0812': 16,
    'Calcipotriol': 16,
    '4-(3-Tert-Butylamino-2-hydroxypropoxy)benzimidazol-2-one': 16,
    'Meropenem': 15,
    '(2S,3S)-N-(2-Methoxybenzyl)-2-phenylpiperidin-3-amine': 15,
    'Granisetron': 15,
    'Raclopride': 15,
    'Idasanutlin': 15,
    'Spiperone': 15,
    'Tamsulosin': 14,
    'Ethoxzolamide': 14,
    '(10R,13S,17S)-17-Hydroxy-10,13-dimethyl-1,2,6,7,8,9,11,12,14,15,16,17-dodecahydrocyclopenta[a]phenanthren-3-one': 14,
    'Dexamethasone': 14,
    'Liothyronine': 13,
    'Isotretinoin': 13,
    'NNC-55-0396 Free base': 13,
    '8-[4-(4-Fluorophenyl)-4-oxobutyl]-3-(3-fluorobenzyl)-1-phenyl-1,3,8-triazaspiro[4.5]decan-4-one': 13,
    'Carazolol': 13,
    '4-{2-[(7-Amino-2-Furan-2-Yl[1,2,4]triazolo[1,5-A][1,3,5]triazin-5-Yl)amino]ethyl}phenol': 12,
    'Nandrolone': 12,
    '2-(Furan-2-yl)-7-phenethyl-7H-pyrazolo[4,3-e][1,2,4]triazolo[1,5-c]pyrimidin-5-amine': 12,
    'Timolol': 12,
    'Penbutolol': 12,
    'Carvedilol': 12,
    '4-(4-Fluoro-3-(4-methoxypiperidine-1-carbonyl)benzyl)phthalazin-1(2H)-one': 12,
    'Rolofylline': 12,
    'Topotecan': 12,
    'Fulvestrant': 12,
    'Luminespib': 12,
    'Estradiol': 12,
    'Nalfurafine': 11,
    'Ibrutinib': 11,
    '5-[2-Amino-4-chloro-7-[(4-methoxy-3,5-dimethylpyridin-2-yl)methyl]pyrrolo[2,3-d]pyrimidin-5-yl]-2-methylpent-4-yn-2-ol': 10,
    'Prepulsid': 9,
    'Flumethasone': 9,
    '3,4-Difluoro-2-(2-fluoro-4-iodophenylamino)-N-(2-hydroxyethoxy)-5-((3-oxomorpholino)methyl)benzamide': 8,
    'MK-2461': 8,
    'Alprenolol': 8,
    'Sobetirome': 8,
    'Norethindrone': 8,
    '(4R,5S)-3-[(3S,5S)-5-[(3-Carboxyphenyl)carbamoyl]pyrrolidin-3-yl]sulfanyl-6-[(1R)-1-hydroxyethyl]-4-methyl-7-oxo-1-azabicyclo[3.2.0]hept-2-ene-2-carboxylic acid': 8,
    'Darunavir': 8,
    '1-Cyclopropyl-3-(3-(5-(morpholinomethyl)-1H-benzo[d]imidazol-2-yl)-1H-pyrazol-4-yl)urea': 7,
    'Seocalcitol': 7,
    'Tretinoin': 7,
    '[2-(4-Tert-butyl-2-ethoxyphenyl)-4,5-bis(4-chlorophenyl)-4,5-dimethylimidazol-1-yl]-[4-(3-methylsulfonylpropyl)piperazin-1-yl]methanone': 6,
    'Camptothecin': 6,
    'Sertraline': 6,
    'Butofilolol': 6,
    'Cianidanol': 6,
    '10-Hydroxycamptothecin': 6,
    '(2-(2,6-Dimethoxy)phenoxyethylamino)methylbenzo-1,4-dioxane': 5,
    'Zacopride': 5,
    'Dipalmitoyl phosphatidylcholine': 5,
    'Prazosin': 5,
    '3,4-Difluoro-N-[2-[1-(3-fluorophenyl)-4-oxo-1,3,8-triazaspiro[4.5]decan-8-yl]ethyl]benzamide': 5,
    'Ascomycin, Streptomyces hygroscopicus': 4,
    'beta-Carotene': 4,
    'Etizolam': 4,
    'Maropitant': 4,
    'Xmd8-92': 4,
    '3-[(3-Hydroxy-2-phenylpropanoyl)oxy]-8,8-dimethyl-8-azoniabicyclo[3.2.1]octane': 4,
    '9-Aminocamptothecin': 4,
    '1-Methyl-N-pyridin-3-yl-6,7-dihydropyrrolo[2,3-f]indole-5-carboxamide': 4,
    'N-[2-[[(Hexahydro-2-oxo-1H-azepin-3-yl)amino]carbonyl]phenyl]-benzo[b]thiophene-2-carboxamide': 3,
    'N-(3-Aminopropyl)-N-[(1R)-1-(3-benzyl-7-chloro-4-oxochromen-2-yl)-2-methylpropyl]-4-methylbenzamide': 3,
    'Levothyroxine': 3,
    'Tiratricol': 3,
    'beta-Funaltrexamine': 3,
    'Danatrol': 3,
    'Pregna-1,4-diene-3,20-dione, 9-chloro-11,17,21-trihydroxy-16-methyl-, (11beta,16beta)-': 3,
    'Cyclohexanecarboxamide, n-[2-[4-(2-methoxyphenyl)-1-piperazinyl]ethyl]-n-2-pyridinyl-': 3,
    '1-Palmitoyl-2-linoleoyl-sn-glycero-3-phosphocholine': 2,
    '1-[3-[[(2R,3S,4R,5R)-5-(4-Amino-5-bromopyrrolo[2,3-d]pyrimidin-7-yl)-3,4-dihydroxyoxolan-2-yl]methyl-propan-2-ylamino]propyl]-3-(4-tert-butylphenyl)urea': 2,
    '(8S,9S,10S,11R,13S,14S,16S,17S)-9-Fluoro-11,17-dihydroxy-17-(2-hydroxyacetyl)-10,13,16-trimethyl-6,7,8,11,12,14,15,16-octahydrocyclopenta[a]phenanthren-3-one': 2,
    'Saxagliptin': 2,
    'Cyanopindolol': 2,
    'Aclidinium': 2,
    '1-Butyl-3-(3-hydroxypropyl)-8-(3-tricyclo[3.3.1.03,7]nonanyl)-7H-purine-2,6-dione': 2,
    'Pirinixic acid': 2,
    'Gestodene': 2,
    'Endurobol': 2,
    'Methyltestosterone': 2,
    'Abt-737': 2,
    'Forodesine': 2,
    '(S)-(-)-Pindolol': 1,
    'Retinal': 1,
    '(R)-6-(4-((4-Ethylpiperazin-1-yl)methyl)phenyl)-N-(1-phenylethyl)-7H-pyrrolo[2,3-d]pyrimidin-4-amine': 1,
    '1-(Isopropylamino)-3-(1-naphthyloxy)-2-propanol': 1,
    'Unii-5KK52HG8DY': 1,
    'Unii-772CP7W12N': 1,
    '[2-[(7R,9S,10R,11S,13S,14S,16R)-7-Chloro-11-hydroxy-10,13,16-trimethyl-3-oxo-17-propanoyloxy-7,8,9,11,12,14,15,16-octahydro-6H-cyclopenta[a]phenanthren-17-yl]-2-oxoethyl] propanoate': 1,
    'Pipenzolate': 1,
    'N-(6,8-Difluoro-2-methyl-4-quinolinyl)-N-[4-(dimethylamino)phenyl]urea': 1,
    '5-[(2R)-3-(Tert-butylamino)-2-hydroxypropoxy]-3,4-dihydro-2H-naphthalen-1-one': 1,
    'Latanoprost': 1,
    '4-[(4-Chloro-3-hydroxy-5,5,8,8-tetramethyl-6,7-dihydronaphthalene-2-carbonyl)amino]-2,6-difluorobenzoic acid': 1,
    'Golvatinib': 1,
    '4-(4-Fluorophenyl)-2-(4-hydroxyphenyl)-5-(4-pyridyl)-1H-imidazole': 1,
    '9-Chloro-2-(2-furyl)-(1,2,4)triazolo(1,5-c)quinazolin-5-imine': 1,
    '[2-[(1R,2S,4R,8S,9S,11S,12S,13R)-11-Hydroxy-6,9,13-trimethyl-16-oxo-5-oxa-7-azapentacyclo[10.8.0.02,9.04,8.013,18]icosa-6,14,17-trien-8-yl]-2-oxoethyl] acetate': 1,
    'Solifenacin': 1,
    'Xibenolol': 1,
    'Sulpiride': 1,
    '3-(1H-Indol-5-yl)-5-(4-((4-methylpiperazin-1-yl)methyl)phenyl)-1H-pyrrolo[2,3-b]pyridine': 1,
    'Stanozolol': 1,
    'Trimethoprim': 1
}

# Second output data (repurposing)
repurposing_data = {
    'Fulvestrant': 143,
    'GW0742': 143,
    '[(6S,8S,9S,10S,11R,13S,14S,16S,17S)-17-(2-Chloroacetyl)-6,9-difluoro-11-hydroxy-10,13,16-trimethyl-3-oxo-6,7,8,11,12,14,15,16-octahydrocyclopenta[a]phenanthren-17-yl] propanoate': 139,
    'Meropenem': 138,
    'Norethindrone': 125,
    'Dexamethasone': 109,
    'beta-Funaltrexamine': 104,
    'Butofilolol': 100,
    'Clobetasone butyrate': 77,
    '9-Aminocamptothecin': 72,
    '3-[(3-Hydroxy-2-phenylpropanoyl)oxy]-8,8-dimethyl-8-azoniabicyclo[3.2.1]octane': 70,
    'Seocalcitol': 67,
    'N-[2-[[(Hexahydro-2-oxo-1H-azepin-3-yl)amino]carbonyl]phenyl]-benzo[b]thiophene-2-carboxamide': 32,
    'Sertraline': 29,
    'Tiratricol': 24,
    '4-[(4-Chloro-3-hydroxy-5,5,8,8-tetramethyl-6,7-dihydronaphthalene-2-carbonyl)amino]-2,6-difluorobenzoic acid': 18,
    'Tacalcitol': 11,
    'Silodosin': 8,
    '(S)-(-)-Pindolol': 8,
    'Cyclohexanecarboxamide, n-[2-[4-(2-methoxyphenyl)-1-piperazinyl]ethyl]-n-2-pyridinyl-': 6,
    'UNK': 2,
    'N-(6,8-Difluoro-2-methyl-4-quinolinyl)-N-[4-(dimethylamino)phenyl]urea': 2,
    'Aclidinium': 2,
    'Emodin': 1,
    'Mometasone furoate': 1,
    'Prazosin': 1,
    'N-(Benzenesulfonyl)-2-[4-(4,9-diethoxy-3-oxo-1H-benzo[f]isoindol-2-yl)phenyl]acetamide': 1,
    '6-Chloro-9-((4-methoxy-3,5-dimethylpyridin-2-yl)methyl)-9H-purin-2-amine': 1,
    '(7R,9S,13S,14R,17R)-17-Ethynyl-17-hydroxy-7,13-dimethyl-1,2,4,6,7,8,9,11,12,14,15,16-dodecahydrocyclopenta[a]phenanthren-3-one': 1,
    'Dexpropranolol': 1,
    'Naltrexone': 1,
    'Buparlisib': 1,
    'Androstanolone': 1,
    '(1R,3R,6R,7S,8S,10R,12R,16S,17R)-8-Tert-butyl-6,12,17-trihydroxy-16-methyl-2,4,14,19-tetraoxahexacyclo[8.7.2.01,11.03,7.07,11.013,17]nonadecane-5,15,18-trione': 1
}

# Combine the two dictionaries
combined_data = {}

for drug, count in screening_data.items():
    if drug in repurposing_data:
        combined_data[drug] = [count, repurposing_data[drug]]
    else:
        combined_data[drug] = [count, 0]

for drug, count in repurposing_data.items():
    if drug not in combined_data:
        combined_data[drug] = [0, count]

df = pd.DataFrame.from_dict(combined_data, orient='index', columns=['Screening Count', 'Repurposing Count'])

df['Total Count'] = df['Screening Count'] + df['Repurposing Count']
df = df.sort_values(by='Total Count', ascending=False)

df.index.name = 'Drug Name'

df.to_csv('drug_counts.csv', index=True)

print("CSV file 'drug_counts.csv' created successfully.")


