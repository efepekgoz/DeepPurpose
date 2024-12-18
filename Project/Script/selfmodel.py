from DeepPurpose import DTI
from DeepPurpose.utils import *
from DeepPurpose.dataset import *
from DeepPurpose import DTI as models

X_drug, X_target, y = load_process_DAVIS(path='/Users/efepekgoz/Project/selfmodel',binary=False)

drug_encoding, target_encoding = 'CNN', 'CNN'

train, val, test = data_process(X_drug, X_target, y, drug_encoding, \
                                    target_encoding, split_method='random', \
frac=[0.7,0.1,0.2], random_seed = 1)

print("generating config...")
config = generate_config(drug_encoding, target_encoding, \
                             cls_hidden_dims = [1024,1024,512], \
                             train_epoch = 100, LR = 0.001, batch_size = 256, \
                             cnn_drug_filters = [32,64,96], \
                             cnn_drug_kernels = [4,8,12], \
                             cnn_target_filters = [32,64,96], \
                             cnn_target_kernels = [4,8,12])


print("initializing model...")
model = models.model_initialize(**config)

model.train(train, val, test)