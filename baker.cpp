#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ofstream site("index.html");
    site << "<!DOCTYPE html>\n<html><head><style>"
         << "body { font-family: 'Courier New'; background: #0a0a0a; color: #00ff41; padding: 20px; }"
         << ".btn { display: inline-block; padding: 10px; border: 2px solid #e5e4e2; color: #e5e4e2; text-decoration: none; margin: 10px 5px; font-weight: bold; }"
         << ".btn:hover { background: #e5e4e2; color: #000; }"
         << ".section { border-left: 3px solid #00ff41; padding-left: 15px; margin-bottom: 30px; }"
         << "</style></head><body>"
         << "<h1>CANCANKERN <span style='background:#00ff41; color:#000; padding:2px 5px;'>PLATINUM PORTAL</span></h1>"
         << "<div class='section'><h3>💎 MONETIZE THE MATRIX</h3>"
         << "<a href='#' class='btn'>LICENSE DATASET (DOI: 10.5281/...)</a>"
         << "<a href='#' class='btn'>SPONSOR 100-YEAR AUDIT</a>"
         << "<a href='#' class='btn' style='border-color:#00ff41; color:#00ff41;'>PURCHASE CARBON CREDITS</a>"
         << "</div>"
         << "<footer>© 2026 CANCANKERN™ | EIN VERIFIED | 1501 Pearl St</footer>"
         << "</body></html>";
    site.close();
    return 0;
}
