bugs = []

def add_bug(title, description, severity):
  bugs.append({
    'title': title,
    'description': description,
    'severity': severity,
    'resolved': False
  })

def view_bugs():
  for i, bug in enumerate(bugs):
    print(f"{i+1}. {bug['title']} ({bug['severity']})")

def view_bug(index):
  bug = bugs[index]
  print(f"Title: {bug['title']}")
  print(f"Description: {bug['description']}")
  print(f"Severity: {bug['severity']}")
  print(f"Resolved: {bug['resolved']}")

def edit_bug(index, field, value):
  bug = bugs[index]
  bug[field] = value
  print(f"{field} for bug '{bug['title']}' has been updated to '{value}'")

def search_bugs(search_term):
  found_bugs = False
  for i, bug in enumerate(bugs):
    if search_term in bug['title'] or search_term in bug['description']:
      print(f"{i+1}. {bug['title']} ({bug['severity']})")
      found_bugs = True
  if not found_bugs:
    print(f"No bugs found with the search term '{search_term}'")

def filter_bugs(severity):
  filtered_bugs = [bug for bug in bugs if bug['severity'] == severity]
  if not filtered_bugs:
    print(f"No bugs found with severity '{severity}'")
  else:
    for i, bug in enumerate(filtered_bugs):
      print(f"{i+1}. {bug['title']} ({bug['severity']})")

def resolve_bug(index):
  bug = bugs[index]
  bug['resolved'] = True
  print(f"Bug '{bug['title']}' has been marked as resolved")

while True:
  print("1. Add a new bug")
  print("2. View all bugs")
  print("3. View a specific bug")
  print("4. Edit a specific bug")
  print("5. Search for a bug")
  print("6. Filter bugs by severity")
  print("7. Mark a bug as resolved")
  print("8. Quit")
  choice = input("Enter your choice: ")
  if choice == "1":
    title = input("Enter the title of the bug: ")
    description = input("Enter the description of the bug: ")
    severity = input("Enter the severity of the bug (low, medium, high): ")
    add_bug(title, description, severity)
  elif choice == "2":
    view_bugs()
  elif choice == "3":
    index = int(input("Enter the index of the bug: ")) 
