import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def util_data(request):
	cropdata = pd.read_csv("static/csv/modified_cropdata.csv")

	# split the dataset into features (X) and target variable (y)
	X = cropdata.drop("CROP", axis=1)
	y = cropdata["CROP"]

	# split the dataset into training and testing sets
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

	# train a decision tree classifier
	clf = DecisionTreeClassifier(random_state=42)
	clf.fit(X_train, y_train)

	# evaluate the accuracy of the model
	y_pred = clf.predict(X_test)
	accuracy = accuracy_score(y_test, y_pred)
	print("Accuracy:", accuracy)

	# save the trained model as a pickle file
	joblib.dump(clf, "static/pkl/crop_classifier.pkl")
	return JsonResponse({"Accuracy":accuracy},safe=False)

@csrf_exempt
def crop_analyze(request):
    if request.method == 'POST':
        clf = joblib.load('static/pkl/crop_classifier.pkl')

        N_SOIL = request.POST['N_SOIL']
        P_SOIL = request.POST['P_SOIL']
        K_SOIL = request.POST['K_SOIL']
        TEMPARATURE = request.POST['TEMPARATURE']
        HUMIDITY = request.POST['HUMIDITY']
        PH = request.POST['PH']
        RAINFALL = request.POST['RAINFALL']

        X = pd.DataFrame([[N_SOIL,P_SOIL,K_SOIL,TEMPARATURE,HUMIDITY,PH,RAINFALL]],columns=["N_SOIL","P_SOIL","K_SOIL","TEMPERATURE","HUMIDITY","ph","RAINFALL"])
        prediction = {"prediction":clf.predict(X)[0]}

        return JsonResponse(prediction,safe=False)