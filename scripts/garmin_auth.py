#!/usr/bin/env python3.11
"""Garmin Connect authentication script.
Saves session tokens for reuse by other scripts.
Usage: python3 garmin_auth.py <email> <password> [mfa_code]
"""
import sys
import os
import json
from pathlib import Path
from garminconnect import Garmin

TOKEN_DIR = "/tmp/garmin_session/tokens"

def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Usage: garmin_auth.py <email> <password> [mfa_code]"}))
        sys.exit(1)

    email = sys.argv[1]
    password = sys.argv[2]

    # Ensure token directory exists
    Path(TOKEN_DIR).mkdir(parents=True, exist_ok=True)

    try:
        api = Garmin(email=email, password=password)
        result = api.login(tokenstore=TOKEN_DIR)

        # If MFA is required, result contains state for resume
        if result and result[0] == "MFA_REQUIRED":
            if len(sys.argv) >= 4:
                mfa_code = sys.argv[3]
                api.resume_login(json.loads(result[1]), mfa_code)
                api.login(tokenstore=TOKEN_DIR)
            else:
                print(json.dumps({
                    "status": "mfa_required",
                    "message": "MFA code needed. Re-run with: garmin_auth.py <email> <password> <mfa_code>",
                    "client_state": result[1]
                }))
                sys.exit(0)

        # Verify login worked
        name = api.get_full_name()
        print(json.dumps({
            "status": "success",
            "name": name,
            "token_path": TOKEN_DIR,
            "message": f"Logged in as {name}. Tokens saved."
        }))

    except Exception as e:
        error_type = type(e).__name__
        print(json.dumps({
            "status": "error",
            "error_type": error_type,
            "message": str(e)
        }))
        sys.exit(1)

if __name__ == "__main__":
    main()
