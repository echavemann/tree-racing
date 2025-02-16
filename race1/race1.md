Tree Racing Race 1: Categorical Classifier

Due 3/2.

REQUIREMENTS

You must build a categorical classifying decision Tree in Cpp. This means features are categorical inputs (IE Labels, encoded as integers) and the target is a class, also encoded as an integer.

You MUST use the classical ID3 tree growing algorithm. This means you must MINIMIZE ENTROPY, or, equivalently, MAXIMIZE INFO GAIN. Any optimizations to the growth process are allowed, but ALL SPLITS MUST BE EVALUATED. 

ALL 3 BASE CASES OF ID3 MUST BE HANDLED.

Additionally, you must implement the following parameter:

min_samples_split: The number of samples required to generate a split. If the number of discrete samples must be greater than this when splitting - if not select the most common class. This should default to 2 - which should have no impact. This is used to control complexity and reduce overfitting.

REFERENCE

The only allowed reference is the ID3 Wikipedia page. Obviously I cannot stop you from using other references, but figuring it out directly from the ID3 page will be beneficial to learning. 
https://en.wikipedia.org/wiki/ID3_algorithm

You can also look up train test split and k fold cross validation.

TESTING
This dataset will be used in evaluation. There may be additional categorical -> categorical datasets that will be used - be aware that this is a very simple example. You should expect very high accuracy - likely 100% with 80% TTS
https://www.kaggle.com/datasets/fredericobreno/play-tennis
Datasets will be provided already encoded - you do not need to convert labels into integers.

SCORING
You will be submitting only a binary. Scoring will be 50% Training Speed, 40% Inference Speed, and 10% Accuracy Speed.
However, you must score 100% in-sample accuracy on the provided tennis dataset to be considered.

Submissions will be in binary form, with exact details coming soon. NO COMPILE TIME TRAINING OR PRELOADING. (sorry ryan). 

OTHER
The only allowed library is self.requires("fast-cpp-csv-parser/20191004"), from conancenter. you MUST use this to read the CSV. 
