# MoodWave

An audio-intelligence platform that understands the emotional landscape of music. MoodWave uses deep audio analysis, multi-modal ML, and generative techniques to detect, visualize, and transform mood in music — going beyond simple genre tags to model how music actually makes you *feel*.

## Vision

Most music apps treat mood as a tag. MoodWave treats it as a **continuous, multi-dimensional signal** extracted directly from raw audio. The goal is a system that can:

1. **Detect** — classify emotional valence and arousal from audio waveforms in real time, using learned spectral representations rather than hand-picked features.
2. **Understand** — fuse audio features with lyric sentiment (NLP) and album art tone (vision) for multi-modal mood understanding.
3. **Visualize** — map songs into a learned emotion embedding space and let users explore it interactively, seeing how tracks cluster and relate.
4. **Transform** — given a detected mood, generate or suggest transitions that guide the listener along an emotional trajectory (e.g., "take me from anxious to calm over 30 minutes").

## Architecture

```
┌──────────────┐     ┌──────────────────────────────────────────────┐
│   Frontend   │     │                  Backend                     │
│              │     │                                              │
│  Waveform    │────▶│  /analyze     Audio Feature Extraction       │
│  Visualizer  │     │               (mel spectrograms, MFCCs,      │
│              │     │                chroma, temporal features)     │
│  Embedding   │◀────│                                              │
│  Explorer    │     │  /mood        Mood Classification             │
│              │     │               (CNN on spectrograms or         │
│  Mood        │     │                fine-tuned audio transformer)  │
│  Trajectory  │     │                                              │
│  Planner     │────▶│  /recommend   Spotify + Generation Pipeline  │
│              │     │                                              │
│              │◀────│  /embed       Latent Space Projection         │
└──────────────┘     │               (UMAP/t-SNE over learned       │
                     │                emotion embeddings)            │
                     └──────────────────────────────────────────────┘
```

## Project Structure

```
moodwave/
├── backend/
│   ├── app/
│   │   ├── main.py        # FastAPI app and endpoints
│   │   ├── audio.py       # DSP and feature extraction (librosa)
│   │   ├── model.py       # ML inference logic
│   │   ├── spotify.py     # Spotify API integration
│   │   └── schemas.py     # Pydantic request/response schemas
│   └── requirements.txt
└── frontend/              # (planned)
```

## Tech Stack

| Layer              | Technology                                       |
| ------------------ | ------------------------------------------------ |
| API Framework      | FastAPI                                          |
| Audio Processing   | librosa, scipy, soundfile                        |
| ML / Inference     | PyTorch, scikit-learn, joblib                    |
| Embeddings & Viz   | UMAP / t-SNE, Plotly                             |
| NLP (lyrics)       | Hugging Face Transformers                        |
| External API       | Spotify Web API                                  |
| Frontend           | React + Web Audio API + D3.js (planned)          |

## Getting Started

### Prerequisites

- Python 3.12+

### Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs at `/docs`.

### Verify

```bash
curl http://127.0.0.1:8000/api/v1/health
# {"Ok": true}
```

## Roadmap

### Phase 1 — Audio Feature Pipeline
- [x] Project structure and FastAPI skeleton
- [ ] Mel spectrogram and MFCC extraction from uploaded audio
- [ ] Chroma and temporal feature extraction
- [ ] Audio preprocessing (resampling, normalization, silence trimming)

### Phase 2 — Mood Classification Model
- [ ] Dataset preparation (MER datasets: PMEmo, DEAM, MusicNet)
- [ ] CNN-based classifier on mel spectrograms
- [ ] Valence-arousal regression (continuous mood, not just discrete labels)
- [ ] Model evaluation and comparison against hand-crafted feature baselines

### Phase 3 — Multi-Modal Fusion
- [ ] Lyric sentiment analysis via pre-trained transformer
- [ ] Album art mood extraction via vision model
- [ ] Late-fusion architecture combining audio + text + image signals

### Phase 4 — Embedding Space & Visualization
- [ ] Learn emotion embeddings from the classifier's penultimate layer
- [ ] UMAP projection for 2D/3D interactive exploration
- [ ] Frontend embedding explorer (D3.js or Three.js)

### Phase 5 — Recommendation & Mood Trajectories
- [ ] Spotify integration for track recommendations
- [ ] Mood trajectory planning (user defines start → end mood)
- [ ] Playlist generation optimized for smooth emotional transitions

### Phase 6 — Real-Time & Production
- [ ] WebSocket streaming for real-time mood detection
- [ ] Web Audio API integration for in-browser analysis
- [ ] Model optimization (ONNX export, quantization)
- [ ] Containerized deployment (Docker)

## Research Influences

- Russell's circumplex model of affect (valence-arousal space)
- Music Emotion Recognition (MER) literature
- Audio spectrogram transformers (AST)
- Spotify's audio feature analysis
