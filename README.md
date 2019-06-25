# Markov-text-generator
Generates text based on Markov chains, after learning a corpus.


### Initialisation

Clone the git folder, cd into the folder and install Numpy : <br>
```
git clone https://github.com/nitinkgp23/Markov-text-generator.git
cd Markov-text-generator
pip install numpy
```

### Usage
To learn a bunch of text (larger the corpus, better it learns), run the command <br>
`python learnText.py <path/to/text/file>`

To generate new text, run the command <br>
`python generateText.py` <br> or to begin from a specific word, run <br>
`python generateText.py beginWord`

For e.g., after learning the Harry Potter books, and to start new text genaration from the word 'Harry', do this: <br>
`python generateText.py Harry`
