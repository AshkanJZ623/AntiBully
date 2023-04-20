Here you can find the results of the training using the whole dataset instances. test have been done using 5000 sentences, 2500 Offensive and 2500 non-offensive.

Here are the parameters used for this training:

%run "/content/AntiBully/text/train.py" -bs=32 -lr=3e-6 -ep=2 -pa=3 --model=bert --task=a --clip --cuda=0 --dataset=train_kids_test_kids

Further testing is able to perform using the saved model (pytorch_model.bin), using the mytestsentence.py script

You can find the diagrams, the model, log and confusion matrix and everything here.