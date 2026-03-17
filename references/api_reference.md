# Garmin Connect API Reference

Complete method reference for the `garminconnect` Python library (class `Garmin`).

## Authentication
| Method | Signature | Description |
|--------|-----------|-------------|
| `login` | `(tokenstore: str \| None = None)` | Login and optionally save tokens |
| `resume_login` | `(client_state: dict, mfa_code: str)` | Complete MFA login |
| `logout` | `()` | Logout current session |

## Activities
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_activities` | `(start=0, limit=20, activitytype=None)` | List activities with pagination |
| `get_activities_by_date` | `(startdate, enddate=None, activitytype=None, sortorder=None)` | Activities in date range |
| `get_activities_fordate` | `(fordate)` | Activities for a specific date |
| `get_activity` | `(activity_id)` | Single activity summary |
| `get_activity_details` | `(activity_id, maxchart=2000, maxpoly=4000)` | Full details with charts |
| `get_activity_splits` | `(activity_id)` | Split data |
| `get_activity_typed_splits` | `(activity_id)` | Typed split data |
| `get_activity_split_summaries` | `(activity_id)` | Split summaries |
| `get_activity_exercise_sets` | `(activity_id)` | Exercise sets (strength) |
| `get_activity_hr_in_timezones` | `(activity_id)` | HR zone distribution |
| `get_activity_weather` | `(activity_id)` | Weather during activity |
| `get_activity_gear` | `(activity_id)` | Gear used |
| `get_last_activity` | `()` | Most recent activity |
| `count_activities` | `()` | Total activity count |
| `download_activity` | `(activity_id, dl_fmt=TCX)` | Download in TCX/GPX/CSV/Original |

## Daily Stats & Health
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_stats` | `(cdate)` | Daily stats summary |
| `get_stats_and_body` | `(cdate)` | Stats + body composition |
| `get_user_summary` | `(cdate)` | User daily summary |
| `get_heart_rates` | `(cdate)` | HR data for a day |
| `get_rhr_day` | `(cdate)` | Resting heart rate |
| `get_daily_steps` | `(start, end)` | Daily steps in range |
| `get_steps_data` | `(cdate)` | Detailed step data |
| `get_weekly_steps` | `(end, weeks=52)` | Weekly step totals |
| `get_floors` | `(cdate)` | Floors climbed |
| `get_intensity_minutes_data` | `(cdate)` | Intensity minutes |
| `get_weekly_intensity_minutes` | `(start, end)` | Weekly intensity |

## Sleep
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_sleep_data` | `(cdate)` | Full sleep data |

## Stress & Body Battery
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_stress_data` | `(cdate)` | All-day stress |
| `get_all_day_stress` | `(cdate)` | Stress summary |
| `get_weekly_stress` | `(end, weeks=52)` | Weekly stress |
| `get_body_battery` | `(startdate, enddate=None)` | Body battery range |
| `get_body_battery_events` | `(cdate)` | Battery drain/charge events |

## Training & Performance
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_training_readiness` | `(cdate)` | Training readiness score |
| `get_morning_training_readiness` | `(cdate)` | Morning readiness |
| `get_training_status` | `(cdate)` | Training status (productive, etc.) |
| `get_max_metrics` | `(cdate)` | VO2max and max metrics |
| `get_race_predictions` | `(startdate=None, enddate=None, _type=None)` | Race time predictions |
| `get_endurance_score` | `(startdate, enddate=None)` | Endurance score |
| `get_hill_score` | `(startdate, enddate=None)` | Hill score |
| `get_fitnessage_data` | `(cdate)` | Fitness age |
| `get_lactate_threshold` | `(latest=True, start_date=None, end_date=None, aggregation='daily')` | Lactate threshold |
| `get_personal_record` | `()` | Personal records |

## Respiration & SpO2
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_respiration_data` | `(cdate)` | Respiration rate |
| `get_spo2_data` | `(cdate)` | Blood oxygen |

## HRV
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_hrv_data` | `(cdate)` | HRV for a day |

## Body Composition & Weight
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_body_composition` | `(startdate, enddate=None)` | Body composition range |
| `get_weigh_ins` | `(startdate, enddate)` | Weight measurements |
| `get_daily_weigh_ins` | `(cdate)` | Weigh-ins for a day |
| `add_weigh_in` | `(weight, unitKey='kg', timestamp='')` | Add weight entry |

## Workouts & Plans
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_workouts` | `(start=0, limit=100)` | Saved workouts |
| `get_workout_by_id` | `(workout_id)` | Specific workout |
| `get_training_plans` | `()` | Active training plans |
| `get_training_plan_by_id` | `(plan_id)` | Specific plan details |
| `upload_running_workout` | `(workout)` | Upload running workout |
| `upload_cycling_workout` | `(workout)` | Upload cycling workout |

## Devices & Profile
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_devices` | `()` | Connected devices |
| `get_device_last_used` | `()` | Last used device |
| `get_device_settings` | `(device_id)` | Device settings |
| `get_user_profile` | `()` | User profile |
| `get_userprofile_settings` | `()` | Profile settings |
| `get_unit_system` | `()` | Unit system (metric/imperial) |
| `get_full_name` | `()` | Display name |
| `get_gear` | `(userProfileNumber)` | User gear |

## Progress & Goals
| Method | Signature | Description |
|--------|-----------|-------------|
| `get_progress_summary_between_dates` | `(startdate, enddate, metric='distance', groupbyactivities=True)` | Progress summary |
| `get_goals` | `(status='active', start=0, limit=30)` | Active goals |

## Date Format
All dates use `YYYY-MM-DD` format (e.g., `2026-03-12`).
