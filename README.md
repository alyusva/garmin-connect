# 🏃 Garmin Connect Skill for Claude Code

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Garmin Connect](https://img.shields.io/badge/Garmin-Connect-blue)](https://connect.garmin.com/)
[![Security Check](https://github.com/alyusva/garmin-connect/workflows/Security%20Check/badge.svg)](https://github.com/alyusva/garmin-connect/actions)

**Conecta Claude con tu cuenta de Garmin Connect** para analizar tus entrenamientos, recuperación y métricas de salud usando inteligencia artificial.

## 🎯 ¿Qué puede hacer esta skill?

Pregúntale a Claude sobre tu actividad física en **lenguaje natural**:

### 🏃 Entrenamientos
- *"¿Cómo fue mi carrera de esta mañana?"* → Analiza ritmo, frecuencia cardíaca, cadencia, desnivel
- *"Muéstrame mis últimos 10 entrenamientos"* → Listado con resumen de cada actividad
- *"¿Estoy mejorando mi ritmo?"* → Compara progreso entre sesiones
- *"¿Cuánto he corrido esta semana?"* → Suma distancias y duración

### 😴 Recuperación
- *"¿Cómo dormí anoche?"* → Análisis de fases de sueño (profundo/ligero/REM)
- *"¿Estoy bien recuperado para entrenar hoy?"* → Training Readiness + HRV + Body Battery
- *"Muéstrame mi Body Battery de la semana"* → Gráfico de carga/descarga de energía
- *"¿Mi HRV está normal?"* → Estado (equilibrado/bajo/desequilibrado) y tendencia

### 📊 Rendimiento
- *"¿Cuál es mi VO2max actual?"* → Estimación y evolución histórica
- *"¿Qué marca puedo hacer en un 10K?"* → Predicciones de carrera (5K, 10K, media, maratón)
- *"¿Cuál es mi edad de fitness?"* → Fitness Age comparado con edad real
- *"Muéstrame mis récords personales"* → Mejores marcas por distancia

### 🎯 Planificación
- *"¿Qué objetivos tengo activos?"* → Objetivos de pasos, peso, actividades
- *"¿Tengo algún plan de entrenamiento?"* → Planes activos y progreso
- *"Muéstrame mis entrenamientos guardados"* → Biblioteca de workouts

### 📈 Tendencias
- *"¿Estoy entrenando demasiado?"* → Training Status (productivo/recuperación/sobreentrenamiento)
- *"¿Mi estrés está alto esta semana?"* → Niveles de estrés diarios
- *"Compara mi actividad del último mes"* → Volumen, intensidad, progreso

## 💬 Ejemplos de conversación real

```
👤 Usuario: "¿Cómo fue mi última carrera?"

🤖 Claude: [Usa garmin-connect skill]
Tu última carrera fue ayer:
• 10.2 km en 52:14 (5:07 min/km)
• FC media: 152 bpm (máx: 171)
• Cadencia: 174 spm
• Desnivel positivo: 87m
• Training Effect aeróbico: 3.2 (Mantenimiento)

✨ Análisis: Ritmo consistente, mantuviste 5:05-5:10 min/km
todo el recorrido. FC controlada en zona 2-3. ¡Buen entreno base!

---

👤 Usuario: "¿Debería entrenar hoy o descansar?"

🤖 Claude: [Consulta Training Readiness, HRV, Body Battery, Sleep]
📊 Training Readiness: 68/100 (Moderado)
💚 HRV: Equilibrado (54ms - dentro de tu rango)
🔋 Body Battery: 73/100 (Cargado)
😴 Sueño: 7h 23min - Score: 78/100

✅ Recomendación: Estás listo para entrenar, pero evita
sesiones muy intensas. Tu Body Battery está bien pero tu HRV
sugiere que todavía estás recuperando del entreno de ayer.
Ideal para un rodaje suave o descanso activo.
```

## ✨ Datos disponibles

### 🏋️ Actividades y entrenamientos
| Métrica | Qué obtienes |
|---------|--------------|
| **Actividades recientes** | Últimas 10/20/50 carreras, bicis, nados con métricas clave |
| **Detalles de actividad** | Splits por km, zonas FC, elevación, cadencia, potencia |
| **Ritmo y velocidad** | Min/km promedio, máximo, por tramos, negative splits |
| **Frecuencia cardíaca** | Promedio, máxima, tiempo en zonas, cardiac drift |
| **Training Effect** | Impacto aeróbico y anaeróbico (1-5 escala) |
| **Clima** | Condiciones durante el entrenamiento |

### 😴 Recuperación y salud
| Métrica | Qué obtienes |
|---------|--------------|
| **Sueño** | Fases (profundo/ligero/REM), duración, score de calidad |
| **HRV** | Variabilidad cardíaca, estado (equilibrado/bajo), tendencia semanal |
| **Body Battery** | Nivel de energía (0-100), carga/descarga durante el día |
| **Training Readiness** | Score de preparación (0-100) con factores contribuyentes |
| **Estrés** | Nivel de estrés (0-100) durante todo el día |
| **Recuperación FC** | Tiempo de recuperación post-ejercicio |

### 📊 Métricas de rendimiento
| Métrica | Qué obtienes |
|---------|--------------|
| **VO2max** | Capacidad aeróbica estimada (ml/kg/min) con tendencia |
| **Edad de fitness** | Tu edad fisiológica vs edad real |
| **Predicciones de carrera** | Tiempos estimados para 5K, 10K, media maratón, maratón |
| **Umbral de lactato** | Ritmo y FC en umbral anaeróbico |
| **FTP ciclismo** | Functional Threshold Power para ciclistas |
| **Récords personales** | Mejores tiempos en todas las distancias |
| **Endurance Score** | Capacidad de resistencia de larga duración |
| **Hill Score** | Rendimiento en subidas y desnivel |

### 🎯 Planificación y objetivos
| Métrica | Qué obtienes |
|---------|--------------|
| **Training Status** | Estado actual: productivo/peaking/recovery/detraining/overreaching |
| **Training Load** | Carga aeróbica vs anaeróbica, balance de entrenamiento |
| **Objetivos activos** | Pasos diarios, peso objetivo, minutos de intensidad |
| **Planes de entrenamiento** | Programas activos con progreso |
| **Entrenamientos guardados** | Biblioteca de workouts personalizados |

### 📱 Datos adicionales
- **Dispositivos conectados**: Relojes, básculas, sensores
- **Composición corporal**: Peso, IMC, % grasa, masa muscular
- **Pasos y actividad diaria**: Pasos, distancia, calorías
- **Minutos de intensidad**: Tiempo en zonas moderada/vigorosa
- **SpO2**: Saturación de oxígeno
- **Respiración**: Frecuencia respiratoria

## 🚀 Installation

### Prerequisites

- Python 3.11+
- Claude Code CLI
- Garmin Connect account

### Setup as Claude Skill

1. **Clone to skills directory:**
   ```bash
   cd ~/.claude/skills
   git clone https://github.com/alyusva/garmin-connect.git
   ```

2. **Install dependencies:**
   ```bash
   cd garmin-connect
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python3 scripts/garmin_auth.py --help
   ```

## 📖 Usage

### Authentication

**IMPORTANT**: You'll need to provide your Garmin Connect credentials. They are used only for the current session and stored temporarily.

```bash
# Authenticate (saves session tokens to /tmp/garmin_session/tokens)
python3 scripts/garmin_auth.py your-email@example.com your-password

# If MFA is enabled
python3 scripts/garmin_auth.py your-email@example.com your-password 123456
```

Tokens are valid for ~24 hours. After that, re-run the auth script.

### Fetching Data

```bash
# Recent activities
python3 scripts/garmin_fetch.py activities 10

# Single activity details
python3 scripts/garmin_fetch.py activity 123456789

# Sleep data
python3 scripts/garmin_fetch.py sleep 2026-03-17

# HRV data
python3 scripts/garmin_fetch.py hrv 2026-03-17

# Body Battery (last 7 days)
python3 scripts/garmin_fetch.py body_battery 2026-03-10 2026-03-17

# Training Readiness
python3 scripts/garmin_fetch.py training_readiness 2026-03-17

# Race Predictions
python3 scripts/garmin_fetch.py race_predictions

# VO2max and max metrics
python3 scripts/garmin_fetch.py max_metrics 2026-03-17
```

All commands output JSON to stdout.

### Available Commands

| Command | Description | Arguments |
|---------|-------------|-----------|
| `activities` | Recent activities | `[limit] [type]` |
| `activity` | Single activity | `<id>` |
| `activity_details` | Full activity details | `<id>` |
| `sleep` | Sleep data | `[date]` |
| `hrv` | HRV data | `[date]` |
| `body_battery` | Body battery data | `<start> [end]` |
| `training_readiness` | Training readiness | `[date]` |
| `training_status` | Training status | `[date]` |
| `stress` | Stress data | `[date]` |
| `stats` | Daily stats summary | `[date]` |
| `race_predictions` | Race predictions | - |
| `max_metrics` | VO2max and metrics | `[date]` |
| `steps` | Daily steps | `<start> <end>` |
| `weight` | Weight/body comp | `<start> <end>` |
| `heart_rate` | Heart rate data | `[date]` |
| `personal_records` | Personal records | - |
| `fitness_age` | Fitness age | `[date]` |
| `devices` | Connected devices | - |
| `goals` | Active goals | - |
| `workouts` | Saved workouts | `[limit]` |
| `training_plans` | Training plans | - |
| `last_activity` | Most recent activity | - |

Date format: `YYYY-MM-DD` (defaults to today if omitted)

### Using with Claude Code

Once installed as a skill, you can ask Claude naturally:

```
You: "How was my run yesterday?"
Claude: [Uses garmin-connect skill to fetch and analyze your activity]

You: "What's my VO2max?"
Claude: [Fetches max metrics and presents VO2max with trend]

You: "Am I ready to train today?"
Claude: [Checks training readiness, HRV, body battery, sleep]
```

Claude will automatically:
1. Authenticate if needed (asking for credentials)
2. Fetch the appropriate data
3. Analyze and present insights in Spanish (configurable)
4. Compare to historical data when available
5. Flag concerning patterns

## 🔧 Advanced Usage

### Custom Python Scripts

You can write custom analysis scripts using the Garmin API directly:

```python
import garminconnect
import garth
import json
from datetime import date

# Load saved session
garth.resume("/tmp/garmin_session/tokens")
api = garminconnect.Garmin()
api.login(tokenstore="/tmp/garmin_session/tokens")

# Fetch data
activities = api.get_activities(start=0, limit=5)
sleep_data = api.get_sleep_data(date.today().isoformat())
hrv_data = api.get_hrv_data(date.today().isoformat())

# Process and analyze
print(json.dumps(activities, indent=2, default=str))
```

See `references/api_reference.md` for the complete API method list.

## 🛡️ Security

### Credentials Handling

- ✅ Credentials passed as command-line arguments (not stored)
- ✅ Session tokens saved to `/tmp` (cleared on system restart)
- ✅ No credentials in code or config files
- ✅ Tokens expire after ~24 hours

### Best Practices

1. **Never commit credentials** to version control
2. **Use strong passwords** for your Garmin account
3. **Enable MFA** on your Garmin account for extra security
4. **Re-authenticate daily** to minimize token exposure
5. **Don't share tokens** - they provide full account access

### Token Security

Session tokens are stored in `/tmp/garmin_session/tokens`. This directory:
- Is cleared on system restart
- Is user-specific (not accessible by other users)
- Contains OAuth2 tokens (not your password)
- Expires automatically after ~24 hours

## 📁 Project Structure

```
garmin-connect/
├── scripts/
│   ├── garmin_auth.py       ← Authentication script
│   └── garmin_fetch.py      ← Data fetching script
├── references/
│   └── api_reference.md     ← Complete API documentation
├── venv/                    ← Virtual environment (not in git)
├── SKILL.md                 ← Skill definition for Claude
├── README.md                ← This file
├── requirements.txt         ← Python dependencies
├── .gitignore              ← Git ignore rules
└── LICENSE                  ← MIT License
```

## 🔍 Troubleshooting

**"Auth failed" error**
→ Session tokens expired or invalid. Re-run `garmin_auth.py`

**"TOO_MANY_REQUESTS" error**
→ Rate limited by Garmin. Wait 60 seconds and retry.

**"MFA required" message**
→ Your account has MFA enabled. Provide the 6-digit code as third argument.

**Empty or missing data**
→ Verify the date is correct and data exists in Garmin Connect for that date.

**Import errors**
→ Make sure you're using the virtual environment: `source venv/bin/activate`

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

Please ensure:
- Code follows existing style
- No credentials in commits
- Documentation is updated
- Scripts are tested

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 👤 Author

**Álvaro Yuste Valles**
- GitHub: [@alyusva](https://github.com/alyusva)

## 🙏 Acknowledgments

- [Garmin Connect](https://connect.garmin.com/) - Fitness tracking platform
- [python-garminconnect](https://github.com/cyberjunky/python-garminconnect) - Python API wrapper
- [Garth](https://github.com/matin/garth) - Garmin authentication library
- [Claude Code](https://claude.ai/claude-code) - AI-powered coding assistant

## 📚 Resources

- [Garmin Connect API Documentation](https://developer.garmin.com/connect-api/)
- [python-garminconnect GitHub](https://github.com/cyberjunky/python-garminconnect)
- [Claude Skills Documentation](https://docs.claude.ai/claude-code/skills)

---

⭐ **If you find this useful, give it a star!**

🏃 **Track your fitness with AI-powered insights**
