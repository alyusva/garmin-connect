#!/usr/bin/env python3.11
"""Garmin Connect data fetcher.
Usage: python3 garmin_fetch.py <command> [args...]
Outputs JSON to stdout. Requires prior authentication (tokens in /tmp/garmin_session/tokens).
"""
import sys
import json
import garminconnect
import garth
from datetime import date, timedelta

TOKEN_DIR = "/tmp/garmin_session/tokens"

def get_api():
    """Initialize and return authenticated Garmin API client."""
    try:
        garth.resume(TOKEN_DIR)
        api = garminconnect.Garmin()
        api.login(tokenstore=TOKEN_DIR)
        return api
    except Exception as e:
        print(json.dumps({"error": f"Auth failed: {e}. Run garmin_auth.py first."}))
        sys.exit(1)

def today():
    return date.today().isoformat()

def days_ago(n):
    return (date.today() - timedelta(days=n)).isoformat()

def output(data):
    print(json.dumps(data, indent=2, default=str, ensure_ascii=False))

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No command provided. Use: activities, activity, sleep, hrv, etc."}))
        sys.exit(1)

    cmd = sys.argv[1]
    args = sys.argv[2:]
    api = get_api()

    try:
        if cmd == "activities":
            limit = int(args[0]) if args else 10
            atype = args[1] if len(args) > 1 else None
            data = api.get_activities(start=0, limit=limit, activitytype=atype)
            # Simplify output: extract key fields
            simplified = []
            for a in data:
                simplified.append({
                    "id": a.get("activityId"),
                    "name": a.get("activityName"),
                    "type": a.get("activityType", {}).get("typeKey") if isinstance(a.get("activityType"), dict) else a.get("activityType"),
                    "date": a.get("startTimeLocal"),
                    "distance_km": round(a.get("distance", 0) / 1000, 2) if a.get("distance") else None,
                    "duration_min": round(a.get("duration", 0) / 60, 1) if a.get("duration") else None,
                    "avg_hr": a.get("averageHR"),
                    "max_hr": a.get("maxHR"),
                    "avg_pace_min_km": round(1000 / a["averageSpeed"] / 60, 2) if a.get("averageSpeed") and a["averageSpeed"] > 0 else None,
                    "calories": a.get("calories"),
                    "avg_cadence": a.get("averageRunningCadenceInStepsPerMinute"),
                    "elevation_gain": a.get("elevationGain"),
                    "training_effect_aerobic": a.get("aerobicTrainingEffect"),
                    "training_effect_anaerobic": a.get("anaerobicTrainingEffect"),
                    "vo2max": a.get("vO2MaxValue"),
                })
            output(simplified)

        elif cmd == "activity":
            activity_id = args[0]
            data = api.get_activity(activity_id)
            output(data)

        elif cmd == "activity_details":
            activity_id = args[0]
            data = api.get_activity_details(activity_id)
            output(data)

        elif cmd == "activity_splits":
            activity_id = args[0]
            data = api.get_activity_splits(activity_id)
            output(data)

        elif cmd == "sleep":
            cdate = args[0] if args else today()
            data = api.get_sleep_data(cdate)
            output(data)

        elif cmd == "hrv":
            cdate = args[0] if args else today()
            data = api.get_hrv_data(cdate)
            output(data)

        elif cmd == "body_battery":
            start = args[0] if args else days_ago(7)
            end = args[1] if len(args) > 1 else today()
            data = api.get_body_battery(start, end)
            output(data)

        elif cmd == "training_readiness":
            cdate = args[0] if args else today()
            data = api.get_training_readiness(cdate)
            output(data)

        elif cmd == "morning_readiness":
            cdate = args[0] if args else today()
            data = api.get_morning_training_readiness(cdate)
            output(data)

        elif cmd == "training_status":
            cdate = args[0] if args else today()
            data = api.get_training_status(cdate)
            output(data)

        elif cmd == "stress":
            cdate = args[0] if args else today()
            data = api.get_stress_data(cdate)
            output(data)

        elif cmd == "stats":
            cdate = args[0] if args else today()
            data = api.get_stats(cdate)
            output(data)

        elif cmd == "race_predictions":
            start = args[0] if args else None
            end = args[1] if len(args) > 1 else None
            data = api.get_race_predictions(startdate=start, enddate=end)
            output(data)

        elif cmd == "max_metrics":
            cdate = args[0] if args else today()
            data = api.get_max_metrics(cdate)
            output(data)

        elif cmd == "steps":
            start = args[0] if args else days_ago(7)
            end = args[1] if len(args) > 1 else today()
            data = api.get_daily_steps(start, end)
            output(data)

        elif cmd == "weight":
            start = args[0] if args else days_ago(30)
            end = args[1] if len(args) > 1 else today()
            data = api.get_weigh_ins(start, end)
            output(data)

        elif cmd == "heart_rate":
            cdate = args[0] if args else today()
            data = api.get_heart_rates(cdate)
            output(data)

        elif cmd == "rhr":
            cdate = args[0] if args else today()
            data = api.get_rhr_day(cdate)
            output(data)

        elif cmd == "personal_records":
            data = api.get_personal_record()
            output(data)

        elif cmd == "fitness_age":
            cdate = args[0] if args else today()
            data = api.get_fitnessage_data(cdate)
            output(data)

        elif cmd == "endurance":
            start = args[0] if args else days_ago(30)
            end = args[1] if len(args) > 1 else None
            data = api.get_endurance_score(start, end)
            output(data)

        elif cmd == "hill_score":
            start = args[0] if args else days_ago(30)
            end = args[1] if len(args) > 1 else None
            data = api.get_hill_score(start, end)
            output(data)

        elif cmd == "weekly_steps":
            end = args[0] if args else today()
            weeks = int(args[1]) if len(args) > 1 else 4
            data = api.get_weekly_steps(end, weeks)
            output(data)

        elif cmd == "weekly_stress":
            end = args[0] if args else today()
            weeks = int(args[1]) if len(args) > 1 else 4
            data = api.get_weekly_stress(end, weeks)
            output(data)

        elif cmd == "devices":
            data = api.get_devices()
            output(data)

        elif cmd == "goals":
            data = api.get_goals()
            output(data)

        elif cmd == "workouts":
            limit = int(args[0]) if args else 20
            data = api.get_workouts(start=0, limit=limit)
            output(data)

        elif cmd == "training_plans":
            data = api.get_training_plans()
            output(data)

        elif cmd == "last_activity":
            data = api.get_last_activity()
            output(data)

        elif cmd == "activities_by_date":
            start = args[0] if args else days_ago(7)
            end = args[1] if len(args) > 1 else today()
            atype = args[2] if len(args) > 2 else None
            data = api.get_activities_by_date(start, end, activitytype=atype)
            output(data)

        elif cmd == "intensity_minutes":
            cdate = args[0] if args else today()
            data = api.get_intensity_minutes_data(cdate)
            output(data)

        elif cmd == "respiration":
            cdate = args[0] if args else today()
            data = api.get_respiration_data(cdate)
            output(data)

        elif cmd == "spo2":
            cdate = args[0] if args else today()
            data = api.get_spo2_data(cdate)
            output(data)

        elif cmd == "lactate_threshold":
            data = api.get_lactate_threshold()
            output(data)

        elif cmd == "cycling_ftp":
            data = api.get_cycling_ftp()
            output(data)

        elif cmd == "body_composition":
            start = args[0] if args else days_ago(30)
            end = args[1] if len(args) > 1 else today()
            data = api.get_body_composition(start, end)
            output(data)

        elif cmd == "user_profile":
            data = api.get_user_profile()
            output(data)

        elif cmd == "progress":
            start = args[0] if args else days_ago(30)
            end = args[1] if len(args) > 1 else today()
            metric = args[2] if len(args) > 2 else "distance"
            data = api.get_progress_summary_between_dates(start, end, metric=metric)
            output(data)

        elif cmd == "activity_weather":
            activity_id = args[0]
            data = api.get_activity_weather(activity_id)
            output(data)

        elif cmd == "activity_hr_zones":
            activity_id = args[0]
            data = api.get_activity_hr_in_timezones(activity_id)
            output(data)

        else:
            print(json.dumps({"error": f"Unknown command: {cmd}. Available: activities, activity, sleep, hrv, body_battery, training_readiness, stress, stats, race_predictions, max_metrics, steps, weight, heart_rate, personal_records, fitness_age, endurance, hill_score, weekly_steps, devices, goals, workouts, training_plans, last_activity, activities_by_date, intensity_minutes, respiration, spo2, lactate_threshold, cycling_ftp, body_composition, user_profile, progress, activity_weather, activity_hr_zones"}))
            sys.exit(1)

    except Exception as e:
        print(json.dumps({
            "error": type(e).__name__,
            "message": str(e)
        }))
        sys.exit(1)

if __name__ == "__main__":
    main()
