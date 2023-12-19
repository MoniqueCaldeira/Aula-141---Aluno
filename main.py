from flask import Flask, jsonify, request
from demographic_filtering import output
from content_filtering import get_recommendations
import pandas as pd

