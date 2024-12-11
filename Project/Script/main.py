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

import time
from DeepPurpose import utils, DTI, dataset
import os
os.chdir('../')

#FILE_PATH = load_AID1706_txt_file()

def load_target(target,target_name):
	target_name = "mlh1isoform1"
	return target, target_name


def load_mlh1_assay(path = './data', binary = True, threshold = 15, balanced = True, oversample_num = 30, seed = 1):
	print('Beginning Processing...')
	if not os.path.exists(path):
		os.makedirs(path)

	target = 'MSFVAGVIRRLDETVVNRIAAGEVIQRPANAIKEMIENCLDAKSTSIQVIVKEGGLKLIQIQDNGTGIRKEDLDIVCERFTTSKLQSFEDLASISTYGFRGEALASISHVAHVTITTKTADGKCAYRASYSDGKLKAPPKPCAGNQGTQITVEDLFYNIATRRKALKNPSEEYGKILEVVGRYSVHNAGISFSVKKQGETVADVRTLPNASTVDNIRSIFGNAVSRELIEIGCEDKTLAFKMNGYISNANYSVKKCIFLLFINHRLVESTSLRKAIETVYAAYLPKNTHPFLYLSLEISPQNVDVNVHPTKHEVHFLHEESILERVQQHIESKLLGSNSSRMYFTQTLLPGLAGPSGEMVKSTTSLTSSSTSGSSDKVYAHQMVRTDSREQKLDAFLQPLSKPLSSQPQAIVTEDKTDISSGRARQQDEEMLELPAPAEVAAKNQSLEGDTTKGTSEMSEKRGPTSSNPRKRHREDSDVEMVEDDSRKEMTAACTPRRRIINLTSVLSLQEEINEQGHEVLREMLHNHSFVGCVNPQWALAQHQTKLYLLNTTKLSEELFYQILIYDFANFGVLRLSEPAPLFDLAMLALDSPESGWTEEDGPKEGLAEYIVEFLKKKAEMLADYFSLEIDEEGNLIGLPLLIDNYVPPLEGLPIFILRLATEVNWDEEKECFESLSKECAMFYSIRKQYISEESTLSGQQSEVPGSIPNSWKWTVEHIVYKALRSHILPPKHFTEDGNILQLANLPDLYKVFERC'

	#url = "https://pubchem.ncbi.nlm.nih.gov/assay/pcget.cgi?query=download&record_type=datatable&aid=720552&version=2.1&response_type=save"
	#url = "https://pubchem.ncbi.nlm.nih.gov/assay/pcget.cgi?query=download&record_type=datatable&aid=171&version=1.1&response_type=save"
	#saved_path_data = wget.download(url, path)
	saved_path_data = "./Project/csv_files/AID_171_clean.csv"
	
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


X_repurpose, drug_names, drug_CIDs = dataset.load_broad_repurposing_hub('./data')

"""
def load_cancerxgene_drugs(file_path='/Users/efepekgoz/Project/csv_files/cancerxgene_combined_drugs.csv'):
    # Read the CSV file from the local path
    df = pd.read_csv(file_path, sep = ',')  # Assuming the CSV is comma-separated
    df = df.fillna('UNK')
    return df['smiles'].values, df['title'].values, df['cid'].astype(str).values

X_repurpose, drug_names, drug_CIDs = load_cancerxgene_drugs()

def load_broad_depmap(file_path='/Users/efepekgoz/Project/csv_files/cancerxgene_combined_drugs.csv'):
    # Read the CSV file from the local path
    df = pd.read_csv(file_path, sep = ',')  # Assuming the CSV is comma-separated
    df = df.fillna('UNK')
    return df['smiles'].values, df['title'].values, df['cid'].astype(str).values

X_repurpose, drug_names, drug_CIDs = load_cancerxgene_drugs()


def load_thousand_candidate(file_path='/Users/efepekgoz/Project/csv_files/thousand_candidate_drugs.tab'):
    # Read the tab-separated file from the local path
    df = pd.read_csv(file_path, sep='\t')  # Assuming the file is tab-separated
    df = df.fillna('UNK')
    return df['smiles'].values, df['title'].values, df['cid'].astype(str).values

X_repurpose, drug_names, drug_CIDs = load_thousand_candidate()
"""

oneliner.repurpose(target = target, 
                    target_name = target_name, 
                    X_repurpose = X_repurpose,
                    drug_names = drug_names,					
                    train_drug = train_drug,
                    train_target = train_target,
                    train_y = train_y,
                    save_dir = './save_folder',
                    finetune_batch_size = 128,
                    finetune_LR = 0.001,
                    finetune_epochs=10,
                    split='HTS',
                    convert_y = False,
                    frac=[0.8,0.1,0.1],
                    pretrained = False,
                    agg = 'agg_mean_max')


"""oneliner.repurpose(*read_file_target_sequence('/Users/efepekgoz/Project/csv_files/target.txt'),
				   *read_file_repurposing_library('/Users/efepekgoz/Project/csv_files/repurpose.txt'),
				   *read_file_training_dataset_bioassay('/Users/efepekgoz/Project/csv_files/train.txt'),
				   split='HTS',convert_y = False, frac=[0.8,0.1,0.1],finetune_LR=1e-3,pretrained=False,
				   agg='max_effect',save_dir='./save_folder_jak2_binary'
				   )"""
"""oneliner.repurpose(*read_file_target_sequence('/Users/efepekgoz/Project/csv_files/target.txt'),
				   *read_file_repurposing_library('/Users/efepekgoz/Project/csv_files/repurpose.txt'),
				   save_dir='./save_folder_jak2_reg')"""
"""
oneliner.repurpose(*read_file_target_sequence('/Users/efepekgoz/Project/csv_files/target.txt'),
				   *read_file_repurposing_library('/Users/efepekgoz/Project/csv_files/repurpose.txt'),
				   save_dir='./save_folder_jak2_reg',agg='mean')
"""