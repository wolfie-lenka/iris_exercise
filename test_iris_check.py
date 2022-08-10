import streamlit as st
import pytest
import pickle
from calc import predict_species

def test_iris():

   # Arrange
   sepal_length = 5.1
   sepal_width = 3.5
   petal_length = 1.4
   petal_width = 0.2

   # Assert
   assert predict_species(sepal_length, sepal_width, petal_length, petal_width) == "setosa"  

   
   
   
          
