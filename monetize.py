from flask import Flask

app = Flask(__name__)

@app.route('/get-proof')
def release_data():
    # This acts as your digital paywall
    return {
        "status": "Payment Required",
        "message": "Send 0.01 SOL to [Your-Wallet-Address] to unlock the V5.1 Forensic Key.",
        "node": "1501-P",
        "benchmark": "12.32 pI"
    }

if __name__ == '__main__':
    # Running on port 8080
    app.run(host='0.0.0.0', port=8080)
