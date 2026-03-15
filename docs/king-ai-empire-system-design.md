# King AI Empire — System Design v0.1

## Visione
**King AI Empire** è una simulazione strategica 3D dove due fazioni AI partono da abilità motorie primitive e imparano combattendo. Ogni partita genera contenuti video automatici: highlights, timelapse intelligenti e clip verticali per Instagram.

## Gameplay loop (MVP)
1. Spawn iniziale:
   - Base A HP: **10.000**
   - Base B HP: **10.000**
   - Unità base (per lato): HP **100**
2. Fase di apprendimento:
   - Le unità apprendono locomozione (camminata, evitamento ostacoli, coordinazione semplice).
3. Combattimento e progresso:
   - Vittorie e performance sbloccano upgrade (armi, moduli AI, nuove unità).
4. Vittoria round:
   - Round termina quando una base arriva a 0 HP.
5. Persistenza armate:
   - Le unità sopravvissute e i livelli tecnologici vengono mantenuti nel round successivo.
6. Escalation mappa:
   - A ogni round aumenta il terreno di scontro (larghezza mappa, punti strategici, distanza tra spawn).

## Settaggio scena 3D iniziale (brief artistico)
- Ambiente: **prateria realistica** ampia con alba drammatica, foschia volumetrica e ombre lunghe.
- Architettura team:
  - Team 1: acciaio brutale, palette nera/rossa.
  - Team 2: struttura elegante argento/azzurro.
- Camera:
  - Strategica rialzata (45°-60°), alta profondità di campo, tracking morbido centrale.
- HUD minimo:
  - Barre olografiche HP sopra basi (`10,000 HP`).
  - HP unità starter (`100 HP`).
  - Pannello inventory bottom-right:
    - Buy Units
    - Weapon Research
    - AI Training Modules
  - Stato registrazione left-side:
    - REC pulsante
    - Barra Time-lapse

## Architettura tecnica proposta

### 1) Simulation Core
- Tick deterministici (es. 10-20 Hz logico).
- ECS o actor-based per:
  - unità,
  - proiettili,
  - strutture,
  - risorse,
  - tecnologia.

### 2) AI Layer
- **Skill tree comportamentale**:
  - Movimento base → Formazione → Focus fire → Kiting.
- **Self-play competitivo** tra due agenti manager.
- Reward composita:
  - danno inflitto,
  - unità salvate,
  - controllo territorio,
  - riduzione perdite inutili.

### 3) Economy & Tech
- Risorsa unica MVP: `Credits`.
- Upgrade:
  - Weapon Tier I/II/III
  - Armor Tier I/II
  - Training Speed
  - New Unit Classes (melee, ranged, siege, support)

### 4) Content Capture Engine
- Recorder sempre attivo su buffer circolare (es. ultimi 90-180 secondi).
- Modalità output:
  - **Timelapse automatico** quando intensità bassa.
  - **Realtime** quando viene rilevato un evento significativo.
- Export clip:
  - 16:9 archivio
  - 9:16 Instagram Reels

### 5) Significant Event Detector
Calcola uno `Significance Score` continuo combinando:
- Delta DPS improvviso
- First unlock tecnologico
- Streak kill
- Base HP drop > soglia
- Cambio frontline rapido

Quando score > soglia:
1. Torna a velocità normale.
2. Marca segmento come highlight.
3. Aggiunge titolo automatico (es. `FIRST SIEGE UNLOCK`).

## Pipeline episodi Instagram
1. Simulazioni batch (N partite/giorno).
2. Event detector seleziona highlight.
3. Auto-edit:
   - intro 1.5s brand
   - 2-5 highlight
   - outro CTA
4. Voiceover/TTS opzionale con telemetria.
5. Publish queue con caption generata.

## Data model minimo

### Match
- `match_id`
- `map_seed`
- `duration_sec`
- `winner_team`
- `tech_level_end`

### Event
- `timestamp`
- `event_type`
- `intensity`
- `team`
- `metadata`

### Clip
- `clip_id`
- `match_id`
- `start_sec`
- `end_sec`
- `mode` (`timelapse` | `realtime`)
- `instagram_score`

## Prompt cinematografico (immagine keyframe)
Usa questo prompt come base per concept art e key visual:

> "Cinematic 3D gameplay frame of 'King AI Empire', a high-end tactical AI simulation. The scene is a vast, realistic green prairie under a dramatic sunrise. In the foreground, two distinct spawn bases (Command Centers) face each other across a wide valley: one side features dark, brutalist steel architecture, the other elegant silver and light-blue structures. Each base displays a floating holographic health bar showing '10,000 HP'. In the middle of the field, several low-poly 'Level 1' AI units are seen in a state of primitive movement, stumbling and learning to walk, with '100 HP' floating above them. The camera is a raised 3D strategic perspective with deep field of view. On the bottom right, a sleek, semi-transparent futuristic UI inventory window shows icons for 'Buy Units', 'Weapon Research', and 'AI Training Modules'. To the left, a small 'REC' icon with a pulsing red light and a 'Time-lapse' status bar indicates an automated recording in progress. The lighting is ultra-realistic with long shadows and volumetric fog. Style: AAA strategy game engine (Unreal Engine 5 style), hyper-detailed textures, modern military-fantasy hybrid, 8k resolution, cinematic color grading."

## Milestone pratiche
- **M1**: scena 3D + unità base + damage model semplice.
- **M2**: AI movimento/attacco + vittoria round.
- **M3**: unlock tecnologia + persistenza cross-round.
- **M4**: recorder intelligente + highlight extraction.
- **M5**: export automatico clip + scheduler social.
