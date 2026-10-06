#!/usr/bin/env bash
# Starts backend (8000) and frontend (8501)
uvicorn legalEaseAPI.main:app --reload --port 8000 &
BACK=$!
trap "kill $BACK" EXIT
streamlit run frontend/app.py
