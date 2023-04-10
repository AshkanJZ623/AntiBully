Here you can find the results of the training using 40k instances, 17467 Offensive and 22533 non-offensive. test have been done using 5000 sentences, 2500 Offensive and 2500 non-offensive.

Here are the parameters used for this training:

python -u "c:\Users\Ashkan_JZ\Desktop\AntiBully\train.py" -bs=16 -lr=3e-6 -ep=5 -pa=3 --model=bert --task=a --clip --cuda=0 --dataset=train_kids_test_kids

Further testing is able to perform using the saved model (pytorch_model.bin), using the mytestsentence.py script

You can find the diagrams, the model, log and confusion matrix and everything here.