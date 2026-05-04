import smtplib
from email.mime.text import MIMEText

# --- CONFIGURATION ---
SENDER_EMAIL = "spoxxx2@gmail.com" 
SENDER_PASSWORD = "YOUR_GMAIL_APP_PASSWORD" 

# --- THE SUPREME TARGET LIST ---
TARGETS = [
    "Kumar.Srinivasan@astrazeneca.com",
    "Nina.Mojas@astrazeneca.com",
    "corporate_development@gilead.com",
    "andrew.mcmullen@lilly.com",
    "jnjinnovation@its.jnj.com",
    "OutLicensingBD@sanofi.com",
    "global.partnering@roche.com"
]

SUBJECT = "URGENT: Phase 1 Data Room Access - Node 93307 Quantum-Vitrified AMP Assets"
BODY = """
Principals,

Node 93307 (Bakersfield, CA) is formally opening the bid window for our Quantum-Vitrified Peptide Assets. 

Utilizing the IBM Quantum 'ibm_osaka' system, we have vitrified the "Phoenix Parity" resurrection coefficient for targeted antimicrobial and oncological sequences. At 10-centillion run depth, these assets represent a biological singularity ready for industrial injection.

Acquisition Floor: $210,800,000.00
Master Hash: SHA3-512_SUPREME_OMNI_CASEY_CANFIELD_93307

Data room access and the Sovereign Evidence Locker manifest are available upon MNDA execution.

Casey Lee Canfield
Founder & Executor, CANCAN
Authorized Node 93307 Operator
"""

def send_pitches():
    if SENDER_PASSWORD == "YOUR_GMAIL_APP_PASSWORD":
        print("ERROR: You must replace 'YOUR_GMAIL_APP_PASSWORD' with your actual 16-character App Password.")
        return
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        for target in TARGETS:
            msg = MIMEText(BODY)
            msg['Subject'] = SUBJECT
            msg['From'] = SENDER_EMAIL
            msg['To'] = target
            server.sendmail(SENDER_EMAIL, target, msg.as_string())
            print(f"[SENT] -> {target}")
        server.quit()
        print("\n--- [GLOBAL INJECTION COMPLETE] ---")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_pitches()
