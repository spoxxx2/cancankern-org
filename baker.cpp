#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ofstream site("index.html");
    site << "<!DOCTYPE html>\n<html lang='en'>\n<head>\n"
         << "<meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
         << "<title>CANCANKERN | Platinum Zenith</title>\n"
         << "<style>:root { --plat: #e5e4e2; --neon: #00ff41; --bg: #0a0a0a; }\n"
         << "body { font-family: 'Courier New', monospace; background: var(--bg); color: var(--neon); padding: 20px; line-height: 1.5; }\n"
         << ".section { border: 1px solid #333; padding: 20px; margin-bottom: 20px; background: #111; }\n"
         << ".platinum-card { border: 2px solid var(--plat); color: var(--plat); padding: 15px; text-align: center; margin: 10px 0; }\n"
         << ".tag { background: var(--neon); color: #000; padding: 2px 5px; font-weight: bold; }\n"
         << "a { color: var(--neon); text-decoration: none; border-bottom: 1px solid var(--neon); }\n"
         << "a:hover { background: var(--neon); color: #000; }\n"
         << "</style></head><body>\n"
         << "<header><h1>CANCANKERN <span class='tag'>PLATINUM ZENITH NODE</span></h1>\n"
         << "<p>501(c)(3) Non-Profit | 1501 Pearl St | Bakersfield, CA</p></header>\n"
         << "<div class='section'><h3>🛡️ Founder's Daily Directive</h3><p><i>\"The archive is live. 318 units secured. The Zenith Matrix is now a citeable scientific asset.\"</i></p></div>\n"
         << "<div class='section'><h3>📊 Audit Metrics (Q1 2026)</h3>"
         << "<ul><li><b>Audited Units:</b> 318</li>"
         << "<li><b>DOI:</b> 10.5281/zenodo.cancankern.2026.01</li>"
         << "<li><b>Carbon Impact:</b> 326.90 kg CO2e Sequestrated</li></ul>"
         << "<a href='PLATINUM_REPORT.md'>View Full Impact Report</a></div>\n"
         << "<div class='section'><h3>🤖 AI & Commercial Licensing</h3>"
         << "<div class='platinum-card'>PLATINUM DATA ACCESS ACTIVE</div>"
         << "<p>Proprietary training data for AI/ML sorting robots and climate modeling. Includes hyperspectral metadata and 100-year decay forecasts.</p>"
         << "<a href='mailto:licensing@cancankern.org'>Request API License</a></div>\n"
         << "<footer><p>© 2026 CANCANKERN™ | USPTO Patent Pending CC-KERN-2026</p></footer>\n"
         << "</body></html>";
    site.close();
    std::cout << "🚀 Platinum Site Baked: Optimized for AI/ML Outreach." << std::endl;
    return 0;
}
