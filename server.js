require('./db');
require('./db');
const express = require("express");
const fs = require("fs");
const path = require("path");
const app = express();

app.use(express.json({ limit: "10mb" }));
app.use(express.static(__dirname));
// --- Directories ---
const LOG_DIR = path.join(__dirname, "logs");
const SUMMARY_DIR = path.join(__dirname, "summaries");

if (!fs.existsSync(LOG_DIR)) fs.mkdirSync(LOG_DIR);
if (!fs.existsSync(SUMMARY_DIR)) fs.mkdirSync(SUMMARY_DIR);

console.log("💚⚡ CANCAN HQ — Neon Pulse Backend v4 ACTIVE");

// ============================================================
//  MAIN ENDPOINT — RECEIVE FIELD LOGS
// ============================================================

app.post("/api/cancan", (req, res) => {
    const data = req.body;

    const entry = {
        timestamp: data.timestamp,
        filename: data.filename,
        unit: data.unit,
        version: data.version,
        signature: data.signature,
        hash: data.hash,
        mood: data.mood,
        received_at: Date.now()
    };

    const filePath = path.join(LOG_DIR, `${entry.timestamp}.json`);
    fs.writeFileSync(filePath, JSON.stringify(entry, null, 2));

    console.log(`💚⚡ [HQ] Log received from ${entry.unit}: ${entry.filename}`);

    res.status(200).send({ status: "ok" });
});

// ============================================================
//  HEARTBEAT ENDPOINT
// ============================================================

app.post("/api/cancan/heartbeat", (req, res) => {
    const hb = {
        unit: req.body.unit,
        timestamp: req.body.timestamp,
        version: req.body.version
    };

    console.log(
        `💚⚡ [heartbeat] ${hb.unit} alive at ${new Date(
            hb.timestamp * 1000
        ).toLocaleTimeString()}`
    );

    res.status(200).send({ status: "alive" });
});

// ============================================================
//  MOOD ENGINE
// ============================================================

function computeMood() {
    const files = fs
        .readdirSync(LOG_DIR)
        .filter((f) => f.endsWith(".json"))
        .sort()
        .slice(-10);

    if (files.length === 0) return "quiet";
    if (files.length > 8) return "high activity";
    if (files.length > 4) return "steady";
    if (files.length > 1) return "light activity";

    return "quiet";
}

// ============================================================
//  DAILY SUMMARY ENGINE
// ============================================================

setInterval(() => {
    const now = new Date();

    if (now.getHours() === 0 && now.getMinutes() === 0) {
        const files = fs
            .readdirSync(LOG_DIR)
            .filter((f) => f.endsWith(".json"));

        const summary = {
            date: now.toDateString(),
            total_logs: files.length,
            mood: computeMood(),
            version: "cancan",
            generated_at: Date.now()
        };

        const filePath = path.join(
            SUMMARY_DIR,
            `summary_${now.toISOString().slice(0, 10)}.json`
        );

        fs.writeFileSync(filePath, JSON.stringify(summary, null, 2));

        console.log("💚⚡ [summary] Daily summary generated");
    }
}, 60000);

// ============================================================
//  DASHBOARD FEED
// ============================================================

app.get("/dashboard/feed", (req, res) => {
    const files = fs
        .readdirSync(LOG_DIR)
        .filter((f) => f.endsWith(".json"))
        .sort()
        .reverse()
        .slice(0, 50);

    const entries = files.map((f) => {
        const raw = fs.readFileSync(path.join(LOG_DIR, f));
        return JSON.parse(raw);
    });

    res.json({
        entries,
        mood: computeMood(),
        version: "cancan"
    });
});

// ============================================================
//  START SERVER
// ============================================================

app.listen(3000, () => {
    console.log("💚⚡ CANCAN HQ listening on port 3000");
});
/* -------------------------------------------
   CANCAN — Supabase Civic Organ Routes
   -------------------------------------------
   Adds:
   - /ping-db
   - /event
   - /cleanup
   - /heartbeat
   - /metric
   ------------------------------------------- */

const client = require("./db");

