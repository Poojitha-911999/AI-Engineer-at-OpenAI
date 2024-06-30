from datasets import load_dataset
import pandas as pd


dataset = load_dataset('imdb')


train_df = pd.DataFrame(dataset['train'])
test_df = pd.DataFrame(dataset['test'])


print(train_df.head())


print(test_df.head())
