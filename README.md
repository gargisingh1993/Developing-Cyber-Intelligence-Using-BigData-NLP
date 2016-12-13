# Developing-Cyber-Intelligence-Using-BigData-NLP
BigData-FinalProject-Fall2016
/*
-----------------------------------------------------------------------------------------------------------------------------------------
README.txt - Final Analytics Code Drop
-----------------------------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------------------------
Name: Jubin Soni (jas1464)
Team Members: Balaji Reddy(bbr234), Gargi Singh(gsc326)
Project: Developing Cyber Intelligence
-----------------------------------------------------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------------------------------------------------
ALGORITHMS USED
-----------------------------------------------------------------------------------------------------------------------------------------
Please follow this file for execution of our Big Data Project and going through how our Analytic was developed. For developing the Analytic we divided the project into three parts:

1. Using MapReduce for Cleaning Code for two datasets: NVDVulnerability Dataset and Hackerforum Discussions.
2. Using NLTK and Multinomial Naive Bayes to do Sentiment Analysis (Natural Language Processing) on Hackerforum discussions.
3. Using Impala to develop the Analytic and getting the word count

-----------------------------------------------------------------------------------------------------------------------------------------
CODE EXECUTION
-----------------------------------------------------------------------------------------------------------------------------------------
First, download the three folders in finaldrop, and from that open JubinSoni(jas1464) folder, it contains three subfolders as below:
1. MapReduce_CleaningCode folder contains two MapReduce codes for two datasets each:
	-NVDVulnerability Dataset - MapReduce code is written to get the wordcount directly.
	-Hackerforum Discussions - MapReduce code is written to profile and clean the code and   bring it in desired format.
	Execute these MapReduce codes after putting the 'NVDVulnerabilityDataset.txt' and 'MRinputposts.csv' file on Dumbo cluster.

Now, copy the output of MapReduce job for MRinputposts.csv to your local computer and run the Sentiment Analysis code from the below folder:
2. NLP_SentimentAnalysisCode folder contains the train_model.py that is used to do the sentiment analysis and the output of Hackerforum discussions 
'MRinputposts_inputFile.csv' is fed into the train_model.py to do sentiment analysis of discussions and get pos/neg sentiments.

Next, copy the output of SentimentAnalysis back to Dubmo cluster and execute the impala commands given in below folder.
3. Impala_AnalyticsCode folder contains the Impala code and screenshots of the analytic. We executed the Impala code on Dumbo cluster and input file was output file of hackerforum I got after doing NLP (SentimentAnalysis).

-----------------------------------------------------------------------------------------------------------------------------------------
SCREENSHOTS
-----------------------------------------------------------------------------------------------------------------------------------------
Screenshots, Output files and Code are added in all three folders and also available on GitHub: https://github.com/jubins/Developing-Cyber-Intelligence-Using-BigData-NLP

Please let me know if you have any questions. jas1464@nyu.edu

-----------------------------------------------------------------------------------------------------------------------------------------
DATA SETS
-----------------------------------------------------------------------------------------------------------------------------------------
- The data set Hackerforum Discussions citation - 
Name:			Hackerforum Discussions
Description: This dataset contains the discussions of hackers and cyber securty enthusiats who try different techniques and discuss them on forums.
By University of Arizona Artificial Intelligence Lab, AZSecure-data, Director Hsinchun Chen
[AZSecure-data has not yet implemented Digital Object Identifiers or Persistent URLs, please 
copy and paste the location where you retrieve this file from within http://www.azsecure-data.org/]
Size of data: ~5 MB

- The data set NVDVulnerability Dataset citation - 
Name:           NVD Data Feeds 	
Description: The dataset contains an analysis of the CVEs from multiple sources. It includes information such as vulnerability severity and category of vulnerability. 
Size of data: ~500 MB
-----------------------------------------------------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------------------------------------------------
CONTACT
-----------------------------------------------------------------------------------------------------------------------------------------
GitHub: https://github.com/jubins/Developing-Cyber-Intelligence-Using-BigData-NLP
Email: Please let me know if you have any questions. jas1464@nyu.edu

-----------------------------------------------------------------------------------------------------------------------------------------
*/
