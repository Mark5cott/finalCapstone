# Project Name: Garden Path Sentence Analysis with spaCy

## Description
This project demonstrates the use of the spaCy open-source library for Natural Language Processing (NLP) to analyze and tokenize garden path sentences. Garden path sentences are sentences that initially lead a reader to interpret them in one way but then require them to reanalyze what they have read as more information is revealed. The project showcases the tokenization and named entity recognition capabilities of spaCy.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Credits](#credits)

## Installation
To install and run this project on your local Windows device, follow these steps:

1. Make sure you have Python installed on your machine. If not, download and install the latest version of Python from the official Python website (https://www.python.org/downloads/).

2. Open a command prompt or terminal.

3. Install the spaCy library by running the following command:
```shell
pip install spacy
```

4. Download the English language model for spaCy by running the following command:
```shell
python -m spacy download en_core_web_sm
```

5. Once the installation is complete, you can run the code using a Python interpreter or an integrated development environment (IDE) of your choice.

## Usage
To use this project, follow these steps:

1. Ensure that you have installed spaCy and downloaded the English language model as described in the installation section.

2. Open a Python interpreter or IDE (e.g., Visual Studio).

3. Copy and paste the provided code into your Python environment (amend the garden path sentences starting on line 13, if you want to test this on other sentences)

4. Execute the code.

5. The program will tokenize the garden path sentences and print the output (see screenshot below)

<img width="388" alt="image" src="https://github.com/Mark5cott/finalCapstone/assets/127673887/9a6e6745-1528-4a8d-896d-85b1c9223f51">

6. It will also perform named entity recognition (NER) and print the recognized entities in each sentence.

7. Additionally, the program includes explanations of the recognized entities 'FAC' and 'GPE' from spaCy (change the spaCy entity code to obtain other explanations)

## Credits
Author: Mark Scott / Hyperion

