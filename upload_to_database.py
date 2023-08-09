# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 16:23:28 2023

@author: MANaser
"""

import streamlit_authenticator as stauth

import database as db

usernames = ["mohamed", "shimaa", "maryam", "jannah", "sarah", "nadia"]
names = ["Mohamed Naser", "Shimaa Abdelsalam", "Maryam Naser", "Jannah Naser", "Sarah Naser", "Nadia Naser"]
passwords = ["moh77", "shi86", "mar10", "jan12", "sar18", "nad55"]
hashed_passwords = stauth.Hasher(passwords).generate()

for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
    db.insert_user(username, name, hash_password)