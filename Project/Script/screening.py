from DeepPurpose import oneliner
from DeepPurpose.dataset import *
import pandas as pd
import numpy as np
import wget
from zipfile import ZipFile
from DeepPurpose.utils import *
import json
import os
import requests
import re
import wget
import assays
import random
import time
from DeepPurpose import utils, DTI, dataset
import os
os.chdir('../')


def load_target(target,target_name):
	target_name = "mlh1isoform1"
	return target, target_name


def load_mlh1_assay(path = './data', binary = True, threshold = 15, balanced = True, oversample_num = 30, seed = 1):
	print('Beginning Processing...')
	if not os.path.exists(path):
		os.makedirs(path)

	target = 'MSFVAGVIRRLDETVVNRIAAGEVIQRPANAIKEMIENCLDAKSTSIQVIVKEGGLKLIQIQDNGTGIRKEDLDIVCERFTTSKLQSFEDLASISTYGFRGEALASISHVAHVTITTKTADGKCAYRASYSDGKLKAPPKPCAGNQGTQITVEDLFYNIATRRKALKNPSEEYGKILEVVGRYSVHNAGISFSVKKQGETVADVRTLPNASTVDNIRSIFGNAVSRELIEIGCEDKTLAFKMNGYISNANYSVKKCIFLLFINHRLVESTSLRKAIETVYAAYLPKNTHPFLYLSLEISPQNVDVNVHPTKHEVHFLHEESILERVQQHIESKLLGSNSSRMYFTQTLLPGLAGPSGEMVKSTTSLTSSSTSGSSDKVYAHQMVRTDSREQKLDAFLQPLSKPLSSQPQAIVTEDKTDISSGRARQQDEEMLELPAPAEVAAKNQSLEGDTTKGTSEMSEKRGPTSSNPRKRHREDSDVEMVEDDSRKEMTAACTPRRRIINLTSVLSLQEEINEQGHEVLREMLHNHSFVGCVNPQWALAQHQTKLYLLNTTKLSEELFYQILIYDFANFGVLRLSEPAPLFDLAMLALDSPESGWTEEDGPKEGLAEYIVEFLKKKAEMLADYFSLEIDEEGNLIGLPLLIDNYVPPLEGLPIFILRLATEVNWDEEKECFESLSKECAMFYSIRKQYISEESTLSGQQSEVPGSIPNSWKWTVEHIVYKALRSHILPPKHFTEDGNILQLANLPDLYKVFERC'

	url = "https://pubchem.ncbi.nlm.nih.gov/assay/pcget.cgi?query=download&record_type=datatable&aid=720552&version=2.1&response_type=save"
	#saved_path_data = wget.download(url, path)
	saved_path_data = "./Project/csv_files/mlh1_assay_AID_171.csv"
	
	url = 'https://github.com/futianfan/DeepPurpose_Data/blob/main/AID1706_training_conversions.csv?raw=true'
	#saved_path_conversion = wget.download(url, path)
	saved_path_conversion = "./Project/csv_files/mlh1_modified_conversions.csv"

	df_data = pd.read_csv(saved_path_data)
	df_conversion = pd.read_csv(saved_path_conversion)
	val = df_data.iloc[4:][['PUBCHEM_CID','PUBCHEM_ACTIVITY_SCORE']]
	
	val['binary_label'] = 0
	val['binary_label'][(val.PUBCHEM_ACTIVITY_SCORE >= threshold) & (val.PUBCHEM_ACTIVITY_SCORE <=100)] = 1

	if balanced:
		val = pd.concat([val[val.binary_label==0].sample(n = len(val[val.binary_label==1]) * oversample_num, replace = True, random_state = seed), pd.concat([val[val.binary_label==1]]*oversample_num, ignore_index=True)]).sample(frac = 1, replace = False, random_state = seed).reset_index(drop = True)

	cid2smiles = dict(zip(df_conversion[['cid','smiles']].values[:, 0], df_conversion[['cid','smiles']].values[:, 1]))
	X_drug = [cid2smiles[i] for i in val.PUBCHEM_CID.values]

	if binary:
		print('Default binary threshold for the binding affinity scores is 15, recommended by the investigator')
		y = val.binary_label.values
	else:
		y = val.PUBCHEM_ACTIVITY_SCORE.values

	print('Done!')
	return np.array(X_drug), target, np.array(y)


