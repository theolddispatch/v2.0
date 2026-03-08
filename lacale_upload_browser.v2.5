#!/bin/sh
# =============================================================================
# Script créé par Theolddispatch
#      ___           ___       ___           ___           ___     
#     /\  \         /\__\     /\  \         /\  \         /\__\   
#    /::\  \       /:/  /    /::\  \       /::\  \       /:/  /   
#   /:/\:\  \     /:/  /    /:/\:\  \     /:/\:\  \     /:/__/    
#  /::\~\:\__\   /:/  /    /::\~\:\  \   /:/  \:\  \   /::\__\____
# /:/\:\ \:|__| /:/__/    /:/\:\ \:\__\ /:/__/ \:\__\ /:/\:::::\__\
# \:\~\:\/:/  / \:\  \    \/__\:\/:/  / \:\  \  \/__/ \/_|:|~~|~  
#  \:\ \::/  /   \:\  \        \::/  /   \:\  \          |:|  |   
#   \:\/:/  /     \:\  \       /:/  /     \:\  \         |:|  |   
#    \::/__/       \:\__\     /:/  /       \:\__\        |:|  |   
#     ~~            \/__/     \/__/         \/__/         \|__|    
#      ___           ___       ___           ___     
#     /\  \         /\__\     /\  \         /\  \    
#    /::\  \       /:/  /    /::\  \       /::\  \   
#   /:/\:\  \     /:/  /    /:/\:\  \     /:/\:\  \  
#  /::\~\:\  \   /:/  /    /::\~\:\  \   /:/  \:\  \ 
# /:/\:\ \:\__\ /:/__/    /:/\:\ \:\__\ /:/__/_\:\__\
# \/__\:\ \/__/ \:\  \    \/__\:\/:/  / \:\  /\ \/__/
#      \:\__\    \:\  \        \::/  /   \:\ \:\__\  
#       \/__/     \:\  \       /:/  /     \:\/:/  /  
#                  \:\__\     /:/  /       \::/  /   
#                   \/__/     \/__/         \/__/     — version formulaire web
# =============================================================================
# lacale_upload_browser.sh — Upload automatique depuis Radarr vers La Cale
#                            via simulation navigateur (https://la-cale.space/upload)
# Version : 2.5 — Ajout actualisation radarr si sélection
#                 Ajout d'une vérification seed avant upload
#                 Ajout grades pour max_movies
#                 Ajout d'une vérification pendings
#                 Ajout d'un temps d'attente pour que le seed se charge et s'active
# Emplacement : [chemin-vers-votre-dossier-scripts]
# Dépendances : curl, jq (NAS), docker (pour création torrent via Alpine)
# =============================================================================

# =============================================================================
# ─── !! À CONFIGURER AVANT UTILISATION !! ────────────────────────────────────
# =============================================================================
# Toutes les valeurs ci-dessous sont à renseigner manuellement.
# Elles peuvent aussi être passées en variables d'environnement (prioritaires).

# ─── Grades La Cale & limite d'upload ────────────────────────────────────────
# Grade         │ Cargaisons uploadées nécessaires │ MAX_MOVIES conseillé
# ─────────────────────────────────────────────────────────────────────────────
# Observateur   │   0  (débutant, en attente valid.)│  1
# Initié        │   5  cargaisons validées          │  5
# Matelot       │  ?? cargaisons validées           │ ??
# Quartier-     │  ?? cargaisons validées           │ ??
#  maître       │                                   │
# Officier      │  ?? cargaisons validées           │ ??
# Capitaine     │  ?? cargaisons validées           │ ??
# (complétez les grades manquants depuis la-cale.space/forums)
# ─────────────────────────────────────────────────────────────────────────────
MAX_MOVIES="${MAX_MOVIES:-1}"   # ← Modifiez cette valeur selon votre grade

# -- Radarr --
RADARR_URL="${RADARR_URL:-http://[adresse-ip-nas]:[port-radarr]}"       # ex: http://192.168.1.10:7878
RADARR_API_KEY="${RADARR_API_KEY:-[clé-api-radarr]}"                    # Radarr → Paramètres → Général → Clé API
MEDIAINFO_URL="${MEDIAINFO_URL:-http://[adresse-ip-nas]:[port-mediainfo]}"

# -- La Cale --
LACALE_URL="${LACALE_URL:-https://la-cale.space}"
LACALE_USER="${LACALE_USER:-[email-compte-lacale]}"                     # email du compte La Cale
LACALE_PASS="${LACALE_PASS:-[mot-de-passe-lacale]}"                     # mot de passe du compte La Cale
# Cookies exportés depuis Chrome/Firefox (DevTools → Application → Cookies)
# Quand définis, le login automatique est bypassed — ces cookies sont prioritaires
# Cookies de session plus nécessaires — le login altcha fonctionne directement depuis le NAS
# LACALE_COOKIE_SESSION et LACALE_COOKIE_CF ne sont plus utilisés
TRACKER_URL="${TRACKER_URL:-https://tracker.la-cale.space/announce?passkey=[passkey-lacale]}"  # passkey visible dans votre profil La Cale

# -- qBittorrent --
QB_URL="${QB_URL:-http://[adresse-ip-nas]:[port-qbittorrent]}"          # ex: http://192.168.1.10:8080
QB_USER="${QB_USER:-[utilisateur-qbittorrent]}"
QB_PASS="${QB_PASS:-[mot-de-passe-qbittorrent]}"

# -- Notifications mail (Gmail) --
MAIL_TO="${MAIL_TO:-[email-destinataire]}"
MAIL_FROM="${MAIL_FROM:-[email-expediteur]}"
MAIL_SUBJECT="${MAIL_SUBJECT:-La Cale Upload Report}"
GMAIL_USER="${GMAIL_USER:-[email-gmail]}"
GMAIL_PASS_FILE="${GMAIL_PASS_FILE:-[chemin-vers-fichier-mot-de-passe-app-gmail]}"  # fichier contenant le mot de passe d'application Gmail
SMTP_URL="${SMTP_URL:-smtps://smtp.gmail.com:465}"

# -- Chemins NAS --
# Correspondance chemins Radarr (conteneur) → NAS réel
RADARR_PATH_PREFIX="${RADARR_PATH_PREFIX:-[préfixe-chemin-films-dans-radarr]}"    # ex: /Films/Films
NAS_FILMS_GLOB="[glob-vers-dossier-films-nas]"                                     # ex: /share/DATA/Media*/Films
NAS_PATH_PREFIX="${NAS_PATH_PREFIX:-[préfixe-chemin-nas]}"                         # ex: /share/DATA
QB_PATH_PREFIX="${QB_PATH_PREFIX:-}"  # Préfixe chemin vu par qBittorrent si différent du NAS (ex: Docker)

# -- Répertoires de travail (BLACK FLAG) --
BLACK_FLAG_DIR="${BLACK_FLAG_DIR:-[chemin-complet-dossier-black-flag]}"            # dossier racine du projet sur le NAS
# Les sous-dossiers ci-dessous sont dérivés automatiquement de BLACK_FLAG_DIR :
NFO_DIR="${NFO_DIR:-${BLACK_FLAG_DIR}/NFO}"
TORRENTS_DIR="${TORRENTS_DIR:-${BLACK_FLAG_DIR}/torrents ready}"
LOGS_DIR="${LOGS_DIR:-${BLACK_FLAG_DIR}/_logs}"
HISTORIQUE_DIR="${HISTORIQUE_DIR:-${BLACK_FLAG_DIR}/_historique}"

# -- Script Python altcha (chemin absolu) --
# ALTCHA_SOLVER est utilisé dans lacale_login() — ajuster si le script est ailleurs
# Valeur par défaut : ${BLACK_FLAG_DIR}/scripts/altcha_solver.py

# =============================================================================
# ─── Fin de la section de configuration ──────────────────────────────────────
# =============================================================================

# User-Agent navigateur (doit correspondre au navigateur qui a généré les cookies)
BROWSER_UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"

# User-Agent navigateur (doit correspondre au navigateur qui a généré les cookies)
BROWSER_UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"

# Correspondance chemins Radarr (conteneur) → NAS réel

# Fonction pour résoudre le chemin réel d'un film via glob
resolve_nas_path() {
    _RADARR_PATH="$1"
    _FOLDER=$(echo "$_RADARR_PATH" | sed "s|^${RADARR_PATH_PREFIX}/||" | cut -d'/' -f1)
    _FILE=$(echo "$_RADARR_PATH" | sed "s|^${RADARR_PATH_PREFIX}/||" | cut -d'/' -f2-)
    _RESOLVED=$(ls -d ${NAS_FILMS_GLOB}/"${_FOLDER}"/"${_FILE}" 2>/dev/null | head -1)
    echo "$_RESOLVED"
}

# Répertoires BLACK FLAG version web
HISTORIQUE_FILE="${HISTORIQUE_DIR}/uploaded_torrents.txt"

# Image Docker pour Python 3
DOCKER_PYTHON="${DOCKER_PYTHON:-alpine:3.20}"


# ─── Init répertoires & logs ──────────────────────────────────────────────────
mkdir -p "$NFO_DIR" "$TORRENTS_DIR" "$LOGS_DIR" "$HISTORIQUE_DIR" 2>/dev/null

LOG_DATE=$(date '+%Y-%m-%d_%H-%M-%S')
LOG_FILE="${LOGS_DIR}/lacale_upload_${LOG_DATE}.log"
WORK_DIR="${BLACK_FLAG_DIR}/_tmp/lacale_$$"
mkdir -p "$WORK_DIR"
REPORT_FILE="${WORK_DIR}/report.txt"
COOKIE_FILE="${WORK_DIR}/lacale_cookies.txt"
touch "$REPORT_FILE" "$LOG_FILE"

# ─── Logging ──────────────────────────────────────────────────────────────────
log() {
    _msg="[$(date '+%Y-%m-%d %H:%M:%S')] $*"
    echo "$_msg"
    echo "$_msg" >> "$REPORT_FILE"
    echo "$_msg" >> "$LOG_FILE"
}
log_section() {
    log ""; log "══════════════════════════════════════════"
    log "  $*"; log "══════════════════════════════════════════"
}

