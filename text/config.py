OLID_PATH = '/content/AntiBully/text/OLIDv1.0'
GERMEVAL_PATH = './GermEval2018'
PERSIAN_PATH  = './Persian'
SAVE_PATH = './content/drive/MyDrive/save'

'''
COLAB: /content/drive/MyDrive/checkpoint.pth'
'''
# CHECKPOINT_SAVE_PATH = input("Enter the location that you want to save the checkpoint: ")
'''
LOCALHOST: ./dataset
COLAB: /content/AntiBully/dataset,
KAGGLE: /kaggle/working/AntiBully/dataset)
'''
KIDS_PATH = './'

# SAVE_PT_RESULT_PATH = input("Enter the .pt result path savefile: ")

'''
C:/Users/Ashkan_JZ/Desktop/AntiBully/save/results/kidstrainresults.pt
'''

SAVE_MODEL_PATH = './'

'''
'C:/Users/Ashkan_JZ/Desktop/AntiBully/save/results'
'''

LABEL_DICT_OLID = dict()
LABEL_DICT_GERMEVAL = dict()
LABEL_DICT_EN_DE = dict()
LABEL_DICT_FA = dict()
LABEL_DICT_KIDS = dict()


ID_LABEL = 'id'
TWEET_LABEL = 'tweet'

TASKS = ['a', 'b', 'c']

TASK_PREFIX = 'subtask_'
TASK_A_LABEL = TASK_PREFIX + 'a'
TASK_B_LABEL = TASK_PREFIX + 'b'
TASK_C_LABEL = TASK_PREFIX + 'c'
