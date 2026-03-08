import hashlib, json, base64, time, sys
try:
    with open(sys.argv[1], 'r') as f: challenge_data = json.loads(f.read())
    algorithm = challenge_data.get('algorithm', 'SHA-256')
    challenge = challenge_data.get('challenge', '')
    salt = challenge_data.get('salt', '')
    signature = challenge_data.get('signature', '')
    maxnumber = int(challenge_data.get('maxNumber', challenge_data.get('maxnumber', 1000000)))
    start = time.time()
    for n in range(maxnumber + 1):
        test = hashlib.sha256((salt + str(n)).encode('utf-8')).hexdigest()
        if test == challenge:
            took = int((time.time() - start) * 1000)
            payload = {"algorithm": algorithm, "challenge": challenge, "number": n, "salt": salt, "signature": signature, "took": took}
            sys.stdout.write(base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8') + "\n")
            sys.exit(0)
    sys.exit(1)
except Exception as e:
    sys.stderr.write("ERROR: " + str(e) + "\n")
    sys.exit(1)