# ─── Génération BBCode (description La Cale) ──────────────────────────────────
# Reproduit EXACTEMENT le comportement de generateBBCode() du frontend La Cale
# (analysé depuis le bundle 8dd0f5d0032cce4a_js, confirmé dans 9f1380cda80e4497_js).
# Template : [center][img]…[size=6][color=#eab308]…[quote]synopsis…[DÉTAILS]…[CASTING]
generate_bbcode() {
    local title="$1"
    local year="$2"
    local overview="$3"
    local cover_url="$4"
    local quality_name="$5"
    local video_codec="$6"
    local audio_codec="$7"
    local audio_langs="$8"
    local file_size_bytes="$9"
    local rating="${10}"       # ex: "7.2"
    local genres="${11}"       # ex: "Thriller, Horreur"
    local cast_json="${12}"    # JSON array: [{"name":"...","character":"..."},…]
    local subtitles="${13}"
    local dyn_range="${14}"
    local dyn_type="${15}"

    # ── Résolution depuis quality_name ────────────────────────────────────────
    local resolution="1080p"
    case "$quality_name" in
        *2160*|*4K*|*UHD*) resolution="2160p" ;;
        *1080*)             resolution="1080p" ;;
        *720*)              resolution="720p"  ;;
        *576*)              resolution="576p"  ;;
        *480*)              resolution="480p"  ;;
    esac

    # ── Format conteneur ──────────────────────────────────────────────────────
    local container="MKV"

    # ── Taille fichier lisible (formatBytes: ≥1GiB→GiB, sinon MiB) ───────────
    local file_size_hr="Variable"
    if [ -n "$file_size_bytes" ] && [ "$file_size_bytes" -gt 0 ] 2>/dev/null; then
        file_size_hr=$(awk "BEGIN {
            b=$file_size_bytes
            if (b >= 1073741824) printf \"%.2f GiB\", b/1073741824
            else printf \"%.2f MiB\", b/1048576
        }")
    fi

    # ── Langues / sous-titres ─────────────────────────────────────────────────
    local lang_display="${audio_langs:-Français (VFF)}"
    [ -z "$audio_langs" ] || [ "$audio_langs" = "null" ] && lang_display="Français (VFF)"
    local subs_display="${subtitles:-Français}"
    [ -z "$subtitles" ] || [ "$subtitles" = "null" ] && subs_display="Français"

    # ── Note (arrondie à 1 décimale) ─────────────────────────────────────────
    local rating_display="N/A"
    if [ -n "$rating" ] && [ "$rating" != "null" ] && [ "$rating" != "0" ]; then
        rating_display=$(printf "%.1f" "$rating" 2>/dev/null || echo "$rating")
    fi

    # ── Genres ────────────────────────────────────────────────────────────────
    local genres_display="${genres:-N/A}"
    [ -z "$genres" ] || [ "$genres" = "null" ] && genres_display="N/A"

    # ── Poster URL (si relatif, préfixer https://image.tmdb.org/t/p/w500) ─────
    local poster_url="$cover_url"
    if [ -n "$poster_url" ] && [ "$poster_url" != "null" ]; then
        case "$poster_url" in
            http*) : ;;  # déjà absolu
            *)     poster_url="https://image.tmdb.org/t/p/w500${poster_url}" ;;
        esac
    fi

    # ── Casting (5 premiers acteurs depuis JSON) ───────────────────────────────
    local cast_block=""
    if [ -n "$cast_json" ] && [ "$cast_json" != "null" ] && [ "$cast_json" != "[]" ]; then
        local cast_lines
        cast_lines=$(printf '%s' "$cast_json" | \
            jq -r '.[:5][] | select(.name != null and .name != "") | "[b]" + .name + "[/b] (" + (.character // .role // "") + ")"' \
            2>/dev/null)
        if [ -n "$cast_lines" ]; then
            cast_block="

[color=#eab308][b]--- CASTING ---[/b][/color]

${cast_lines}"
        fi
    fi

    # ── Construction BBCode (template exact du site) ───────────────────────────
    printf '[center]\n'
    if [ -n "$poster_url" ] && [ "$poster_url" != "null" ]; then
        printf '[img]%s[/img]\n\n' "$poster_url"
    fi
    printf '[size=6][color=#eab308][b]%s (%s)[/b][/color][/size]\n\n' "$title" "$year"
    printf '[b]Note :[/b] %s/10\n' "$rating_display"
    printf '[b]Genre :[/b] %s\n\n' "$genres_display"
    if [ -n "$overview" ] && [ "$overview" != "null" ]; then
        printf '[quote]%s[/quote]\n\n' "$overview"
    fi
    printf '[color=#eab308][b]--- DÉTAILS ---[/b][/color]\n\n'
    printf '[b]Qualité :[/b] %s\n' "$resolution"
    printf '[b]Format :[/b] %s\n' "$container"
    printf '[b]Codec Vidéo :[/b] %s\n' "${video_codec:-x264}"
    printf '[b]Codec Audio :[/b] %s\n' "${audio_codec:-AAC}"
    printf '[b]Langues :[/b] %s\n' "$lang_display"
    printf '[b]Sous-titres :[/b] %s\n' "$subs_display"
    printf '[b]Taille :[/b] %s' "$file_size_hr"
    if [ -n "$cast_block" ]; then
        printf '%s' "$cast_block"
    fi
    printf '\n\n[i]Généré par La Cale[/i]\n[/center]'
}

# ─── Utilitaires ──────────────────────────────────────────────────────────────
radarr_get() {
    curl -sf --max-time 30 \
        -H "X-Api-Key: $RADARR_API_KEY" \
        "${RADARR_URL}/api/v3/$1"
}

# ─── Requête navigateur générique (avec cookies, Referer, User-Agent) ─────────
browser_get() {
    curl -sf --max-time 30 \
        -A "$BROWSER_UA" \
        -b "$COOKIE_FILE" -c "$COOKIE_FILE" \
        -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
        -H "Accept-Language: fr-FR,fr;q=0.9,en;q=0.8" \
        -H "Accept-Encoding: gzip, deflate, br" \
        -H "Connection: keep-alive" \
        -H "Upgrade-Insecure-Requests: 1" \
        --compressed \
        "${LACALE_URL}$1"
}

