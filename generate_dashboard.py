import sqlite3
import datetime

def build_dashboard():
    conn = sqlite3.connect('overlord_vault.db')
    # Pulling the latest audit and total equity
    audit = conn.execute("SELECT * FROM audits ORDER BY timestamp DESC LIMIT 1").fetchone()
    total_equity = conn.execute("SELECT SUM(valuation_usd) FROM audits").fetchone()[0] or 0
    
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ background: #0a0a0a; color: #ffd700; font-family: 'Courier New', monospace; padding: 20px; }}
            .box {{ border: 2px solid #ffd700; padding: 15px; margin-bottom: 20px; box-shadow: 0 0 15px #ffd700; }}
            h1 {{ text-shadow: 2px 2px #ff4500; font-size: 2em; }}
            .stat {{ font-size: 1.5em; margin: 10px 0; }}
            .oracle {{ color: #00ffff; }}
        </style>
    </head>
    <body>
        <h1>🔱 SOVEREIGN DASHBOARD: NODE 93307</h1>
        <div class="box">
            <div class="stat">STELLAR EQUITY: ${total_equity:,.2f}</div>
            <div class="stat">PHARMA YIELD: {audit[2] if audit else 0}mg (99.8% Purity)</div>
            <div class="stat">GENETIC ALPHA: {audit[8] if audit else '1.000'}</div>
        </div>
        <div class="box oracle">
            <h3>ORACLE PREDICTION: BULLISH</h3>
            <p>KERN BASIN METABOLIC VELOCITY: +0.082</p>
            <p>SIGMA-12 HASH: {audit[7] if audit else 'PENDING'}</p>
        </div>
        <div style="font-size: 0.8em;">LAST AUDIT: {audit[0] if audit else 'N/A'} | EIN: 39-2261270</div>
    </body>
    </html>
    """
    with open("dashboard.html", "w") as f:
        f.write(html_content)
    print("🔱 DASHBOARD UPDATED: Open ~/dashboard.html in your browser.")

if __name__ == "__main__":
    build_dashboard()