mlh1 = 'MSFVAGVIRRLDETVVNRIAAGEVIQRPANAIKEMIENCLDAKSTSIQVIVKEGGLKLIQIQDNGTGIRKEDLDIVCERFTTSKLQSFEDLASISTYGFRGEALASISHVAHVTITTKTADGKCAYRASYSDGKLKAPPKPCAGNQGTQITVEDLFYNIATRRKALKNPSEEYGKILEVVGRYSVHNAGISFSVKKQGETVADVRTLPNASTVDNIRSIFGNAVSRELIEIGCEDKTLAFKMNGYISNANYSVKKCIFLLFINHRLVESTSLRKAIETVYAAYLPKNTHPFLYLSLEISPQNVDVNVHPTKHEVHFLHEESILERVQQHIESKLLGSNSSRMYFTQTLLPGLAGPSGEMVKSTTSLTSSSTSGSSDKVYAHQMVRTDSREQKLDAFLQPLSKPLSSQPQAIVTEDKTDISSGRARQQDEEMLELPAPAEVAAKNQSLEGDTTKGTSEMSEKRGPTSSNPRKRHREDSDVEMVEDDSRKEMTAACTPRRRIINLTSVLSLQEEINEQGHEVLREMLHNHSFVGCVNPQWALAQHQTKLYLLNTTKLSEELFYQILIYDFANFGVLRLSEPAPLFDLAMLALDSPESGWTEEDGPKEGLAEYIVEFLKKKAEMLADYFSLEIDEEGNLIGLPLLIDNYVPPLEGLPIFILRLATEVNWDEEKECFESLSKECAMFYSIRKQYISEESTLSGQQSEVPGSIPNSWKWTVEHIVYKALRSHILPPKHFTEDGNILQLANLPDLYKVFERC'

tp53 = 'MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD'

tp53bp1 = 'MDPTGSQLDSDFSQQDTPCLIIEDSQPESQVLEDDSGSHFSMLSRHLPNLQTHKENPVLDVVSNPEQTAGEERGDGNSGFNEHLKENKVADPVDSSNLDTCGSISQVIEQLPQPNRTSSVLGMSVESAPAVEEEKGEELEQKEKEKEEDTSGNTTHSLGAEDTASSQLGFGVLELSQSQDVEENTVPYEVDKEQLQSVTTNSGYTRLSDVDANTAIKHEEQSNEDIPIAEQSSKDIPVTAQPSKDVHVVKEQNPPPARSEDMPFSPKASVAAMEAKEQLSAQELMESGLQIQKSPEPEVLSTQEDLFDQSNKTVSSDGCSTPSREEGGCSLASTPATTLHLLQLSGQRSLVQDSLSTNSSDLVAPSPDAFRSTPFIVPSSPTEQEGRQDKPMDTSVLSEEGGEPFQKKLQSGEPVELENPPLLPESTVSPQASTPISQSTPVFPPGSLPIPSQPQFSHDIFIPSPSLEEQSNDGKKDGDMHSSSLTVECSKTSEIEPKNSPEDLGLSLTGDSCKLMLSTSEYSQSPKMESLSSHRIDEDGENTQIEDTEPMSPVLNSKFVPAENDSILMNPAQDGEVQLSQNDDKTKGDDTDTRDDISILATGCKGREETVAEDVCIDLTCDSGSQAVPSPATRSEALSSVLDQEEAMEIKEHHPEEGSSGSEVEEIPETPCESQGEELKEENMESVPLHLSLTETQSQGLCLQKEMPKKECSEAMEVETSVISIDSPQKLAILDQELEHKEQEAWEEATSEDSSVVIVDVKEPSPRVDVSCEPLEGVEKCSDSQSWEDIAPEIEPCAENRLDTKEEKSVEYEGDLKSGTAETEPVEQDSSQPSLPLVRADDPLRLDQELQQPQTQEKTSNSLTEDSKMANAKQLSSDAEAQKLGKPSAHASQSFCESSSETPFHFTLPKEGDIIPPLTGATPPLIGHLKLEPKRHSTPIGISNYPESTIATSDVMSESMVETHDPILGSGKGDSGAAPDVDDKLCLRMKLVSPETEASEESLQFNLEKPATGERKNGSTAVAESVASPQKTMSVLSCICEARQENEARSEDPPTTPIRGNLLHFPSSQGEEEKEKLEGDHTIRQSQQPMKPISPVKDPVSPASQKMVIQGPSSPQGEAMVTDVLEDQKEGRSTNKENPSKALIERPSQNNIGIQTMECSLRVPETVSAATQTIKNVCEQGTSTVDQNFGKQDATVQTERGSGEKPVSAPGDDTESLHSQGEEEFDMPQPPHGHVLHRHMRTIREVRTLVTRVITDVYYVDGTEVERKVTEETEEPIVECQECETEVSPSQTGGSSGDLGDISSFSSKASSLHRTSSGTSLSAMHSSGSSGKGAGPLRGKTSGTEPADFALPSSRGGPGKLSPRKGVSQTGTPVCEEDGDAGLGIRQGGKAPVTPRGRGRRGRPPSRTTGTRETAVPGPLGIEDISPNLSPDDKSFSRVVPRVPDSTRRTDVGAGALRRSDSPEIPFQAAAGPSDGLDASSPGNSFVGLRVVAKWSSNGYFYSGKITRDVGAGKYKLLFDDGYECDVLGKDILLCDPIPLDTEVTALSEDEYFSAGVVKGHRKESGELYYSIEKEGQRKWYKRMAVILSLEQGNRLREQYGLGPYEAVTPLTKAADISLDNLVEGKRKRRSNVSSPATPTASSSSSTTPTRKITESPRASMGVLSGKRKLITSEEERSPAKRGRKSATVKPGAVGAGEFVSPCESGDNTGEPSALEEQRGPLPLNKTLFLGYAFLLTMATTSDKLASRSKLPDGPTGSSEEEEEFLEIPPFNKQYTESQLRAGAGYILEDFNEAQCNTAYQCLLIADQHCRTRKYFLCLASGIPCVSHVWVHDSCHANQLQNYRNYLLPAGYSLEEQRILDWQPRENPFQNLKVLLVSDQQQNFLELWSEILMTGGAASVKQHHSSAHNKDIALGVFDVVVTDPSCPASVLKCAEALQLPVVSQEWVIQCLIVGERIGFKQHPKYKHDYVSH'