# ─── Connexion à La Cale (API REST JSON — Next.js) ────────────────────────────
# Le site utilise POST /api/auth/login en JSON avec {email, password, altcha, formLoadedAt}
# altcha est un Proof-of-Work (SHA-256) résolu localement depuis le challenge
# fourni par /api/auth/altcha/challenge?scope=login (spec open-source: altcha.org)
# Cloudflare peut bloquer la page /login mais l'API POST reste accessible
lacale_login() {
    log "Connexion à La Cale via API REST JSON..."

    if [ -z "$LACALE_USER" ] || [ -z "$LACALE_PASS" ]; then
        log "ERREUR: LACALE_USER et LACALE_PASS doivent être définis."
        return 1
    fi

    # ── Login avec PoW Altcha ─────────────────────────────────────────────────
    # Pas besoin de cf_clearance : Cloudflare laisse passer l'IP du NAS directement.
    # Le flow : GET challenge → solver SHA-256 → POST login → cookie session HttpOnly
    log "  Récupération du challenge Altcha..."
    FORM_LOADED_AT=$(awk "BEGIN{print int(systime()*1000)}" /dev/null 2>/dev/null || echo "$(date +%s)000")
    ALTCHA_CHALLENGE=$(curl -sf --max-time 15 \
        -A "$BROWSER_UA" \
        -c "$COOKIE_FILE" -b "$COOKIE_FILE" \
        -H "Accept: application/json" \
        -H "Referer: ${LACALE_URL}/login" \
        --compressed \
        "${LACALE_URL}/api/auth/altcha/challenge?scope=login" 2>/dev/null)

    ALTCHA_TOKEN=""
    if [ -n "$ALTCHA_CHALLENGE" ]; then
        # ── Étape 2 : résoudre le PoW SHA-256 via fichier Python temporaire ──
        log "  Résolution du PoW Altcha..."
        ALTCHA_SOLVER="${BLACK_FLAG_DIR}/scripts/altcha_solver.py"
        # Écrire le challenge dans un fichier pour éviter les problèmes d'échappement shell
        CHALLENGE_FILE="${WORK_DIR}/altcha_challenge.json"
        printf '%s' "$ALTCHA_CHALLENGE" > "$CHALLENGE_FILE"
        ALTCHA_TOKEN=$(python "$ALTCHA_SOLVER" "$CHALLENGE_FILE" 2>/dev/null)
        if [ -n "$ALTCHA_TOKEN" ]; then
            log "  ✓ PoW résolu"
        else
            log "  WARN: PoW non résolu, tentative sans altcha"
        fi
    else
        log "  WARN: challenge Altcha non disponible, tentative sans"
    fi

    # ── Étape 3 : POST login avec altcha ──────────────────────────────────────
    LOGIN_BUILDER="${WORK_DIR}/login_payload.py"
    cat > "$LOGIN_BUILDER" << 'BUILDER_EOF'
import json, os, sys
payload = {
    'email': os.environ['LOGIN_EMAIL'],
    'password': os.environ['LOGIN_PASS'],
    'formLoadedAt': int(os.environ['FORM_LOADED_AT'])
}
altcha = os.environ.get('ALTCHA_TOKEN', '').strip()
if altcha:
    payload['altcha'] = altcha
sys.stdout.write(json.dumps(payload) + "
")
BUILDER_EOF
    # Build JSON payload with jq (no python needed on host)
    if [ -n "$ALTCHA_TOKEN" ]; then
        LOGIN_PAYLOAD=$(jq -cn --arg e "$LACALE_USER" --arg p "$LACALE_PASS" \
            --argjson f "$FORM_LOADED_AT" --arg a "$ALTCHA_TOKEN" \
            '{email:$e, password:$p, formLoadedAt:$f, altcha:$a}')
    else
        LOGIN_PAYLOAD=$(jq -cn --arg e "$LACALE_USER" --arg p "$LACALE_PASS" \
            --argjson f "$FORM_LOADED_AT" \
            '{email:$e, password:$p, formLoadedAt:$f}')
    fi

    LOGIN_RESPONSE=$(curl -si --max-time 30 \
        -A "$BROWSER_UA" \
        -c "$COOKIE_FILE" -b "$COOKIE_FILE" \
        -H "Content-Type: application/json" \
        -H "Accept: application/json" \
        -H "Referer: ${LACALE_URL}/login" \
        -H "Origin: ${LACALE_URL}" \
        --compressed \
        -X POST \
        -d "$LOGIN_PAYLOAD" \
        "${LACALE_URL}/api/auth/login")

    HTTP_CODE=$(echo "$LOGIN_RESPONSE" | grep -oE '^HTTP/[0-9.]+ [0-9]+' | tail -1 | grep -oE '[0-9]+$')
    LOGIN_BODY=$(echo "$LOGIN_RESPONSE" | sed -n '/^\r\{0,1\}$/,$ p' | tail -n +2)

    log "  HTTP login: ${HTTP_CODE:-?}"

    if [ "$HTTP_CODE" = "200" ] || echo "$LOGIN_BODY" | grep -q '"success"\s*:\s*true\|"user"\s*:'; then
        log "  ✓ Connexion réussie"
        return 0
    fi

    # Fallback : cookie de session manuel (export depuis navigateur)
    ERR=$(echo "$LOGIN_BODY" | grep -oE '"message":"[^"]*"' | head -1)
    log "  ERREUR: connexion échouée (HTTP $HTTP_CODE) — $ERR"
    log "  → Vérifiez LACALE_USER et LACALE_PASS dans le script"
    return 1
}

# ─── Récupération du CSRF token depuis la page upload ─────────────────────────
# NOTE: L'app est 100% Next.js avec API REST — pas de CSRF token HTML.
# Cette fonction est conservée pour compatibilité mais retourne vide.
get_upload_csrf() {
    UPLOAD_PAGE=$(browser_get "/upload")
    if [ -z "$UPLOAD_PAGE" ]; then
        log "ERREUR: impossible de charger la page /upload"
        echo ""
        return 1
    fi

    # Chercher le token dans le formulaire (Next.js n'en a pas, retournera vide)
    _TOKEN=$(echo "$UPLOAD_PAGE" | grep -oE 'name="_token"\s+value="[^"]+"' | grep -oE 'value="[^"]+"' | grep -oE '"[^"]+"' | tr -d '"' | head -1)
    if [ -z "$_TOKEN" ]; then
        _TOKEN=$(echo "$UPLOAD_PAGE" | grep -oE '"csrfToken":"[^"]+"' | grep -oE '"[^"]+"}' | sed 's/["}]//g' | head -1)
    fi
    echo "$_TOKEN"
}

# ─── Vérification doublon via page de recherche ───────────────────────────────
lacale_check_duplicate() {
    _TMDB_ID="$1"
    _TITLE="$2"

    # Recherche par titre sur le moteur interne
    SEARCH_RESULT=$(curl -sf --max-time 30 \
        -A "$BROWSER_UA" \
        -b "$COOKIE_FILE" -c "$COOKIE_FILE" \
        -H "Accept: application/json, */*" \
        -H "X-Requested-With: XMLHttpRequest" \
        -H "Referer: ${LACALE_URL}/torrents" \
        --compressed \
        "${LACALE_URL}/api/internal/torrents/filter?search=$(echo "$_TITLE" | sed 's/ /+/g')&category=films" 2>/dev/null)

    if [ -z "$SEARCH_RESULT" ]; then
        # Fallback : chercher via la page /torrents avec paramètre GET
        SEARCH_RESULT=$(browser_get "/torrents?search=$(echo "$_TITLE" | sed 's/ /+/g')&categories%5B%5D=films")
    fi

    FOUND=$(echo "$SEARCH_RESULT" | grep -ic "$_TITLE" 2>/dev/null || echo "0")
    [ "$FOUND" -gt 0 ] && echo "true" || echo "false"
}

send_report() {
    _subject="$1"; _body="$2"
    [ -f "$GMAIL_PASS_FILE" ] || { log "WARN: mot de passe Gmail introuvable: $GMAIL_PASS_FILE"; return 1; }
    _pass=$(cat "$GMAIL_PASS_FILE")
    curl -sf --url "$SMTP_URL" --ssl-reqd \
        --mail-from "$MAIL_FROM" --mail-rcpt "$MAIL_TO" \
        --user "$GMAIL_USER:$_pass" \
        --upload-file - << MAIL_EOF
From: $MAIL_FROM
To: $MAIL_TO
Subject: $_subject
Content-Type: text/plain; charset=utf-8

$(cat "$_body")
MAIL_EOF
    log "✓ Mail envoyé à $MAIL_TO"
}

# ─── Démarrage ────────────────────────────────────────────────────────────────
printf '\n'
echo '     ___           ___       ___           ___           ___     '
echo '    /\  \         /\__\     /\  \         /\  \         /\__\   '
echo '   /::\  \       /:/  /    /::\  \       /::\  \       /:/  /   '
echo '  /:/\:\  \     /:/  /    /:/\:\  \     /:/\:\  \     /:/__/    '
echo ' /::\~\:\__\   /:/  /    /::\~\:\  \   /:/  \:\  \   /::\__\____'
echo '/:/\:\ \:|__| /:/__/    /:/\:\ \:\__\ /:/__/ \:\__\ /:/\:::::\__\'
echo '\:\~\:\/:/  / \:\  \    \/__\:\/:/  / \:\  \  \/__/ \/_|:|~~|~  '
echo ' \:\ \::/  /   \:\  \        \::/  /   \:\  \          |:|  |   '
echo '  \:\/:/  /     \:\  \       /:/  /     \:\  \         |:|  |   '
echo '   \::/__/       \:\__\     /:/  /       \:\__\        |:|  |   '
echo '    ~~            \/__/     \/__/         \/__/         \|__|    '
echo '     ___           ___       ___           ___     '
echo '    /\  \         /\__\     /\  \         /\  \    '
echo '   /::\  \       /:/  /    /::\  \       /::\  \   '
echo '  /:/\:\  \     /:/  /    /:/\:\  \     /:/\:\  \  '
echo ' /::\~\:\  \   /:/  /    /::\~\:\  \   /:/  \:\  \ '
echo '/:/\:\ \:\__\ /:/__/    /:/\:\ \:\__\ /:/__/_\:\__\'
echo '\/__\:\ \/__/ \:\  \    \/__\:\/:/  / \:\  /\ \/__/'
echo '     \:\__\    \:\  \        \::/  /   \:\ \:\__\  '
echo '      \/__/     \:\  \       /:/  /     \:\/:/  /  '
echo '                 \:\__\     /:/  /       \::/  /   '
echo '                  \/__/     \/__/         \/__/     — version formulaire web'
printf '\n'
log_section "Démarrage La Cale Upload Script v2.5 (Browser Mode — termIds auto)"
log "MAX_MOVIES : $MAX_MOVIES"
log "NFO dir    : $NFO_DIR"
log "Torrents   : $TORRENTS_DIR"
log "Log file   : $LOG_FILE"
log "Mode       : Simulation navigateur (https://la-cale.space/upload)"

# ─── Connexion à La Cale ──────────────────────────────────────────────────────
lacale_login || { log "ERREUR: connexion La Cale impossible. Abandon."; exit 1; }

# ─── Récupération des métadonnées (catégorie Films) via API ───────────────────
log ""
log "Récupération de la catégorie Films via /api/internal/categories..."

# Utilise l'API REST plutôt que le HTML de /upload (la page peut être bloquée par Cloudflare)
CATEGORIES_JSON=$(curl -sf --max-time 15 \
    -A "$BROWSER_UA" \
    -b "$COOKIE_FILE" -c "$COOKIE_FILE" \
    -H "Accept: application/json" \
    --compressed \
    "${LACALE_URL}/api/internal/categories" 2>/dev/null)

CATEGORY_ID=""
if [ -n "$CATEGORIES_JSON" ]; then
    # Chercher une catégorie dont le nom contient "film" ou "movie" (insensible à la casse)
    CATEGORY_ID=$(printf '%s' "$CATEGORIES_JSON" | \
        jq -r '
          (if type == "array" then . else (.data // .categories // []) end)
          | .. | objects | select(.name? and ((.name | ascii_downcase) | test("film|movie")))
          | .id
        ' 2>/dev/null | head -1)
fi

if [ -z "$CATEGORY_ID" ] || [ "$CATEGORY_ID" = "null" ]; then
    log "WARN: catégorie Films non trouvée dans /api/internal/categories — utilisation de l'ID hardcodé"
    CATEGORY_ID="[id-categorie-films-lacale]"  # À récupérer via /api/internal/categories ou dans les DevTools
fi

log "Catégorie Films : id=$CATEGORY_ID"

# ─── Récupération films Radarr ────────────────────────────────────────────────
log ""; log "Récupération des films Radarr..."
MOVIES_JSON="${WORK_DIR}/movies.json"
radarr_get "movie" > "$MOVIES_JSON" || { log "ERREUR: impossible de joindre Radarr"; exit 1; }
TOTAL=$(jq 'length' "$MOVIES_JSON")
TOTAL_WITH_FILE=$(jq '[.[] | select(.hasFile==true)] | length' "$MOVIES_JSON")
log "Total films : $TOTAL (avec fichier : $TOTAL_WITH_FILE)"

# ─── Statistiques ─────────────────────────────────────────────────────────────
UPLOADED=0; SKIPPED=0; ERRORS=0; LAST_ERROR=""
RESULTS_FILE="${WORK_DIR}/results.txt"
touch "$RESULTS_FILE"

# ─── Script Python pour création du torrent ───────────────────────────────────
PY="${WORK_DIR}/make_torrent.py"
printf '%s\n' '#!/usr/bin/env python3' > "$PY"
printf '%s\n' 'import sys, os, hashlib, time' >> "$PY"
printf '%s\n' '' >> "$PY"
printf '%s\n' 'def bencode(v):' >> "$PY"
printf '%s\n' '    if isinstance(v, int): return b"i" + str(v).encode() + b"e"' >> "$PY"
printf '%s\n' '    if isinstance(v, (bytes, bytearray)): return str(len(v)).encode() + b":" + bytes(v)' >> "$PY"
printf '%s\n' '    if isinstance(v, str):' >> "$PY"
printf '%s\n' '        e = v.encode("utf-8"); return str(len(e)).encode() + b":" + e' >> "$PY"
printf '%s\n' '    if isinstance(v, list): return b"l" + b"".join(bencode(i) for i in v) + b"e"' >> "$PY"
printf '%s\n' '    if isinstance(v, dict):' >> "$PY"
printf '%s\n' '        out = b"d"' >> "$PY"
printf '%s\n' '        for k in sorted(v.keys()):' >> "$PY"
printf '%s\n' '            bk = k.encode() if isinstance(k, str) else k' >> "$PY"
printf '%s\n' '            out += str(len(bk)).encode() + b":" + bk + bencode(v[k])' >> "$PY"
printf '%s\n' '        return out + b"e"' >> "$PY"
printf '%s\n' '' >> "$PY"
printf '%s\n' 'file_path, release_name, tracker_url, output_path = sys.argv[1:5]' >> "$PY"
printf '%s\n' 'piece_length = 512 * 1024' >> "$PY"
printf '%s\n' 'if not os.path.exists(file_path):' >> "$PY"
printf '%s\n' '    print("ERREUR: fichier non trouve: " + file_path, file=sys.stderr); sys.exit(1)' >> "$PY"
printf '%s\n' 'file_size = os.path.getsize(file_path)' >> "$PY"
printf '%s\n' 'pieces = bytearray(); read = 0; last_pct = -1' >> "$PY"
printf '%s\n' 'print("  Fichier : " + os.path.basename(file_path))' >> "$PY"
printf '%s\n' 'print("  Taille  : " + str(round(file_size/(1024**3),2)) + " GiB")' >> "$PY"
printf '%s\n' 'print("  Calcul SHA1...")' >> "$PY"
printf '%s\n' 'with open(file_path, "rb") as f:' >> "$PY"
printf '%s\n' '    while True:' >> "$PY"
printf '%s\n' '        chunk = f.read(piece_length)' >> "$PY"
printf '%s\n' '        if not chunk: break' >> "$PY"
printf '%s\n' '        pieces += hashlib.sha1(chunk).digest(); read += len(chunk)' >> "$PY"
printf '%s\n' '        pct = int(read * 100 / file_size)' >> "$PY"
printf '%s\n' '        if pct // 10 != last_pct // 10: print("  " + str(pct) + "%", flush=True); last_pct = pct' >> "$PY"
printf '%s\n' '# Utiliser le nom de fichier réel (sans extension) comme nom dans le torrent' >> "$PY"
printf '%s\n' '# pour que qBittorrent puisse seeder sans renommage' >> "$PY"
printf '%s\n' 'import os as _os' >> "$PY"
printf '%s\n' '# info.name = nom complet avec extension (requis pour seed single-file)' >> "$PY"
printf '%s\n' 'file_basename = _os.path.basename(file_path)' >> "$PY"
printf '%s\n' 'info = {"name": file_basename, "piece length": piece_length, "pieces": bytes(pieces), "length": file_size, "private": 1, "source": "lacale"}' >> "$PY"
printf '%s\n' 'torrent = {"announce": tracker_url, "info": info, "created by": "uTorrent/3.5.5", "creation date": int(time.time()), "comment": ""}' >> "$PY"
printf '%s\n' 'with open(output_path, "wb") as f: f.write(bencode(torrent))' >> "$PY"
printf '%s\n' 'print("  Torrent OK: " + output_path)' >> "$PY"

# ─── Boucle sur les films ─────────────────────────────────────────────────────
jq -c '.[] | select(.hasFile==true and .movieFile != null)' "$MOVIES_JSON" \
    > "${WORK_DIR}/movies_with_files.jsonl"

while IFS= read -r MOVIE_JSON; do

    [ "$((UPLOADED + ERRORS))" -ge "$MAX_MOVIES" ] && break

    # ── Extraction des champs ────────────────────────────────────────────
    MOVIE_ID=$(echo "$MOVIE_JSON"       | jq -r '.id')
    TITLE=$(echo "$MOVIE_JSON"          | jq -r '.title')
    YEAR=$(echo "$MOVIE_JSON"           | jq -r '.year')
    TMDB_ID=$(echo "$MOVIE_JSON"        | jq -r '.tmdbId // ""')
    OVERVIEW=$(echo "$MOVIE_JSON"       | jq -r '.overview // ""')
    RADARR_PATH=$(echo "$MOVIE_JSON"    | jq -r '.movieFile.path // ""')
    RELEASE_GROUP=$(echo "$MOVIE_JSON"  | jq -r '.movieFile.releaseGroup // ""')
    QUALITY_NAME=$(echo "$MOVIE_JSON"   | jq -r '.movieFile.quality.quality.name // ""')
    VIDEO_CODEC=$(echo "$MOVIE_JSON"    | jq -r '.movieFile.mediaInfo.videoCodec // ""')
    AUDIO_LANGS=$(echo "$MOVIE_JSON"    | jq -r '.movieFile.mediaInfo.audioLanguages // ""')
    DYN_RANGE=$(echo "$MOVIE_JSON"      | jq -r '.movieFile.mediaInfo.videoDynamicRange // ""')
    DYN_TYPE=$(echo "$MOVIE_JSON"       | jq -r '.movieFile.mediaInfo.videoDynamicRangeType // ""')
    FILE_SIZE=$(echo "$MOVIE_JSON"      | jq -r '.movieFile.size // 0')
    RUN_TIME=$(echo "$MOVIE_JSON"       | jq -r '.movieFile.mediaInfo.runTime // ""')
    AUDIO_CODEC=$(echo "$MOVIE_JSON"    | jq -r '.movieFile.mediaInfo.audioCodec // ""')
    AUDIO_CH=$(echo "$MOVIE_JSON"       | jq -r '.movieFile.mediaInfo.audioChannels // ""')
    SUBTITLES=$(echo "$MOVIE_JSON"      | jq -r '.movieFile.mediaInfo.subtitles // ""')
    VIDEO_BIT=$(echo "$MOVIE_JSON"      | jq -r '.movieFile.mediaInfo.videoBitrate // ""')
    VIDEO_FPS=$(echo "$MOVIE_JSON"      | jq -r '.movieFile.mediaInfo.videoFps // ""')
    VIDEO_DEPTH=$(echo "$MOVIE_JSON"    | jq -r '.movieFile.mediaInfo.videoBitDepth // ""')
    AUDIO_BIT=$(echo "$MOVIE_JSON"      | jq -r '.movieFile.mediaInfo.audioBitrate // ""')
    COVER_URL=$(echo "$MOVIE_JSON"      | jq -r '.images[]? | select(.coverType=="poster") | .remoteUrl // ""' | head -1)
    RATING=$(echo "$MOVIE_JSON"         | jq -r '.ratings.tmdb.value // .ratings.value // 0')
    GENRES=$(echo "$MOVIE_JSON"         | jq -r '[.genres[]? ] | join(", ")' 2>/dev/null || echo "")

    log ""
    log "────────────────────────────────────────────────────────────"
    log "Film          : $TITLE ($YEAR)  [Radarr ID: $MOVIE_ID]"

    FILENAME=$(basename "$RADARR_PATH")
    FNAME_UP=$(echo "$FILENAME" | tr '[:lower:]' '[:upper:]')

    log "Fichier       : $FILENAME"
    log "ReleaseGroup  : ${RELEASE_GROUP:-<vide>}"
    log "Qualite       : $QUALITY_NAME"

    [ -z "$RADARR_PATH" ] && {
        log "  SKIP: chemin fichier vide"
        SKIPPED=$((SKIPPED+1))
        echo "SKIP|$TITLE ($YEAR)|Chemin vide" >> "$RESULTS_FILE"
        continue
    }

    # ── Chemin réel sur le NAS ───────────────────────────────────────────
    NAS_FILE_PATH=$(resolve_nas_path "$RADARR_PATH")
    log "Chemin NAS    : ${NAS_FILE_PATH:-INTROUVABLE}"

    if [ -z "$NAS_FILE_PATH" ] || [ ! -f "$NAS_FILE_PATH" ]; then
        log "  SKIP: fichier introuvable sur le NAS (Radarr desynchronise ?)"
        SKIPPED=$((SKIPPED+1))
        echo "SKIP|$TITLE ($YEAR)|Fichier manquant" >> "$RESULTS_FILE"
        continue
    fi

    # ── Release group ────────────────────────────────────────────────────
    if [ -z "$RELEASE_GROUP" ] || [ "$RELEASE_GROUP" = "null" ]; then
        STEM=$(echo "$FILENAME" | sed 's/\.[^.]*$//')
        RELEASE_GROUP=$(echo "$STEM" | grep -oE '\-[A-Za-z0-9]+$' | tr -d '-')
        if [ -n "$RELEASE_GROUP" ]; then
            log "  WARN: releaseGroup vide → extrait du nom de fichier: $RELEASE_GROUP"
        else
            log "  WARN: releaseGroup inconnu → release name sans groupe"
        fi
    fi

    # ── Construction du nom de release ───────────────────────────────────
    # Si le fichier est déjà au format scene (points, pas d'espaces ni parenthèses)
    # → utiliser directement le stem du fichier comme RELEASE_NAME
    FILE_STEM=$(echo "$FILENAME" | sed 's/\.[^.]*$//')
    if ! echo "$FILE_STEM" | grep -q '[[:space:]()\[]'; then
        RELEASE_NAME="$FILE_STEM"
        log "Release name  : $RELEASE_NAME  (depuis nom fichier)"
    else
        # Fallback : reconstruction depuis métadonnées Radarr
        log "  WARN: nom fichier non-scene → reconstruction depuis métadonnées"
        TITLE_CLEAN=$(echo "$TITLE" | sed "s/[':!?,]//g" | sed 's/  */ /g' | sed 's/ /./g')

        # Langue
        if echo "$FNAME_UP" | grep -q 'MULTI'; then
            if echo "$FNAME_UP" | grep -qE 'TRUEFRENCH|VFF'; then LANG_TAG="MULTi.VFF"
            elif echo "$FNAME_UP" | grep -q 'VF2';            then LANG_TAG="MULTi.VF2"
            else                                                    LANG_TAG="MULTi"
            fi
        elif echo "$FNAME_UP" | grep -qE 'TRUEFRENCH|VFF'; then LANG_TAG="TRUEFRENCH"
        elif echo "$FNAME_UP" | grep -q 'VOSTFR';          then LANG_TAG="VOSTFR"
        elif echo "$FNAME_UP" | grep -qE 'FRENCH';         then LANG_TAG="FRENCH"
        else
            LANG_COUNT=$(echo "$AUDIO_LANGS" | tr '/' '\n' | grep -c '[a-z]' 2>/dev/null || echo 0)
            if [ "$LANG_COUNT" -gt 1 ]; then LANG_TAG="MULTi"
            elif echo "$AUDIO_LANGS" | grep -qi 'french\|fr'; then LANG_TAG="FRENCH"
            else LANG_TAG="FRENCH"
            fi
        fi

        # HDR / DV
        HDR_TAG=""
        if echo "$FNAME_UP$DYN_RANGE$DYN_TYPE" | grep -qi 'HDR10+\|HDR10PLUS'; then HDR_TAG="HDR10+"
        elif echo "$FNAME_UP$DYN_RANGE$DYN_TYPE" | grep -qi 'HDR'; then HDR_TAG="HDR"
        fi
        if echo "$FNAME_UP$DYN_TYPE" | grep -qi 'DV\|DOLBY.VISION\|DOLBYVISION'; then
            [ -n "$HDR_TAG" ] && HDR_TAG="${HDR_TAG}.DV" || HDR_TAG="DV"
        fi

        # Résolution
        QN_UP=$(echo "$QUALITY_NAME" | tr '[:lower:]' '[:upper:]')
        if   echo "$QN_UP$FNAME_UP" | grep -qE '2160|4K'; then RESOLUTION="2160p"
        elif echo "$QN_UP$FNAME_UP" | grep -q '1080';     then RESOLUTION="1080p"
        elif echo "$QN_UP$FNAME_UP" | grep -q '720';      then RESOLUTION="720p"
        else RESOLUTION=""
        fi

        # Source
        QL=$(echo "$QUALITY_NAME" | tr '[:upper:]' '[:lower:]')
        if echo "$QL$FNAME_UP" | grep -qi 'bluray\|blu-ray'; then
            if echo "$FNAME_UP" | grep -q 'REMUX';      then SOURCE="BluRay.REMUX"
            elif echo "$FNAME_UP" | grep -q 'COMPLETE'; then SOURCE="COMPLETE.UHD.BLURAY"
            else SOURCE="BluRay"
            fi
        elif echo "$QL$FNAME_UP" | grep -qi 'webdl\|web-dl'; then SOURCE="WEB-DL"
        elif echo "$QL$FNAME_UP" | grep -qi 'webrip';         then SOURCE="WEBRip"
        elif echo "$QL"           | grep -qi 'web';            then SOURCE="WEB"
        elif echo "$QL$FNAME_UP" | grep -qi 'hdtv';           then SOURCE="HDTV"
        elif echo "$FNAME_UP"    | grep -q  'BDRIP';          then SOURCE="BDRip"
        elif echo "$FNAME_UP"    | grep -q  'DVD';            then SOURCE="DVDRip"
        else SOURCE="WEB"
        fi

        # Codec
        if   echo "$FNAME_UP$VIDEO_CODEC" | grep -qiE 'X265|H265|HEVC'; then CODEC="x265"
        elif echo "$FNAME_UP$VIDEO_CODEC" | grep -qiE 'X264|H264|AVC';  then CODEC="x264"
        elif echo "$FNAME_UP$VIDEO_CODEC" | grep -qi  'AV1';            then CODEC="AV1"
        elif echo "$FNAME_UP"             | grep -qi  'XVID';           then CODEC="XviD"
        elif echo "$FNAME_UP"             | grep -qi  'MPEG2';          then CODEC="MPEG2"
        else CODEC="x264"
        fi

        # Assemblage
        RELEASE_NAME="${TITLE_CLEAN}.${YEAR}.${LANG_TAG}"
        [ -n "$HDR_TAG" ]    && RELEASE_NAME="${RELEASE_NAME}.${HDR_TAG}"
        [ -n "$RESOLUTION" ] && RELEASE_NAME="${RELEASE_NAME}.${RESOLUTION}"
        if [ -n "$RELEASE_GROUP" ]; then
            RELEASE_NAME="${RELEASE_NAME}.${SOURCE}.${CODEC}-${RELEASE_GROUP}"
        else
            RELEASE_NAME="${RELEASE_NAME}.${SOURCE}.${CODEC}"
        fi
        log "Release name  : $RELEASE_NAME  (reconstruit)"
    fi

    # FNAME_UP recalculé depuis RELEASE_NAME final pour les termIds
    FNAME_UP=$(echo "$RELEASE_NAME" | tr '[:lower:]' '[:upper:]')

    # ── Vérification historique local ────────────────────────────────────
    if [ -f "$HISTORIQUE_FILE" ] && grep -qiF "$RELEASE_NAME" "$HISTORIQUE_FILE"; then
        log "  SKIP: déjà dans l'historique local"
        SKIPPED=$((SKIPPED+1))
        echo "SKIP|$TITLE ($YEAR)|Historique local" >> "$RESULTS_FILE"
        continue
    fi

    # ── Vérification doublon sur La Cale (via recherche navigateur) ───────
    log "  Vérification doublon sur La Cale (recherche navigateur)..."
    SKIP_FILM=0

    TITLE_ENCODED=$(printf '%s' "$TITLE" | sed 's/ /+/g')
    SEARCH_PAGE=$(curl -sf --max-time 30 \
        -A "$BROWSER_UA" \
        -b "$COOKIE_FILE" -c "$COOKIE_FILE" \
        -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
        -H "Accept-Language: fr-FR,fr;q=0.9,en;q=0.8" \
        -H "Referer: ${LACALE_URL}/torrents" \
        --compressed \
        "${LACALE_URL}/torrents?search=${TITLE_ENCODED}&categories%5B%5D=films" 2>/dev/null)

    if echo "$SEARCH_PAGE" | grep -qi "$TITLE"; then
        log "  SKIP: \"$TITLE\" semble déjà présent sur La Cale (recherche titre)"
        echo "$RELEASE_NAME" >> "$HISTORIQUE_FILE"
        SKIPPED=$((SKIPPED+1))
        echo "SKIP|$TITLE ($YEAR)|Déjà sur La Cale (recherche titre)" >> "$RESULTS_FILE"
        SKIP_FILM=1
    fi

    [ "$SKIP_FILM" -eq 1 ] && continue
    log "  → Absent sur La Cale, on continue."

    # ── Récupération casting TMDB (via API La Cale) ───────────────────────
    CAST_JSON="[]"
    if [ -n "$TMDB_ID" ] && [ "$TMDB_ID" != "null" ] && [ "$TMDB_ID" != "0" ]; then
        TMDB_DETAIL=$(curl -sf --max-time 15 \
            -A "$BROWSER_UA" \
            -b "$COOKIE_FILE" -c "$COOKIE_FILE" \
            -H "Accept: application/json" \
            --compressed \
            "${LACALE_URL}/api/internal/tmdb/details?id=${TMDB_ID}&type=movie" 2>/dev/null)
        if [ -n "$TMDB_DETAIL" ]; then
            # Extraire cast: array [{name, character}]
            CAST_JSON=$(printf '%s' "$TMDB_DETAIL" | jq '[.cast[]? | {name:.name, character:.character}] // []' 2>/dev/null || echo "[]")
            # Récupérer rating/genres TMDB si meilleurs que ceux de Radarr
            TMDB_RATING=$(printf '%s' "$TMDB_DETAIL" | jq -r '.rating // 0' 2>/dev/null)
            TMDB_GENRES=$(printf '%s' "$TMDB_DETAIL" | jq -r '.genres // ""' 2>/dev/null)
            [ -n "$TMDB_RATING" ] && [ "$TMDB_RATING" != "0" ] && [ "$TMDB_RATING" != "null" ] && RATING="$TMDB_RATING"
            [ -n "$TMDB_GENRES" ] && [ "$TMDB_GENRES" != "null" ] && GENRES="$TMDB_GENRES"
        fi
    fi

    # ── Rescan Radarr pour synchroniser relativePath avec le fichier réel ──
    RESCAN_RESP=$(curl -sf --max-time 30 \
        -X POST \
        -H "Content-Type: application/json" \
        "${RADARR_URL}/api/v3/command?apikey=${RADARR_API_KEY}" \
        -d "{\"name\":\"RescanMovie\",\"movieId\":${MOVIE_ID}}" 2>/dev/null)
    if [ -n "$RESCAN_RESP" ]; then
        sleep 5
        FRESH_JSON=$(curl -sf --max-time 15 \
            "${RADARR_URL}/api/v3/movie/${MOVIE_ID}?apikey=${RADARR_API_KEY}" 2>/dev/null)
        if [ -n "$FRESH_JSON" ]; then
            RADARR_PATH=$(echo "$FRESH_JSON"  | jq -r '.movieFile.path // ""')
            RELEASE_GROUP=$(echo "$FRESH_JSON"| jq -r '.movieFile.releaseGroup // ""')
            QUALITY_NAME=$(echo "$FRESH_JSON" | jq -r '.movieFile.quality.quality.name // ""')
            VIDEO_CODEC=$(echo "$FRESH_JSON"  | jq -r '.movieFile.mediaInfo.videoCodec // ""')
            AUDIO_LANGS=$(echo "$FRESH_JSON"  | jq -r '.movieFile.mediaInfo.audioLanguages // ""')
            DYN_RANGE=$(echo "$FRESH_JSON"    | jq -r '.movieFile.mediaInfo.videoDynamicRange // ""')
            DYN_TYPE=$(echo "$FRESH_JSON"     | jq -r '.movieFile.mediaInfo.videoDynamicRangeType // ""')
            FILE_SIZE=$(echo "$FRESH_JSON"    | jq -r '.movieFile.size // 0')
            RUN_TIME=$(echo "$FRESH_JSON"     | jq -r '.movieFile.mediaInfo.runTime // ""')
            AUDIO_CODEC=$(echo "$FRESH_JSON"  | jq -r '.movieFile.mediaInfo.audioCodec // ""')
            AUDIO_CH=$(echo "$FRESH_JSON"     | jq -r '.movieFile.mediaInfo.audioChannels // ""')
            SUBTITLES=$(echo "$FRESH_JSON"    | jq -r '.movieFile.mediaInfo.subtitles // ""')
            VIDEO_BIT=$(echo "$FRESH_JSON"    | jq -r '.movieFile.mediaInfo.videoBitrate // ""')
            VIDEO_FPS=$(echo "$FRESH_JSON"    | jq -r '.movieFile.mediaInfo.videoFps // ""')
            VIDEO_DEPTH=$(echo "$FRESH_JSON"  | jq -r '.movieFile.mediaInfo.videoBitDepth // ""')
            AUDIO_BIT=$(echo "$FRESH_JSON"    | jq -r '.movieFile.mediaInfo.audioBitrate // ""')
            FILENAME=$(basename "$RADARR_PATH")
            FNAME_UP=$(echo "$FILENAME" | tr '[:lower:]' '[:upper:]')
            log "  ✓ Rescan Radarr OK — fichier: $FILENAME"
        fi
    else
        log "  WARN: Rescan Radarr echoue — donnees potentiellement obsoletes"
    fi

    # ── MediaInfo + Création du torrent (Docker Alpine) ──────────────────
    log "  Génération NFO (mediainfo) + création du torrent..."
    NFO_PATH="${NFO_DIR}/${RELEASE_NAME}.nfo"
    TORRENT_PATH="${TORRENTS_DIR}/${RELEASE_NAME}.torrent"

    FOLDER_NAME=$(echo "$RADARR_PATH" | sed "s|^${RADARR_PATH_PREFIX}/||" | cut -d'/' -f1)
    log "  Dossier film  : $FOLDER_NAME"

    TORRENT_OK=0
    docker run --rm \
        -v "${NAS_PATH_PREFIX}:/mnt/zfs:ro" \
        -v "${WORK_DIR}:/work:rw" \
        -e "IN_FOLDER=${FOLDER_NAME}" \
        -e "IN_FILE=$(echo "$RADARR_PATH" | sed "s|^${RADARR_PATH_PREFIX}/||" | cut -d'/' -f2-)" \
        -e "REL_NAME=${RELEASE_NAME}" \
        -e "TRACKER=${TRACKER_URL}" \
        "$DOCKER_PYTHON" \
        sh -c '
            apk add --no-cache python3 mediainfo -q 2>/dev/null
            FULL_PATH=$(ls -d /mnt/zfs/*/Films/"$IN_FOLDER"/"$IN_FILE" 2>/dev/null | head -1)
            if [ -z "$FULL_PATH" ] || [ ! -f "$FULL_PATH" ]; then
                echo "ERREUR: fichier non trouvé dans Docker: $IN_FOLDER/$IN_FILE" >&2
                exit 1
            fi
            echo "  Chemin Docker : $FULL_PATH"
            mediainfo "$FULL_PATH" > "/work/$REL_NAME.nfo" 2>/dev/null || true
            python3 /work/make_torrent.py \
                "$FULL_PATH" \
                "$REL_NAME" \
                "$TRACKER" \
                "/work/$REL_NAME.torrent"
        ' && TORRENT_OK=1

    # NFO : priorité mediainfo, fallback Radarr
    NFO_SOURCE="mediainfo (Alpine)"
    if [ -f "${WORK_DIR}/${RELEASE_NAME}.nfo" ] && [ -s "${WORK_DIR}/${RELEASE_NAME}.nfo" ]; then
        # Nettoie le chemin Docker interne (/mnt/zfs/...) → juste le nom de fichier
        _EXT=$(echo "$FILENAME" | grep -oE '\.[^.]+$' | tr '[:upper:]' '[:lower:]')
        sed "s|Complete name[[:space:]]*:.*|Complete name                            : ${RELEASE_NAME}${_EXT}|g" \
            "${WORK_DIR}/${RELEASE_NAME}.nfo" > "$NFO_PATH"
        log "  NFO : $(wc -c < "$NFO_PATH") chars via $NFO_SOURCE"
    else
        NFO_SOURCE="Radarr mediaInfo (fallback)"
        SIZE_GIB=$(echo "$FILE_SIZE" | awk '{printf "%.2f", $1/1073741824}')
        printf 'General\nComplete name : %s\nFile size     : %s GiB\nDuration      : %s\n\nVideo\nFormat        : %s\nBit rate      : %s kb/s\nFrame rate    : %s FPS\nBit depth     : %s bits\nHDR           : %s\n\nAudio\nFormat        : %s\nBit rate      : %s kb/s\nChannel(s)    : %s channels\nLanguage(s)   : %s\n\nSubtitles     : %s\n' \
            "$FILENAME" "$SIZE_GIB" "$RUN_TIME" \
            "$VIDEO_CODEC" "$VIDEO_BIT" "$VIDEO_FPS" "$VIDEO_DEPTH" "$DYN_RANGE" \
            "$AUDIO_CODEC" "$AUDIO_BIT" "$AUDIO_CH" "$AUDIO_LANGS" \
            "$SUBTITLES" > "$NFO_PATH"
        log "  WARN: mediainfo échoué → NFO depuis données Radarr"
        log "  NFO : $(wc -c < "$NFO_PATH") chars via $NFO_SOURCE"
    fi
    log "  NFO sauvegardé : $NFO_PATH"

    if [ "$TORRENT_OK" -eq 1 ] && [ -f "${WORK_DIR}/${RELEASE_NAME}.torrent" ]; then
        cp "${WORK_DIR}/${RELEASE_NAME}.torrent" "$TORRENT_PATH"
    fi

    if [ "$TORRENT_OK" -eq 0 ] || [ ! -f "$TORRENT_PATH" ]; then
        log "  ERREUR: création du torrent échouée"
        ERRORS=$((ERRORS+1))
        echo "ERREUR|$TITLE ($YEAR)|Création torrent échouée" >> "$RESULTS_FILE"
        continue
    fi
    log "  ✓ Torrent créé : $TORRENT_PATH"

    # ── Vérification doublon par info_hash (API parse) ────────────────────────
    PARSE_RESULT=$(curl -sf --max-time 30 \
        -A "$BROWSER_UA" \
        -b "$COOKIE_FILE" -c "$COOKIE_FILE" \
        -H "Accept: application/json" \
        -H "Referer: ${LACALE_URL}/upload" \
        -H "Origin: ${LACALE_URL}" \
        --compressed \
        -X POST \
        -F "file=@${TORRENT_PATH};type=application/x-bittorrent" \
        "${LACALE_URL}/api/internal/torrents/parse" 2>/dev/null)
    if echo "$PARSE_RESULT" | grep -qi '"duplicate"[[:space:]]*:[[:space:]]*true\|"exists"[[:space:]]*:[[:space:]]*true\|already exist\|torrentId'; then
        log "  SKIP: torrent déjà présent sur La Cale (info_hash identique)"
        echo "$RELEASE_NAME" >> "$HISTORIQUE_FILE"
        SKIPPED=$((SKIPPED+1))
        echo "SKIP|$TITLE ($YEAR)|Doublon hash détecté via /api/internal/torrents/parse" >> "$RESULTS_FILE"
        continue
    fi


    # ── Mapping des termIds (Caractéristiques de la release) ─────────────────
    TERM_IDS=""

    # Helper: ajouter un term
    add_term() { TERM_IDS="${TERM_IDS:+${TERM_IDS},}$1"; }

    # --- Genres (depuis Radarr/TMDB) ---
    echo "$GENRES" | tr ',/' '\n' | while read -r G; do
        G=$(echo "$G" | sed 's/^ *//;s/ *$//')
        case "$G" in
            Action)           echo "term_561bfb1bc6aa4eb236a0096055df56d3" ;;
            Animation)        echo "term_104b4c4889059907b69469199e91e650" ;;
            Adventure|Aventure) echo "term_53318115f9881cba4ea3c5d5fbcbdd7a" ;;
            Biography|Biopic) echo "term_fc1f45b5830a6c43ac1e04c15de20fd6" ;;
            Comedy|Comédie)   echo "term_2565c6c823f8770fd7bcaaf8825676e1" ;;
            Documentary|Documentaire) echo "term_5c93004f538b8ff2d0384371e52f6926" ;;
            Drama|Drame)      echo "term_86aac9f2daee035fd7fdbec3c01ec49c" ;;
            Family|Familial)  echo "term_15736578e8038ed0adb120204921a6e3" ;;
            Fantasy|Fantastique) echo "term_2c74d8bf4a34c8b3f1f41e66aebd5ec9" ;;
            History|Historique) echo "term_6b60cdc761f4ea38e98a035868a73692" ;;
            Horror|Horreur)   echo "term_6ec3481f6e45a178a3246e09a3be844b" ;;
            Music|Musical)    echo "term_983454715ab3dbc095012bf20dc27ba7" ;;
            "Crime"|"Policier / Thriller"|Thriller|Crime) echo "term_6dbb7e22f0aae37746d710ea3e23ce03" ;;
            Romance)          echo "term_fb1342ef0b14b7384a3e450335e3fdc2" ;;
            "Science Fiction"|"Science-fiction"|Sci-Fi) echo "term_845f0e31f46f4cfdf305681732759559" ;;
            Sport|Sports)     echo "term_c6d861d65b8d6191e24d48fd18347581" ;;
            War|Guerre)       echo "term_ffcb1f78a535d21a627116bb84b9fdb3" ;;
            Western)          echo "term_6ba0e4717a668f400cd2526debb7d0fc" ;;
            Suspense)         echo "term_788f7971971cfa7d4f7ff3028b17dcda" ;;
            "TV Movie"|Téléfilm) echo "term_30d959f14ad88fc00700173a23c386d8" ;;
        esac
    done > "${WORK_DIR}/genre_terms.txt"
    while IFS= read -r T; do [ -n "$T" ] && add_term "$T"; done < "${WORK_DIR}/genre_terms.txt"

    # --- Qualité / Résolution ---
    case "$RESOLUTION" in
        2160p) add_term "term_947df6343911cdf2c9e477cf4bddfc56" ;;
        1080p) add_term "term_e7dd3707cd20c0cfccd272334eba5bbf" ;;
        720p)  add_term "term_4437c0c05981fa692427eb0d92a25a34" ;;
        *)     add_term "term_6ade2712b8348f39b892c00119915454" ;;  # SD
    esac

    # --- Codec vidéo ---
    case "$CODEC" in
        x265) add_term "term_27dc36ee2c6fad6b87d71ed27e4b8266" ;;
        x264) add_term "term_9289368e710fa0c350a4c64f36fb03b5" ;;
        AV1)  add_term "term_e2806600360399f7597c9d582325d1ea" ;;
    esac

    # --- Caractéristiques vidéo ---
    if [ -n "$HDR_TAG" ]; then
        case "$HDR_TAG" in
            *HDR10+*) add_term "term_3458ddfaf530675b6566cf48cda76001" ;;
            *HDR*)    add_term "term_1e6061fe0dd0f6ce8027b1bce83b6b7d" ;;
        esac
        echo "$HDR_TAG" | grep -qi 'DV\|Dolby' && add_term "term_51d58202387e82525468fc738da02246"
    fi
    [ "$VIDEO_DEPTH" = "10" ] && add_term "term_ca34690b0fb2717154811a343bbfe05a"

    # --- Source / Type ---
    case "$SOURCE" in
        "BluRay.REMUX") add_term "term_fdb58f8f752de86716d0312fcfecbc71" ; add_term "term_6251bf6918d6193d846e871b8b1c2f58" ;;
        "BluRay")       add_term "term_6251bf6918d6193d846e871b8b1c2f58" ;;
        "WEB-DL")       add_term "term_8d7cfc3d0e1178ae2925ef270235b8d3" ;;
        "WEBRip")       add_term "term_2ad87475841ea5d8111d089e5f6f2108" ;;
        "DVDRip")       add_term "term_7321eb03c51abdd81902fcff4cd26171" ;;
        "HDTV")         add_term "term_b3cd9652a11c4bd9cdcbb7597ab8c39b" ;;
        "WEB")          add_term "term_8d7cfc3d0e1178ae2925ef270235b8d3" ;;
    esac

    # --- Codec audio ---
    AUDIO_UP=$(echo "$AUDIO_CODEC" | tr '[:lower:]' '[:upper:]')
    case "$AUDIO_UP" in
        *TRUEHD*ATMOS*|*ATMOS*TRUEHD*) add_term "term_a2cf45267addea22635047c4d69465a0" ;;
        *TRUEHD*)   add_term "term_99a276df7596f2eb0902463e95111b76" ;;
        *EAC3*ATMOS*|*ATMOS*EAC3*) add_term "term_4671d371281904dcc885ddc92e92136d" ;;
        *EAC3*|*E-AC3*) add_term "term_8945be80314068e014c773f9d4cd7eb2" ;;
        *AC3*|*DD*)  add_term "term_e72a6bc1a89ca8c39f7a7fac21b95ef8" ;;
        *DTS:X*)     add_term "term_b3c9a9660e1c6ab6910859254fd592e1" ;;
        *DTSHDMA*|*DTSHD*MA*) add_term "term_49617ee39348e811452a2a4b7f5c0c64" ;;
        *DTSHD*|*DTS-HD*) add_term "term_934dcc048eaa8b4ef48548427735a797" ;;
        *DTS*)       add_term "term_d908f74951dee053ddada1bc0a8206db" ;;
        *AAC*)       add_term "term_b7ce0315952660c99a4ef7099b9154cb" ;;
        *FLAC*)      add_term "term_d857503fbf92ed967f81742146619c40" ;;
        *MP3*)       add_term "term_0e2cdd8fd9f0031e7ffdbdb9255b8a31" ;;
    esac

    # --- Langues audio ---
    case "$LANG_TAG" in
        MULTi*VFF|MULTi*VF2)
            add_term "term_fd7d017b825ebf12ce579dacea342e9d"  # MULTI
            add_term "term_bf31bb0a956b133988c2514f62eb1535"  # VFF
            ;;
        MULTi)
            add_term "term_fd7d017b825ebf12ce579dacea342e9d"  # MULTI
            add_term "term_bf918c3858a7dfe3b44ca70232f50272"  # French
            add_term "term_c87b5416341e6516baac12aa01fc5bc9"  # English
            ;;
        TRUEFRENCH|VFF)
            add_term "term_bf31bb0a956b133988c2514f62eb1535"  # VFF
            ;;
        FRENCH)
            add_term "term_bf918c3858a7dfe3b44ca70232f50272"  # French
            ;;
        VOSTFR)
            add_term "term_c87b5416341e6516baac12aa01fc5bc9"  # English
            ;;
    esac

    # --- Sous-titres ---
    if [ -n "$SUBTITLES" ]; then
        echo "$SUBTITLES" | grep -qi 'fre\|fr\b' && add_term "term_9ef8bba2b9cd0d6c167f97b64c216d91"
        echo "$SUBTITLES" | grep -qi 'eng\|en\b' && add_term "term_c0468b06760040c3a9a0674cd7eb224f"
    fi

    # --- Langues (champ séparé) ---
    case "$LANG_TAG" in
        MULTi*)
            add_term "term_9cf21ecaa17940f8ea4f3b2d44627876"  # Français
            add_term "term_de9f4583ec916d7778e08783574796a5"  # Anglais
            ;;
        FRENCH|TRUEFRENCH|VFF|VOSTFR)
            add_term "term_9cf21ecaa17940f8ea4f3b2d44627876"  # Français
            ;;
    esac

    # --- Extension ---
    FILE_EXT=$(echo "$FILENAME" | grep -oE '\.[^.]+$' | tr '[:upper:]' '[:lower:]')
    case "$FILE_EXT" in
        .mkv) add_term "term_513ee8e7d062c6868b092c9a4267da8a" ;;
        .mp4) add_term "term_069f4f60531ce23f9f2bfe4ce834d660" ;;
        .avi) add_term "term_79db12fca0a1e537f6185f7aee22b8d7" ;;
    esac

    log "  TermIds : ${TERM_IDS:-<aucun>}"

    # Construire les arguments -F termIds[] pour curl
    TERM_CURL_ARGS=""
    if [ -n "$TERM_IDS" ]; then
        OLD_IFS="$IFS"; IFS=','
        for TID in $TERM_IDS; do
            [ -n "$TID" ] && TERM_CURL_ARGS="$TERM_CURL_ARGS -F termIds[]=$TID"
        done
        IFS="$OLD_IFS"
    fi

    # ── Vérification seed : fichier physique accessible par qBittorrent ─────────
    log "  Vérification seed qBittorrent..."
    SEED_OK=0

    # Chemin vu par qBittorrent (sans le préfixe NAS)
    QB_FILE_PATH=$(echo "$NAS_FILE_PATH" | sed "s|^${NAS_PATH_PREFIX}||")

    # Vérifier via l'API qBittorrent si le fichier est accessible
    QB_COOKIE_PRE="${WORK_DIR}/qb_pre_cookie.txt"
    QB_LOGIN_PRE=$(curl -sf --max-time 10 \
        -c "$QB_COOKIE_PRE" -X POST \
        "${QB_URL}/api/v2/auth/login" \
        -d "username=${QB_USER}&password=${QB_PASS}" 2>/dev/null)

    if echo "$QB_LOGIN_PRE" | grep -qi 'Ok'; then
        # Vérifier si le fichier existe déjà dans un torrent qBittorrent en seed
        _QB_ALL=$(curl -sf --max-time 10 \
            -b "$QB_COOKIE_PRE" \
            "${QB_URL}/api/v2/torrents/info" 2>/dev/null)
        _ALREADY_SEEDING=$(echo "$_QB_ALL" | python -c "
import json,sys
data=json.loads(sys.stdin.read())
fname='$(echo "$FILENAME" | sed "s/'/'\''/g")'
for t in data:
    n = t.get('name','')
    state = t.get('state','')
    if (n == fname or n == fname.rsplit('.',1)[0]) and any(s in state for s in ['UP','seeding','uploading']):
        print('already_seeding')
        break
" 2>/dev/null)

        if [ "$_ALREADY_SEEDING" = "already_seeding" ]; then
            log "  ✓ Fichier déjà en seed dans qBittorrent"
            SEED_OK=1
        else
            # Vérifier simplement que le fichier physique est accessible
            QB_CHECK=$(curl -sf --max-time 10 \
                -b "$QB_COOKIE_PRE" \
                "${QB_URL}/api/v2/app/version" 2>/dev/null)
            if [ -n "$QB_CHECK" ] && [ -f "$NAS_FILE_PATH" ]; then
                log "  ✓ Fichier accessible — seed possible après upload"
                SEED_OK=1
            else
                log "  ✗ Fichier inaccessible : $NAS_FILE_PATH"
            fi
        fi
    else
        log "  ✗ Connexion qBittorrent échouée"
    fi

    if [ "$SEED_OK" -eq 0 ]; then
        log "  ✗ ERREUR: La cargaison n'est pas scellée !"
        ERRORS=$((ERRORS+1))
        echo "ERREUR|$TITLE ($YEAR)|La cargaison n'est pas scellée !" >> "$RESULTS_FILE"
        continue
    fi

    # ── Upload sur La Cale via /api/internal/torrents/upload (API REST Next.js) ───────
    log "  Upload sur La Cale via API REST /api/internal/torrents/upload..."

    # Pas de CSRF token (app Next.js full REST, sessions via cookies httpOnly)
    # isAnonymous: "false" ou "true" (string)
    # IMPORTANT: les champs multilignes (nfoText, description) doivent être passés
    # via fichiers temporaires avec la syntaxe curl -F "champ=<fichier"
    # (évite la corruption des sauts de ligne quand bash expand la variable)
    NFO_TEXT_FILE="${WORK_DIR}/nfotext_field.txt"
    DESCRIPTION_FILE="${WORK_DIR}/description_field.txt"
    printf '%s' "" > "$NFO_TEXT_FILE"
    printf '%s' "" > "$DESCRIPTION_FILE"
    [ -f "$NFO_PATH" ] && cat "$NFO_PATH" > "$NFO_TEXT_FILE"
    generate_bbcode \
        "$TITLE" "$YEAR" "$OVERVIEW" "$COVER_URL" \
        "$QUALITY_NAME" "$VIDEO_CODEC" "$AUDIO_CODEC" "$AUDIO_LANGS" \
        "$FILE_SIZE" "$RATING" "$GENRES" "$CAST_JSON" \
        "$SUBTITLES" "$DYN_RANGE" "$DYN_TYPE" \
        > "$DESCRIPTION_FILE"

    CURL_DEBUG="${WORK_DIR}/curl_upload_debug.txt"

    UPLOAD_RESPONSE=$(curl -si --max-time 120 \
        --trace-ascii "$CURL_DEBUG" \
        -A "$BROWSER_UA" \
        -b "$COOKIE_FILE" -c "$COOKIE_FILE" \
        -H "Accept: application/json" \
        -H "Accept-Language: fr-FR,fr;q=0.9,en;q=0.8" \
        -H "Referer: ${LACALE_URL}/upload" \
        -H "Origin: ${LACALE_URL}" \
        --compressed \
        -X POST \
        -F "title=${RELEASE_NAME}" \
        -F "categoryId=${CATEGORY_ID}" \
        -F "isAnonymous=false" \
        -F "file=@${TORRENT_PATH};type=application/x-bittorrent" \
        -F "nfoText=<${NFO_TEXT_FILE}" \
        -F "nfoFile=@${NFO_PATH};type=text/plain" \
        -F "description=<${DESCRIPTION_FILE}" \
        ${TMDB_ID:+-F "tmdbId=${TMDB_ID}" -F "tmdbType=MOVIE"} \
        ${TERM_CURL_ARGS} \
        "${LACALE_URL}/api/internal/torrents/upload" 2>/dev/null)

    HTTP_UPLOAD=$(echo "$UPLOAD_RESPONSE" | grep -oE '^HTTP/[0-9.]+ [0-9]+' | tail -1 | grep -oE '[0-9]+$')
    # Séparer headers et body
    UPLOAD_HEADERS=$(echo "$UPLOAD_RESPONSE" | sed -n '1,/^\r\{0,1\}$/p')
    UPLOAD_BODY=$(echo "$UPLOAD_RESPONSE" | sed -n '/^\r\{0,1\}$/,$ p' | tail -n +2)
    log "  HTTP upload: ${HTTP_UPLOAD:-?}"
    log "  Headers réponse: $(echo "$UPLOAD_HEADERS" | grep -iE 'content-type|x-|cf-' | tr '\n' ' ')"
    # Log du body complet pour diagnostic (limité à 800 chars)
    log "  Body upload: $(echo "$UPLOAD_BODY" | head -c 800)"
    # Copier le debug curl dans les logs permanents
    [ -f "$CURL_DEBUG" ] && cp "$CURL_DEBUG" "${LOGS_DIR}/curl_upload_debug_${LOG_DATE}.txt" && \
        log "  Debug curl: ${LOGS_DIR}/curl_upload_debug_${LOG_DATE}.txt"

    # Détection du résultat JSON
    UPLOAD_OK="false"
    TORRENT_SLUG=""
    TORRENT_LINK=""

    # Parsing JSON de la réponse API REST
    if echo "$UPLOAD_BODY" | grep -q '"success"'; then
        UPLOAD_OK=$(echo "$UPLOAD_BODY" | jq -r '.success // false' 2>/dev/null)
        TORRENT_SLUG=$(echo "$UPLOAD_BODY" | jq -r '.slug // ""' 2>/dev/null)
        TORRENT_LINK=$(echo "$UPLOAD_BODY" | jq -r '.link // ""' 2>/dev/null)
    fi

    # Fallback : HTTP 200 avec data.torrentId = succès
    if [ "$UPLOAD_OK" != "true" ] && [ "$HTTP_UPLOAD" = "200" ]; then
        if echo "$UPLOAD_BODY" | grep -q '"torrentId"\|"infoHash"\|"slug"'; then
            UPLOAD_OK="true"
            TORRENT_SLUG=$(echo "$UPLOAD_BODY" | jq -r '.slug // .data.slug // ""' 2>/dev/null)
        fi
    fi

    if [ "$UPLOAD_OK" != "true" ]; then
        ERR_MSG=$(echo "$UPLOAD_BODY" | jq -r '.message // .error // ""' 2>/dev/null)
        [ -z "$ERR_MSG" ] && ERR_MSG=$(echo "$UPLOAD_BODY" | head -c 300)
        LAST_ERROR="$ERR_MSG"
        log "  ERREUR upload (HTTP $HTTP_UPLOAD): $ERR_MSG"
        ERRORS=$((ERRORS+1))
        echo "ERREUR|$TITLE ($YEAR)|Upload: $ERR_MSG" >> "$RESULTS_FILE"
        continue
    fi

    log "  ✓ Upload OK"
    [ -n "$TORRENT_SLUG" ] && log "  ✓ Slug : $TORRENT_SLUG"
    [ -n "$TORRENT_LINK" ] && log "  ✓ Lien : $TORRENT_LINK"

    # ── Ajout dans qBittorrent (seed) ─────────────────────────────────────
    log "  Ajout qBittorrent (seed mode)..."
    NAS_SAVE_DIR=$(dirname "$NAS_FILE_PATH" | sed "s|^${NAS_PATH_PREFIX}||" | python -c "import sys,unicodedata; print(unicodedata.normalize('NFC', sys.stdin.read().strip()))")
    QB_COOKIE="${WORK_DIR}/qb_cookie.txt"

    QB_LOGIN=$(curl -sf --max-time 10 \
        -c "$QB_COOKIE" -X POST \
        "${QB_URL}/api/v2/auth/login" \
        -d "username=${QB_USER}&password=${QB_PASS}" 2>/dev/null)

    QB_OK=0
    QB_HASH=""
    if echo "$QB_LOGIN" | grep -qi 'Ok'; then
        QB_ADD=$(curl -sf --max-time 30 \
            -b "$QB_COOKIE" -X POST \
            "${QB_URL}/api/v2/torrents/add" \
            -F "torrents=@${TORRENT_PATH};type=application/x-bittorrent" \
            -F "savepath=${NAS_SAVE_DIR}" \
            -F "skip_checking=true" \
            -F "paused=false" \
            2>/dev/null)
        if echo "$QB_ADD" | grep -qi 'Ok'; then
            QB_OK=1
            # Récupérer le hash du torrent ajouté pour vérification
            log "  ~ Chargement de la cargaison en cours, attendez 30 secondes ~"
            sleep 30
            QB_HASH=$(curl -sf --max-time 10 \
                -b "$QB_COOKIE" \
                "${QB_URL}/api/v2/torrents/info" 2>/dev/null | python -c "
import json,sys
data=json.loads(sys.stdin.read())
fname='$(echo "$FILENAME" | sed "s/'/'\''/g")'
for t in data:
    n = t.get('name','')
    if n == fname or n == fname.rsplit('.',1)[0]:
        print(t.get('hash',''))
        break
" 2>/dev/null)
            if [ -n "$QB_HASH" ]; then
                QB_STATE=$(curl -sf --max-time 10 \
                    -b "$QB_COOKIE" \
                    "${QB_URL}/api/v2/torrents/info?hashes=${QB_HASH}" 2>/dev/null | python -c "
import json,sys
data=json.loads(sys.stdin.read())
print(data[0].get('state','') if data else '')
" 2>/dev/null)
                log "  État qBittorrent : ${QB_STATE:-inconnu}"

                # Si en cours de vérification → attendre 30s et re-vérifier
                if echo "$QB_STATE" | grep -qiE 'checking|metaDL'; then
                    log "  ~ Vérification en cours, attendez 30 secondes ~"
                    sleep 30
                    QB_STATE=$(curl -sf --max-time 10 \
                        -b "$QB_COOKIE" \
                        "${QB_URL}/api/v2/torrents/info?hashes=${QB_HASH}" 2>/dev/null | python -c "
import json,sys
data=json.loads(sys.stdin.read())
print(data[0].get('state','') if data else '')
" 2>/dev/null)
                    log "  État après attente : ${QB_STATE:-inconnu}"
                fi

                # Si missingFiles → forcer recheck
                if echo "$QB_STATE" | grep -qi 'missingFiles\|error'; then
                    log "  WARN: fichier non trouvé par qBittorrent — recheck forcé..."
                    curl -sf --max-time 10 -b "$QB_COOKIE" -X POST \
                        -d "hashes=${QB_HASH}" \
                        "${QB_URL}/api/v2/torrents/recheck" >/dev/null 2>&1
                    sleep 30
                    QB_STATE=$(curl -sf --max-time 10 \
                        -b "$QB_COOKIE" \
                        "${QB_URL}/api/v2/torrents/info?hashes=${QB_HASH}" 2>/dev/null | python -c "
import json,sys
data=json.loads(sys.stdin.read())
print(data[0].get('state','') if data else '')
" 2>/dev/null)
                    log "  État après recheck : ${QB_STATE:-inconnu}"
                fi

                log "  État final qBittorrent : ${QB_STATE:-inconnu}"
            fi
        fi
    fi

    if [ "$QB_OK" -eq 1 ]; then
        log "  ✓ Torrent ajouté dans qBittorrent (état: ${QB_STATE:-OK})"
    else
        log "  WARN: ajout qBittorrent échoué (upload La Cale OK)"
        log "  qBittorrent login: $QB_LOGIN"
    fi

    # ── Historique ────────────────────────────────────────────────────────
    echo "$RELEASE_NAME" >> "$HISTORIQUE_FILE"
    UPLOADED=$((UPLOADED+1))
    QB_STATUS="OK"; [ "$QB_OK" -eq 0 ] && QB_STATUS="ERREUR"
    echo "OK|$TITLE ($YEAR)|$RELEASE_NAME|${TORRENT_LINK}|qBittorrent=$QB_STATUS|NFO=$NFO_SOURCE" >> "$RESULTS_FILE"

done < "${WORK_DIR}/movies_with_files.jsonl"

# ─── Rapport final ─────────────────────────────────────────────────────────────
log_section "RAPPORT FINAL"
log "Uploadés : $UPLOADED  |  Skippés : $SKIPPED  |  Erreurs : $ERRORS"
log ""
while IFS='|' read -r STATUS REST; do
    case "$STATUS" in
        OK)     ICON="✓" ;;
        SKIP)   ICON="⏭" ;;
        ERREUR) ICON="✗" ;;
        *)      ICON="?" ;;
    esac
    log "  $ICON [$STATUS] $REST"
done < "$RESULTS_FILE"

# ─── Envoi mail ───────────────────────────────────────────────────────────────
log_section "Envoi rapport par mail"
STATS_LINE="${UPLOADED} uploadé(s), ${SKIPPED} skip, ${ERRORS} erreur(s)"
send_report "$MAIL_SUBJECT — $(date '+%Y-%m-%d %H:%M') — $STATS_LINE" "$REPORT_FILE"

cp "$REPORT_FILE" "$LOG_FILE" 2>/dev/null || true
log "=== Terminé — Log: $LOG_FILE ==="

# ─── Nettoyage ─────────────────────────────────────────────────────────────────
log ""; log "Nettoyage des fichiers temporaires..."
OLD_COUNT=$(find "${BLACK_FLAG_DIR}/_tmp" -maxdepth 1 -name "lacale_*" -mtime +1 2>/dev/null | wc -l)
rm -rf "$WORK_DIR"
echo "[$(date '+%Y-%m-%d %H:%M:%S')]   ✓ Dossier session supprimé : $WORK_DIR"
find "${BLACK_FLAG_DIR}/_tmp" -maxdepth 1 -name "lacale_*" -mtime +1 -exec rm -rf {} \; 2>/dev/null || true
if [ "$OLD_COUNT" -gt 0 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')]   ✓ $OLD_COUNT ancien(s) dossier(s) temporaire(s) supprimé(s)"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')]   ✓ Aucun ancien dossier temporaire à nettoyer"
fi
echo '             .                         .               +                         '"'"'        '
echo '        .   .                  .        .                                      '"'"'          '
echo '               .  |                  '"'"' '"'"'      '"'"'                  .                        '
echo '                --o--                            +                                        '
echo ' .     .     '"'"'    |       '"'"'   .        '"'"'               .       '"'"'      '"'"'+    '"'"'             '
echo '                           '"'"'                                    +                 '"'"'  '"'"'    '
echo '               o   .    +            .                     .o                   '"'"'         '
echo '                                                                + .                       '
if [ "$UPLOADED" -gt 1 ]; then
    echo '        '"'"'                .        ~ cargaisons en route ~             .        *   o  '
elif [ "$UPLOADED" -eq 1 ]; then
    echo '        '"'"'                .        ~ cargaison en route ~              .        *   o  '
elif [ "$UPLOADED" -eq 0 ] && echo "$LAST_ERROR" | grep -q "Limite de 1 torrent"; then
    echo '        '"'"'                .    ~ c'"'"'est la chope! reviens demain! ~             .        *   o  '
elif [ "$UPLOADED" -eq 0 ] && [ "$ERRORS" -gt 0 ]; then
    echo '        '"'"'                .    ~ le navire est resté à quai ~             .        *   o  '
else
    echo '        '"'"'                .        ~ pas de vent aujourd'"'"'hui ~             .        *   o  '
fi
echo '                         .                                    +          +                '
echo '                          o                +                                              '
echo ' '"'"'                      .                      .                            *             '
echo '                     .                      o          *                                  '
echo '.                    o                                                                    '
echo '                                      o   *     o       .           .    .                '
echo '                                                                                o         '
echo '                          .              .                                                '
echo '               '"'"'                   .                                              .      '"'"' '
echo '         o      .                 '"'"'                     '"'"'                                 '
echo '           .       .                '"'"'                              o            '"'"'          '
