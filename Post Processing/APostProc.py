# READ PROJECT REQUIREMENTS AND RECOMMENDATIONS
projects = []
import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()

with open('3epochs.txt') as infile:

	project = None
	readrequirements = False
	readrecommendations = False
	for line in infile:
		if line.startswith("Project "):
			if project:
				projects.append(project)
			project = {"requirements": [], "recommendations": []}
			project["name"] = line.split(':')[-1].strip()
		elif line.startswith("Requirements"):
			readrequirements = not readrequirements
		elif readrequirements:
			if not line.strip():
				readrequirements = not readrequirements
				continue
			project["requirements"].append(line.strip())
		elif line.startswith("Recommendations"):
			readrecommendations = not readrecommendations
		elif readrecommendations:
			if not line.strip():
				readrecommendations = not readrecommendations
				continue
			project["recommendations"].append(line.strip())

########################################################################


# PRINT RECOMMENDATIONS BEFORE PROCESSING
for p, project in enumerate(projects):
	print("\n\nPROJECT " + str(p+1) + " - " + project["name"])
	print("REQUIREMENTS")
	for i, r in enumerate(project["requirements"]):
		print("%2d. %s" %(i + 1, r))

	########################################################################

	# PROCESS RECOMMENDATIONS
	import nltk
	from nltk.corpus import stopwords
	from nltk.tokenize import word_tokenize
	# Uncomment the following line if stopwords are not downloaded
	# nltk.download('stopwords')
	thestopwords = set(stopwords.words("english"))
	thestopwords.update(["must", "be", "able", "to"])

	# Get tokens from requirements
	requirementstokens = []
	for r in project["requirements"]:
		rset = set([ps.stem(t).lower() for t in word_tokenize(r) if not (t.lower() in thestopwords or len(t.lower()) <= 2)])
		
		requirementstokens.append(rset)

	# Get tokens from recommendations and process them
	recommendationstokens = []
	newrecommendations = []
	for r in project["recommendations"]:
		# Heuristic changes
		r = r.replace("must be able to have the ability to", "must be able to") ## add here any other heuristic changes
		# Tokenization
		rset = set([ps.stem(t).lower() for t in word_tokenize(r) if not (t.lower() in thestopwords or len(t.lower()) <= 2)])
		# Remove recommendation if it only has one token
		if len(rset) <= 2: continue
		# Remove recommendation if it has a subset of same tokens as another set (either recommendation or requirement)
		if any(rset.issubset(aset) for aset in recommendationstokens) or \
				any(rset.issubset(aset) for aset in requirementstokens):
			continue
		recommendationstokens.append(rset)
		# Get final recommendation
		newrecommendations.append(r)

	########################################################################

	# PRINT RECOMMENDATIONS AFTER PROCESSING
	print("\nFINAL RECOMMENDATIONS")
	for i, r in enumerate(newrecommendations):
		print("%2d. %s" %(i + 1, r))
	
	print("-------------------------------------------------------------")
