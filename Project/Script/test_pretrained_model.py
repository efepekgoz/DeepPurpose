import os
os.chdir('../')

import DeepPurpose.oneliner as oneliner
from DeepPurpose import dataset
import time
import pandas as pd

X_repurpose, drug_names, drug_CIDs = dataset.load_broad_repurposing_hub('./data')
"""def load_thousand_candidate(file_path='/Users/efepekgoz/Project/csv_files/thousand_candidate_drugs.tab'):
    # Read the tab-separated file from the local path
    df = pd.read_csv(file_path, sep='\t')  # Assuming the file is tab-separated
    df = df.fillna('UNK')
    return df['smiles'].values, df['title'].values, df['cid'].astype(str).values

X_repurpose, drug_names, drug_CIDs = load_thousand_candidate()"""
jak2 = 'MGMACLTMTEMEGTSTSSIYQNGDISGNANSMKQIDPVLQVYLYHSLGKSEADYLTFPSGEYVAEEICIAASKACGITPVYHNMFALMSETERIWYPPNHVFHIDESTRHNVLYRIRFYFPRWYCSGSNRAYRHGISRGAEAPLLDDFVMSYLFAQWRHDFVHGWIKVPVTHETQEECLGMAVLDMMRIAKENDQTPLAIYNSISYKTFLPKCIRAKIQDYHILTRKRIRYRFRRFIQQFSQCKATARNLKLKYLINLETLQSAFYTEKFEVKEPGSGPSGEEIFATIIITGNGGIQWSRGKHKESETLTEQDLQLYCDFPNIIDVSIKQANQEGSNESRVVTIHKQDGKNLEIELSSLREALSFVSLIDGYYRLTADAHHYLCKEVAPPAVLENIQSNCHGPISMDFAISKLKKAGNQTGLYVLRCSPKDFNKYFLTFAVERENVIEYKHCLITKNENEEYNLSGTKKNFSSLKDLLNCYQMETVRSDNIIFQFTKCCPPKPKDKSNLLVFRTNGVSDVPTSPTLQRPTHMNQMVFHKIRNEDLIFNESLGQGTFTKIFKGVRREVGDYGQLHETEVLLKVLDKAHRNYSESFFEAASMMSKLSHKHLVLNYGVCVCGDENILVQEFVKFGSLDTYLKKNKNCINILWKLEVAKQLAWAMHFLEENTLIHGNVCAKNILLIREEDRKTGNPPFIKLSDPGISITVLPKDILQERIPWVPPECIENPKNLNLATDKWSFGTTLWEICSGGDKPLSALDSQRKLQFYEDRHQLPAPKWAELANLINNCMDYEPDFRPSFRAIIRDLNSLFTPDYELLTENDMLPNMRIGALGFSGAFEDRDPTQFEERHLKFLQQLGKGNFGSVEMCRYDPLQDNTGEVVAVKKLQHSTEEHLRDFEREIEILKSLQHDNIVKYKGVCYSAGRRNLKLIMEYLPYGSLRDYLQKHKERIDHIKLLQYTSQICKGMEYLGTKRYIHRDLATRNILVENENRVKIGDFGLTKVLPQDKEYYKVKEPGESPIFWYAPESLTESKFSVASDVWSFGVVLYELFTYIEKSKSPPAEFMRMIGNDKQGQMIVFHLIELLKNNGRLPRPDGCPDEIYMIMTECWNNNVNQRPSFRDLALRVDQIRDNMAG'
mlh1 = 'MSFVAGVIRRLDETVVNRIAAGEVIQRPANAIKEMIENCLDAKSTSIQVIVKEGGLKLIQIQDNGTGIRKEDLDIVCERFTTSKLQSFEDLASISTYGFRGEALASISHVAHVTITTKTADGKCAYRASYSDGKLKAPPKPCAGNQGTQITVEDLFYNIATRRKALKNPSEEYGKILEVVGRYSVHNAGISFSVKKQGETVADVRTLPNASTVDNIRSIFGNAVSRELIEIGCEDKTLAFKMNGYISNANYSVKKCIFLLFINHRLVESTSLRKAIETVYAAYLPKNTHPFLYLSLEISPQNVDVNVHPTKHEVHFLHEESILERVQQHIESKLLGSNSSRMYFTQTLLPGLAGPSGEMVKSTTSLTSSSTSGSSDKVYAHQMVRTDSREQKLDAFLQPLSKPLSSQPQAIVTEDKTDISSGRARQQDEEMLELPAPAEVAAKNQSLEGDTTKGTSEMSEKRGPTSSNPRKRHREDSDVEMVEDDSRKEMTAACTPRRRIINLTSVLSLQEEINEQGHEVLREMLHNHSFVGCVNPQWALAQHQTKLYLLNTTKLSEELFYQILIYDFANFGVLRLSEPAPLFDLAMLALDSPESGWTEEDGPKEGLAEYIVEFLKKKAEMLADYFSLEIDEEGNLIGLPLLIDNYVPPLEGLPIFILRLATEVNWDEEKECFESLSKECAMFYSIRKQYISEESTLSGQQSEVPGSIPNSWKWTVEHIVYKALRSHILPPKHFTEDGNILQLANLPDLYKVFERC'

def load_target(target,target_name):
	target_name = "JAK2"
	return target, target_name

target, target_name = load_target(jak2, "JAK2")

"""def load_cancerxgene_drugs(file_path='/Users/efepekgoz/Project/csv_files/cancerxgene_set2.csv'):
    # Read the CSV file from the local path
    df = pd.read_csv(file_path, sep = ',')  # Assuming the CSV is comma-separated
    df = df.fillna('UNK')
    return df['smiles'].values, df['title'].values, df['cid'].astype(str).values

X_repurpose, drug_names, drug_CIDs = load_cancerxgene_drugs()
"""
#start = time.time()

"""oneliner.repurpose(target = target, 
                    target_name = target_name, 
                    X_repurpose = X_repurpose,
                    drug_names = drug_names,
                    save_dir = './save_folder',
                    pretrained_dir = './save_folder/pretrained_models/DeepPurpose_BindingDB/',
                    agg = 'mean')

"""
"""
df = pd.read_csv('depmap_targets_only.csv')
base_dir = './save_folder'
for i in range(1, 146):
    # Construct the directory name
    save_dir = f'{base_dir}{i}'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    target = df.loc[0, 'target']
    target_name = df.loc[0, 'target_name']
    df = df.drop(index=0).reset_index(drop=True)
  
    oneliner.repurpose(target = target, 
                    target_name = target_name, 
                    X_repurpose = X_repurpose,
                    drug_names = drug_names,
                    save_dir = './save_folder',
                    pretrained_dir = './save_folder/pretrained_models/DeepPurpose_BindingDB/',
                    agg = 'agg_mean_max')
"""

oneliner.repurpose(target = target, 
                target_name = target_name, 
                X_repurpose = X_repurpose,
                drug_names = drug_names,
                save_dir = './save_folder',
                pretrained_dir = './save_folder/pretrained_models/DeepPurpose_BindingDB/',
                agg = 'agg_mean_max')