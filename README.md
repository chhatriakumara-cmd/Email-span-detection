# Email Spam Detection Web App

## Files
- `app.py`: Streamlit web application.
- `email_spam_detection_model.pkl`: trained model downloaded from Google Colab.
- `requirements.txt`: required Python packages.

## Publish online
1. Download the trained `email_spam_detection_model.pkl` from your Colab notebook.
2. Extract this ZIP file.
3. Put the `.pkl` model file in the same folder as `app.py`.
4. Create a GitHub repository and upload `app.py`, `requirements.txt`, and the `.pkl` file.
5. Open https://share.streamlit.io/ and connect your GitHub account.
6. Choose **Create app**, select your repository, branch `main`, and main file `app.py`.
7. Click **Deploy**. Streamlit will provide a public `*.streamlit.app` link.

## Important: match the scikit-learn version
A Joblib/pickle model should be loaded with a compatible scikit-learn version, ideally the same version used during training. In Colab, run:
`import sklearn; print(sklearn.__version__)`
Then pin that exact version in `requirements.txt`, for example:
`scikit-learn==1.6.1`
Replace `1.6.1` with the version printed in your Colab session.

Only load `.pkl` files you created or trust. Do not upload private emails or credentials.
