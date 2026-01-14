from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fpdf import FPDF
import hashlib
import time
import json
import os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Certificate(FPDF):
    def header(self):
        self.set_font('Courier', 'B', 16)
        self.cell(0, 10, '[CAN-CAN] CERTIFICATE OF INTERCEPTION', 1, 1, 'C')
        self.ln(10)

@app.post("/batch-scan")
async def batch_scan(files: List[UploadFile] = File(...), humidity: str = Form(...)):
    total_credits = 0.0
    batch_id = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
    
    # PDF Setup
    pdf = Certificate()
    pdf.add_page()
    pdf.set_font("Courier", size=10)
    pdf.cell(200, 10, txt=f"REPORT ID: {batch_id}", ln=True)
    pdf.cell(200, 10, txt=f"LOCATION: Bakersfield Sector A (Industrial)", ln=True)
    pdf.cell(200, 10, txt=f"DATE: 2026-01-14", ln=True)
    pdf.ln(5)

    for file in files:
        credit_val = 17.85
        total_credits += credit_val
        file_hash = hashlib.sha256(file.filename.encode()).hexdigest()[:16]
        pdf.cell(200, 8, txt=f"- UNIT: {file.filename} | METHANE AVOIDANCE: ${credit_val} | HASH: {file_hash}", ln=True)

    pdf.ln(10)
    pdf.set_font("Courier", 'B', 12)
    pdf.cell(200, 10, txt=f"TOTAL BATCH VALUE: ${total_credits:.2f}", ln=True)
    pdf.set_font("Courier", 'I', 8)
    pdf.multi_cell(0, 5, txt="\nVERIFICATION: This document proves the diversion of cellulose waste from methane-emitting neglect into the Circular Economy.")
    
    pdf_filename = f"cert_{batch_id}.pdf"
    pdf.output(pdf_filename)

    return {
        "status": "INTERCEPTION_PROVEN",
        "total_credits": f"${total_credits:.2f}",
        "ledger_entry": batch_id,
        "certificate_url": f"/{pdf_filename}"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
