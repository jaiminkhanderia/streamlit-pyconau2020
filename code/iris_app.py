import numpy as np
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
import streamlit as st


@st.cache
def load_data():
    iris_data = datasets.load_iris()
    return iris_data


@st.cache
def train(features, targets):
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(features, targets)
    return clf


def predict(clf, feature):
    return clf.predict(feature)


def display_sidebar(feature_names, features):
    feature = []
    for index, feature_name in enumerate(feature_names):
        value = st.sidebar.slider(feature_name, float(np.min(features[:, index])), float(np.max(features[:, index])),
                                  float(np.median(features[:, index])))
        feature.append(value)
    feature = np.array(feature).reshape((1, len(feature_names)))
    return feature


def main():
    st.markdown("# Iris flower type prediction app")
    st.write("This app predicts the iris flower type based on user inputs")

    iris_data = load_data()
    features = iris_data.data
    targets = iris_data.target
    feature_names = iris_data.feature_names
    
    clf = train(features, targets)

    st.sidebar.markdown("## User defined input features")
    feature = display_sidebar(feature_names, features)
    
    st.write("Feature")
    st.write(feature)

    prediction = predict(clf, feature)[0]
    predicted_class = iris_data.target_names[prediction]
    st.subheader(f"Model predicted class _{predicted_class}_ for the given user inputs")
    
    st.balloons()


if __name__ == "__main__":
    main()
