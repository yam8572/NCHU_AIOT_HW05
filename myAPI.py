# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:11:21 2022

@author: yun
"""

from flask import Flask, render_template, jsonify
import pandas as pd
from six.moves import urllib
import json
 
def index2():
    return "test"
if __name__ == '__main__':
    print(index2())