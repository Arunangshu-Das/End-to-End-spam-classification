# Spam Classification Model using Naive Bayes

This repository contains code for training and saving two Naive Bayes models (GaussianNB and MultinomialNB) for spam classification. The models are trained on a dataset stored in a MongoDB database. The text data is preprocessed using NLTK, and the models are serialized using the pickle library.

## Requirements
```
- Python 3.x
- pymongo
- pandas
- nltk
- scikit-learn
```

Install the required packages using the following command:

```
pip install pymongo pandas nltk scikit-learn
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Arunangshu-Das/End-to-End-spam-classification.git
cd End-to-End-spam-classification
```

2. Install the required dependencies.

3. Update the MongoDB connection string:
   - Open the script file `spam_classification.py`.
   - Locate the line containing the `MongoClient` connection creation.
   - Replace `url` with your own MongoDB connection string.

4. Run the script:

```bash
python spam_classification.py
```

The script will connect to the specified MongoDB database, retrieve the spam classification dataset, preprocess the text data, train two Naive Bayes models (GaussianNB and MultinomialNB), and print the accuracy scores for both models.

## Files

- `spam_classification.py`: Python script containing the code for training and saving the models.
- `GaussianNB.pkl`: Serialized file containing the trained GaussianNB model.
- `MultinomialNB.pkl`: Serialized file containing the trained MultinomialNB model.

Feel free to explore and modify the code according to your needs. Happy spam classification!
```

Update the MongoDB connection string in the script to match your own database.

Make sure to include the `GaussianNB.pkl`, `MultinomialNB.pkl`, and `README.md` files in the same directory as the `spam_classification.py` script.
