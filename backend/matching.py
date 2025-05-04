from database import db  # ✅ Import Firestore client

#Match Users with Jobs
def match_jobs(user_skills, job_list):
    return [job for job in job_list if set(user_skills) & set(job['required_skills'])]

#Match Users with Mentors
def match_mentors(user_skills, mentor_list):
    return [mentor for mentor in mentor_list if set(user_skills) & set(mentor['expertise'])]

def analyze_applications(user_id):
    applications = db.collection("applications").where("user_id", "==", user_id).stream()
    statuses = [app.to_dict()["status"] for app in applications]

# AI Career Feedback
def analyze_applications(user_id):
    applications = db.collection("applications").where("user_id", "==", user_id).stream()
    statuses = [app.to_dict()["status"] for app in applications]

    # AI Suggestion Logic
    if "Applied" in statuses and "Interviewing" not in statuses:
        return "Consider improving your resume or applying to more tailored roles."
    elif "Interviewing" in statuses and "Offer Received" not in statuses:
        return "Practice interview questions—confidence matters!"
    else:
        return "You're progressing well! Keep refining skills."

# ✅ Match Users with Mentors Based on Career Interest
def match_mentor(career_interest):
    mentors = db.collection("mentors").where("expertise","==", career_interest).stream()
    return [{"name": mentor.to_dict()["name"], "expertise": mentor.to_dict()["expertise"]} for mentor in mentors]
 