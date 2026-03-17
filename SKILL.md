---
name: garmin-connect
description: >
  Fetch and analyze Garmin Connect fitness data using the python-garminconnect library.
  Use this skill whenever the user asks about their workouts, training, running, cycling,
  swimming, heart rate, sleep, HRV, body battery, training readiness, stress, VO2max,
  race predictions, training plans, recovery, fitness age, steps, weight, or any Garmin
  device data. Also trigger when the user says "Garmin", "entreno", "entrenamiento",
  "mi reloj", "mi actividad", or references exercise/fitness data they've recorded.
  This skill handles authentication, data retrieval, analysis, and visualization.
---

# Garmin Connect Skill

Connect to Garmin Connect to retrieve and analyze fitness, training, and recovery data.

## Prerequisites

- Python library `garminconnect` (pre-installed)
- User must provide Garmin credentials (email + password) for authentication
- Credentials are used only for the current session and never stored permanently

## Authentication Flow

**IMPORTANT**: Authentication requires the user's Garmin email and password. Handle with care:

1. Ask the user for their Garmin Connect email and password
2. Run the auth script: `python3 /path/to/skill/scripts/garmin_auth.py <email> <password>`
3. This saves session tokens to `/tmp/garmin_session/tokens` (valid ~24h)
4. All subsequent API calls load tokens from that path — no need to re-enter credentials

If MFA is enabled on the user's account, the script will prompt for a code. Ask the user and pass it along.

If login fails with "TOO_MANY_REQUESTS" or rate-limit errors, wait a few minutes and retry.

## Core Workflow

For every Garmin data request:

1. **Check session**: Verify `/tmp/garmin_session/tokens` exists. If not, run auth flow.
2. **Fetch data**: Use the appropriate script from `scripts/` or write inline Python using the API reference.
3. **Analyze**: Process the raw JSON data into meaningful insights.
4. **Present**: Summarize findings conversationally in Spanish, with key metrics highlighted.

## Available Scripts

### `scripts/garmin_auth.py`
Authenticates and saves session tokens. Usage:
```bash
python3 scripts/garmin_auth.py <email> <password>
```

### `scripts/garmin_fetch.py`
General-purpose data fetcher. Usage:
```bash
python3 scripts/garmin_fetch.py <command> [args...]
```

Commands:
- `activities [limit] [type]` — Recent activities (default: 10)
- `activity <id>` — Single activity details with splits
- `activity_details <id>` — Full activity details (HR, pace charts, laps)
- `sleep <date>` — Sleep data for a date (YYYY-MM-DD)
- `hrv <date>` — HRV data for a date
- `body_battery <start> [end]` — Body battery over date range
- `training_readiness <date>` — Training readiness score
- `training_status <date>` — Training status (productive, recovery, etc.)
- `stress <date>` — All-day stress data
- `stats <date>` — Daily stats summary
- `race_predictions` — Current race time predictions
- `max_metrics <date>` — VO2max and other max metrics
- `steps <start> <end>` — Daily steps over range
- `weight <start> <end>` — Weight/body composition over range
- `heart_rate <date>` — Heart rate for a date
- `personal_records` — All personal records
- `fitness_age <date>` — Fitness age data
- `endurance <start> [end]` — Endurance score
- `hill_score <start> [end]` — Hill score
- `weekly_steps <end> [weeks]` — Weekly step totals
- `devices` — Connected devices
- `goals` — Active goals
- `workouts [limit]` — Saved workouts
- `training_plans` — Active training plans
- `last_activity` — Most recent activity

Output is always JSON to stdout. Claude should parse it and present insights.

## Analysis Guidelines

When analyzing training data, focus on:

### Entrenamientos (Running/Cycling/etc.)
- **Ritmo/Velocidad**: Pace per km, average vs max, negative splits
- **FC**: Average, max, time in zones, cardiac drift
- **Distancia y duración**: Compare to recent history
- **Tendencias**: Improving pace? More volume? Recovery between sessions?

### Recuperación
- **Sueño**: Duration, deep/light/REM phases, sleep score
- **HRV**: Status (balanced, low, unbalanced), weekly trend
- **Body Battery**: Morning charge level, drain patterns
- **Training Readiness**: Score and contributing factors

### Planificación
- **Race Predictions**: 5K, 10K, half marathon, marathon estimates
- **VO2max**: Current estimate and trend
- **Training Status**: Productive, peaking, recovery, detraining, etc.
- **Training Load**: Balance between easy/hard sessions

### Presentation Style
- Always respond in Spanish (the user prefers it)
- Use clear metrics: "4:52 min/km" not raw seconds
- Compare to previous data when available: "Tu ritmo medio mejoró 5s/km respecto a la semana pasada"
- Flag concerning patterns: poor sleep before hard training, overtraining signs
- Offer actionable suggestions when appropriate

## API Reference

For operations not covered by the fetch script, see `references/api_reference.md` for the complete method list with signatures. You can write inline Python:

```python
import garminconnect, garth, json

# Load saved session
garth.resume("/tmp/garmin_session/tokens")
api = garminconnect.Garmin()
api.login(tokenstore="/tmp/garmin_session/tokens")

# Now call any method
data = api.get_activities(start=0, limit=5)
print(json.dumps(data, indent=2, default=str))
```

## Date Formats
- Most methods use `YYYY-MM-DD` format
- Use `datetime.date.today().isoformat()` for "today"
- Some methods accept date ranges (startdate, enddate)

## Error Handling
- **GarminConnectAuthenticationError**: Bad credentials or expired session → re-auth
- **GarminConnectTooManyRequestsError**: Rate limited → wait 60s and retry
- **GarminConnectConnectionError**: Network issue → retry
- If tokens expire mid-session, re-run auth script
