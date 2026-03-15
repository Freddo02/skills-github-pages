# King AI Empire

Sistema di simulazione strategica 3D per creare battaglie tra due AI che evolvono da movimento primitivo fino a eserciti avanzati, con generazione automatica di clip highlight per social.

## Contenuti aggiunti
- `docs/king-ai-empire-system-design.md`: blueprint completo di gameplay, scena 3D iniziale, pipeline AI, e recorder intelligente.
- `configs/significant-events.yaml`: regole e soglie per il rilevamento automatico degli eventi significativi.
- `scripts/simulate_episode.py`: prototipo eseguibile che simula un match e alterna `timelapse`/`realtime` in base al punteggio di significatività.

## Avvio rapido prototipo
```bash
python3 scripts/simulate_episode.py
```

## Obiettivo MVP
1. Scena in prateria con due basi (10.000 HP) e unità base (100 HP).
2. Loop di combattimento con unlock tecnologici progressivi.
3. Detector eventi per clip automatiche (timelapse ↔ realtime).
4. Export clip pensato per formato orizzontale e verticale (Instagram Reels).
