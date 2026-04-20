from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# -----------------------------
# NOTE:
# Loading model lazily to avoid heavy init during import
# -----------------------------
_model = None

def _load_model():
    global _model
    if _model is None:
        # lightweight model (fast enough for this prototype)
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


# -----------------------------
# Simulating stored personas (like pgvector table)
# -----------------------------
PERSONA_STORE = {
    "tech_maximalist": "Strong believer in AI, crypto, and space tech. Very optimistic about future.",
    "system_skeptic": "Critical of big tech and capitalism. Cares about privacy and environment.",
    "finance_guy": "Focused on markets, trading, ROI and macro trends."
}

persona_ids = list(PERSONA_STORE.keys())


# -----------------------------
# Building vector index only when needed
# -----------------------------
_index = None

def _get_index():
    global _index

    if _index is None:
        model = _load_model()

        # embedding personas once (in-memory DB simulation)
        persona_vectors = model.encode(list(PERSONA_STORE.values()))

        dim = persona_vectors.shape[1]
        idx = faiss.IndexFlatL2(dim)
        idx.add(np.array(persona_vectors))

        _index = idx

    return _index


# -----------------------------
# Core routing logic
# -----------------------------
def match_relevant_personas(post_text: str, threshold: float = 0.35):
    """
    Instead of broadcasting every post,
    we try to match only relevant personas using semantic similarity.
    """

    model = _load_model()
    index = _get_index()

    query_vec = model.encode([post_text])
    distances, indices = index.search(np.array(query_vec), k=3)

    matched = []

    for idx, dist in zip(indices[0], distances[0]):
        # converting L2 distance → similarity (rough heuristic)
        score = 1 / (1 + dist)

        # threshold tuned after a few manual tests
        if score > threshold:
            matched.append(persona_ids[idx])

    return matched