all: compile audit push

compile:
g++ -o aud_engine aud_engine.cpp
g++ -o strategy_manifest strategy.cpp

audit:
./aud_engine "Polymer" "Degraded" > latest_audit.txt
xz -f latest_audit.txt

push:
git add .
git commit -m "Automated Audit Update - UEI: SSWWJ3SEMZ73"
git push origin main
