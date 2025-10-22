# Big Data

# Introdução 
Projeto relizado pelo aluno **Matheus Marques Eiras** para a diciplina de sexto perio do curso de ciência da computação no Instituto Federal do Paraná (IFPR-Pinhais).

Este projeto procura desenvolver um modelo de *Named Entity Recognition* (NER) em que busca recohecer uma serie de entidades

# Entidades usadas 
| Dataset                        | Entidades                                                                                                                                                                                                                                                               | Liceça             |
| :----------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------: |
| Multilingual NER Dataset       | {'O': 0, 'B-PER': 1, 'I-PER': 2, 'B-ORG': 3, 'I-ORG': 4, 'B-LOC': 5, 'I-LOC': 6, 'B-MISC': 7, 'I-MISC': 8}                                                                                                                                                              | CC0: Public Domain |
| LeNER-Br: Portuguese Legal NER | {"O", "B-ORGANIZACAO", "I-ORGANIZACAO", "B-PESSOA", "I-PESSOA", "B-TEMPO", "I-TEMPO", "B-LOCAL", "I-LOCAL", "B-LEGISLACAO", "I-LEGISLACAO", "B-JURISPRUDENCIA", "I-JURISPRUDENCIA}                                                                                      | CC0: Public Domain |
| HAREM Portuguese NER Corpus    | {"O", "B-PESSOA", "I-PESSOA", "B-ORGANIZACAO", "I-ORGANIZACAO", "B-LOCAL", "I-LOCAL", "B-TEMPO", "I-TEMPO", "B-VALOR", "I-VALOR", "B-ABSTRACCAO", "I-ABSTRACCAO", "B-ACONTECIMENTO", "I-ACONTECIMENTO", "B-COISA", "I-COISA", "B-OBRA", "I-OBRA", "B-OUTRO", "I-OUTRO"} | CC0: Public Domain |

# Desenvovimento

## Datasets utiluzados
- MultL: https://www.kaggle.com/datasets/thedevastator/multilingual-ner-dataset | https://huggingface.co/datasets/Babelscape/wikineural
- LeNER-Br: https://www.kaggle.com/datasets/thedevastator/lener-br-portuguese-legal-ner-dataset | https://github.com/peluz/lener-br/blob/master/leNER-Br/train/train.conll
- HAREM: https://www.kaggle.com/datasets/thedevastator/harem-portuguese-ner-corpus | https://github.com/gdutramartins/po-ner-2-portuguese-ner/tree/main/dataset

# Execução

## Instalação 

Para roda este codigo é necessario instalar o CUDA Tool kit da nvidia instalado, o compilador de C/C++, o pytorch referente a verção do CUDA instalado no sistema e as dependencias descritas no *requirements.txt* 

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.9