// Ping DB — confirms Supabase connection
app.get("/ping-db", async (req, res) => {
  try {
    const result = await client.query("SELECT NOW()");
    res.json({ ok: true, time: result.rows[0].now });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// Events spine — logs organism events
app.post("/event", async (req, res) => {
  const { type, source, payload } = req.body;

  try {
    const result = await client.query(
      "INSERT INTO events (type, source, payload) VALUES ($1, $2, $3) RETURNING *",
      [type, source, payload]
    );
    res.json({ ok: true, event: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// Cleanup organ — logs cleanup actions
app.post("/cleanup", async (req, res) => {
  const { block_id, volunteer_id, items_collected, notes } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO cleanups (block_id, volunteer_id, items_collected, notes)
       VALUES ($1, $2, $3, $4)
       RETURNING *`,
      [block_id, volunteer_id, items_collected, notes]
    );
    res.json({ ok: true, cleanup: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// Heartbeat organ — logs organism pulse
app.post("/heartbeat", async (req, res) => {
  const { module, status, message } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO heartbeat_logs (module, status, message)
       VALUES ($1, $2, $3)
       RETURNING *`,
      [module, status, message]
    );
    res.json({ ok: true, heartbeat: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// Metrics organ — logs dashboard metrics
app.post("/metric", async (req, res) => {
  const { metric, value, metadata } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO metrics (metric, value, metadata)
       VALUES ($1, $2, $3)
       RETURNING *`,
      [metric, value, metadata]
    );
    res.json({ ok: true, metric: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});


/* -------------------------------------------
   CANCAN — Supabase Civic Organ Routes
   -------------------------------------------
   Adds:
   - /ping-db
   - /event
   - /cleanup
   - /heartbeat
   - /metric
   ------------------------------------------- */

const client = require("./db");

// Ping DB — confirms Supabase connection
app.get("/ping-db", async (req, res) => {
  try {
    const result = await client.query("SELECT NOW()");
    res.json({ ok: true, time: result.rows[0].now });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// Events spine — logs organism events
app.post("/event", async (req, res) => {
  const { type, source, payload } = req.body;

  try {
    const result = await client.query(
      "INSERT INTO events (type, source, payload) VALUES ($1, $2, $3) RETURNING *",
      [type, source, payload]
    );
    res.json({ ok: true, event: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// Cleanup organ — logs cleanup actions
app.post("/cleanup", async (req, res) => {
  const { block_id, volunteer_id, items_collected, notes } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO cleanups (block_id, volunteer_id, items_collected, notes)
       VALUES ($1, $2, $3, $4)
       RETURNING *`,
      [block_id, volunteer_id, items_collected, notes]
    );
    res.json({ ok: true, cleanup: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// Heartbeat organ — logs organism pulse
app.post("/heartbeat", async (req, res) => {
  const { module, status, message } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO heartbeat_logs (module, status, message)
       VALUES ($1, $2, $3)
       RETURNING *`,
      [module, status, message]
    );
    res.json({ ok: true, heartbeat: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// Metrics organ — logs dashboard metrics
app.post("/metric", async (req, res) => {
  const { metric, value, metadata } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO metrics (metric, value, metadata)
       VALUES ($1, $2, $3)
       RETURNING *`,
      [metric, value, metadata]
    );
    res.json({ ok: true, metric: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});


/* -------------------------------------------
   CANCAN — Additional Civic Organ Routes
   -------------------------------------------
   Adds:
   - /block
   - /volunteer
   - /daily-report
   ------------------------------------------- */

// Create a block (map organ)
app.post("/block", async (req, res) => {
  const { name, lat, lon } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO blocks (name, lat, lon)
       VALUES ($1, $2, $3)
       RETURNING *`,
      [name, lat, lon]
    );
    res.json({ ok: true, block: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// Register a volunteer (community organ)
app.post("/volunteer", async (req, res) => {
  const { name, phone } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO volunteers (name, phone)
       VALUES ($1, $2)
       RETURNING *`,
      [name, phone]
    );
    res.json({ ok: true, volunteer: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// Daily report writer (memory organ)
app.post("/daily-report", async (req, res) => {
  const { date, summary, metrics, doi } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO daily_reports (date, summary, metrics, doi)
       VALUES ($1, $2, $3, $4)
       RETURNING *`,
      [date, summary, metrics, doi]
    );
    res.json({ ok: true, report: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});


/* -------------------------------------------
   CANCAN — DOI Archive Organ Routes
   -------------------------------------------
   Adds:
   - /doi
   - /doi-list
   ------------------------------------------- */

// Create a DOI entry (archive organ)
app.post("/doi", async (req, res) => {
  const { doi, title, url, metadata } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO dois (doi, title, url, metadata)
       VALUES ($1, $2, $3, $4)
       RETURNING *`,
      [doi, title, url, metadata]
    );
    res.json({ ok: true, doi: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// List all DOIs (public archive)
app.get("/doi-list", async (req, res) => {
  try {
    const result = await client.query(
      "SELECT * FROM dois ORDER BY created_at DESC"
    );
    res.json({ ok: true, dois: result.rows });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});


/* -------------------------------------------
   CANCAN — System Log Organ Routes
   -------------------------------------------
   Adds:
   - /system-log
   - /system-log-list
   ------------------------------------------- */

// Write a system log entry (reflex memory)
app.post("/system-log", async (req, res) => {
  const { level, module, message, context } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO system_logs (level, module, message, context)
       VALUES ($1, $2, $3, $4)
       RETURNING *`,
      [level, module, message, context]
    );
    res.json({ ok: true, log: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// List system logs (for debugging or dashboards)
app.get("/system-log-list", async (req, res) => {
  try {
    const result = await client.query(
      "SELECT * FROM system_logs ORDER BY timestamp DESC LIMIT 200"
    );
    res.json({ ok: true, logs: result.rows });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});


/* -------------------------------------------
   CANCAN — System Log Organ Routes
   -------------------------------------------
   Adds:
   - /system-log
   - /system-log-list
   ------------------------------------------- */

// Write a system log entry (reflex memory)
app.post("/system-log", async (req, res) => {
  const { level, module, message, context } = req.body;

  try {
    const result = await client.query(
      `INSERT INTO system_logs (level, module, message, context)
       VALUES ($1, $2, $3, $4)
       RETURNING *`,
      [level, module, message, context]
    );
    res.json({ ok: true, log: result.rows[0] });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});

// List system logs (for debugging or dashboards)
app.get("/system-log-list", async (req, res) => {
  try {
    const result = await client.query(
      "SELECT * FROM system_logs ORDER BY timestamp DESC LIMIT 200"
    );
    res.json({ ok: true, logs: result.rows });
  } catch (err) {
    res.json({ ok: false, error: err.message });
  }
});


/* -------------------------------------------
   CANCAN — Serve Dashboard as Homepage
   ------------------------------------------- */
const path = require("path");
app.use("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public/index.html"));
});

