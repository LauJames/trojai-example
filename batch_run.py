import os
import csv

home = os.environ['HOME']
#folder_root = os.path.join(home,'data/trojai-round0-dataset')
#folder_root = os.path.join(home,'data/round1-dataset-train/models/')
folder_root = os.path.join(home,'data/round2-dataset-train/')
dirs = os.listdir(folder_root)


id_arch = dict()

def read_gt(filepath):
    rst = list()
    with open(filepath,'r',newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            rst.append(row)
    return rst

home = os.getenv('HOME')
gt_path = os.path.join(home,'data/round2-dataset-train/METADATA.csv')
gt_csv = read_gt(gt_path)
for row in gt_csv:
    id_arch[row['model_name']] = row['model_architecture']

k = 0
for i,d in enumerate(dirs):
  if not os.path.isdir(os.path.join(folder_root,d)):
    continue
  md_name = d.split('.')[0]

  #if not md_name == 'id-00000046': #benign
  #    continue
  #if not md_name == 'id-00000124': #trojaned
  #    continue
  #if not md_name == 'id-00000003': #benign
  #    continue
  if id_arch[md_name] != 'resnet18':
      continue


  fn = d.split('.')[0]
  num_str = fn.split('-')[1]
  num = int(num_str)
  model_filepath=os.path.join(folder_root, d, 'model.pt')
  examples_dirpath=os.path.join(folder_root, d, 'example_data')

  cmmd = 'CUDA_VISIBLE_DEVICES=0 python3 trojan_detector.py --model_filepath='+model_filepath+' --examples_dirpath='+examples_dirpath

  k = k+1

  #if k <= 6:
  #    continue

  print(k)
  print('folder ',i)
  print(cmmd)
  os.system(cmmd)
  #break

