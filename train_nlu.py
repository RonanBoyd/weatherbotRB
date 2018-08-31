from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, nlu_config, directory):
  training_data = load_data(data)

  # Creates an instance of the Trainer using the nlu_config
  trainer = Trainer(config.load(nlu_config))

  # Starts training
  trainer.train(training_data)

  # Tells the training data where to go
  trainer.persist(directory, fixed_model_name = 'nlu')

if __name__ == '__main__':
  # Calls trainer
  # Looks at the training data and spacy config files, and looks at the output directory
  train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')