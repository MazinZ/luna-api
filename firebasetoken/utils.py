import jwt  # Requires: pip install python-jwt
import Crypto.PublicKey.RSA as RSA  # Requires: pip install pycrypto

import datetime
import json
from firebasetoken.token import FIREBASE_KEY

def create_firebase_token(uid, username):
  
  #f = open('/Users/mazin/Development/luna/Luna-cc6e11f09f31.json', 'r')
  #content = f.read()
  #jsonFile = json.loads(content)

  # Get your service account's email address and private key from the JSON key file
  service_account_email = "token-gen@luna-c2c2f.iam.gserviceaccount.com"
  private_key = RSA.importKey(FIREBASE_KEY)
  try:
    payload = {
      "iss": service_account_email,
      "sub": service_account_email,
      "aud": "https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit",
      "uid": uid,
      "claims": {
        "username": username
      }
    }
    exp = datetime.timedelta(minutes=60)
    return jwt.generate_jwt(payload, private_key, "RS256", exp)
  except Exception as e:
    print "Error creating custom token: " + e.message
    return None