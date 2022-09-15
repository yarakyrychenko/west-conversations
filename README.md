# west-conversations
:star: A template repository for linguistic analysis of conversations from scratch using [ConvoKit](https://github.com/CornellNLP/ConvoKit). 

## Goal

This repository provides a quick way to analyze custom conversational datasets by first converting them into a [ConvoKit](https://github.com/CornellNLP/ConvoKit) Corpus object. The ConvoKit module has many interesting [linguistic analyses](https://convokit.cornell.edu/documentation/transformers.html) you can run on your conversation data. This template covers creating a corpus from your data ([MakeConvokitCorpus.ipynb](https://github.com/yarakyrychenko/west-conversations/blob/39b56af3e3aee36b4a363fdb2f67753958ca4e4a/processing/MakeConvokitCorpus.ipynb)), basic descriptive statistics ([DescriptiveStatistics.ipynb](https://github.com/yarakyrychenko/west-conversations/blob/39b56af3e3aee36b4a363fdb2f67753958ca4e4a/analysis/DescriptiveStatistics.ipynb)), linguistic coordination ([LinguisticCoordination.ipynb](https://github.com/yarakyrychenko/west-conversations/blob/39b56af3e3aee36b4a363fdb2f67753958ca4e4a/analysis/LinguisticCoordination.ipynb)), and politness strategies speakers employ ([Politeness.ipynb](https://github.com/yarakyrychenko/west-conversations/blob/39b56af3e3aee36b4a363fdb2f67753958ca4e4a/analysis/Politeness.ipynb)).


## Using the Template 

- Step 1: Click the green button that says `Use this template` at the top. 
- Step 2: Follow the instructions on the screen to create your repository. 
- Step 3: Clone it to your local machine (you can use [GitHub Desktop](https://desktop.github.com/)).
- Step 4: Go to `.gitignore` and uncomment `data/` to keep your data private at all times. 
- Step 5: Upload your data (`master.csv` and `transcritps`) to your local repostiory. There is an example `master.csv` in this template to help you with formatting. 
- Step 6: Run [MakeConvokitCorpus.ipynb](https://github.com/yarakyrychenko/west-conversations/blob/39b56af3e3aee36b4a363fdb2f67753958ca4e4a/processing/MakeConvokitCorpus.ipynb) to create your corpus. 
- Step 7: Check out the python notebooks in the `analysis` folder.


## Template Structure 

    .
    ├── data
    │   ├── processed
    │   │   └── corpus
    │   └── raw
    │       ├── master.csv
    │       └── transcripts
    ├── processing
    │   └── MakeConvokitCorpus.ipynb
    ├── analysis
    │   ├── LinguisticCoordination.ipynb
    │   ├── DescriptiveStatistics.ipynb
    │   ├── Politeness.ipynb
    │   └── utils.py
    ├── results
    ├── viz
    └── README.md
    
