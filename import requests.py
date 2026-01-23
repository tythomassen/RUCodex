import requests

# Parameters for the current semester
YEAR = "2026"
TERM = "1"
CAMPUS = "NB"

url = f"https://sis.rutgers.edu/soc/api/courses.json?year={YEAR}&term={TERM}&campus=NB"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("Fetching data... (this may take a moment for the full campus list)")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    courses = response.json()
    found = False
    
    print(f"\n--- PREREQUISITES FOR THERMODYNAMICS COURSES ---")
    
    for course in courses:
        # Search for 'Thermodynamics' in the title (case-insensitive)
        if "THERMODYNAMICS" in course['title'].upper():
            found = True
            title = course['title']
            subject = course['subject']
            course_num = course['courseNumber']
            # Get the pre-req notes; if none exist, return 'None listed'
            prereqs = course.get('preReqNotes', 'No prerequisites listed in the system.')
            
            print(f"\nCourse: {title} ({subject}:{course_num})")
            print(f"Prerequisites: {prereqs}")
            print("-" * 50)
            
    if not found:
        print("No courses found with that title.")
else:
    print(f"Failed to connect. Status code: {response.status_code}")