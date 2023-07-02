# Topic Modeling and Software Requirements' Recommendation System using Transformers

## Abstract
The requirements elicitation phase is one of the most important challenges of Software Engineering. Incomplete or improperly defined requirements result in delays and increased costs during the software development process. In this context, a significant part of research in requirements engineering focuses on generating requirements recommendations based on past software projects, as well as on requirements understanding and validation. This thesis presents a topic modeling system designed for analyzing a pool of Functional Requirements derived from past projects. The system leverages the BERT model, which is based on the Transformer architecture, to identify the topics within the requirements. Furthermore, the topic modeling process is iteratively applied within each cluster, resulting in the formation of internal clusters within the original ones. Consequently, the requirements of each project are decomposed and categorized into individual clusters, enabling thus the engineer to better understand the project under consideration and to be able to easily compare it with similar projects.

Finally, a new dataset is constructed from these sub-groups, which is then utilized to fine-tune a pre-trained BART model. More specifically, pairs of relevant requirements are extracted and used to train the model so that it can propose new requirements based on existing ones.

Overall, the utilization of semantic information plays a crucial role in enhancing the relevance of the generated recommendations. By leveraging semantic analysis techniques, the system gains a deeper understanding of the underlying meaning and context within the requirements text. After evaluating the approach on a collection of requirements from software projects, it is demonstrated that it can be useful for engineers in the process of requirements elicitation in new software projects.

Chrysa Lampropoulou<br>
Electrical and Computer Engineering School<br>
Aristotle University of Thessaloniki, Greece<br>
June 2023<br>


## Code Run
### Topic Modeling
Perform Topic Modeling with the BERTopic technique using the /Topic Modeling/topic_modeling_final.ipynb notebook. The corresponding  dataset can be found in the /Datasets/Projects/ folder.

### BART fine-tuning
Fine-tune the BART model with the /BART Fine-Tuning/BART-fine-tuning-final.ipynb notebook. The corresponding  dataset is the /Datasets/BART_fine_tuning/all_clusters_df523.xlsx .

### Post-Processing Unit
Use the text file that can be found in /Post Processing/3epochs.txt to run the post-processing /Post Processing/APostProc.py .