train_drug, train_target, train_y = load_mlh1_assay('./data', seed = 1234)

print("train_drug: ",train_drug)

print("train_target: ",train_target)

print("train_y: ",train_y)

target, target_name = load_target(mlh1, "mlh1 isoform 1")
#target, target_name = load_target(tp53bp1, "TP53 binding protein 1")

def load_cancerxgene_drugs(file_path='/Users/efepekgoz/Project/csv_files/cancerxgene_combined_drugs.csv'):
    
    df = pd.read_csv(file_path, sep = ',') 
    df = df.fillna('UNK')
    return df['smiles'].values, df['title'].values, df['cid'].astype(str).values

def load_broad_depmap(file_path='/Users/efepekgoz/Project/csv_files/broad_depmap_combined.csv'):
    
    df = pd.read_csv(file_path, sep=',')  
    df = df.fillna('UNK')
    return df['smiles'].values, df['TARGET_SEQUENCE'].values, df['X_repurpose'].values, df['target_name'].values
def load_broad_depmapX(file_path='/Users/efepekgoz/Project/csv_files/broad_depmap_combined.csv'):
   
    df = pd.read_csv(file_path, sep=',')  
    df = df.fillna('UNK')
    return df['smiles'].values#, df['TARGET_SEQUENCE'].values, df['X_repurpose'].values, df['target_name'].values
def load_broad_depmapT(file_path='/Users/efepekgoz/Project/csv_files/broad_depmap_combined.csv'):
    
    df = pd.read_csv(file_path, sep=',')  
    df = df.fillna('UNK')
    return df['TARGET_SEQUENCE'].values#df['smiles'].values, df['TARGET_SEQUENCE'].values, df['X_repurpose'].values, df['target_name'].values

#X_repurpose, drug_names, drug_CIDs = dataset.load_broad_repurposing_hub('./data')
#X_repurpose, drug_names, drug_CIDs = load_cancerxgene_drugs()

"""oneliner.virtual_screening(target=load_broad_depmapT(),
					X_repurpose=load_broad_depmapX(),
					target_name = load_broad_depmap(), 
					drug_names = load_broad_depmap(),
					train_drug = load_broad_depmap(), 
					train_target = load_broad_depmap(), 
					train_y = load_broad_depmap(), 
					save_dir = './save_folder',               
					pretrained_dir = None,
					finetune_epochs = 10,
					finetune_LR = 0.01,
					finetune_batch_size = 32,
					convert_y = True,
					subsample_frac = 1,
					pretrained = True,
					split = 'random',
					frac = [0.7,0.1,0.2],
					agg = 'agg_mean_max',
					output_len = 30)
"""

#oneliner.virtual_screening(*load_IC50_1000_Samples())
#oneliner.virtual_screening(*load_broadxdepmapfull(),save_dir='./save_folder3')

"""X_repurpose, target, drug_names, target_names = load_broadxdepmapfull()
oneliner.virtual_screening(X_repurpose, target, drug_names=drug_names, target_name=target_names, save_dir='./save_folder3')
"""

def shuffle_columns(file_path='/Users/efepekgoz/Project/csv_files/broad_depmap_combined_repeat.csv', output_path='/Users/efepekgoz/Project/csv_files/shuffled_file.csv'):
    
    df = pd.read_csv(file_path)

    random_numbers = list(range(6111))
    random.shuffle(random_numbers)

    df['Column1_Shuffled'] = df.iloc[random_numbers, 0].values
    df['Column3_Shuffled'] = df.iloc[random_numbers, 2].values

    df.iloc[:, 0] = df['Column1_Shuffled']
    df.iloc[:, 2] = df['Column3_Shuffled']

    df.drop(columns=['Column1_Shuffled', 'Column3_Shuffled'], inplace=True)

    df.to_csv(output_path, index=False)

    print(f"Columns 1 and 3 have been shuffled and saved to '{output_path}'.")

base_dir = './save_folder'
for i in range(1, 100):
    save_dir = f'{base_dir}{i}'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    shuffle_columns()
    X_repurpose, target, drug_names, target_names = load_broadxdepmapfull()
    oneliner.virtual_screening(X_repurpose, target, drug_names=drug_names, target_name=target_names, save_dir=save_dir)



#shuffle_columns('./csv_files/broad_depmap_combined_repeat.csv', './csv_files/shuffled_file.csv')
